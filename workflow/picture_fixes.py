"""Build the "Picture Fixes" tab of Ambient_Beauty_Listing_Worksheet.

Lists every workflow draft that is not live (DRAFT or UNLISTED in Shopify) because it has no photo,
or only one, after photos were missing or rejected. The most common issue type comes first, so
repeated problems (wrong product photo, broken cut-out, ...) are grouped and easy to fix in bulk.

Usage:
  python3 picture_fixes.py build prod.json plan.json state.json existing.json done.json > rows.json
    prod.json     get_values of Products!A3:Y   ({"values": [...]})
    plan.json     get_values of 'Daily Plan'!A1:N
    state.json    {"gid://shopify/Product/<id>": ["DRAFT"|"UNLISTED"|"ACTIVE", mediaCount], ...}
    existing.json get_values of 'Picture Fixes'!A1:K (current tab, to keep ticks and run results)
    done.json     workflow/picture_fixes_done.json (owner-approved uploads, shown for 3 days)
  Prints {"rows", "sheet_rows" (write these with update_formulas from A1), "groups", "counts",
          "format" (update_spreadsheet requests that redo the group shading)}.
"""
import json, re, sys, datetime

HEADER = ["Fixed ✓", "Issue", "What's wrong", "What to do", "Barcode (folder)", "Product title",
          "Drive folder", "Shopify", "Status", "Photos now", "Last run result"]
NOTE_ROW = ("Tick 'Fixed ✓' once you have replaced the photos in the product's Drive folder (main.jpg = product, "
            "box.jpg = with box). The next scheduled run uploads ticked photos without rejecting them, "
            "then removes the row. Most common issues are listed first.")

# (issue name, regex on the reason text, what to do) – first match wins, in this order.
ISSUES = [
    ("File named wrongly",
     r"named|rename",
     "Rename the files to main.jpg (product) and box.jpg (with box)."),
    ("Wrong product in photo",
     r"\bnot (the |this |a )?[A-Z0-9]|\bdifferent\b|\binstead\b|holds .* photos|is the \d+ ?ml|reads \d+ ?ml|shows the \d+ ?ml|"
     r"photos (are|show) [A-Z]|is a [A-Z][a-z]+ [A-Z]|is [A-Z][\w'’]+ [\w'’]+ \(|box photo is [A-Z]|main is a [a-z ]*bottle|\bedition\b|"
     r"doesn'?t show|reads '|'Daily Cleansing|\bnot Intense|no 'Intense'|Hair & Body Wash|shows? the [A-Z][\w']+ [A-Z]",
     "Replace with photos of this exact product – check name, edition, size and set contents match the title."),
    ("Can't confirm it's this product",
     r"can'?t confirm|cannot confirm|can't be matched|generic .* box",
     "Add a clear photo where the product name / edition is readable on the bottle or box."),
    ("Not a product photo",
     r"advert|promo|graphic|swirl|sketch|texture|embossed panel|model\b",
     "Replace with a real photo of the bottle (main) and the bottle with its box (box)."),
    ("Cut-out broken (bottle lost, washed out or ragged)",
     r"cut-?out|washed out|ragged|jagged|fragment|sliver|breaks up|artefact|smudge|torn|disappears|edges lost|messy|unclean",
     "Re-shoot on a plain coloured (not white) background with good contrast, so the bottle cuts out cleanly."),
    ("Product too small or cropped",
     r"tiny|cropped|cut off|cap only|only the cap|close-up|cap fragment|banner|very small|blurry",
     "Take a closer photo with the whole product in frame (not cropped, product filling most of the picture)."),
    ("Low quality or watermark",
     r"watermark|low-res|low resolution|\d{2,3} ?x ?\d{2,3}",
     "Use your own clean, larger photo (no other shop's watermark)."),
    ("Photo missing",
     r"no main|no box|no photo|not in (the )?folder|awaiting photos|no main\.\*|please add",
     "Add main.jpg (product on its own) and box.jpg (product with its box) to the folder."),
]
ONE_PHOTO = ("Only one photo attached",
             "Add the missing photo (main.jpg = product, box.jpg = with box) or replace the rejected one.")
NO_PHOTO = ("Photo missing", "Add main.jpg (product on its own) and box.jpg (product with its box) to the folder.")
DONE = "Fixed – uploaded"


def pad(r, n): return list(r) + [""] * (n - len(r))


def photo_reason(note, plan_m):
    """The short photo-problem text: Daily Plan column M if it says rejected/partial, else from the note."""
    m = (plan_m or "").strip()
    if re.match(r"rejected", m, re.I):
        return re.sub(r"^rejected\s*[–-]\s*", "", m, flags=re.I)
    if re.search(r"\((box|main) only|1 image|rejected", m, re.I):
        return re.sub(r"^attached\s*", "", m).strip("() ")
    n = note or ""
    x = re.search(r"\b(Main|Box|Second) photo NOT attached[^:]*:\s*(?:it is |it's )?([^.]+)", n, re.I)
    if x:
        return f"{x.group(1).title()} photo rejected – {x.group(2).strip()}"
    for pat in (r"Photos? (?:NOT attached|rejected)[^:]*:\s*(.+?)(?:\s*[–-]\s*please.*|\. Needs.*|\. Awaiting.*|$)",
                r"(Photo label reads[^.]*)",
                r"\(((?:main|box)[^)]*rejected[^)]*)\)",
                r"((?:main|box) photo (?:rejected|not attached)[^.;)]*)",
                r"(no (?:main|box)[^.;)]*)"):
        x = re.search(pat, n, re.I | re.S)
        if x:
            return x.group(1).strip().rstrip(".")
    return ""


def classify(reason, photos):
    for name, rx, todo in ISSUES:
        if reason and re.search(rx, reason, re.I if name != "Wrong product in photo" else 0):
            return name, todo
    if reason and re.search(r"(?i)\bnot\b|different", reason):
        return next((n, t) for n, _, t in ISSUES if n == "Wrong product in photo")
    return ONE_PHOTO if photos else NO_PHOTO


def build(prod, plan, state, existing, done, today=None):
    today = today or datetime.date.today()
    P = [pad(r, 25) for r in prod]
    D = {pad(r, 14)[6].strip().lstrip("'"): pad(r, 14) for r in plan[1:]}
    ex = {}
    for r in existing[2:]:
        r = pad(r, 11)
        bc = str(r[4]).strip().lstrip("'")
        if bc:
            ex[bc] = {"tick": str(r[0]).upper() == "TRUE", "result": r[10]}
    items = []
    seen = set()
    for r in P:
        m = re.search(r"products/(\d+)", r[23])
        bc = str(r[10]).strip().lstrip("'")
        if not m or not bc or bc in seen:
            continue
        gid = "gid://shopify/Product/" + m.group(1)
        st = state.get(gid)
        if not st or st[0] not in ("DRAFT", "UNLISTED") or st[1] is None or st[1] >= 2:
            continue
        seen.add(bc)
        reason = photo_reason(r[24], D.get(bc, pad([], 14))[12])
        reason = re.sub(r"^1 image;\s*", "", reason)
        if reason.count("(") > reason.count(")"):
            reason += ")"
        issue, todo = classify(reason, st[1])
        if not reason:
            reason = "No photos have been added yet" if st[1] == 0 else "Only one of the two photos is attached"
        prev = ex.get(bc, {})
        items.append([prev.get("tick", False), issue, reason[:1].upper() + reason[1:], todo, "'" + bc, r[4],
                      r[19], "https://admin.shopify.com/store/f1d55c-f7/products/" + m.group(1),
                      st[0].title(), st[1], prev.get("result", "")])
    counts = {}
    for it in items:
        counts[it[1]] = counts.get(it[1], 0) + 1
    items.sort(key=lambda it: (-counts[it[1]], it[1], it[5].lower()))
    # Owner-approved uploads from the last 3 days, shown at the bottom as confirmation.
    recent = []
    for d in done:
        try:
            when = datetime.datetime.strptime(d["date"], "%d/%m/%Y").date()
        except Exception:
            continue
        if (today - when).days <= 3 and d["barcode"] not in seen:
            recent.append([False, DONE, d.get("detail", "Owner-approved photos uploaded"), "Nothing – check the listing",
                           "'" + d["barcode"], d["title"], d.get("folder", ""), d.get("shopify", ""), d.get("status", "Draft"),
                           d.get("photos", ""), "Uploaded " + d["date"]])
    rows = [[NOTE_ROW] + [""] * 10, HEADER] + items + recent
    groups, start = [], 2
    for i in range(2, len(rows) + 1):
        if i == len(rows) or rows[i][1] != rows[start][1]:
            groups.append([start + 1, i, rows[start][1]])   # 1-based sheet rows
            start = i
    return {"rows": rows, "groups": groups, "counts": counts, "format": format_requests(groups, len(rows))}


def sheet_rows(rows):
    """Rows ready for update_formulas: links become HYPERLINK formulas."""
    out = [list(r) for r in rows]
    for r in out[2:]:
        if r[6] and not str(r[6]).startswith("="):
            r[6] = f'=HYPERLINK("{r[6]}","Open folder")'
        if r[7] and not str(r[7]).startswith("="):
            r[7] = f'=HYPERLINK("{r[7]}","Open in Shopify")'
    return out


def format_requests(groups, nrows, sheet_id=2300):
    """Alternate shading per issue group + a line above each group (after clearing old shading)."""
    rng = lambda r0, r1, c0, c1: {"sheetId": sheet_id, "startRowIndex": r0, "endRowIndex": r1,
                                  "startColumnIndex": c0, "endColumnIndex": c1}
    col = lambda h: {"rgbColor": {"red": int(h[1:3], 16) / 255, "green": int(h[3:5], 16) / 255, "blue": int(h[5:7], 16) / 255}}
    req = [{"repeatCell": {"range": rng(2, 1000, 1, 11), "cell": {"userEnteredFormat": {"backgroundColorStyle": col("#FFFFFF")}},
                           "fields": "userEnteredFormat.backgroundColorStyle"}},
           {"updateBorders": {"range": rng(2, 1000, 0, 11), "innerHorizontal": {"style": "NONE"}, "top": {"style": "NONE"}}}]
    for i, (a, b, _) in enumerate(groups):
        req.append({"repeatCell": {"range": rng(a - 1, b, 1, 11),
                                   "cell": {"userEnteredFormat": {"backgroundColorStyle": col(["#ECEFF1", "#FFFFFF"][i % 2])}},
                                   "fields": "userEnteredFormat.backgroundColorStyle"}})
        req.append({"updateBorders": {"range": rng(a - 1, b, 0, 11),
                                      "top": {"style": "SOLID_MEDIUM", "colorStyle": col("#90A4AE")}}})
    return req


if __name__ == "__main__":
    if len(sys.argv) != 7 or sys.argv[1] != "build":
        sys.exit(__doc__)
    L = lambda p: json.load(open(p))
    V = lambda p: L(p).get("values", []) if isinstance(L(p), dict) else L(p)
    out = build(V(sys.argv[2]), V(sys.argv[3]), L(sys.argv[4]), V(sys.argv[5]), L(sys.argv[6]))
    out["sheet_rows"] = sheet_rows(out["rows"])
    json.dump(out, sys.stdout, ensure_ascii=False)
