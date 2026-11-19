import sys; sys.path.insert(0, "/home/claude/ambient-beauty-images/workflow")
from lib import *
AF = "Abercrombie & Fitch"
TC = dict(conc="Eau De Toilette", concl="Eau de Toilette")
COLOGNE = dict(conc="Eau De Cologne", concl="Eau de Cologne")

def GS(bc, vendor, title, seo_t, gender, size, price, cmp, qty, pyr, profile, hook, intro, contents, love, note, seo_d,
       of, fr, name, conc="Eau De Toilette", concl="Eau de Toilette", status="done"):
    """Fragrance gift set: fragrance standard (3 tags) plus a 'What's in the set' block."""
    q2 = {"Men": ("Is it for men?", "Yes, it is a men's fragrance gift set."),
          "Women": ("Is it for women?", "Yes, it is a women's fragrance gift set."),
          "Unisex": ("Is it unisex?", "Yes, it is made for everyone.")}[gender]
    qs = [(f"What does {name} smell like?", pyramid_answer(pyr)), ("What's in the set?", "; ".join(contents) + "."), q2]
    blocks = [("What's in the set", ul(contents)), ("Scent pyramid", kd(pyr))]
    add(cat_name="Fragrances", bc=bc, title=title, vendor=vendor, type=TYPE[gender], gender=gender, cat=TAXON["perfume"],
        price=price, cmp=cmp, qty=qty, tags=[vendor, gender, conc], seo=(seo_t, f"{seo_t}: {seo_d}" + FREE), status=status,
        form=concl + " Gift Set", size=size, unit="ml", note=note, gpc=GPC["fragrance"],
        mf={"age-group": ["Adults"], "product-form": ["Spray"], "dispenser-type": ["Spray"], "olfactory-family": list(of), "fragrance": list(fr)},
        desc=body(hook, intro, blocks,
                  [("Brand", vendor), ("Concentration", concl), ("Contents", " + ".join(c.split(" (")[0] for c in contents)),
                   ("Scent profile", profile), ("Wear", gender)], love, qs))


AD = "Adidas"
UNI = ("Supplier gender Unisex kept; Coty positions it as {pos}, while UK retailers (Superdrug/Boots) sell the Vibes range as 'For All'. ")

# ---------------- A&F gift sets and EDP
t = "Abercrombie & Fitch Fierce Eau de Cologne 100ml Gift Set with 10ml Travel Spray"
GS("0085715166685", AF, t, "A&F Fierce EDC 100ml & 10ml Travel Spray Gift Set", "Men", "100", "44.49", "59.99", 5,
   [("Top", "Lemon, Fir, Cardamom, Orange, Petitgrain"), ("Heart", "Lily of the Valley, Rosemary, Rose, Jasmine"), ("Base", "Oakmoss, Brazilian Rosewood, Musk, Vetiver")],
   "Aromatic · Woody · Fresh", "The legendary A&amp;F signature, at home and on the go.",
   f"{t} pairs a full-size bottle of the iconic Fierce, first launched in 2002, with a handy travel spray. Lemon, fir, cardamom, orange and petitgrain open freshly, a heart of lily of the valley, rosemary, rose and jasmine follows, and it settles on oakmoss, Brazilian rosewood, musk and vetiver.",
   ["Fierce Eau de Cologne 100ml (spray)", "Fierce Eau de Cologne 10ml (travel spray)"],
   ["The iconic A&amp;F signature scent", "Fresh citrus and fir with a hint of cardamom", "Travel spray for your bag or gym kit", "Ready to give as a gift"],
   "EAN and contents (100ml EDC + 10ml EDC) confirmed by Superdrug and World of Cosmetics (EAN pages); Cosmetify agrees on contents. Notes agreed by Parfumo and Notino (all tiers). Men per all sources. Store has Fierce 100ml/200ml and new 30/50ml drafts – not duplicates. Awaiting photos.",
   "lemon and fir over rosemary, musk and oakmoss, with travel spray.", ["Aromatic", "Woody", "Fresh"], ["Citrus", "Fresh", "Floral", "Woody"],
   name="Fierce", conc="Eau De Cologne", concl="Eau de Cologne")

t = "Abercrombie & Fitch First Instinct Extreme Eau de Parfum 100ml"
F("0085715167507", AF, t, "Men", "100", "34.99", "47.99", 4,
  [("Top", "Kiwano, Gin & Tonic"), ("Heart", "Violet Leaf, Sichuan Pepper, Citrus"), ("Base", "Amber, Suede, Musk")],
  "Fruity · Spicy · Woody", "A bolder, warmer take on First Instinct.",
  f"{t} is the intense 2018 version of First Instinct. Kiwano and a gin &amp; tonic accord open crisply, a heart of violet leaf, Sichuan pepper and citrus follows, and it settles into a warm base of amber, suede and musk.",
  ["A crisp kiwano and gin &amp; tonic opening", "A peppery heart of Sichuan pepper and violet leaf", "A warm, sensual base of amber and suede", "Eau de Parfum strength"],
  "Supplier name 'First Extreme Instinct' – retail name is First Instinct Extreme (title uses retail name). EAN 085715167507 matched on Paco Perfumerias UK (100ml EDP, him, 2018). Notes agreed by Parfumo and Notino (musk also ScentVerdict; cardamom, saffron, coconut only on ScentVerdict, left out). Launch 2018 per Parfumo, ScentVerdict. Awaiting photos.",
  "kiwano and gin &amp; tonic over pepper, amber and suede.", ["Fruity", "Spicy", "Woody"], ["Fruity", "Citrus", "Spicy", "Woody"],
  name="First Instinct Extreme")

t = "Abercrombie & Fitch First Instinct Blue for Her Eau de Parfum 50ml Gift Set with 200ml Body Lotion"
GS("0085715167316", AF, t, "A&F First Instinct Blue Her EDP 50ml & Lotion Gift Set", "Women", "50", "24.49", "31.99", 5,
   [("Top", "Bergamot, Sea Salt, Blackberry"), ("Heart", "Apricot, Peony, Jasmine"), ("Base", "Patchouli, Vanilla, Sandalwood")],
   "Fruity · Floral · Woody", "A fresh, salty-sweet floral with a matching body lotion.",
   f"{t} pairs First Instinct Blue for Her with a softly scented body lotion. Bergamot, sea salt and blackberry open freshly, a heart of apricot, peony and jasmine follows, and it settles on patchouli, vanilla and sandalwood.",
   ["First Instinct Blue for Her Eau de Parfum 50ml (spray)", "First Instinct Blue for Her Body Lotion 200ml"],
   ["A fresh opening of bergamot, sea salt and blackberry", "A soft floral heart of peony and jasmine", "Matching body lotion to layer the scent", "Ready to give as a gift"],
   "Needs review: EAN 0085715167316 found only on Superdrug's First Instinct Blue for Her gift set (EDP + body lotion, no sizes shown); 50ml EDP + 200ml lotion confirmed by TJ Hughes, Flannels, Cosmetify (no EANs). A 100ml + 15ml + lotion version also exists – please check the box. Notes agreed by LookFantastic, ScentVerdict, Cosmetify; Flannels/TJ Hughes give a different pyramid (apple/orange blossom/amber), left out. Not the non-Blue First Instinct for Her. Awaiting photos.",
   "bergamot and sea salt over peony, vanilla and sandalwood, with lotion.", ["Fruity", "Floral", "Woody"], ["Fruity", "Citrus", "Floral", "Jasmine", "Vanilla", "Sandalwood"],
   name="First Instinct Blue for Her", conc="Eau De Parfum", concl="Eau de Parfum", status="needs-review")

t = "Abercrombie & Fitch First Instinct Eau de Toilette 100ml Gift Set with 200ml Body Wash"
GS("0085715163394", AF, t, "A&F First Instinct EDT 100ml & Body Wash Gift Set", "Men", "100", "29.49", "36.99", 5,
   [("Top", "Gin, Tonic, Melon"), ("Heart", "Sichuan Pepper, Violet Leaf, Citrus"), ("Base", "Musk, Suede, Amber")],
   "Aromatic · Fougere · Oriental", "The fresh, sensual First Instinct with a matching wash.",
   f"{t} pairs First Instinct for men with a matching body wash. Gin, tonic and melon open crisply, a heart of Sichuan pepper, violet leaf and citrus follows, and it settles on musk, suede and amber.",
   ["First Instinct Eau de Toilette 100ml (spray)", "First Instinct Body Wash 200ml"],
   ["A crisp gin, tonic and melon opening", "A peppery heart of Sichuan pepper and violet leaf", "Matching wash to layer the scent", "Great value gift for him"],
   "Needs review: EAN 0085715163394 not confirmed online (only an unloadable beautyplaza search hit). Superdrug lists other men's First Instinct sets with different EANs (0085715165534 = 100ml + 15ml EDT + 200ml hair & body wash; 0085715163301). Contents per supplier; Cosmetify/eBay show a 100ml EDT + 200ml hair & body wash set – please check the box. Notes agreed by Superdrug, Cosmetify, ScentVerdict, NST. Aromatic fougère per Superdrug/NST. Awaiting photos.",
   "gin and melon over Sichuan pepper, suede and amber, with body wash.", ["Aromatic", "Fougere", "Oriental"], ["Fresh", "Fruity", "Citrus", "Spicy"],
   name="First Instinct", status="needs-review")

# ---------------- Adidas Vibes (2024, Coty) + Pure Game
def V(bc, nm, qty, price, cmp, pyr, profile, hook, intro, love, note, seo_d, of, fr, status="done"):
    t = f"Adidas Vibes {nm} Eau de Parfum 50ml"
    F(bc, AD, t, "Unisex", "50", price, cmp, qty, pyr, profile, hook, f"{t} {intro}", love, note, seo_d, of, fr,
      name=f"Vibes {nm}", status=status)

V("3616305447111", "Chill Zone", 5, "17.99", "23.99",
  [("Top", "Bergamot, Black Pepper, Williams Pear, Ginger"), ("Heart", "Lavender, Eucalyptus, Incense"), ("Base", "Vanilla, Moss, Patchouli, Vetiver")],
  "Aromatic · Fresh · Spicy", "A calming lavender-vanilla scent made to help you unwind.",
  "is part of the 2024 Adidas Vibes mood-fragrance collection, created to help you relax. Bergamot, black pepper, Williams pear and ginger open, a soothing heart of lavender, eucalyptus and incense follows, and it settles on vanilla, moss, patchouli and vetiver.",
  ["Key notes of lavender and vanilla", "Designed to help you relax and switch off", "Eau de Parfum strength in a handy 50ml", "Made for everyone"],
  UNI.format(pos="gender neutral") + "EAN matched on Amazon US (50ml). Pyramid agreed by Nahdi and Taniaksiazka (FragranceNet agrees on top/base); key notes lavender + vanilla agreed by Coty, Luxplus, Lyko, Parfumo; absinthe (Parfumo only) left out. 2024 launch per Coty, Parfumo. Awaiting photos.",
  "lavender and vanilla with pear, incense and vetiver.", ["Aromatic", "Fresh", "Spicy"], ["Lavender", "Vanilla", "Fruity", "Spicy", "Woody"])

V("3616305447043", "Energy Drive", 5, "17.99", "22.99",
  [("Top", "Bergamot, Pink Pepper, Grapefruit, Orange"), ("Heart", "Cardamom, Clary Sage, Violet Leaves"), ("Base", "Cashmeran, Vetiver, Tonka Bean, Musk")],
  "Fresh · Citrus · Spicy", "A zesty, spicy shot of energy.",
  "is part of the 2024 Adidas Vibes mood-fragrance collection, created to give you a boost of energy. Bergamot, pink pepper, grapefruit and orange open brightly, a heart of cardamom, clary sage and violet leaves follows, and it settles on cashmeran, vetiver, tonka bean and musk.",
  ["Key notes of cardamom and pink pepper", "Designed to boost your energy", "Eau de Parfum strength in a handy 50ml", "Fresh, zesty and easy to wear"],
  UNI.format(pos="masculine (Parfumo and Rossmann also list it for men)") + "EAN matched on Rossmann PL/HU, Allegro (50ml). Pyramid agreed by Rossmann.pl and Nahdi; key notes cardamom + pink pepper agreed by Coty, Parfumo, Luxplus, Lyko. 2024 launch per Coty. Awaiting photos.",
  "pink pepper and grapefruit over cardamom, vetiver and tonka.", ["Fresh", "Citrus", "Spicy"], ["Citrus", "Spicy", "Fresh", "Woody"])

V("3616305447098", "Full Recharge", 5, "17.99", "24.99",
  [("Top", "Green Sap, Peppermint Leaves, Green Mandarin"), ("Heart", "Lavender, Geranium Leaves, Ginger"), ("Base", "Cedarwood, Musk, Vetiver")],
  "Fresh · Aromatic · Woody", "A green, refreshing scent made to help you recharge.",
  "is part of the 2024 Adidas Vibes mood-fragrance collection, created as a refreshing escape. Green sap, peppermint leaves and green mandarin open crisply, a heart of lavender, geranium leaves and ginger follows, and it settles on cedarwood, musk and vetiver.",
  ["Fresh green mandarin and peppermint", "An aromatic heart of lavender and ginger", "A clean base of cedarwood, musk and vetiver", "Eau de Parfum strength in a handy 50ml"],
  UNI.format(pos="masculine (Parfumo and Lyko also list it for men)") + "EAN matched on Zapachnisci.pl and Amazon US (50ml). Pyramid agreed by Zapachnisci and Nahdi; Coty/Parfumo/Luxplus/Lyko headline notes are cedar leaf + clary sage (clary sage not in the tiered pyramid, so not shown). 2024 launch per Coty. Awaiting photos.",
  "green mandarin and peppermint over lavender, cedar and vetiver.", ["Fresh", "Aromatic", "Woody"], ["Fresh", "Citrus", "Lavender", "Woody"])

V("3616305447241", "Get Comfy", 5, "17.99", "23.99",
  [("Top", "Mandarin, Blackcurrant, Bergamot"), ("Heart", "Cyclamen, Rose, Jasmine Sambac"), ("Base", "Sandalwood, Ambrox")],
  "Floral · Fruity · Woody", "A soft, cosy scent made for comfort.",
  "is part of the 2024 Adidas Vibes mood-fragrance collection, created to bring a feeling of comfort. Mandarin, blackcurrant and bergamot open softly, a floral heart of cyclamen, rose and jasmine sambac follows, and it settles on sandalwood and ambrox.",
  ["A juicy mandarin and blackcurrant opening", "A soft floral heart of rose and jasmine", "Designed to feel calming and comforting", "Made for everyone"],
  "Needs review: notes. Pyramid agreed by Drogerie Natura and Nahdi's description, but Coty/Superdrug/Boots headline notes are vanilla + mandarin and vanilla is missing from that pyramid; Nahdi's features box shows a second pyramid (Spark Up's), Parfumo's flat list differs (peony, vanilla, patchouli). Please check the box notes. EAN matched on Drogerie Natura and Morele (50ml). Unisex per Coty and all retailers. 2024 launch per Coty. Awaiting photos.",
  "mandarin and blackcurrant over rose, jasmine and sandalwood.", ["Floral", "Fruity", "Woody"], ["Citrus", "Fruity", "Floral", "Rose", "Jasmine", "Sandalwood"], status="needs-review")

V("3616305447203", "Spark Up", 5, "17.99", "22.99",
  [("Top", "Guava, Mango, Lemon"), ("Heart", "Freesia, Nectarine, Geranium"), ("Base", "Cedarwood, Blond Woods")],
  "Fruity · Floral · Woody", "A bright, fruity scent made to lift your mood.",
  "is part of the 2024 Adidas Vibes mood-fragrance collection, created to boost your mood. Guava, mango and lemon open juicily, a heart of freesia, nectarine and geranium follows, and it settles on cedarwood and blond woods.",
  ["A juicy guava, mango and lemon opening", "A bright heart of freesia and nectarine", "Designed to lift your mood", "Eau de Parfum strength in a handy 50ml"],
  "Needs review: notes. " + UNI.format(pos="feminine (Parfumo and Rossmann HU also list it for women)") + "Pyramid agreed by Nahdi and Centrepoint (Parfumo backs guava, mango, lemon, blond woods), but Coty/Superdrug/Rossmann/Lyko headline notes are sweet orange + black pepper, not in the pyramid. EAN matched on Rossmann HU and bol.com (50ml). 2024 launch per Coty. Awaiting photos.",
  "guava and mango over freesia, nectarine and cedarwood.", ["Fruity", "Floral", "Woody"], ["Fruity", "Citrus", "Floral", "Woody"], status="needs-review")

t = "Adidas Pure Game Eau de Toilette 100ml"
F("3616303322021", AD, t, "Men", "100", "15.99", "20.99", 5,
  [("Top", "Pepper, Basil, Grapefruit, Mandarin"), ("Heart", "Cypress, Guaiac Wood, Lavender"), ("Base", "Tonka Bean, Incense, Patchouli, Sandalwood")],
  "Woody · Spicy · Aromatic", "A sporty, woody-spicy classic.",
  f"{t} is a woody, spicy fragrance first launched in 2010. Pepper, basil, grapefruit and mandarin open with energy, a heart of cypress, guaiac wood and lavender follows, and it settles on tonka bean, incense, patchouli and sandalwood.",
  ["A lively opening of pepper, basil and grapefruit", "A woody heart of cypress and guaiac wood", "A warm base of tonka, incense and sandalwood", "Great value everyday fragrance"],
  "EAN and 100ml EDT confirmed on Superdrug (EAN page). Notes agreed by Superdrug, Parfumo, ScentVerdict (all tiers; Tamboti wood only on NST, left out; The Perfume Shop list differs). 2010 launch per Superdrug, Parfumo, NST. Store has Pure Game Shower Gel only – not a duplicate. Awaiting photos.",
  "pepper and grapefruit over cypress, tonka and sandalwood.", ["Woody", "Spicy", "Aromatic"], ["Spicy", "Citrus", "Woody", "Lavender", "Sandalwood"],
  name="Pure Game", **TC)

for p in P:
    if p["bc"] == "0085715167507":
        p["seo"] = ("A&F First Instinct Extreme Eau de Parfum 100ml", p["seo"][1].replace("Abercrombie & Fitch", "A&F"))
    p["seo"] = (p["seo"][0], p["seo"][1].replace("&amp;", "&"))
    for a, b in [("sichuan", "Sichuan"), ("williams", "Williams"), ("brazilian", "Brazilian")]:
        p["desc"] = p["desc"].replace(a, b)
write_outputs()
