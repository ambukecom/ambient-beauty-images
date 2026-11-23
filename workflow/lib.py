"""Ambient Beauty listing helpers, used by every scheduled workflow run.

A run writes runs/<date>-b<batch>/build.py that does:
    import sys; sys.path.insert(0, "<repo>/workflow"); from lib import *
    F(...) / add(...)          # one call per product (see RUNBOOK.md for the standard)
    write_outputs()            # writes P.json + vars.json (productSet inputs i1..iN)
then, after the drafts exist:
    python3 -c "from lib import *; metafields('P.json', ids)"   -> mf.json (c0..cN)
"""
import json, re

LOC = "gid://shopify/Location/93812949332"
FREE = " Free UK delivery over £40."
STORE_ADMIN = "https://admin.shopify.com/store/f1d55c-f7/products/"

# ---- publications (8 channels; collections are published without the UK market) ----
PUBLICATIONS = ["211750551892", "211750322516", "211750519124", "214562865492",
                "284028698964", "285202121044", "285141631316", "307533545812"]

# ---- collections ----
COL = {
    "all1": "636660580692", "all2": "667912405332", "new": "636867641684",
    "Fragrances": "636468625748", "Haircare": "636468756820", "Bath & Body": "667722383700",
    "Makeup": "636468789588",
    "Men": "636542714196", "Women": "636636594516", "Unisex": "636637053268",
}
# Skincare / Makeup category collections: look up by title the first time and add here.
BRAND_COL = {
    "Hamidi": "716111348052", "Lattafa": "667451425108", "Maison Alhambra": "668572057940",
    "Lacoste": "711869399380", "Jean Paul Gaultier": "669660512596", "L'Oréal": "668571271508",
    "Paco Rabanne": "715110711636", "Molton Brown": "670228054356", "Moschino": "711213711700",
    "Paris Corner": "675531129172", "Street Origins": "735309398356", "Surrati": "720731210068",
    "Swiss Arabian": "693164081492", "Tommy Hilfiger": "669659431252", "Sol de Janeiro": "737218396500",
    "Dumont": "737079165268", "Clarins": "715842715988", "Ajmal": "707767140692",
    "Arabiyat Prestige": "711639204180", "Ahmed Al Maghribi": "688564437332",
    "Ard Al Zaafaran": "667485077844", "Ted Baker": "713988473172",
    "Armaf": "668574646612", "French Avenue": "672815546708", "Gulf Orchid": "713790980436",
    "Rasasi": "672893305172", "Rue Broca": "676211622228",
    "Abercrombie & Fitch": "709036835156", "Marc Jacobs": "710321733972", "Police": "711536705876", "Adidas": "715892785492",
    "Anna Sui": "715893637460", "Antonio Banderas": "709039128916",
    "Ariana Grande": "708990763348", "Azzaro": "669576757588", "Bentley": "709021696340", "Britney Spears": "709118689620",
    "Dolce & Gabbana": "669610017108", "Elie Saab": "709054103892", "Elizabeth Arden": "716106465620",
    "Estée Lauder": "668571795796", "Gisada": "709062918484", "Hermès": "737778991444", "Hugo Boss": "636872098132",
    "Issey Miyake": "669725557076", "Jimmy Choo": "714162897236",
    "Michael Kors": "710499959124", "Missoni": "710500811092", "Mont Blanc": "668574548308",
    "Ford Mustang": "713734259028", "Narciso Rodriguez": "711329939796",
    "Versace": "713749037396", "Zimaya": "672813580628",
    "Reebok": "713726230868", "Rochas": "713807626580", "Salvatore Ferragamo": "714017997140",
    "Burberry": "669620142420", "Bvlgari": "738036285780", "Cacharel": "709361992020",
    "Calvin Klein": "669662576980", "Carolina Herrera": "668571205972", "Cerruti": "715956060500",
    "Davidoff": "669676470612", "Bujairami": "711639531860",
}

# ---- taxonomy + Google product category ----
TAXON = {"perfume": "hb-3-2-8", "hair-perfume": "hb-3-2-8-6", "body-wash": "hb-3-2-1-5",
         "shampoo": "hb-3-10-13-3", "conditioner": "hb-3-10-13-1", "hair-treatment": "hb-3-10-14",
         "hair-mask": "hb-3-10-14-1", "mascara": "hb-3-2-6-3-8"}
GPC = {"fragrance": 479, "shampoo": 543615, "conditioner": 543616, "body-wash": 2747, "hair-care": 486, "mascara": 2834}

# ---- metaobject IDs (category metafields) ----
MO = {
    "target-gender": {"Men": "140156862804", "Women": "124573286740", "Unisex": "140156961108"},
    "age-group": {"Adults": "186959888724"},
    "product-form": {"Spray": "652353503572", "Gel": "652382994772", "Cream": "186959364436", "Liquid": "186959790420"},
    "dispenser-type": {"Spray": "151079813460"},
    "package-type": {"Bottle": "652385583444"},
    "suitable-for-hair-type": {"Fine": "660165460308", "Damaged": "186959921492", "Colored": "186959855956"},
    "conditioner-effect": {"Color protection": "186961559892", "Shine": "186961658196", "Detangling": "186961592660", "Strengthening": "660039237972"},
    "olfactory-family": {"Gourmand": "513199505748", "Citrus": "652353372500", "Spicy": "652353405268",
                         "Woody": "652353438036", "Musky": "652353470804", "Floral": "652383224148",
                         "Fruity": "652383256916", "Oriental": "652383289684", "Aromatic": "652383322452",
                         "Fresh": "652383355220", "Aquatic": "660039336276", "Leather": "652383387988",
                         "Powdery": "660039369044", "Fougere": "660165493076"},
    "fragrance": {"Floral": "148512866644", "Spicy": "148512932180", "Citrus": "652353536340",
                  "Woody": "652353601876", "Fruity": "652383420756", "Vanilla": "652383453524",
                  "Jasmine": "652383486292", "Fresh": "652383519060", "Rose": "652383551828",
                  "Lavender": "652383584596", "Sandalwood": "652383617364", "Aquatic": "660039303508",
                  "Oriental": "148512899412"},
    "color-pattern": {"Black": "652384010580"},
}
GG = {"Men": "male", "Women": "female", "Unisex": "unisex"}
TYPE = {"Men": "Men's Fragrance", "Women": "Women's Fragrance", "Unisex": "Unisex Fragrances"}

# ---------------------------------------------------------------- description HTML
def ul(items): return "<ul>" + "".join(f"<li>{x}</li>" for x in items) + "</ul>"
def kd(pairs): return ul([f"<strong>{a}:</strong> {b}" for a, b in pairs])

def body(hook, intro, blocks, details, love, qs):
    h = f"<p><em>{hook}</em></p><p>{intro}</p>"
    for t, c in blocks:
        h += f"<h2>{t}</h2>{c}"
    return (h + "<h2>Key details</h2>" + kd(details) + "<h2>Why you'll love it</h2>" + ul(love)
            + "<h2>FAQ</h2>" + "".join(f"<h3>{q}</h3><p>{a}</p>" for q, a in qs))

def handle(title):
    import unicodedata
    title = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode().replace("'", "")
    h = title.lower().replace(" & ", "-").replace("&", "and").replace("+", "")
    h = re.sub(r"[^a-z0-9]+", "-", h.replace(".", ""))
    return re.sub(r"-+", "-", h).strip("-")

def pyramid_answer(pyr):
    a = [" and ".join(v.lower().rsplit(", ", 1)) for _, v in pyr]
    cap = lambda s: s[0].upper() + s[1:]
    if len(a) == 3: return f"{cap(a[0])} first, then {a[1]}, finishing with {a[2]}."
    if len(a) == 2: return f"{cap(a[0])} first, finishing with {a[1]}."
    return cap(a[0]) + "."

P = []
def add(**k):
    """Generic product. Required: cat_name, bc, title, vendor, type, gender, cat (taxonomy id), price, cmp, qty,
    tags (>4 for non-fragrance), seo=(title<=60, desc<=160), desc (HTML), form, size, unit, note, status,
    mf={metafield key: [labels from MO]}, gpc (Google category number). Optional: handle."""
    k.setdefault("handle", handle(k["title"]))
    k.setdefault("status", "done")
    P.append(k)

def F(bc, vendor, title, gender, size, price, cmp, qty, pyr, profile, hook, intro, love, note, seo_d,
      of, fr, name, conc="Eau De Parfum", concl="Eau de Parfum", status="done", hair=False):
    """Fragrance (perfume or hair mist). pyr = [("Top","a, b"),("Heart",..),("Base",..)] or [] if unconfirmed.
    of / fr = olfactory family / fragrance labels from MO. Exactly 3 tags: brand, gender, concentration."""
    q2 = {"Unisex": ("Is it unisex?", "Yes, it is made for everyone."),
          "Men": ("Is it for men?", "Yes, it is a men's fragrance."),
          "Women": ("Is it for women?", "Yes, it is a women's fragrance.")}[gender]
    qs = ([(f"What does {name} smell like?", pyramid_answer(pyr))] if pyr else []) + [q2]
    add(cat_name="Fragrances", bc=bc, title=title, vendor=vendor, type=TYPE[gender], gender=gender,
        cat=TAXON["hair-perfume" if hair else "perfume"], price=price, cmp=cmp, qty=qty,
        tags=[vendor, gender, conc], seo=(title[:60], f"{title}: {seo_d}" + FREE), status=status,
        form=concl, size=size, unit="ml", note=note, gpc=GPC["fragrance"],
        mf={"age-group": ["Adults"], "product-form": ["Spray"], "dispenser-type": ["Spray"],
            "olfactory-family": list(of), "fragrance": list(fr)},
        desc=body(hook, intro, [("Scent pyramid", kd(pyr))] if pyr else [],
                  [("Brand", vendor), ("Concentration", concl), ("Size", f"{size}ml"),
                   ("Scent profile", profile), ("Wear", gender)], love, qs))

# ---------------------------------------------------------------- outputs
def write_outputs(path="."):
    inputs = {}
    for i, p in enumerate(P, 1):
        assert len(p["seo"][0]) <= 60 and len(p["seo"][1]) <= 160, (p["title"], len(p["seo"][0]), len(p["seo"][1]))
        if p["cat_name"] == "Fragrances":
            assert len(p["tags"]) == 3, p["title"]
        else:
            assert len(p["tags"]) > 4, p["title"]
        inputs[f"i{i}"] = {
            "title": p["title"], "handle": p["handle"], "status": "DRAFT", "vendor": p["vendor"],
            "productType": p["type"], "category": "gid://shopify/TaxonomyCategory/" + p["cat"],
            "tags": p["tags"], "descriptionHtml": p["desc"],
            "seo": {"title": p["seo"][0], "description": p["seo"][1]},
            "productOptions": [{"name": "Title", "values": [{"name": "Default Title"}]}],
            "variants": [{"optionValues": [{"optionName": "Title", "name": "Default Title"}],
                          "price": p["price"], "compareAtPrice": p["cmp"], "barcodes": [{"value": p["bc"]}],
                          "inventoryItem": {"tracked": True},
                          "inventoryQuantities": [{"locationId": LOC, "name": "available", "quantity": p["qty"]}]}]}
    json.dump(inputs, open(f"{path}/vars.json", "w"), ensure_ascii=False)
    json.dump(P, open(f"{path}/P.json", "w"), ensure_ascii=False)
    for p in P:
        print(p["title"], "|", len(p["seo"][0]), len(p["seo"][1]))
    print("productSet mutation:", productset_mutation(len(P)))

def productset_mutation(n):
    return ("mutation(" + ",".join(f"$i{i}:ProductSetInput!" for i in range(1, n + 1)) + "){" +
            " ".join(f"p{i}: productSet(synchronous:true, input:$i{i}){{ product{{ id variants(first:1){{nodes{{id inventoryItem{{id}}}}}} }} userErrors{{ field message }} }}"
                     for i in range(1, n + 1)) + "}")

def metafields(p_json, ids, path="."):
    """ids = [(product_gid, variant_gid), ...] in P order. Writes mf.json with c0..cN and prints the mutation."""
    P_ = json.load(open(p_json))
    out = {}
    for i, (p, (pid, vid)) in enumerate(zip(P_, ids)):
        L = []
        def s(key, labels):
            ref = [f"gid://shopify/Metaobject/{MO[key][x]}" for x in labels]
            if ref:
                L.append({"ownerId": pid, "namespace": "shopify", "key": key,
                          "type": "list.metaobject_reference", "value": json.dumps(ref)})
        if p["cat"] != TAXON["mascara"]:  # mascara category has no target-gender attribute
            s("target-gender", [p["gender"]])
        for key, labels in p.get("mf", {}).items():
            s(key, labels)
        L.append({"ownerId": pid, "namespace": "mm-google-shopping", "key": "google_product_category",
                  "type": "single_line_text_field", "value": str(p["gpc"])})
        for k, val in [("gender", GG[p["gender"]]), ("age_group", "adult"), ("condition", "new"),
                       ("size_type", "regular"), ("size_system", "UK")]:
            L.append({"ownerId": vid, "namespace": "mm-google-shopping", "key": k,
                      "type": "single_line_text_field", "value": val})
        out[f"c{i}"] = L
    json.dump(out, open(f"{path}/mf.json", "w"))
    n = len(out)
    print("mutation(" + ",".join(f"$c{i}:[MetafieldsSetInput!]!" for i in range(n)) + "){" +
          " ".join(f"c{i}: metafieldsSet(metafields:$c{i}){{ userErrors{{ field message }} }}" for i in range(n)) + "}")

def collections_and_publish(p_json, pids):
    """Prints one mutation: join collections + publish to all 8 channels, for each product."""
    P_ = json.load(open(p_json))
    parts = []
    for i, (p, pid) in enumerate(zip(P_, pids)):
        cat = COL.get(p["cat_name"])
        brand = BRAND_COL.get(p["vendor"])
        cols = [COL["all1"], COL["all2"], COL["new"]] + ([cat] if cat else []) + [COL[p["gender"]]] + ([brand] if brand else [])
        if not cat: print(f"!! no category collection for {p['cat_name']}: look it up and add to COL")
        if not brand: print(f"!! no brand collection for {p['vendor']}: look it up (or create it) and add to BRAND_COL")
        cj = ",".join(f'"gid://shopify/Collection/{c}"' for c in cols)
        parts.append(f'u{i}: productUpdate(product:{{id:"{pid}",collectionsToJoin:[{cj}]}}){{ userErrors{{ message }} }}')
        pubs = ",".join(f'{{publicationId:"gid://shopify/Publication/{x}"}}' for x in PUBLICATIONS)
        parts.append(f'p{i}: publishablePublish(id:"{pid}", input:[{pubs}]){{ userErrors{{ message }} }}')
    print("mutation {\n" + "\n".join(parts) + "\n}")
