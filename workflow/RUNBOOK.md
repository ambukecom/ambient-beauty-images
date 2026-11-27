# Ambient Beauty – scheduled draft run (runbook)

Read this whole file before doing anything. It is the standing procedure for the four daily
scheduled runs (00:10, 06:10, 12:10, 18:10 UK time). Each run creates **10 Shopify DRAFTS**.
Nobody is watching: never ask questions, decide sensibly, flag doubts in the worksheet notes,
and report at the end.

## Files and IDs
| What | ID / location |
|---|---|
| Supplier Vs Website (Google Sheet) | `1h19ssZfD2nZxabmu0TPXBkCpjUQlbmzlk5WdmunAW6w` |
| Ambient_Beauty_Listing_Worksheet (Google Sheet) | `1SUnFbCIZl87AH6sLiUYFKKZHkmANSBwes5TD6SJFNA8` |
| Drive "Product Images" folder | `18basmN8GWnhplngT_Sb5gIvNp4v3lfCJ` |
| Shopify store | `f1d55c-f7.myshopify.com` (Admin GraphQL 2026-10) |
| Image robot repo | GitHub `ambukecom/ambient-beauty-images` (needs push access) |
| Listing helpers | `workflow/lib.py` in that repo |

Supplier Vs Website tabs: `Fragrance / Skincare / Haircare / Makeup / Bath and Body Clean Variant`
(B Brand, C Product name, D Form, E Size, F Unit, G Gender, H Barcode, I Price £, J Compare-at £, K Stock Qty),
`Stockfile Import` (J Name = supplier title, I Barcode), `Website Stock` (A Product Title, B Website Qty),
`Drafts Stock and Price Changes` (sync tracking list, cols A–Q).

Worksheet tabs: `Products` (A–Y; row 2 is the header; column B is a formula, never write it),
`Daily Plan` (A–N), `Picture Fixes Verified` (sheetId 2301; A Verified on, B Barcode, C Title, D Issue that was
fixed, E What was wrong, F Photos, G Shopify status, H Drive folder, I Shopify), `Picture Fixes` (sheetId 2300; row 1 note, row 2 header, data from row 3:
A Fixed ✓ checkbox, B Issue, C What's wrong, D What to do, E Barcode, F Title, G Drive folder, H Shopify,
I Status, J Photos now, K Last run result). Built by `workflow/picture_fixes.py`.

## Step 0 – set up
1. Work out today's date and which run this is from the **UK time** now:
   00:00–05:59 → batch 1, 06:00–11:59 → batch 2, 12:00–17:59 → batch 3, 18:00–23:59 → batch 4.
2. Make sure the repo is available at a local path with push access. If it is not in the session,
   attach `ambukecom/ambient-beauty-images` with push access and clone it. `git pull` first.
   Work in `runs/<yyyy-mm-dd>-b<batch>/` inside the repo (commit it at the end).
3. Read the `Daily Plan` tab.

## Step 1 – the day's plan (batch 1 creates it for all 40)
If the Daily Plan has **no rows for today**, create the plan now for this batch **and every later batch
of the day** (batch 1 → 4 batches = 40 items; batch 3 → batches 3 and 4 = 20 items, and so on).

Choosing items (per batch of 10): **2 from each category** – Fragrance, Skincare, Haircare, Makeup,
Bath and Body – taken from the top of each Clean Variant tab; **Fragrance fills any shortfall**.
Skip anything already planned (any date), already in the worksheet Products tab (same barcode), or
with Stock Qty 0. Before planning an item, **check Shopify for duplicates**:
`productVariants(query:"barcode:<bc>")` and separate `products(query:"title:*<key words>*")` searches
(individual queries, never OR-joined titles). A duplicate is not planned; instead append it to
Website Stock (supplier stockfile Name, qty `0`) so it drops out of the Clean Variant tabs, and
pick the next item. Skip items whose identity is unclear (e.g. supplier name contradicts itself) and
mention them in the report.

For every planned item:
- Create a Drive folder inside Product Images named **`<barcode> - <Clean Variant product name>`**.
  If a folder for that barcode already exists, reuse it.
- Append a Daily Plan row: A date (dd/MM/yyyy), B batch, C run time (00:10 / 06:10 / 12:10 / 18:10),
  D category, E brand, F product name, G barcode (text), H folder name, I folder link,
  J `planned`, K–N blank.

If there are fewer items left than needed, plan what exists and say so in the report.
If today's plan already exists, do not re-plan: just use this batch's rows.

## Step 2 – check this batch's items are still valid
For each `planned` row of this batch: re-check the Clean Variant tab (still listed, stock > 0) and
Shopify (no duplicate created since). If not valid, set J to `skipped – <reason>`, and if it is
a duplicate add it to Website Stock with qty 0. Do **not** pull replacements from later batches.

## Step 3 – research (2 sources each)
For every item, confirm the facts with **two independent sources** (brand site, reputable retailers;
an EAN match is a strong source). Fragrance: scent pyramid (only notes both sources agree on; if top/
heart/base disagree, show only the agreed tiers and say so in the note), concentration, size.
Other categories: what it is, key ingredients/claims, who it suits, how to use, size.
- **Gender: always keep the supplier's gender.** If retailers market it differently, say so in the note.
- Never invent facts. If something can't be confirmed, leave it out and mark the row `needs-review`.

## Step 4 – build the drafts (listing standard)
Write `runs/<date>-b<n>/build.py` using `workflow/lib.py` (`from lib import *`), one call per product,
then `write_outputs()`. Look at an earlier `runs/*/build.py` for tone and structure.

**Fragrances** (`F(...)`): title `"<Brand> <Name> <Concentration> <size>ml"`; exactly **3 tags**:
Brand, Gender, Concentration (e.g. `Eau De Parfum`); product type Men's Fragrance / Women's Fragrance /
Unisex Fragrances; taxonomy perfume `hb-3-2-8` (hair mists `hair=True` → `hb-3-2-8-6`); description:
italic hook, intro paragraph, Scent pyramid, Key details, Why you'll love it (4 bullets), FAQ
("What does X smell like?" built automatically + gender question). Olfactory family / fragrance
labels must come from `MO` in lib.py.

**Other categories** (`add(...)`): more than 4 tags (brand, gender, category, product type, range,
key benefits); product type = category name; correct taxonomy (`TAXON`); description: hook, intro,
sections such as Key ingredients / Suits / Scent / How to use / Good to know, then Key details,
Why you'll love it, FAQ; `mf` with the relevant category metafields (age-group, product-form,
hair type, conditioner effect, fragrance…) and `gpc` from `GPC`.

All products: SEO title ≤ 60 chars, SEO description ≤ 160 chars ending with " Free UK delivery over £40.";
price, compare-at and quantity **exactly as the Clean Variant tab**; barcode as text with leading zeros;
status **DRAFT** (never ACTIVE). If a metaobject label you need is not in `MO`, look it up
(`metaobjects(type:"shopify--<key>")`) and add it to `MO` in lib.py (commit it).

Create in Shopify, with large payloads passed as variables (the GraphQL document limit is 16384 chars):
1. `productSet` for all products (mutation printed by `write_outputs()`, variables from vars.json).
   Record product, variant and inventory-item IDs.
2. `metafields('P.json', [(pid, vid), …])` → run the printed `metafieldsSet` mutation with mf.json.
3. `collections_and_publish('P.json', [pid, …])` → run the printed mutation. If it reports a missing
   brand collection, find it by title or create it (`collectionCreate(collection:{…})`, published to
   the 7 channels without the UK market) and add it to `BRAND_COL`.
4. Check every userErrors list is empty. Fix and retry anything that failed.
Deprecated fields are rejected: use `barcodes(first:N){nodes{value}}` not `barcode`, `productUpdate
collectionsToJoin` not `collectionAddProducts`, `collectionCreate(collection:)` not `input:`.

## Step 5 – record everything
- **Products tab** (worksheet): append one row per draft: A `done` or `needs-review`, B leave empty,
  C category, D brand, E title, G form, H size, I unit, J gender, K barcode, N `£price`, O `£compare-at`,
  Q qty, T folder link, W date written as MM/dd/yyyy (the sheet shows it as dd/MM/yyyy), X `https://admin.shopify.com/store/f1d55c-f7/products/<id>`,
  Y note (sources used, any doubts, "Awaiting photos." unless photos were attached).
  needs-review is flagged **only** here, never as a Shopify tag.
- **Website Stock**: append each draft's **supplier stockfile Name** (Stockfile Import col J, matched by barcode)
  with its quantity.
- **Drafts Stock and Price Changes**: append A barcode (text), B supplier stockfile Name, C Shopify title,
  D category, E product ID (number only), F variant ID, G inventory item ID, H supplier stock level,
  I qty, J supplier price, K price, L compare-at, M `DRAFT`, N photos Yes/No, O blank,
  P `Created <dd/MM/yyyy> run <n>`, Q worksheet row.
- **Daily Plan**: J `drafted`, K product ID, L worksheet row.

## Step 6a – picture fixes the owner ticked (every run, BEFORE step 6)
The owner ticks **Fixed ✓** in the `Picture Fixes` tab after replacing photos in a product's Drive folder.
A tick means "please process my new photos". **They are still checked like any other photo**: good ones
are uploaded, bad ones stay in Picture Fixes with the new reason.
1. Read `'Picture Fixes'!A3:K`. Take every row with A = TRUE.
2. For each, find the Drive folder (G link / barcode E). If the folder is not named with the barcode only,
   rename it to the barcode (Drive `update_file`) so the image robot can find it.
3. Add them to a robot job `jobs/<yyyy-mm-dd>-b<n>-fixes.json` (same format as step 6) with
   **slug = `<handle>-fix<yyyymmdd>`** (a new file name, so Shopify never gets a cached old image).
   Push, wait for `results/<job_id>.json`.
4. Make a contact sheet of the processed images (title + barcode above each pair) and **look at it** with the
   same standard as step 6c: right product (name, edition, size, set contents), whole product visible,
   clean cut-out (bottle not lost or washed out, no ragged edges, no fragments), no watermark, not an advert.
5. For each item, per photo (main / box):
   - Good → it replaces the product's current photo of the same kind: detach the old one with
     `fileUpdate(files:[{id:<media id>, referencesToRemove:["<product gid>"]}])` (the file stays in Shopify's
     Files library; nothing is deleted), then attach the new one (main first, then with-box) with the
     `productUpdate … media:` call from step 6.
   - Bad or missing → do not attach it; keep whatever is there now.
6. Record every product you looked at in `workflow/photo_checks.json` (see step 6c for the format) using the
   product's media ids **after** your changes, and write the row's K, e.g.
   "Rechecked dd/MM: main + box uploaded" or "Rechecked dd/MM: box still washed out – not uploaded".
   **Untick every row you processed** (write FALSE in A) before step 6b re-reads the tab.
   Never change a product's status here (drafts stay drafts).

## Step 6 – photos (every run, for all of today's and earlier drafts)
A folder is **ready** when the user has renamed it to the **barcode only** and put the photos in it
(`main.*` = product, `box.*` = with box).
1. Find every ready folder whose product has no photos in Shopify yet (`mediaCount` 0): this batch's
   new drafts plus any earlier drafts (check Daily Plan rows with Photos blank, and worksheet notes
   that say "Awaiting photos").
2. Write `jobs/<yyyy-mm-dd>-b<n>-photos.json`:
   `{"job_id": "...", "drive_root": "18basmN8GWnhplngT_Sb5gIvNp4v3lfCJ", "items": [{"barcode": "...", "slug": "<handle>"}]}`
   commit and push (commit message ends with the attribution lines in the session's instructions).
3. Wait for the GitHub Action to write `results/<job_id>.json` (poll `git pull` every 60 s, up to 15 min).
4. Download the processed images (`images/<bc>/<slug>.jpg`, `-with-box.jpg`) and make a contact sheet;
   **look at it**. Attach only good images: the right product (name/edition matches), not cropped,
   cut-out clean. Reject anything doubtful and say why in the note.
5. Attach with `productUpdate(product:{id}, media:$v)` (`CreateMediaInput`: originalSource = raw GitHub URL
   `https://raw.githubusercontent.com/ambukecom/ambient-beauty-images/main/images/<bc>/<file>`,
   alt text = product title [+ " with box"], mediaContentType IMAGE).
6. Update worksheet Y note (replace "Awaiting photos." with "Photos attached dd/MM." or the reason
   for rejection), Daily Plan M (`attached` / `rejected – reason`). Write rejection reasons short and
   specific (which photo, what is wrong): they become the "What's wrong" text in Picture Fixes.
7. Record each product you looked at in `workflow/photo_checks.json` (format in step 6c) with its media ids
   after attaching, so step 6c does not check it twice.
A folder not yet renamed is simply not ready: leave it for a later run.
Skip products handled in step 6a in this run.

## Step 6c – check the photos already on non-live drafts (every run, after step 6)
Every DRAFT or UNLISTED product the workflow created must have its attached photos checked once, and again
whenever they change. `workflow/photo_checks.json` remembers each check:
`{"<barcode>": {"media": ["<media id numbers>"], "verdict": "ok" | "one" | "fail", "issue": "<issue name>",
"reason": "<what is wrong, short and specific>", "date": "dd/mm/yyyy", "title": "<title>"}}`.
1. Query every workflow product: `products(query:"(status:draft OR status:unlisted) AND created_at:>=2026-10-25")`
   with `id status variants(first:1){nodes{barcodes(first:1){nodes{value}}}} media(first:6){nodes{id ... on MediaImage{image{url}}}}`
   (page through all, 100 per page). Save as state.json: `{"gid://shopify/Product/<id>": [status, mediaCount, [media ids]]}`.
2. Products whose media ids differ from photo_checks.json (or have no entry) need checking. The attached file is
   the robot's image: the file name in the media URL (after `/files/`, before `?`) is
   `images/<barcode>/<that name>` in this repo. Make contact sheets (8 products each, labelled MAIN / BOX)
   and **look at every image**.
3. Verdicts: `ok` = two good photos (main + with box); `one` = only one photo attached and it is good;
   `fail` = any attached photo is wrong product, cut-out broken, cropped / cap only, watermark, advert or
   graphic, or both photos are the same shot. Use the issue names from `workflow/picture_fixes.py` ISSUES.
   A failed photo stays on the draft (drafts are not live) until a good replacement is uploaded in step 6a.
4. Save photo_checks.json (commit it with the run).

## Step 6b – rebuild Picture Fixes, Picture Fixes Verified and the notes (every run, last of the photo steps)
1. Save to files: `Products!A3:Y` (get_values), `'Daily Plan'!A1:N`, state.json from step 6c,
   `'Picture Fixes Verified'!A1:I`, and **re-read `'Picture Fixes'!A1:K` now** (the owner may have ticked
   boxes during the run).
2. Run `python3 workflow/picture_fixes.py build prod.json plan.json state.json existing.json workflow/photo_checks.json verified.json > pf.json`.
   It lists every non-live draft with no photos or a failed / incomplete check (most common issue first),
   keeps ticks and run results, and returns:
   - `sheet_rows` + `format` for Picture Fixes (rows whose photos now pass are dropped, so the list shrinks);
   - `verified`: products that were on the list and now pass the check – append them to
     `'Picture Fixes Verified'` (A–I; write the barcode as plain text, links as HYPERLINK formulas);
   - `notes`: {worksheet row: "[Photo check dd/MM: …]"} for Products column Y;
   - `unchecked`: must be empty – if not, go back to step 6c.
3. Write Picture Fixes: `sheet_rows` from A1 with `update_formulas`; blank any old rows below with
   `update_values` of "" (empty `updateCells` does not clear); then the `format` requests. Do not touch the
   checkbox validation, conditional formats, column widths or filter.
4. Products notes: for each entry, one `findReplace` request limited to that Y cell, `searchByRegex: true`,
   first removing an older check (`find: "\\s*\\[Photo check [^\\]]*\\]"`, replacement ""), then appending
   (`find: "(?s)^(.*?)\\s*$"`, replacement `"$1 " + sentence`, with `$` in the sentence doubled).
   Never rewrite a whole note by hand.
5. Read back a few rows of each tab to check (barcodes keep leading zeros).

## Step 7 – finish
1. Commit `runs/…` and any lib.py changes, push.
2. Send the owner one short message (SendUserMessage): batch n of 4 for <date>; drafts created (titles);
   ticked picture fixes uploaded / still wrong (and why); products moved to Picture Fixes Verified;
   Picture Fixes rows left by issue;
   skipped items and why; needs-review items and why; photos attached / rejected; items left in the
   Clean Variant tabs. If anything failed, say exactly what and what was left undone.

## Safety rules
- Every photo is reviewed before it is attached, including photos the owner ticked in Picture Fixes.
- Create **drafts only**. Never set a product ACTIVE, never delete products, never edit products that
  this workflow did not create.
- Never overwrite existing sheet rows; append, or update only the specific cells named above.
- If Shopify or Sheets errors persist after a retry, stop that item, record it, and continue with the rest.
