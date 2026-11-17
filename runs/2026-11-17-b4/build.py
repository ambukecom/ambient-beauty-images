import sys; sys.path.insert(0, "/home/claude/ambient-beauty-images/workflow")
from lib import *

# ---------------- Fragrances
t = "Arabiyat Prestige Sugar Coconut Chiffon Eau de Parfum 100ml"
F("6290361916964", "Arabiyat Prestige", t, "Unisex", "100", "25.49", "33.99", 1,
  [("Top", "Coconut"), ("Heart", "Coconut, Jasmine"), ("Base", "Vanilla, Butter, Sugar, Musk")],
  "Gourmand · Oriental · Vanilla", "Creamy coconut and jasmine over buttery vanilla sugar.",
  f"{t} is a creamy, sweet gourmand from the Arabiyat Sugar collection. Soft coconut opens and carries into a heart of coconut and jasmine, before it melts into a warm base of vanilla, butter, sugar and musk.",
  ["A creamy coconut opening", "A soft touch of jasmine", "A buttery base of vanilla, sugar and musk", "Part of the Arabiyat Sugar gourmand collection"],
  "Notes confirmed by 2 sources (Bjutip EAN page, JustMyLook; FilledWithBarakah and Zaoud agree). Caramel (2 of 4 sources) left out. Supplier's 'Coconot' corrected to Coconut in the title. Awaiting photos.",
  "creamy coconut and jasmine over vanilla, butter and sugar.", ["Gourmand", "Oriental"], ["Vanilla", "Jasmine"],
  name="Sugar Coconut Chiffon")

t = "Arabiyat Prestige Sugar Lemon Sorbet Eau de Parfum 100ml"
F("6290361916933", "Arabiyat Prestige", t, "Unisex", "100", "28.49", "37.99", 4,
  [("Top", "Lemon, Rum"), ("Heart", "Gourmand Accord"), ("Base", "Vanilla")],
  "Citrus · Gourmand · Vanilla", "Zesty lemon and a splash of rum over creamy vanilla.",
  f"{t} is a zesty, creamy gourmand from the Arabiyat Sugar collection. Sparkling lemon and rum open brightly, a sweet gourmand accord follows, and it settles into a smooth vanilla base, like a scoop of lemon sorbet.",
  ["A sparkling lemon opening", "A playful splash of rum", "A sweet, creamy gourmand heart", "A smooth vanilla base"],
  "Notes confirmed by 2 sources (Bjutip EAN page, OrientFragance; ArabicParfums and FilledWithBarakah agree). Awaiting photos.",
  "zesty lemon and rum over creamy vanilla.", ["Citrus", "Gourmand"], ["Citrus", "Vanilla"],
  name="Sugar Lemon Sorbet")

t = "Arabiyat Prestige Sugar Matcha Latte Eau de Parfum 100ml"
F("6290361916902", "Arabiyat Prestige", t, "Women", "100", "28.49", "37.99", 2,
  [("Top", "Peach, Coconut, Lily of the Valley"), ("Heart", "Caramel, Milk, Rice, Orange Blossom"), ("Base", "Tonka Bean, Sandalwood, Musk")],
  "Gourmand · Floral · Fruity", "Peach and lily over a milky caramel latte and sandalwood.",
  f"{t} is a creamy floral-fruity gourmand from the Arabiyat Sugar collection. Peach, coconut and lily of the valley open softly, a milky heart of caramel, milk, rice and orange blossom follows, and it settles into a warm base of tonka bean, sandalwood and musk.",
  ["A soft opening of peach and lily of the valley", "A milky, latte-like heart of caramel and rice", "A warm base of tonka bean and sandalwood", "Part of the Arabiyat Sugar gourmand collection"],
  "Notes confirmed by 2 sources (Bjutip EAN page, Boozyshop; ArabicParfums agrees). Bjutip, Boozyshop and aio.lv market it as unisex (ArabicParfums as women's); supplier's Women used. Awaiting photos.",
  "peach and lily over milky caramel and sandalwood.", ["Gourmand", "Floral", "Fruity"], ["Fruity", "Floral", "Sandalwood"],
  name="Sugar Matcha Latte")

t = "Ard Al Zaafaran I Am The Queen Ana Al Malikah Eau de Parfum 100ml"
F("6295199791189", "Ard Al Zaafaran", t, "Women", "100", "24.49", "31.99", 1,
  [("Top", "Bergamot"), ("Heart", "Jasmine, Orange Blossom")],
  "Floral · Oriental", "Bright bergamot opening onto jasmine and orange blossom.",
  f"{t} is a feminine floral fragrance. Bright bergamot opens into an elegant heart of jasmine and orange blossom for a graceful, regal trail.",
  ["A bright bergamot opening", "An elegant heart of jasmine and orange blossom", "Feminine floral character", "Great value 100ml bottle"],
  "Needs review: retailers publish different pyramids (McGrocer/ArabicParfums: clove, tonka, guaiac, oud; TJ Hughes/Onarys: cherry, peony, musk; Superdrug EAN page: rose, oud, amber, vanilla). Only bergamot (top) and jasmine/orange blossom (heart), agreed across sources, are shown; base not shown. EAN confirmed by Superdrug and Kruidvat. Please check the box notes. Awaiting photos.",
  "bergamot opening onto jasmine and orange blossom.", ["Floral"], ["Floral", "Jasmine", "Citrus"],
  name="I Am The Queen", status="needs-review")

t = "Ard Al Zaafaran Layalina Eau de Parfum 100ml"
F("6438585524675", "Ard Al Zaafaran", t, "Unisex", "100", "23.49", "30.99", 1,
  [("Top", "Lavender, Mandarin"), ("Heart", "Orange Blossom"), ("Base", "Amber, Musk, Vanilla")],
  "Aromatic · Floral · Amber", "Lavender and mandarin over warm amber and vanilla.",
  f"{t} is a warm, aromatic-floral fragrance. Lavender and mandarin open freshly, a heart of orange blossom follows, and it settles into a sensual base of amber, musk and vanilla.",
  ["A fresh opening of lavender and mandarin", "A soft orange blossom heart", "A warm base of amber, musk and vanilla", "Easy to wear day or night"],
  "Notes confirmed by 2 sources (Triple Traders EAN page, Perfume Trading UK; TRB Cosmetics agrees). Heart moss/oakmoss not agreed by all, so only orange blossom is shown. Superdrug (EAN page) files it under women's; supplier's Unisex used. EAN 643 prefix is GS1 Finland but tied to Layalina by 2 retailers. Awaiting photos.",
  "lavender and mandarin over amber, musk and vanilla.", ["Aromatic", "Floral", "Oriental"], ["Lavender", "Citrus", "Floral", "Vanilla"],
  name="Layalina")

t = "Ard Al Zaafaran Mousuf Azure Eau de Parfum 100ml"
F("6295199790397", "Ard Al Zaafaran", t, "Unisex", "100", "21.99", "29.99", 1,
  [("Top", "Bergamot, Orange, Lime"), ("Heart", "Violet, Nutmeg"), ("Base", "Musk, Amber")],
  "Citrus · Spicy · Musky", "Fresh bergamot and lime over violet, nutmeg and musk.",
  f"{t} is a fresh citrus fragrance with a warm spicy twist. Bergamot, orange and lime open brightly, a heart of violet and nutmeg follows, and it settles into a soft base of musk and amber.",
  ["A bright opening of bergamot, orange and lime", "A heart of violet and nutmeg", "A soft base of musk and amber", "Fresh and easy to wear"],
  "Notes confirmed by 2 sources (Triple Traders EAN page, Emirates Oud; Superdrug EAN page summary agrees, though its features list shows a different pyramid). Superdrug says designed for men; supplier's Unisex used. Awaiting photos.",
  "bergamot and lime over violet, nutmeg and musk.", ["Citrus", "Spicy", "Musky"], ["Citrus", "Spicy", "Fresh"],
  name="Mousuf Azure")

t = "Ard Al Zaafaran Mousuf Eau de Parfum 100ml"
F("6295199790380", "Ard Al Zaafaran", t, "Women", "100", "21.99", "28.99", 3,
  [("Top", "Chocolate, Grape"), ("Heart", "Musk, Oud"), ("Base", "Toffee, Tobacco, Floral Notes")],
  "Gourmand · Oriental · Woody", "Chocolate and grape over oud, toffee and tobacco.",
  f"{t} is a rich, sweet oriental gourmand. Chocolate and grape open indulgently, a heart of musk and oud follows, and it dries down to a warm base of toffee, tobacco and floral notes.",
  ["An indulgent chocolate and grape opening", "A warm heart of musk and oud", "A rich base of toffee and tobacco", "Sweet, long-lasting oriental character"],
  "Needs review: barcode. Supplier's EAN 6295199790380 was not found on any page; retailers list Mousuf under 6437842514039, 6295199796061 and 6290362344513, and Kruidvat/Dubai Perfume Shop show different pyramids. Notes shown are agreed by Triple Traders, Elryan, Perfume Trading UK and Almanaar. Retailers mostly market it as unisex; supplier's Women used. Please check the box barcode and notes. Awaiting photos.",
  "chocolate and grape over oud, toffee and tobacco.", ["Gourmand", "Oriental", "Woody"], ["Fruity", "Oriental"],
  name="Mousuf", status="needs-review")

# ---------------- Bath & Body
t = "Molton Brown Tobacco Absolute Bath & Shower Gel 300ml"
add(cat_name="Bath & Body", bc="5030805002942", title=t, vendor="Molton Brown", type="Bath & Body", gender="Unisex", cat=TAXON["body-wash"],
    price="27.49", cmp="36.99", qty=5, form="Bath & Shower Gel", size="300", unit="ml", gpc=GPC["body-wash"],
    tags=["Molton Brown", "Unisex", "Bath & Body", "Shower Gel", "Tobacco Absolute", "Woody", "Vegan"],
    seo=("Molton Brown Tobacco Absolute Shower Gel 300ml", f"{t}: smoky tobacco, leather and spicy nutmeg." + FREE),
    mf={"age-group": ["Adults"], "product-form": ["Gel"], "fragrance": ["Woody", "Citrus", "Spicy"]},
    desc=body("Smoky tobacco and supple leather for an indulgent shower.",
      "Molton Brown Tobacco Absolute Bath &amp; Shower Gel 300ml is a richly scented body wash with a bold, woody character. Bright elemi, bergamot and grapefruit open onto cedarwood, nutmeg and rosewood, over a smoky base of tobacco, leather and Peru balsam.",
      [("Scent", kd([("Top", "Elemi, Bergamot, Grapefruit"), ("Heart", "Cedarwood, Nutmeg, Rosewood"), ("Base", "Tobacco, Leather, Peru Balsam")])),
       ("Suits", ul(["All skin types", "Anyone who loves woody, smoky scents"])),
       ("How to use", ul(["Shower: work into a rich lather on damp skin, then rinse", "Bath: pour under warm running water"])),
       ("Good to know", ul(["Vegan and cruelty-free", "Paraben- and phthalate-free", "Made in England"]))],
      [("Brand", "Molton Brown"), ("Product", "Tobacco Absolute Bath & Shower Gel"), ("Scent profile", "Woody · Smoky · Spicy"), ("Size", "300ml")],
      ["Bold tobacco and leather scent", "Use in the bath or shower", "Vegan formula, made in England", "Suits all skin types"],
      [("What does it smell like?", "Elemi, bergamot and grapefruit with cedarwood and nutmeg over tobacco, leather and Peru balsam."), ("Is it unisex?", "Yes, it is made for everyone.")]),
    note="Facts confirmed by 2+ sources (Superdrug, Argos and Bluemercury EAN pages; Niche Beauty). Notes from Niche Beauty and Argos. Vegan, cruelty-free, paraben/phthalate-free and Made in England each confirmed by 2 sources. Bluemercury files it under men's; supplier's Unisex used. Awaiting photos.")

t = "Ted Baker Fusion Cosmic Crush Body & Hair Mist 200ml"
add(cat_name="Bath & Body", bc="5060412678889", title=t, vendor="Ted Baker", type="Bath & Body", gender="Women", cat=TAXON["hair-perfume"],
    price="19.49", cmp="24.99", qty=5, form="Body & Hair Mist", size="200", unit="ml", gpc=GPC["fragrance"],
    tags=["Ted Baker", "Women", "Bath & Body", "Body Mist", "Hair Mist", "Fusion", "Cosmic Crush", "Fruity", "Vegan"],
    seo=("Ted Baker Fusion Cosmic Crush Body & Hair Mist 200ml", f"{t}: melon, coconut and vanilla over warm amber." + FREE),
    mf={"age-group": ["Adults"], "product-form": ["Spray"], "dispenser-type": ["Spray"], "fragrance": ["Fruity", "Floral", "Vanilla"]},
    desc=body("A fruity, floral spritz for body and hair.",
      "Ted Baker Fusion Cosmic Crush Body &amp; Hair Mist 200ml is a fruity-floral mist with warm woody notes. Pink pepper, melon and coconut open playfully, a heart of vanilla, orchid and orange flower follows, and it settles on amber, musk and sandalwood. Glycerin and pro-vitamin B5 leave skin feeling moisturised.",
      [("Scent", kd([("Top", "Pink Pepper, Melon, Coconut"), ("Heart", "Vanilla, Orchid, Orange Flower"), ("Base", "Amber, Musk, Sandalwood")])),
       ("Key ingredients", ul(["<strong>Glycerin</strong> for scented hydration", "<strong>Pro-vitamin B5</strong> (panthenol)"])),
       ("How to use", ul(["Hold about 15cm from body and hair and spritz lightly", "Reapply through the day as you like", "Avoid the eyes"])),
       ("Good to know", ul(["Vegan friendly", "Flammable: keep away from heat"]))],
      [("Brand", "Ted Baker"), ("Range", "Fusion"), ("Type", "Body & hair mist"), ("Scent profile", "Fruity · Floral · Woody"), ("Size", "200ml")],
      ["Fruity-floral scent with a warm base", "Use on body and hair", "With glycerin and pro-vitamin B5", "Vegan friendly"],
      [("What does it smell like?", "Pink pepper, melon and coconut with vanilla and orchid over amber, musk and sandalwood."), ("Can I use it on my hair?", "Yes, spritz lightly over body and hair from about 15cm.")]),
    note="Facts confirmed by 2+ sources (Superdrug EAN page, Cosmetify, KMI Brands; Tesco/Next gift-set pages agree on notes). Vegan friendly confirmed by 3 sources. Awaiting photos.")

P[3]["seo"] = ("Ard Al Zaafaran I Am The Queen Eau de Parfum 100ml", P[3]["seo"][1])
write_outputs()
