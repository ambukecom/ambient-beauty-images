/**
 * Ambient Beauty – Supplier Vs Website
 * Task 1: fetch the BeautyFort stock file from Gmail and refresh the
 * "Stockfile Import" tab. Every other tab (Clean Variants included) recalculates from it.
 * Task 2 (DraftsSync.gs): straight after each import, preview and then apply stock,
 * price and status changes in Shopify for every product in "Drafts Stock and Price Changes".
 *
 * Schedule: BeautyFort sends the stock file at 00:00, 09:00 and 17:00 (UK time).
 * A one-minute trigger does nothing until 5 minutes after each send time, then
 * imports that send's file, previews the Shopify changes and applies them.
 * If an email is late it keeps checking every minute and imports it as soon as it
 * lands; if it is still missing 30 minutes after the send time you get one alert.
 *
 * SETUP (one-off, already done once – rerun setupTriggers after pasting this version):
 *  1. Extensions > Apps Script: paste this file over the old one. Save.
 *  2. Services (+) > "Drive API" must be added (it already is).
 *  3. Choose "setupTriggers" in the toolbar and click Run.
 */

const CONFIG = {
  SENDER: 'info@beautyfort.com',
  SUBJECT_WORDS: 'Stock File',
  ATTACHMENT_PREFIX: 'stockfile',
  MAIN_FOLDER_ID: '1TQKAKBb44qcb24ysBgto-kWZ-eT3CkLA',
  IMPORT_TAB: 'Stockfile Import',
  LOG_TAB: 'Run Log',
  TIMEZONE: 'Europe/London',
  SEND_TIMES: ['00:00', '09:00', '17:00'],   // BeautyFort's scheduled emails
  DELAY_MIN: 5,                              // import 5 minutes after each send time
  ALERT_AFTER_MIN: 30,                       // alert if the email is still missing this long after send time
  MIN_ROWS: 500,                             // safety check: refuse a half-empty file
  REQUIRED_HEADERS: ['Stock Code', 'Category', 'Brand', 'Gender', 'Stock Level', 'Price', 'Barcode', 'Name']
};

/** Menu for manual runs. */
function onOpen() {
  SpreadsheetApp.getUi()
    .createMenu('Workflow')
    .addItem('Fetch stock file now', 'fetchStockFileManual')
    .addSeparator()
    .addItem('Preview Shopify changes (changes nothing)', 'syncDraftsPreview')
    .addItem('Update Shopify now', 'syncDraftsManual')
    .addToUi();
}

/** Run once after pasting: replaces the old hourly trigger with a one-minute check. */
function setupTriggers() {
  ScriptApp.getProjectTriggers()
    .filter(t => ['fetchStockFile', 'downloadImages', 'scheduledCheck'].indexOf(t.getHandlerFunction()) !== -1)
    .forEach(t => ScriptApp.deleteTrigger(t));
  ScriptApp.newTrigger('scheduledCheck').timeBased().everyMinutes(1).create();
  SpreadsheetApp.getActive().setSpreadsheetTimeZone(CONFIG.TIMEZONE);
  // Treat the current send window as already handled so setup does not re-import.
  const s = currentSlot_(new Date());
  if (s) PropertiesService.getScriptProperties().setProperty('doneSlot', s.key);
  log_('Setup', 'Trigger created: checks every minute; imports at ' +
       CONFIG.SEND_TIMES.map(t => addMin_(t, CONFIG.DELAY_MIN)).join(', '));
}

/** Manual menu item: import the latest file now, then preview and update Shopify. */
function fetchStockFileManual() {
  const latest = latestStockEmail_(null);
  if (!latest) { SpreadsheetApp.getUi().alert('No BeautyFort stock file email found in the last 3 days.'); return; }
  SpreadsheetApp.getUi().alert(importAndSync_(latest, 'manual'));
}

/**
 * Trigger handler (every minute). Cheap when there is nothing to do: it only reads
 * the clock and one script property until a send window is due.
 */
function scheduledCheck() {
  const props = PropertiesService.getScriptProperties();
  const now = new Date();
  const slot = currentSlot_(now);

  // Finish a Shopify sync that ran out of time on the previous attempt.
  if (props.getProperty('syncPending') === 'yes' && (!slot || props.getProperty('doneSlot') === slot.key)) {
    return runSync_('resume');
  }
  if (!slot || props.getProperty('doneSlot') === slot.key) return 'Nothing due.';

  const latest = latestStockEmail_(new Date(slot.start.getTime() - 15 * 60000));
  if (!latest) {
    const late = (now - slot.start) / 60000 >= CONFIG.ALERT_AFTER_MIN;
    if (late && props.getProperty('alertSlot') !== slot.key) {
      MailApp.sendEmail(Session.getEffectiveUser().getEmail(),
        'ALERT: BeautyFort ' + slot.label + ' stock file not received',
        'The ' + slot.label + ' stock file email from ' + CONFIG.SENDER + ' has not arrived. ' +
        'Supplier Vs Website is still using the previous file. It keeps checking every minute ' +
        'and will import, preview and update Shopify as soon as the email lands.');
      props.setProperty('alertSlot', slot.key);
      log_('Alert', slot.label + ' stock file not received after ' + CONFIG.ALERT_AFTER_MIN + ' minutes');
    }
    return 'Waiting for the ' + slot.label + ' email.';
  }
  if (props.getProperty('lastMessageId') === latest.getId()) {   // already imported by hand
    props.setProperty('doneSlot', slot.key);
    return 'Already imported.';
  }
  const result = importAndSync_(latest, slot.label);
  if (result.indexOf('File rejected') !== 0 && result.indexOf('Email found but') !== 0) props.setProperty('doneSlot', slot.key);
  return result;
}

/** Import one email's stock file, then preview and apply the Shopify changes. */
function importAndSync_(message, label) {
  const msg = importStockFile_(message);
  if (msg.indexOf('Imported') !== 0) return msg;
  return msg + ' ' + runSync_(label);
}

function runSync_(label) {
  try {
    const preview = syncDrafts({ dryRun: true });
    log_('Shopify preview', label + ': ' + preview);
    const applied = syncDrafts({});
    return 'Preview: ' + preview + ' Update: ' + applied;
  } catch (e) {
    log_('Sync error', String(e.message || e));
    PropertiesService.getScriptProperties().setProperty('syncPending', 'yes');
    MailApp.sendEmail(Session.getEffectiveUser().getEmail(), 'ALERT: Shopify update failed after stock import',
      String(e.message || e) + '\n\nThe stock file import itself worked. The update will be retried automatically.');
    return 'Shopify update failed: ' + (e.message || e);
  }
}

/* ---------------------------------------------------------------- timing */

function addMin_(hhmm, m) {
  const t = Number(hhmm.slice(0, 2)) * 60 + Number(hhmm.slice(3)) + m;
  return ('0' + Math.floor(t / 60) % 24).slice(-2) + ':' + ('0' + t % 60).slice(-2);
}

/**
 * The most recent send window whose import time (send + 5 min) has passed, within the last
 * 12 hours. Returns {key, label, start} or null.
 */
function currentSlot_(now) {
  const tz = CONFIG.TIMEZONE;
  let best = null;
  for (let d = 0; d <= 1; d++) {
    const day = new Date(now.getTime() - d * 86400000);
    const ymd = Utilities.formatDate(day, tz, 'yyyy-MM-dd');
    CONFIG.SEND_TIMES.forEach(t => {
      const start = londonTime_(ymd, t);
      const due = new Date(start.getTime() + CONFIG.DELAY_MIN * 60000);
      if (due <= now && now - start < 12 * 3600000 && (!best || start > best.start)) {
        best = { key: ymd + ' ' + t, label: Utilities.formatDate(start, tz, 'dd/MM HH:mm'), start: start };
      }
    });
  }
  return best;
}

/** A Date for a UK wall-clock time on a given day (handles GMT/BST). */
function londonTime_(ymd, hhmm) {
  const guess = new Date(ymd + 'T' + hhmm + ':00Z');
  const offset = Utilities.formatDate(guess, CONFIG.TIMEZONE, 'Z');           // e.g. +0100
  const mins = (offset[0] === '-' ? -1 : 1) * (Number(offset.slice(1, 3)) * 60 + Number(offset.slice(3)));
  return new Date(guess.getTime() - mins * 60000);
}

/* ---------------------------------------------------------------- import */

/** Latest BeautyFort stock file email, optionally only ones received after `since`. */
function latestStockEmail_(since) {
  const query = 'from:' + CONFIG.SENDER + ' subject:"' + CONFIG.SUBJECT_WORDS + '" has:attachment newer_than:3d';
  let latest = null;
  GmailApp.search(query, 0, 10).forEach(th => th.getMessages().forEach(m => {
    if (since && m.getDate() < since) return;
    if (!latest || m.getDate() > latest.getDate()) latest = m;
  }));
  return latest;
}

function importStockFile_(latest) {
  const props = PropertiesService.getScriptProperties();
  const today = Utilities.formatDate(new Date(), CONFIG.TIMEZONE, 'dd/MM/yyyy HH:mm');

  // Pick the attachment by name, not position.
  const att = latest.getAttachments().find(a =>
    a.getName().toLowerCase().indexOf(CONFIG.ATTACHMENT_PREFIX) === 0 &&
    /\.xlsx?$/i.test(a.getName()));
  if (!att) {
    log_('Error', 'No stockfile attachment in "' + latest.getSubject() + '"');
    return 'Email found but no stockfile attachment.';
  }

  // Save to Main Folder, converted to Google Sheets.
  const baseName = att.getName().replace(/\.xlsx?$/i, '') + ' ' +
                   Utilities.formatDate(latest.getDate(), CONFIG.TIMEZONE, 'HHmm');
  const converted = Drive.Files.create(
    { name: baseName, mimeType: MimeType.GOOGLE_SHEETS, parents: [CONFIG.MAIN_FOLDER_ID] },
    att.copyBlob()
  );
  const values = SpreadsheetApp.openById(converted.id).getSheets()[0].getDataRange().getDisplayValues();

  // Safety checks before overwriting anything.
  const header = values[0].map(h => String(h).trim());
  const missing = CONFIG.REQUIRED_HEADERS.filter(h => header.indexOf(h) === -1);
  if (missing.length || values.length - 1 < CONFIG.MIN_ROWS) {
    const why = missing.length ? 'missing columns: ' + missing.join(', ') : 'only ' + (values.length - 1) + ' rows';
    MailApp.sendEmail(Session.getEffectiveUser().getEmail(),
      'ALERT: BeautyFort stock file looks wrong (' + today + ')',
      'The file ' + att.getName() + ' was not imported (' + why + '). The previous data has been kept and Shopify was not changed.');
    log_('Rejected', att.getName() + ' – ' + why);
    return 'File rejected: ' + why;
  }

  // Replace the Stockfile Import tab (stored as text so barcodes keep leading zeros).
  const ss = SpreadsheetApp.getActive();
  const tab = ss.getSheetByName(CONFIG.IMPORT_TAB) || ss.insertSheet(CONFIG.IMPORT_TAB);
  tab.clearContents();
  if (tab.getMaxRows() < values.length) tab.insertRowsAfter(tab.getMaxRows(), values.length - tab.getMaxRows());
  if (tab.getMaxColumns() < header.length) tab.insertColumnsAfter(tab.getMaxColumns(), header.length - tab.getMaxColumns());
  const range = tab.getRange(1, 1, values.length, header.length);
  range.setNumberFormat('@');
  range.setValues(values);
  SpreadsheetApp.flush();

  props.setProperty('lastMessageId', latest.getId());
  props.setProperty('syncPending', 'yes');
  log_('Imported', att.getName() + ' (' + Utilities.formatDate(latest.getDate(), CONFIG.TIMEZONE, 'dd/MM HH:mm') +
       ' email) – ' + (values.length - 1) + ' products');
  return 'Imported ' + att.getName() + ' (' + (values.length - 1) + ' products).';
}

/** Appends a line to the Run Log tab. */
function log_(status, detail) {
  const ss = SpreadsheetApp.getActive();
  const sh = ss.getSheetByName(CONFIG.LOG_TAB) || (function () {
    const s = ss.insertSheet(CONFIG.LOG_TAB);
    s.appendRow(['Time', 'Status', 'Detail']);
    s.setFrozenRows(1);
    return s;
  })();
  sh.appendRow([Utilities.formatDate(new Date(), CONFIG.TIMEZONE, 'dd/MM/yyyy HH:mm'), status, detail]);
}
