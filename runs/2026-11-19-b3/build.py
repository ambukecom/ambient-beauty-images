import sys; sys.path.insert(0, "/home/claude/ambient-beauty-images/workflow")
from lib import *
AJ, AS, AB = "Ajmal", "Anna Sui", "Antonio Banderas"
TC = dict(conc="Eau De Toilette", concl="Eau de Toilette")

# ---------------- Ajmal
t = "Ajmal My Stellar Eau de Parfum 100ml"
F("6293708018901", AJ, t, "Unisex", "100", "27.99", "35.99", 1,
  [("Top", "Bergamot, Lemon, Pink Grapefruit"), ("Heart", "Magnolia, Jasmine, Peach Blossom"), ("Base", "Vanilla, Orchid, Amber, Musk")],
  "Floral · Fruity · Musky", "A bright citrus-floral that dries down soft and sweet.",
  f"{t} opens with sparkling bergamot, lemon and pink grapefruit, moves into a floral heart of magnolia, jasmine and peach blossom, and settles on a smooth base of vanilla, orchid, amber and musk.",
  ["A sparkling citrus opening of bergamot and pink grapefruit", "A soft floral heart of magnolia and jasmine", "A warm, sweet base of vanilla, amber and musk", "Eau de Parfum strength from Ajmal"],
  "Supplier gender Unisex kept; Ajmal's own site metadata says unisex but its copy, Parfumo and Alshaya market it for women. EAN 6293708018901 matched in Ajmal Bahrain product page URL (100ml EDP). Pyramid agreed by Ajmal BH, Parfumo, Alshaya (blackcurrant, rose, almond only on 2 of 3, left out). Awaiting photos.",
  "citrus and pink grapefruit over magnolia, jasmine and vanilla.", ["Floral", "Fruity", "Musky"], ["Citrus", "Floral", "Jasmine", "Vanilla"],
  name="My Stellar")

t = "Ajmal Silver Shade Eau de Parfum 100ml"
F("6293708005352", AJ, t, "Unisex", "100", "20.99", "27.99", 1,
  [("Top", "Bergamot, Lemon, Blackcurrant"), ("Heart", "Iris, Rose, Jasmine"), ("Base", "Musk, Cedarwood, Sandalwood, Tonka Bean")],
  "Citrus · Floral · Woody", "A fresh citrus scent with a clean, woody finish.",
  f"{t} is a fresh, versatile fragrance first launched in 2012. Bergamot, lemon and blackcurrant open crisply, a floral heart of iris, rose and jasmine follows, and it settles on musk, cedarwood, sandalwood and tonka bean.",
  ["A crisp citrus opening of bergamot and lemon", "An elegant heart of iris, rose and jasmine", "A clean base of cedarwood, sandalwood and musk", "Easy to wear every day"],
  "Supplier gender Unisex kept; ScentVerdict lists it unisex, Ajmal India and Alshaya market it for men. EAN 6293708005352 not found online (Notino/Anabis pages failed to load). Pyramid agreed by Ajmal India (description), Alshaya and ScentVerdict (lime, plum, violet leaf, amber, civet only on 2 of 3, left out). 2012 per ScentVerdict. Awaiting photos.",
  "bergamot and lemon over iris, rose, cedar and sandalwood.", ["Citrus", "Floral", "Woody"], ["Citrus", "Floral", "Rose", "Jasmine", "Woody", "Sandalwood"],
  name="Silver Shade")

# ---------------- Anna Sui
t = "Anna Sui Sky Eau de Toilette 75ml"
F("0085715064752", AS, t, "Women", "75", "24.49", "31.99", 5,
  [("Top", "Pear, Bergamot, Pink Pepper"), ("Heart", "Lily of the Valley, Rose, Lotus"), ("Base", "Musk, Vanilla, Popcorn")],
  "Fruity · Floral · Gourmand", "A dreamy, fruity-floral with a playful popcorn twist.",
  f"{t} is a light-hearted fruity floral with a sweet gourmand touch. Juicy pear, bergamot and pink pepper open brightly, a heart of lily of the valley, rose and lotus follows, and it settles on musk, vanilla and a playful popcorn accord.",
  ["A juicy pear and bergamot opening", "A soft floral heart of rose and lotus", "A sweet, cosy base of vanilla and popcorn", "Light Eau de Toilette for everyday wear"],
  "EAN 0085715064752 not shown online (The Perfume Shop's 50ml shows 0085715064509). 75ml EDT confirmed by Escentual and Justmylook. Pyramid agreed by Escentual, Justmylook, Parfumo (The Perfume Shop base differs: vanilla, peppercorn). Launch 2020 (Parfumo) vs 2021 (TPS), so not stated. Store has Sky 50ml (UNLISTED) – different size, not a duplicate. Awaiting photos.",
  "pear and bergamot over rose, lotus, vanilla and popcorn.", ["Fruity", "Floral", "Gourmand"], ["Fruity", "Citrus", "Floral", "Rose", "Vanilla"],
  name="Sky", **TC)

t = "Anna Sui Sui Dreams Eau de Toilette 50ml"
F("0085715081872", AS, t, "Women", "50", "22.49", "30.99", 5,
  [("Top", "Bergamot, Tangerine, Bitter Orange"), ("Heart", "Rose, Freesia, Peony, Peach"), ("Base", "Vanilla, Sandalwood, Cedarwood, Musk")],
  "Floral · Fruity · Oriental", "A sweet, sunny floral classic from Anna Sui.",
  f"{t} is a much-loved floral first launched in 2000. Bergamot, tangerine and bitter orange open with sunny citrus, a heart of rose, freesia, peony and peach follows, and it settles on vanilla, sandalwood, cedarwood and soft musk.",
  ["A sunny citrus opening of bergamot and tangerine", "A romantic heart of rose, freesia and peony", "A warm base of vanilla and sandalwood", "A classic from the Anna Sui collection"],
  "EAN 0085715081872 not shown online (supplier lists alt EAN 0085715089977). 50ml EDT confirmed by Anna Sui brand site and Justmylook. Pyramid agreed by annasui.com and NST (Osmoz/LookFantastic agree on most notes; nectarine on 3 sources but not Osmoz, left out). 2000 per Osmoz and NST. Awaiting photos.",
  "citrus and tangerine over rose, freesia, vanilla and sandalwood.", ["Floral", "Fruity", "Oriental"], ["Citrus", "Floral", "Rose", "Fruity", "Vanilla", "Sandalwood", "Woody"],
  name="Sui Dreams", **TC)

# ---------------- Antonio Banderas
BS_PYR = [("Top", "Melon, Bergamot, Pear, Violet Leaf"), ("Heart", "Bulgarian Rose, Gardenia, Jasmine, Lily of the Valley, Peony"), ("Base", "Raspberry, Patchouli, Musk, Benzoin")]
for bc, size, price, cmp, extra in [
    ("8411061081587", "200", "24.49", "33.99", "Supplier alt EAN 8411061739877 matched on French Fragrance 200ml page; 200ml EDT also confirmed by Perfumania (6.75oz)."),
    ("8411061982105", "80", "22.49", "29.99", "EAN 8411061982105 not shown online (French Fragrance 80ml page shows 8411061839669); 80ml EDT confirmed by French Fragrance and Perfumania.")]:
    t = f"Antonio Banderas Blue Seduction for Women Eau de Toilette {size}ml"
    F(bc, AB, t, "Women", size, price, cmp, 5, BS_PYR,
      "Fruity · Floral · Fresh", "A fresh, fruity floral full of light and energy.",
      f"{t} is a fresh fruity floral first launched in 2008. Melon, bergamot, pear and violet leaf open brightly, a floral heart of Bulgarian rose, gardenia, jasmine, lily of the valley and peony follows, and it settles on raspberry, patchouli, musk and benzoin.",
      ["A juicy opening of melon and pear", "A rich floral heart of rose, gardenia and jasmine", "A soft base of raspberry, musk and benzoin", "Fresh and easy to wear every day"],
      extra + " Pyramid agreed by Parfumo and Perfumania (all tiers; Osmoz gives a shorter list: pear, lemon, raspberry, white musk). 2008 per Osmoz, Parfumo. Store has the men's Blue Seduction 200ml – different product. Awaiting photos.",
      "melon and pear over rose, jasmine, raspberry and musk.", ["Fruity", "Floral", "Fresh"], ["Fruity", "Citrus", "Floral", "Rose", "Jasmine"],
      name="Blue Seduction for Women", **TC)

# Diavolo gift set
t = "Antonio Banderas Diavolo for Men Eau de Toilette 50ml Gift Set with 75ml Aftershave Balm"
seo_t = "Antonio Banderas Diavolo EDT 50ml & Aftershave Balm Set"
pyr = [("Top", "Mandarin, Bergamot, Green Leaves"), ("Heart", "Patchouli, Pepper"), ("Base", "Leather, Musk, Sandalwood")]
contents = ["Diavolo for Men Eau de Toilette 50ml (spray)", "Diavolo for Men Aftershave Balm 75ml"]
qs = [("What does Diavolo smell like?", pyramid_answer(pyr)), ("What's in the set?", "; ".join(contents) + "."), ("Is it for men?", "Yes, it is a men's fragrance gift set.")]
add(cat_name="Fragrances", bc="8411061044995", title=t, vendor=AB, type=TYPE["Men"], gender="Men", cat=TAXON["perfume"],
    price="24.49", cmp="30.99", qty=5, tags=[AB, "Men", "Eau De Toilette"],
    seo=(seo_t, f"{seo_t}: mandarin and bergamot over patchouli, leather and musk." + FREE),
    form="Eau de Toilette Gift Set", size="50", unit="ml", gpc=GPC["fragrance"],
    mf={"age-group": ["Adults"], "product-form": ["Spray"], "dispenser-type": ["Spray"], "olfactory-family": ["Woody", "Spicy", "Leather"], "fragrance": ["Citrus", "Spicy", "Woody", "Sandalwood"]},
    note="EAN 8411061044995 and contents (50ml EDT + 75ml aftershave balm) confirmed by Superdrug (EAN in spec); contents also Galaxus (GTIN 8411061091647, supplier alt EAN), Cosmetify, Red Label. Pyramid agreed by SohoPerfume and MyPerfumeShop (Parfumo After Shave agrees); Red Label gives a different pyramid (grapefruit, elemi, star anise, ambergris, tonka), left out. Awaiting photos.",
    desc=body("A bold, devilishly charming classic for him.",
              f"{t} pairs the original Diavolo for Men with a matching aftershave balm. Mandarin, bergamot and green leaves open freshly, a spicy heart of patchouli and pepper follows, and it settles on leather, musk and sandalwood.",
              [("What's in the set", ul(contents)), ("Scent pyramid", kd(pyr))],
              [("Brand", AB), ("Concentration", "Eau de Toilette"), ("Contents", "Eau de Toilette 50ml + Aftershave Balm 75ml"),
               ("Scent profile", "Woody · Spicy · Leather"), ("Wear", "Men")],
              ["A fresh opening of mandarin and bergamot", "A spicy heart of pepper and patchouli", "A sensual base of leather, musk and sandalwood", "Aftershave balm to soothe and layer the scent"], qs))

t = "Antonio Banderas Essence of Success Eau de Toilette 100ml"
F("8411061117071", AB, t, "Men", "100", "22.99", "30.99", 1,
  [("Top", "Bergamot, Green Apple"), ("Heart", "Lavender, Sage, Geranium"), ("Base", "Patchouli, Amber")],
  "Aromatic · Fougere · Fresh", "A fresh, confident aromatic fougère.",
  f"{t} is a fresh aromatic fougère for men. Bergamot and green apple open crisply, an aromatic heart of lavender, sage and geranium follows, and it settles on warm patchouli and amber.",
  ["A crisp opening of bergamot and green apple", "A classic aromatic heart of lavender and sage", "A warm base of patchouli and amber", "Fresh and versatile for day or night"],
  "EAN 8411061117071 not shown online. 100ml EDT for him confirmed by Heinemann (travel retail) and Cosmetify. Pyramid agreed by ScentVerdict, Cosmetify, Heinemann (all tiers; Parfumo lists only rose and turmeric, left out). Aromatic fougère per Cosmetify/Heinemann. Awaiting photos.",
  "bergamot and green apple over lavender, sage and amber.", ["Aromatic", "Fougere", "Fresh"], ["Citrus", "Fruity", "Lavender", "Fresh"],
  name="Essence of Success", **TC)

t = "Antonio Banderas Her Secret Absolu Eau de Parfum 80ml"
F("8411061088593", AB, t, "Women", "80", "23.49", "29.99", 5,
  [("Top", "Pear, Apricot, Orange"), ("Heart", "Orange Blossom, Rose, Pink Pepper"), ("Base", "Vanilla, Benzoin, Labdanum, Sandalwood")],
  "Fruity · Floral · Oriental", "A warm, fruity-floral amber with a vanilla glow.",
  f"{t} is a warm, fruity-floral amber scent. Pear, apricot and orange open juicily, a heart of orange blossom, rose and pink pepper follows, and it settles on a cosy base of vanilla, benzoin, labdanum and sandalwood.",
  ["A juicy opening of pear and apricot", "A floral heart of orange blossom and rose", "A cosy base of vanilla and sandalwood", "Eau de Parfum strength"],
  "EAN matched on The Perfume Spot (UPC 08411061088593, 2.7oz/80ml EDP, women). Pyramid agreed by The Perfume Spot and ScentVerdict (all tiers); Perfume.com gives a different list (pomegranate, peony, musk), left out. Launch year conflicts (2019 vs 2024), not stated. Awaiting photos.",
  "pear and apricot over orange blossom, rose and vanilla.", ["Fruity", "Floral", "Oriental"], ["Fruity", "Citrus", "Floral", "Rose", "Vanilla", "Sandalwood"],
  name="Her Secret Absolu")

t = "Antonio Banderas King of Seduction Absolute Eau de Toilette 100ml"
F("8411061081341", AB, t, "Men", "100", "23.49", "30.99", 5,
  [("Top", "Grapefruit, Pomelo, Green Almond"), ("Heart", "Sea Notes, Lavender, Cardamom"), ("Base", "Leather, Oakmoss, Vetiver")],
  "Aquatic · Aromatic · Woody", "A fresh, magnetic aquatic for him.",
  f"{t} is a fresh aquatic fragrance first launched in 2015. Grapefruit, pomelo and green almond open brightly, a heart of sea notes, lavender and cardamom follows, and it settles on leather, oakmoss and vetiver.",
  ["A bright citrus opening of grapefruit and pomelo", "A fresh marine heart with lavender and cardamom", "A sensual base of leather, oakmoss and vetiver", "Fresh and easy to wear every day"],
  "EAN 8411061081341 not shown online. 100ml EDT for men per ScentVerdict and Parfum-Centrum. Pyramid agreed by ScentVerdict, Parfum-Centrum, Reach.dog, NearStore (wormwood/absinthe top on 3 of 4, left out; Parfumo and Perfume.com list different notes). 2015 per ScentVerdict, Parfum-Centrum. Store has King of Seduction EDT (original) – different product. Awaiting photos.",
  "grapefruit and pomelo over sea notes, lavender and leather.", ["Aquatic", "Aromatic", "Woody"], ["Citrus", "Aquatic", "Lavender", "Woody"],
  name="King of Seduction Absolute", **TC)

SEO_T = {"8411061081587": "Antonio Banderas Blue Seduction for Women EDT 200ml",
         "8411061982105": "Antonio Banderas Blue Seduction for Women EDT 80ml",
         "8411061081341": "Antonio Banderas King of Seduction Absolute EDT 100ml"}
for p in P:
    p["desc"] = p["desc"].replace("bulgarian", "Bulgarian")
    p["seo"] = (SEO_T.get(p["bc"], p["seo"][0]), p["seo"][1].replace("&amp;", "&"))
write_outputs()
