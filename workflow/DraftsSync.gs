/**
 * Ambient Beauty – Supplier Vs Website
 * Task 2: after each stock file import, keep every workflow-created Shopify product
 * in step with the supplier: stock, price, compare-at price and listing status.
 *
 * Works from the "Drafts Stock and Price Changes" tab (one row per product the
 * workflow created). Every change is written to "Drafts Change Log", and the
 * product's Website Qty is updated in "Website Stock" (matched by title).
 *
 * Rules
 *  - In the stock file: Shopify stock = supplier tier (1-19 -> 1, 20-29 -> 2,
 *    30-39 -> 3, 40-49 -> 4, 50+ -> 5). Price and compare-at use the same
 *    calculation as the Clean Variant tabs.
 *  - Missing from the stock file (or supplier stock 0): stock 0 and status UNLISTED.
 *    Never deleted.
 *  - Back in the stock file after being unlisted: ACTIVE if the product has at
 *    least one photo, otherwise DRAFT until photos are added.
 *  - Products still in DRAFT that are in stock stay DRAFT. ARCHIVED products are
 *    left alone.
 *  - Safety: if more than 20% of tracked products (and at least 5) would be
 *    unlisted in one go, nothing is changed and an alert email is sent.
 *
 * SETUP (one-off) – see the instructions Claude sent with this file:
 *  Project Settings > Script Properties:
 *    SHOPIFY_SHOP           your-store.myshopify.com
 *    SHOPIFY_CLIENT_ID      from the Dev Dashboard app
 *    SHOPIFY_CLIENT_SECRET  from the Dev Dashboard app
 *  (or SHOPIFY_ADMIN_TOKEN instead of the two above, for an older shpat_ token)
 */

const SYNC = {
  TRACK_TAB: 'Drafts Stock and Price Changes',
  CHANGELOG_TAB: 'Drafts Change Log',
  WEBSITE_TAB: 'Website Stock',
  API_VERSION: '2026-10',
  LOCATION_ID: 'gid://shopify/Location/93812949332',
  MAX_UNLIST_SHARE: 0.2,
  MIN_UNLIST_ALERT: 5,
  TIME_BUDGET_MS: 5 * 60 * 1000   // stop before Apps Script's 6-minute limit; resumes next hour
};

// Tracking tab columns (1-based)
const C = { BC: 1, WS_TITLE: 2, TITLE: 3, CAT: 4, PID: 5, VID: 6, IID: 7, SUP_STOCK: 8, QTY: 9,
            SUP_PRICE: 10, PRICE: 11, CMP: 12, STATUS: 13, PHOTOS: 14, CHECKED: 15, CHANGE: 16, ROW: 17 };
const TRACK_COLS = 17;

/* ---------------------------------------------------------------- menu hooks */

function syncDraftsPreview() {
  const msg = syncDrafts({ dryRun: true });
  SpreadsheetApp.getUi().alert(msg);
}

function syncDraftsManual() {
  const ui = SpreadsheetApp.getUi();
  if (ui.alert('Update Shopify now?', 'This applies stock, price and status changes to Shopify for every tracked product.',
      ui.ButtonSet.OK_CANCEL) !== ui.Button.OK) return;
  ui.alert(syncDrafts({ force: true }));
}

/** Called by the hourly trigger: runs only when an import is waiting to be synced. */
function syncDraftsIfPending() {
  if (PropertiesService.getScriptProperties().getProperty('syncPending') === 'yes') return syncDrafts({});
  return 'No sync pending.';
}

/* ---------------------------------------------------------------- main job */

function syncDrafts(opts) {
  opts = opts || {};
  const dry = opts.dryRun === true;
  const started = Date.now();
  const props = PropertiesService.getScriptProperties();
  const lock = LockService.getScriptLock();
  if (!lock.tryLock(30000)) return 'Another sync is running; try again in a few minutes.';
  try {
    const ss = SpreadsheetApp.getActive();
    const track = ss.getSheetByName(SYNC.TRACK_TAB);
    if (!track || track.getLastRow() < 2) return 'Tracking tab is empty; nothing to sync.';
    const runId = Utilities.formatDate(new Date(), CONFIG.TIMEZONE, 'dd/MM/yyyy HH:mm') + (dry ? ' preview' : '');

    // 1. Supplier data from the imported stock file, keyed by barcode without leading zeros.
    const supplier = readStockfile_(ss);
    if (supplier.count < CONFIG.MIN_ROWS) {
      log_('Sync skipped', 'Stockfile Import has only ' + supplier.count + ' rows');
      return 'Sync skipped: Stockfile Import looks incomplete (' + supplier.count + ' rows).';
    }

    // 2. Tracked products and their live Shopify state.
    const rows = track.getRange(2, 1, track.getLastRow() - 1, TRACK_COLS).getValues();
    const items = rows.map((r, i) => ({ sheetRow: i + 2, r: r, bc: String(r[C.BC - 1]).trim() }))
                      .filter(it => it.bc && String(it.r[C.PID - 1]).trim());
    const live = fetchLive_(items.map(it => 'gid://shopify/Product/' + String(it.r[C.PID - 1]).trim()));

    // 3. Work out the target state for every product.
    const plans = items.map(it => plan_(it, supplier.map[it.bc.replace(/^0+/, '')], live));

    // 4. Safety check: too many products disappearing at once usually means a bad file.
    const newlyUnlisted = plans.filter(p => p.live && p.out && p.live.status !== 'UNLISTED' && p.live.status !== 'ARCHIVED').length;
    // A manual "Update Shopify now" overrides this check (you have looked at the file).
    if (newlyUnlisted >= SYNC.MIN_UNLIST_ALERT && newlyUnlisted > plans.length * SYNC.MAX_UNLIST_SHARE && !opts.force) {
      const why = newlyUnlisted + ' of ' + plans.length + ' tracked products are missing from the stock file';
      if (!dry) {
        MailApp.sendEmail(Session.getEffectiveUser().getEmail(), 'ALERT: Drafts sync stopped (' + runId + ')',
          why + '. Nothing was changed in Shopify. Check the stock file, then use Workflow > Update Shopify now if it is correct.');
        props.setProperty('syncPending', 'no');
        log_('Sync stopped', why);
      }
      return 'Sync stopped: ' + why + '. Nothing changed.';
    }

    // 5. Apply.
    const ws = websiteIndex_(ss);
    const logger = changeLogger_(ss, runId, dry);
    const token = dry ? null : shopifyToken_();
    let done = 0, changed = 0, failed = 0, timedOut = false;

    // Stock first, in batches (one call per 50 products).
    const qtyPlans = plans.filter(p => p.live && p.qtyChange);
    for (let i = 0; i < qtyPlans.length; i += 50) {
      const batch = qtyPlans.slice(i, i + 50);
      let err = null;
      if (!dry) err = setQuantities_(token, batch);
      batch.forEach(p => {
        p.qtyResult = err ? 'FAILED: ' + err : (dry ? 'PREVIEW' : 'OK');
        logger.add(p, 'Stock', p.live.available, p.target.qty, p.qtyResult, p.reason);
      });
    }

    for (const p of plans) {
      if (Date.now() - started > SYNC.TIME_BUDGET_MS) { timedOut = true; break; }
      done++;
      const notes = [];
      if (!p.live) {
        logger.add(p, 'Lookup', '', '', 'NOT FOUND', 'Product not found in Shopify (deleted?)');
        writeTrackRow_(track, p, dry, 'NOT FOUND in Shopify');
        failed++;
        continue;
      }
      if (p.live.status === 'ARCHIVED') {
        writeTrackRow_(track, p, dry, 'Archived in Shopify, left alone');
        continue;
      }
      let ok = !(p.qtyResult && p.qtyResult.indexOf('FAILED') === 0);
      if (p.qtyChange) notes.push('stock ' + p.live.available + '→' + p.target.qty);

      if (p.priceChange) {
        const res = dry ? 'PREVIEW' : updatePrice_(token, p);
        ok = ok && (res === 'OK' || res === 'PREVIEW');
        if (!same_(p.target.price, p.live.price)) logger.add(p, 'Price £', p.live.price, p.target.price, res, p.reason);
        if (!same_(p.target.cmp, p.live.cmp)) logger.add(p, 'Compare-at £', p.live.cmp, p.target.cmp, res, p.reason);
        notes.push('price ' + p.live.price + '→' + p.target.price);
      }
      if (p.statusChange) {
        const res = dry ? 'PREVIEW' : updateStatus_(token, p);
        ok = ok && (res === 'OK' || res === 'PREVIEW');
        logger.add(p, 'Status', p.live.status, p.target.status, res, p.statusWhy);
        notes.push(p.live.status + '→' + p.target.status);
      }
      if (p.qtyChange || p.priceChange || p.statusChange) changed++;
      if (!ok) failed++;

      // Website Stock: keep Website Qty aligned with what Shopify now holds.
      const wsChanged = ws.set(p.wsTitle, p.target.qty, dry);
      if (wsChanged) logger.add(p, 'Website Stock qty', wsChanged.old, p.target.qty, dry ? 'PREVIEW' : 'OK', 'Website Stock row ' + wsChanged.rows.join(', '));
      else if (!ws.has(p.wsTitle)) logger.add(p, 'Website Stock qty', '', p.target.qty, 'NOT FOUND', 'No Website Stock row titled "' + p.wsTitle + '"');

      writeTrackRow_(track, p, dry, notes.length ? (ok ? '' : 'FAILED: ') + notes.join('; ') : '');
      logger.flushIfBig();
    }
    logger.flush();
    ws.flush(dry);
    SpreadsheetApp.flush();

    const summary = (dry ? 'Preview: ' : '') + done + ' of ' + plans.length + ' products checked, ' + changed +
      (dry ? ' would change' : ' changed') + (failed ? ', ' + failed + ' problems' : '') +
      (timedOut ? '. Time limit reached: the rest continue at the next hourly run.' : '.');
    if (!dry) {
      props.setProperty('syncPending', timedOut ? 'yes' : 'no');
      log_('Drafts sync', summary);
      if (failed) MailApp.sendEmail(Session.getEffectiveUser().getEmail(), 'Drafts sync: ' + failed + ' problems (' + runId + ')',
        summary + ' See the "' + SYNC.CHANGELOG_TAB + '" tab for details.');
    }
    return summary + ' Details in "' + SYNC.CHANGELOG_TAB + '".';
  } finally {
    lock.releaseLock();
  }
}

/* ---------------------------------------------------------------- planning */

function plan_(it, sup, live) {
  const r = it.r;
  const pid = 'gid://shopify/Product/' + String(r[C.PID - 1]).trim();
  const lv = live[pid] || null;
  const p = { it: it, bc: it.bc, title: r[C.TITLE - 1], wsTitle: String(r[C.WS_TITLE - 1] || '').trim(), live: lv, sup: sup || null };
  if (sup && sup.name && !p.wsTitle) p.wsTitle = sup.name;
  if (!lv) return p;

  const supStock = sup ? sup.stock : 0;
  const qty = tierQty_(supStock);
  p.out = !sup || qty === 0;
  p.target = {
    qty: qty,
    price: sup && sup.price !== null ? websitePrice_(sup.price) : lv.price,
    cmp: sup && sup.price !== null ? compareAt_(websitePrice_(sup.price), it.bc) : lv.cmp,
    status: lv.status
  };
  p.reason = !sup ? 'Not in stock file' : 'Supplier stock ' + supStock + ', price £' + sup.price;

  if (lv.status !== 'ARCHIVED') {
    if (p.out && lv.status !== 'UNLISTED') {
      p.target.status = 'UNLISTED';
      p.statusWhy = !sup ? 'Not in stock file: out of stock' : 'Supplier stock 0';
    } else if (!p.out && lv.status === 'UNLISTED') {
      p.target.status = lv.photos > 0 ? 'ACTIVE' : 'DRAFT';
      p.statusWhy = 'Back in stock' + (lv.photos > 0 ? '' : ' but no photos yet: kept as draft');
    }
  }
  p.qtyChange = lv.available !== p.target.qty;
  p.priceChange = !p.out && (!same_(p.target.price, lv.price) || !same_(p.target.cmp, lv.cmp));
  p.statusChange = p.target.status !== lv.status;
  return p;
}

/** Same calculations as the Clean Variant tabs. */
function tierQty_(st) { return st >= 50 ? 5 : st >= 40 ? 4 : st >= 30 ? 3 : st >= 20 ? 2 : st >= 1 ? 1 : 0; }

function ceilTo_(x, step) { return Math.ceil(Math.round(x / step * 1e9) / 1e9) * step; }

function same_(a, b) { return (a === null || b === null) ? a === b : Math.abs(a - b) < 0.005; }

function round2_(x) { return Math.round(x * 100) / 100; }

function websitePrice_(pr) {
  return round2_(ceilTo_(round2_((pr + 4.95) * 1.2) + 5 - 0.49, 0.5) + 0.49);
}

function compareAt_(price, bc) {
  const d = String(bc).replace(/\D/g, '');
  const pct = d ? 0.25 + ((Number(d.slice(-7)) * 7919) % 1101) / 10000 : 0.3;
  return round2_(ceilTo_(price * (1 + pct) - 0.99, 1) + 0.99);
}

/* ---------------------------------------------------------------- sheets */

function readStockfile_(ss) {
  const sh = ss.getSheetByName(CONFIG.IMPORT_TAB);
  const v = sh.getDataRange().getDisplayValues();
  const h = v[0].map(x => String(x).trim());
  const iBc = h.indexOf('Barcode'), iSt = h.indexOf('Stock Level'), iPr = h.indexOf('Price'), iNm = h.indexOf('Name');
  const map = {};
  for (let i = 1; i < v.length; i++) {
    const name = String(v[i][iNm]).trim();
    if (!name) continue;
    const st = parseInt(v[i][iSt], 10);
    const pr = parseFloat(v[i][iPr]);
    const rec = { name: name, stock: isNaN(st) ? 0 : st, price: isNaN(pr) ? null : pr };
    String(v[i][iBc]).split(',').forEach(b => {
      const k = b.trim().replace(/^0+/, '');
      if (k && !map[k]) map[k] = rec;
    });
  }
  return { map: map, count: v.length - 1 };
}

function writeTrackRow_(track, p, dry, note) {
  if (dry) return;
  const now = Utilities.formatDate(new Date(), CONFIG.TIMEZONE, 'dd/MM/yyyy HH:mm');
  const row = p.it.sheetRow;
  if (!p.live) {
    track.getRange(row, C.STATUS).setValue('NOT FOUND');
    track.getRange(row, C.CHECKED, 1, 2).setValues([[now, note]]);
    return;
  }
  const t = p.target || {};
  track.getRange(row, C.VID, 1, 2).setValues([[p.live.variantId.split('/').pop(), p.live.inventoryItemId.split('/').pop()]]);
  track.getRange(row, C.SUP_STOCK, 1, 9).setValues([[
    p.sup ? p.sup.stock : 'Not in file',
    t.qty !== undefined ? t.qty : p.live.available,
    p.sup && p.sup.price !== null ? p.sup.price : '',
    t.price !== undefined ? t.price : p.live.price,
    t.cmp !== undefined && t.cmp !== null ? t.cmp : '',
    t.status || p.live.status,
    p.live.photos > 0 ? 'Yes' : 'No',
    now,
    note ? now.slice(0, 10) + ': ' + note : track.getRange(row, C.CHANGE).getValue()
  ]]);
  if (!String(p.it.r[C.WS_TITLE - 1]).trim() && p.wsTitle) track.getRange(row, C.WS_TITLE).setValue(p.wsTitle);
}

/** Website Stock lookup by title (case and spacing ignored); updates every matching row. */
function websiteIndex_(ss) {
  const sh = ss.getSheetByName(SYNC.WEBSITE_TAB);
  const n = Math.max(sh.getLastRow() - 1, 0);
  const vals = n ? sh.getRange(2, 1, n, 2).getValues() : [];
  const idx = {};
  const key = t => String(t).replace(/\s+/g, ' ').trim().toLowerCase();
  vals.forEach((r, i) => { const k = key(r[0]); if (k) (idx[k] = idx[k] || []).push(i); });
  let dirty = false;
  return {
    has: t => !!idx[key(t)],
    set: (t, qty, dry) => {
      const hits = idx[key(t)];
      if (!hits) return null;
      const old = hits.map(i => vals[i][1]);
      if (old.every(o => Number(o) === qty && o !== '')) return null;
      if (!dry) { hits.forEach(i => { vals[i][1] = qty; }); dirty = true; }
      return { old: old.join('/'), rows: hits.map(i => i + 2) };
    },
    flush: dry => { if (dirty && !dry) sh.getRange(2, 2, n, 1).setValues(vals.map(r => [r[1]])); }
  };
}

function changeLogger_(ss, runId, dry) {
  const sh = ss.getSheetByName(SYNC.CHANGELOG_TAB) || (function () {
    const s = ss.insertSheet(SYNC.CHANGELOG_TAB);
    s.appendRow(['Time', 'Run', 'Barcode', 'Product', 'What changed', 'Old value', 'New value', 'Result', 'Note']);
    s.setFrozenRows(1);
    return s;
  })();
  let buf = [];
  const fmt = v => (v === null || v === undefined) ? '' : v;
  const api = {
    add: (p, what, oldV, newV, result, note) => buf.push([
      Utilities.formatDate(new Date(), CONFIG.TIMEZONE, 'dd/MM/yyyy HH:mm:ss'), runId, p.bc, p.title,
      what, fmt(oldV), fmt(newV), result, note || '']),
    flush: () => {
      if (!buf.length) return;
      const start = sh.getLastRow() + 1;
      sh.getRange(start, 3, buf.length, 1).setNumberFormat('@');
      sh.getRange(start, 1, buf.length, 9).setValues(buf);
      buf = [];
    },
    flushIfBig: () => { if (buf.length >= 20) api.flush(); }
  };
  return api;
}

/* ---------------------------------------------------------------- Shopify */

function shopifyToken_() {
  const props = PropertiesService.getScriptProperties();
  const fixed = props.getProperty('SHOPIFY_ADMIN_TOKEN');
  if (fixed) return fixed;
  const cache = CacheService.getScriptCache();
  const cached = cache.get('shopifyToken');
  if (cached) return cached;
  const shop = shopDomain_();
  const res = UrlFetchApp.fetch('https://' + shop + '/admin/oauth/access_token', {
    method: 'post',
    payload: { grant_type: 'client_credentials',
               client_id: props.getProperty('SHOPIFY_CLIENT_ID'),
               client_secret: props.getProperty('SHOPIFY_CLIENT_SECRET') },
    muteHttpExceptions: true
  });
  if (res.getResponseCode() !== 200) throw new Error('Shopify sign-in failed (' + res.getResponseCode() + '): ' + res.getContentText().slice(0, 300));
  const j = JSON.parse(res.getContentText());
  const ttl = Math.min(Math.max((j.expires_in || 3600) - 600, 300), 21600);
  cache.put('shopifyToken', j.access_token, ttl);
  return j.access_token;
}

function shopDomain_() {
  const s = PropertiesService.getScriptProperties().getProperty('SHOPIFY_SHOP');
  if (!s) throw new Error('Script property SHOPIFY_SHOP is not set');
  return s.replace(/^https?:\/\//, '').replace(/\/.*$/, '');
}

function gql_(token, query, variables) {
  for (let attempt = 0; attempt < 4; attempt++) {
    const res = UrlFetchApp.fetch('https://' + shopDomain_() + '/admin/api/' + SYNC.API_VERSION + '/graphql.json', {
      method: 'post', contentType: 'application/json',
      headers: { 'X-Shopify-Access-Token': token },
      payload: JSON.stringify({ query: query, variables: variables || {} }),
      muteHttpExceptions: true
    });
    const code = res.getResponseCode();
    const body = res.getContentText();
    if (code === 429 || code >= 500) { Utilities.sleep(2000 * (attempt + 1)); continue; }
    if (code !== 200) throw new Error('Shopify ' + code + ': ' + body.slice(0, 300));
    const j = JSON.parse(body);
    if (j.errors) {
      if (JSON.stringify(j.errors).indexOf('THROTTLED') !== -1) { Utilities.sleep(2000 * (attempt + 1)); continue; }
      throw new Error('Shopify: ' + JSON.stringify(j.errors).slice(0, 300));
    }
    return j.data;
  }
  throw new Error('Shopify kept refusing (rate limit); will retry next run');
}

/** Live state for many products: status, photos, price, compare-at, available stock. */
function fetchLive_(ids) {
  const token = shopifyToken_();
  const out = {};
  const q = 'query($ids:[ID!]!,$loc:ID!){nodes(ids:$ids){... on Product{id status mediaCount{count} ' +
            'variants(first:1){nodes{id price compareAtPrice inventoryItem{id inventoryLevel(locationId:$loc){quantities(names:["available"]){quantity}}}}}}}}';
  for (let i = 0; i < ids.length; i += 50) {
    const d = gql_(token, q, { ids: ids.slice(i, i + 50), loc: SYNC.LOCATION_ID });
    d.nodes.forEach(n => {
      if (!n || !n.id) return;
      const v = n.variants.nodes[0];
      if (!v) return;
      const lvl = v.inventoryItem.inventoryLevel;
      out[n.id] = {
        id: n.id, status: n.status, photos: n.mediaCount ? n.mediaCount.count : 0,
        variantId: v.id, inventoryItemId: v.inventoryItem.id,
        price: v.price === null ? null : round2_(Number(v.price)),
        cmp: v.compareAtPrice === null ? null : round2_(Number(v.compareAtPrice)),
        available: lvl && lvl.quantities.length ? lvl.quantities[0].quantity : 0
      };
    });
  }
  return out;
}

function setQuantities_(token, batch) {
  const m = 'mutation($input:InventorySetQuantitiesInput!,$key:String!){inventorySetQuantities(input:$input) @idempotent(key:$key){userErrors{field message}}}';
  try {
    const d = gql_(token, m, {
      key: Utilities.getUuid(),
      input: {
        name: 'available', reason: 'correction',
        referenceDocumentUri: 'gid://ambient-beauty/StockfileSync/' + Utilities.formatDate(new Date(), CONFIG.TIMEZONE, 'yyyyMMdd'),
        quantities: batch.map(p => ({ inventoryItemId: p.live.inventoryItemId, locationId: SYNC.LOCATION_ID,
                                      quantity: p.target.qty, changeFromQuantity: p.live.available }))
      }
    });
    const e = d.inventorySetQuantities.userErrors;
    return e.length ? e.map(x => x.message).join('; ') : null;
  } catch (err) { return String(err.message || err); }
}

function updatePrice_(token, p) {
  const m = 'mutation($pid:ID!,$v:[ProductVariantsBulkInput!]!){productVariantsBulkUpdate(productId:$pid,variants:$v){userErrors{field message}}}';
  try {
    const d = gql_(token, m, { pid: p.live.id, v: [{ id: p.live.variantId, price: p.target.price.toFixed(2),
                                                     compareAtPrice: p.target.cmp === null ? null : p.target.cmp.toFixed(2) }] });
    const e = d.productVariantsBulkUpdate.userErrors;
    return e.length ? 'FAILED: ' + e.map(x => x.message).join('; ') : 'OK';
  } catch (err) { return 'FAILED: ' + (err.message || err); }
}

function updateStatus_(token, p) {
  const m = 'mutation($p:ProductUpdateInput!){productUpdate(product:$p){userErrors{field message}}}';
  try {
    const d = gql_(token, m, { p: { id: p.live.id, status: p.target.status } });
    const e = d.productUpdate.userErrors;
    return e.length ? 'FAILED: ' + e.map(x => x.message).join('; ') : 'OK';
  } catch (err) { return 'FAILED: ' + (err.message || err); }
}

/** Run from the editor to confirm the Shopify connection works. */
function testShopifyConnection() {
  const d = gql_(shopifyToken_(), '{shop{name myshopifyDomain}}');
  Logger.log('Connected to ' + d.shop.name + ' (' + d.shop.myshopifyDomain + ')');
  return d.shop.name;
}
