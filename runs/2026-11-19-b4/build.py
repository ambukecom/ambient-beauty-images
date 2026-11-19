import sys; sys.path.insert(0, "/home/claude/ambient-beauty-images/workflow")
from lib import *
TC = dict(conc="Eau De Toilette", concl="Eau de Toilette")

# ---------------- Antonio Banderas
t = "Antonio Banderas Queen of Seduction Eau de Toilette 80ml"
F("8411061081846", "Antonio Banderas", t, "Women", "80", "23.49", "31.99", 5,
  [("Top", "Grapefruit, Raspberry, Water Accord"), ("Heart", "Jasmine, Iris, Peony, Pink Pepper"), ("Base", "Amber")],
  "Fruity · Floral · Fresh", "A fresh, fruity floral made to captivate.",
  f"{t} is the women's partner to King of Seduction, first launched in 2016. Grapefruit, raspberry and a watery accord open brightly, a floral heart of jasmine, iris, peony and pink pepper follows, and it settles on warm amber.",
  ["A juicy opening of grapefruit and raspberry", "A floral heart of jasmine, iris and peony", "A warm amber finish", "Light Eau de Toilette for everyday wear"],
  "EAN 8411061081846 matched on Proshop.no (80ml EDT, women). Pyramid agreed by Proshop and ScentVerdict (NST flat list agrees); base woods disagree (sandalwood/skin accord vs suede/cedar), so only amber shown. 2016 per ScentVerdict and NST. Awaiting photos.",
  "grapefruit and raspberry over jasmine, iris and amber.", ["Fruity", "Floral", "Fresh"], ["Citrus", "Fruity", "Floral", "Jasmine"],
  name="Queen of Seduction", **TC)

# ---------------- Ard Al Zaafaran gift set
AZ = "Ard Al Zaafaran"
t = "Ard Al Zaafaran Turab Al Dhahab Eau de Parfum 100ml Gift Set with 250ml Body Mist and 300ml Air Freshener"
seo_t = "Ard Al Zaafaran Turab Al Dhahab EDP 100ml 3-Piece Gift Set"
pyr = [("Top", "Bergamot, Lime, Tangerine, Coconut"), ("Heart", "Jasmine, Hibiscus, Ylang-Ylang, Ginger"), ("Base", "Sugar Cane, White Musk")]
contents = ["Turab Al Dhahab Eau de Parfum 100ml (spray)", "Turab Al Dhahab Body Mist 250ml", "Turab Al Dhahab Air Freshener 300ml"]
qs = [("What does Turab Al Dhahab smell like?", pyramid_answer(pyr)), ("What's in the set?", "; ".join(contents) + "."),
      ("Is it for women?", "Yes, it is a women's fragrance gift set.")]
add(cat_name="Fragrances", bc="6423080724118", title=t, vendor=AZ, type=TYPE["Women"], gender="Women", cat=TAXON["perfume"],
    price="28.49", cmp="37.99", qty=3, tags=[AZ, "Women", "Eau De Parfum"],
    seo=(seo_t, "Turab Al Dhahab gift set: EDP 100ml, body mist and air freshener. Citrus, coconut and jasmine." + FREE),
    form="Eau de Parfum Gift Set", size="100", unit="ml", gpc=GPC["fragrance"], status="needs-review",
    mf={"age-group": ["Adults"], "product-form": ["Spray"], "dispenser-type": ["Spray"],
        "olfactory-family": ["Fruity", "Floral", "Gourmand"], "fragrance": ["Citrus", "Fruity", "Floral", "Jasmine"]},
    note="NEEDS REVIEW: EAN 6423080724118 not found online (only an unloadable Walmart hit). Set contents (100ml EDP + 250ml mist + 300ml air freshener) confirmed by Triple Traders; Cosmetify lists the EDP gift set (women). Other Turab sets exist with different contents (EDP + deodorant, EDP + 50ml spray) – please check the box. Pyramid agreed by Triple Traders, Almanaar, Perfume.com, Intense Oud; TJ Hughes and ScentVerdict give a different pyramid (lime/coconut/vanilla/nutmeg/musk). Supplier gender Women kept (Perfume.com says unisex; Triple Traders files it under men). Awaiting photos.",
    desc=body("A sunny, tropical gift set wrapped in gold.",
              f"{t} brings together the Turab Al Dhahab Eau de Parfum with a matching body mist and air freshener. Bergamot, lime, tangerine and coconut open with tropical brightness, a heart of jasmine, hibiscus, ylang-ylang and ginger follows, and it settles on sweet sugar cane and white musk.",
              [("What's in the set", ul(contents)), ("Scent pyramid", kd(pyr))],
              [("Brand", AZ), ("Concentration", "Eau de Parfum"), ("Contents", "Eau de Parfum 100ml + Body Mist 250ml + Air Freshener 300ml"),
               ("Scent profile", "Fruity · Floral · Gourmand"), ("Wear", "Women")],
              ["A bright citrus and coconut opening", "A heart of jasmine, hibiscus and ylang-ylang", "A soft, sweet base of sugar cane and white musk", "Scent yourself and your home with one fragrance"], qs))

# ---------------- Ariana Grande
t = "Ariana Grande MOD Blush Eau de Parfum 100ml"
F("0810101500060", "Ariana Grande", t, "Women", "100", "51.49", "69.99", 1,
  [("Top", "Bergamot, Passionfruit, Raspberry, Pink Pepper"), ("Heart", "Magnolia, Rose, Pear"), ("Base", "Ambrox, Dreamwood, Musk")],
  "Fruity · Floral · Musky", "A juicy, rosy blush of fruit and flowers.",
  f"{t} is a modern fruity floral from Ariana Grande's MOD collection, first launched in 2022. Bergamot, passionfruit, raspberry and pink pepper open juicily, a heart of magnolia, rose and pear follows, and it settles on Ambrox, dreamwood and soft musks.",
  ["A juicy opening of passionfruit and raspberry", "A dewy heart of magnolia, rose and pear", "A smooth, skin-like base of Ambrox and musk", "Eau de Parfum strength"],
  "EAN 0810101500060 not shown online. 100ml EDP confirmed by LookFantastic, Sephora, Lyko. Pyramid agreed by LookFantastic, McGrocer, Parfumo, ScentVerdict (sandalwood only on Parfumo/ScentVerdict, left out). 2022 per Parfumo and ScentVerdict. Awaiting photos.",
  "passionfruit and raspberry over magnolia, rose and musk.", ["Fruity", "Floral", "Musky"], ["Fruity", "Citrus", "Floral", "Rose"],
  name="MOD Blush")

# ---------------- Armaf
t = "Armaf L'Homme Parfum Intense Eau de Parfum 100ml"
F("6294015165036", "Armaf", t, "Men", "100", "32.99", "41.99", 1,
  [("Top", "Lemon, Black Pepper, Bergamot"), ("Heart", "Orange Blossom, Artemisia, Violet Leaf"), ("Base", "Ambergris, Woody Notes, Benzoin, Suede, Cedar")],
  "Woody · Spicy · Citrus", "A bold, woody scent with a smooth suede finish.",
  f"{t} is a confident woody fragrance for men. Lemon, black pepper and bergamot open with a spicy-fresh spark, a heart of orange blossom, artemisia and violet leaf follows, and it settles on ambergris, woods, benzoin, suede and cedar.",
  ["A zesty, peppery opening of lemon and bergamot", "An aromatic heart of orange blossom and violet leaf", "A rich base of ambergris, suede and cedar", "Eau de Parfum strength"],
  "EAN 6294015165036 matched on Shop-Apotheke AT and Carrefour UAE (100ml, men). Not the same as Futura La Homme Intense. Concentration labelled 'Parfum' by Carrefour/Rackhams but EDP by Shop-Apotheke, ecosmetics, FilledWithBarakah and supplier – EDP kept. Pyramid agreed by McGrocer, Rackhams, Shop-Apotheke, FilledWithBarakah. Awaiting photos.",
  "lemon and black pepper over orange blossom, suede and cedar.", ["Woody", "Spicy", "Citrus"], ["Citrus", "Spicy", "Floral", "Woody"],
  name="L'Homme Parfum Intense")

t = "Armaf Signature True Eau de Parfum 100ml"
F("6294015101379", "Armaf", t, "Unisex", "100", "24.49", "32.99", 4,
  [("Top", "Pear, Tangerine, Bergamot"), ("Heart", "Strawberry, Passion Fruit"), ("Base", "Praline, Coffee, Caramel, Vanilla, Patchouli")],
  "Gourmand · Fruity · Oriental", "A sweet, fruity gourmand you'll want to keep wearing.",
  f"{t} is a sweet fruity gourmand. Pear, tangerine and bergamot open juicily, a heart of strawberry and passion fruit follows, and it settles on a cosy base of praline, coffee, caramel, vanilla and patchouli.",
  ["A juicy opening of pear and tangerine", "A playful heart of strawberry and passion fruit", "A cosy base of praline, coffee and vanilla", "Eau de Parfum strength"],
  "Supplier gender Unisex kept; eBay and Debenhams AU list it unisex, but Dubai Perfume Shop, Tira, Perfume.com market it for women. EAN 6294015101379 matched on eBay catalogue and Debenhams AU SKU (100ml EDP). Pyramid agreed by Debenhams AU, eBay, ScentVerdict, Dubai Perfume Shop (Parfumo EDP page unreliable, ignored). Awaiting photos.",
  "pear and tangerine over strawberry, praline and vanilla.", ["Gourmand", "Fruity", "Oriental"], ["Fruity", "Citrus", "Vanilla"],
  name="Signature True")

# ---------------- Azzaro
t = "Azzaro Chrome Azure Eau de Toilette 100ml"
F("3614274098440", "Azzaro", t, "Men", "100", "37.99", "50.99", 5,
  [("Top", "Bergamot"), ("Heart", "Lavender"), ("Base", "Marine Notes")],
  "Aromatic · Aquatic · Fresh", "A bright, sea-fresh take on Azzaro Chrome.",
  f"{t} is a fresh aquatic fragrance for men, launched in 2024. Green Italian bergamot opens brightly, French lavender gives an aromatic heart, and it settles on cool marine notes.",
  ["A bright opening of Italian bergamot", "A clean, aromatic heart of French lavender", "A cool marine finish", "Fresh and easy to wear every day"],
  "NEEDS REVIEW: supplier lists this as Eau de Parfum, but EAN 3614274098440 is the Eau de TOILETTE 100ml on Glam4u and Notino UK (image paths), and all retailers sell Chrome Azure as EDT – listed as EDT; please check the bottle. Pyramid agreed by Glam4u, Notino, Lyko (brand site gives the same flat list). 2024 per NST and ScentAdvice. Store has Azzaro Chrome EDT and Chrome Parfum (draft) – different products. Awaiting photos.",
  "bergamot over lavender and marine notes.", ["Aromatic", "Aquatic", "Fresh"], ["Citrus", "Lavender", "Aquatic", "Fresh"],
  name="Chrome Azure", status="needs-review", **TC)

t = "Azzaro Chrome Legend Eau de Toilette 100ml"
F("3614273962391", "Azzaro", t, "Men", "100", "32.49", "41.99", 5,
  [("Top", "Green Apple, Bitter Orange, Tea"), ("Heart", "Oakmoss, Musk, Sea Spray"), ("Base", "Cedar, Vetiver, Tonka Bean, Amber")],
  "Aromatic · Aquatic · Woody", "A fresh, green-citrus aquatic with a woody trail.",
  f"{t} is a fresh aromatic-aquatic fragrance for men from the Chrome family. Green apple, bitter orange and tea open crisply, a heart of oakmoss, musk and sea spray follows, and it settles on cedar, vetiver, tonka bean and amber.",
  ["A crisp opening of green apple and bitter orange", "A breezy heart of sea spray and oakmoss", "A warm base of cedar, vetiver and tonka", "Fresh and versatile for day or night"],
  "EAN 3614273962391 matched on ecosmetics (image/alt text, 3.38oz EDT). Pyramid agreed by perfumes.la and ecosmetics/Osmoz (ecosmetics puts tea in the heart; Parfumo puts musk/moss in the base). Launch 2007 vs 2008, not stated. Awaiting photos.",
  "green apple and bitter orange over sea spray and cedar.", ["Aromatic", "Aquatic", "Woody"], ["Citrus", "Fruity", "Aquatic", "Woody"],
  name="Chrome Legend", **TC)

# ---------------- Bentley
t = "Bentley For Men Silverlake Eau de Parfum 100ml"
F("7640171193403", "Bentley", t, "Men", "100", "35.99", "46.99", 5,
  [("Top", "Lemon, Peppermint"), ("Heart", "Lavender, Pink Pepper, Violet Leaf"), ("Base", "Ambery Woods, Musk")],
  "Aromatic · Aquatic · Woody", "A cool, refined freshness inspired by Silverlake.",
  f"{t} is a fresh aromatic fragrance from the Bentley For Men collection, launched in 2020. Lemon and peppermint open with a cool sparkle, a heart of lavender, pink pepper and violet leaf follows, and it settles on ambery woods and musk.",
  ["A cool opening of lemon and peppermint", "An aromatic heart of lavender and violet leaf", "A smooth base of ambery woods and musk", "Eau de Parfum strength"],
  "100ml EDP and pyramid agreed by Bentley Media press release, Justmylook, Red Label Outlet, Vperfumes. EAN 7640171193403 shown only in eBay/Beautyplaza search results (pages did not load). 2020 per Bentley Media and Motor1. Awaiting photos.",
  "lemon and peppermint over lavender, ambery woods and musk.", ["Aromatic", "Aquatic", "Woody"], ["Citrus", "Lavender", "Fresh", "Woody"],
  name="Silverlake")

t = "Bentley Infinite Intense Eau de Parfum 100ml"
F("7640163970029", "Bentley", t, "Men", "100", "31.99", "43.99", 5,
  [("Top", "Black Pepper, Geranium, Lavender, Violet Leaf"), ("Heart", "Nutmeg, Elemi, Benzoin, Ambergris"), ("Base", "Vetiver, Patchouli, Cedar, Moss")],
  "Spicy · Woody · Aromatic", "A deep, spicy-woody intensity for him.",
  f"{t} is a richer take on Bentley Infinite, launched in 2015. Black pepper, geranium, lavender and violet leaf open aromatically, a warm heart of nutmeg, elemi, benzoin and ambergris follows, and it settles on vetiver, patchouli, cedar and moss.",
  ["A peppery, aromatic opening of lavender and geranium", "A warm, resinous heart of nutmeg and benzoin", "A deep woody base of vetiver and cedar", "Eau de Parfum strength"],
  "EAN 7640163970029 matched on Triple Traders (UPC, 100ml EDP, men). Pyramid agreed by Parfumo, Justmylook, Triple Traders, TJ Hughes. 2015 per Parfumo, Triple Traders, TJ Hughes. Store has Bentley Infinite EDT 100ml and Infinite Rush – different products. Awaiting photos.",
  "black pepper and lavender over nutmeg, vetiver and cedar.", ["Spicy", "Woody", "Aromatic"], ["Spicy", "Lavender", "Woody"],
  name="Infinite Intense")

# ---------------- Britney Spears
t = "Britney Spears Circus Fantasy Eau de Parfum 100ml"
F("0719346567442", "Britney Spears", t, "Women", "100", "24.49", "32.99", 5,
  [("Top", "Raspberry, Apricot Blossom"), ("Heart", "Blue Peony, Orchid, Water Lily"), ("Base", "Vanilla, Musk, Violet Candy")],
  "Fruity · Floral · Gourmand", "A sweet, playful fruity floral from the Fantasy family.",
  f"{t} is a sweet, playful fruity floral. Sugared raspberry and apricot blossom open brightly, a heart of blue peony, orchid and water lily follows, and it settles on vanilla, musk and violet candy.",
  ["A sugary opening of raspberry and apricot blossom", "A soft floral heart of peony and orchid", "A sweet base of vanilla and violet candy", "Eau de Parfum strength"],
  "EAN 0719346567442 matched on The Perfume Spot and eBay catalogue (3.3oz/100ml EDP, women). Pyramid agreed by NST (official copy), eBay and Triple Traders. Launch 2009 only on one source, not stated. Awaiting photos.",
  "raspberry and apricot blossom over peony, vanilla and musk.", ["Fruity", "Floral", "Gourmand"], ["Fruity", "Floral", "Vanilla"],
  name="Circus Fantasy")

SEO_T = {"8411061081846": "Antonio Banderas Queen of Seduction EDT 80ml",
         "6294015165036": "Armaf L'Homme Parfum Intense Eau de Parfum 100ml",
         "7640171193403": "Bentley For Men Silverlake Eau de Parfum 100ml",
         "0719346567442": "Britney Spears Circus Fantasy Eau de Parfum 100ml"}
for p in P:
    p["seo"] = (SEO_T.get(p["bc"], p["seo"][0]), p["seo"][1].replace("&amp;", "&"))
    if len(p["seo"][1]) > 160:
        print("!! long seo desc", p["title"], len(p["seo"][1]))
write_outputs()
