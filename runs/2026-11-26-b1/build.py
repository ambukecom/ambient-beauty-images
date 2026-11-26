import sys; sys.path.insert(0, "/home/claude/ambient-beauty-images/workflow")
from lib import *
TC = dict(conc="Eau De Toilette", concl="Eau de Toilette")
PC = dict(conc="Eau De Parfum", concl="Eau de Parfum")
XC = dict(conc="Extrait De Parfum", concl="Extrait de Parfum")
AW = " Awaiting photos."

def seo(t, d):
    P[-1]["seo"] = (t, f"{t}: {d}" + FREE)

# 1 Jimmy Choo I Want Choo Midnight EDP 100ml
t = "Jimmy Choo I Want Choo Midnight Eau de Parfum 100ml"
F("3386460169400", "Jimmy Choo", t, "Women", "100", "63.49", "81.99", 1,
  [("Top", "Blackberry"), ("Heart", "Night Orchid"), ("Base", "Cedarwood")],
  "Floral · Fruity", "A darker, after-hours take on I Want Choo.",
  f"{t} is a floral fragrance for women, launched in 2026 as the after-dark chapter of the I Want Choo story. A juicy blackberry opening leads into a heart of night orchid, before the scent settles onto a smooth, woody base of cedarwood for a confident evening trail.",
  ["A juicy blackberry opening", "A sensual night orchid heart", "A smooth cedarwood base", "Generous 100ml Eau de Parfum"],
  "EAN 3386460169400 matched on The Perfume Shop UK (100ml) + Nandansons (3.4oz EDP). New 2026 launch (TPS, NST). Pyramid limited to the one note per tier that 2 sources agree on (Escentual, TPS/Sephora/NST list more notes untiered). Floral per Escentual, Sephora, NST. Perfumer single-source, left out. Women." + AW,
  "blackberry and night orchid over cedarwood.", ["Floral", "Fruity"], ["Floral", "Fruity", "Woody"],
  name="I Want Choo Midnight", **PC)

# 2 Lalique Pour Homme Lion EDP 125ml
t = "Lalique Pour Homme Lion Eau de Parfum 125ml"
F("3454960007468", "Lalique", t, "Men", "125", "34.99", "47.99", 3,
  [("Top", "Bergamot, Grapefruit, Lavender, Mandarin, Rosemary"), ("Heart", "Iris, Jasmine, Cedarwood"), ("Base", "Oakmoss, Amber, Patchouli, Sandalwood, Vanilla")],
  "Woody · Aromatic", "A bold, noble woody aromatic with a lion's presence.",
  f"{t} is a woody aromatic fragrance for men, created by perfumer Maurice Roucel and launched in 1997. Bright bergamot, grapefruit and mandarin meet aromatic lavender and rosemary in the opening, a heart of iris, jasmine and cedarwood adds polish, and it settles into a warm, rich base of oakmoss, amber, patchouli, sandalwood and vanilla.",
  ["A fresh citrus, lavender and rosemary opening", "An elegant iris, jasmine and cedarwood heart", "A warm amber, sandalwood and vanilla base", "Generous 125ml Eau de Parfum"],
  "EAN 3454960007468 matched on Direct Fragrance UK (Pour Homme Lion 125ml EDP) + Jomashop/upcitemdb. Pyramid agreed by Lalique UK, vivir, Scentadvice (lily-of-the-valley single-tier source, left out). Woody aromatic per Direct Fragrance + vivir. 1997 + Maurice Roucel per Lalique UK, vivir, Scentadvice. Not the EDT version. Men." + AW,
  "citrus and lavender over iris, amber and sandalwood.", ["Woody", "Aromatic"], ["Woody", "Citrus", "Lavender", "Sandalwood"],
  name="Lalique Pour Homme Lion", **PC)

# 3 Lalique Soleil EDP 100ml
t = "Lalique Soleil Eau de Parfum 100ml"
F("7640171199719", "Lalique", t, "Women", "100", "48.99", "64.99", 5,
  [("Top", "Bitter Almond, Cardamom, Mandarin"), ("Heart", "Pear, Coffee, Jasmine"), ("Base", "Musk, Sandalwood, Praline")],
  "Gourmand · Floral · Fruity", "Sunshine in a bottle, with a creamy gourmand glow.",
  f"{t} is a gourmand fragrance for women, created by Alexandra Monet, Barbara Zoebelein and Benoist Lapouza and inspired by the warmth of the sun. Bitter almond, cardamom and mandarin open it bright and lightly spiced, a heart of pear, coffee and jasmine adds a creamy, radiant sweetness, and it settles into a soft base of musk, sandalwood and praline.",
  ["A bright almond, cardamom and mandarin opening", "A creamy pear, coffee and jasmine heart", "A soft musk, sandalwood and praline base", "Generous 100ml Eau de Parfum"],
  "EAN 7640171199719 matched on Superdrug (Lalique Soleil EDP 100ml) + Tendance image + eBay; plain Soleil, not Soleil Vibrant (EAN 7640171197203). Pyramid agreed by Lalique UK, Superdrug, Tendance (caramel 2 sources only in heart, left out). Gourmand per Superdrug, Tendance, Lalique UK. Perfumers per Lalique UK, Tendance, Cosmetics Business. Launch year disputed (2019/2020), left out. Women." + AW,
  "almond and pear over coffee, jasmine and praline.", ["Gourmand", "Floral", "Fruity"], ["Fruity", "Jasmine", "Sandalwood", "Spicy"],
  name="Lalique Soleil", **PC)

# 4 Lamborghini Essenza EDT 125ml
t = "Lamborghini Essenza Eau de Toilette 125ml"
F("0856857007194", "Lamborghini", t, "Men", "125", "20.49", "27.99", 5,
  [("Top", "Lemon, Lychee, Apple"), ("Heart", "Freesia, Orange Blossom, Vetiver"), ("Base", "Cedarwood, Amber, Teak Wood")],
  "Woody · Citrus · Fruity", "Fresh, fruity citrus over a sleek woody base.",
  f"{t} is a woody fragrance for men from Tonino Lamborghini, launched in 2018. Lemon, lychee and apple open it fresh and juicy, a heart of freesia, orange blossom and vetiver adds a clean, refined lift, and it settles into a smooth base of cedarwood, amber and teak wood.",
  ["A fresh lemon, lychee and apple opening", "A clean freesia, orange blossom and vetiver heart", "A smooth cedarwood, amber and teak base", "Generous 125ml Eau de Toilette"],
  "EAN 0856857007194 matched on Superdrug UK (Tonino Lamborghini Essenza 125ml EDT). Pyramid agreed by Ferwer, FragranceNet, Parfumo review; Perfume.com lists a different (generic-looking) pyramid, ignored. Woody per Superdrug, FragranceNet, Ferwer. 2018 per Ferwer, FragranceNet, Parfumo. Brand is Tonino Lamborghini; vendor kept as 'Lamborghini' to match store. Men." + AW,
  "lemon and lychee over vetiver and cedarwood.", ["Woody", "Citrus", "Fruity"], ["Woody", "Citrus", "Fruity"],
  name="Lamborghini Essenza", **TC)

# 5 Lamborghini Invincibile EDT 125ml
t = "Lamborghini Invincibile Eau de Toilette 125ml"
F("0856857007101", "Lamborghini", t, "Men", "125", "20.49", "27.99", 5,
  [("Top", "Bergamot, Pineapple, Apple, Blackcurrant"), ("Heart", "Birch, Patchouli, Jasmine, Rose"), ("Base", "Ambergris, Musk, Oakmoss, Vanilla")],
  "Woody · Fruity", "Bold fruit and smoky woods, built for confidence.",
  f"{t} is a woody fragrance for men from Tonino Lamborghini, launched in 2018. Bergamot, pineapple, apple and blackcurrant give it a bold, fruity opening, a heart of birch, patchouli, jasmine and rose adds smoky depth, and it settles into a warm base of ambergris, musk, oakmoss and vanilla.",
  ["A bold bergamot, pineapple and blackcurrant opening", "A smoky birch and patchouli heart", "A warm ambergris, musk and vanilla base", "Generous 125ml Eau de Toilette"],
  "EAN 0856857007101 matched on Superdrug UK (Lamborghini Invincibile 125ml EDT) + Allegro. Pyramid agreed by Parfumo, FragranceNet, Ferwer; Perfume.com differs, ignored. Woody per Parfumo, FragranceNet, Superdrug. 2018 per Parfumo, Ferwer, FragranceNet. Men." + AW,
  "pineapple and bergamot over birch and ambergris.", ["Woody", "Fruity"], ["Woody", "Fruity", "Citrus"],
  name="Lamborghini Invincibile", **TC)

# 6 Lamborghini Millennials Dinamico EDT 75ml (needs-review: EAN unmatched)
t = "Lamborghini Millennials Dinamico Eau de Toilette 75ml"
F("0810876038119", "Lamborghini", t, "Men", "75", "18.99", "24.99", 3,
  [("Top", "Lemon, Lime, Grapefruit, Apple, Marine Notes"), ("Heart", "Water Lily, Bay Leaf, Cashmere Wood, Tobacco, Rose"), ("Base", "Ambergris, Oakmoss, Sandalwood, Musk")],
  "Fresh · Citrus · Aquatic", "A zesty, ozonic rush with a warm woody finish.",
  f"{t} is a fresh citrus fragrance for men from Tonino Lamborghini's Millennials line, launched in 2021. Lemon, lime, grapefruit and apple open it zesty and ozonic, a heart of water lily, bay leaf, cashmere wood, tobacco and rose adds depth, and it settles into a base of ambergris, oakmoss, sandalwood and musk.",
  ["A zesty citrus and marine opening", "A water lily, tobacco and cashmere wood heart", "A warm ambergris and sandalwood base", "75ml Eau de Toilette"],
  "NEEDS REVIEW: EAN 0810876038119 not found on any page (prefix matches Millennials family on Superdrug) – please check box EAN/name. Dinamico EDT 75ml exists (Ferwer, Kaufland.de). Pyramid agreed by Ferwer, FragranceNet, Cosmetify (Druni subset). Fresh/citrus per Ferwer + Cosmetify. 2021 per Ferwer, FragranceNet. Men." + AW,
  "zesty citrus over tobacco and sandalwood.", ["Fresh", "Citrus", "Aquatic"], ["Citrus", "Fresh", "Aquatic", "Woody"],
  name="Millennials Dinamico", status="needs-review", **TC)
seo("Lamborghini Millennials Dinamico EDT 75ml", "zesty citrus, tobacco and sandalwood.")

# 7 Lamborghini Millennials EDT 75ml (needs-review: pyramid disputed; only shared notes)
t = "Lamborghini Millennials Eau de Toilette 75ml"
F("0810876038010", "Lamborghini", t, "Men", "75", "18.99", "24.99", 2,
  [("Top", "Grapefruit"), ("Heart", "Violet"), ("Base", "Cedarwood, Patchouli")],
  "Woody · Spicy", "The original Millennials: a modern woody signature.",
  f"{t} is a woody fragrance for men and the original scent of Tonino Lamborghini's Millennials line, launched in 2021 (sometimes sold as Millennials Classic). Sparkling grapefruit opens it, a violet heart adds a cool, modern edge, and it settles into a confident woody base of cedarwood and patchouli.",
  ["A sparkling grapefruit opening", "A cool violet heart", "A woody cedarwood and patchouli base", "75ml Eau de Toilette"],
  "NEEDS REVIEW: pyramid disputed – Parfumo + FragranceNet (Classic) agree on pink pepper/rhubarb/incense, amber/leather/clove, cashmere wood/vetiver, but ePrice (exact EAN page) lists bergamot/lemon, lavender/cardamom, amber; Tesco puts the Parfumo notes on Millennials Winner. Only notes shared by all sources shown. EAN 0810876038010 matched on Superdrug (Millennials 75ml EDT) + ePrice (Millennials Classic 75ml). Woody/spicy per Parfumo + FragranceNet. 2021 per Parfumo, FragranceNet. Not Millennials Winner. Men." + AW,
  "grapefruit and violet over cedarwood and patchouli.", ["Woody", "Spicy"], ["Woody", "Citrus", "Floral"],
  name="Lamborghini Millennials", status="needs-review", **TC)

# 8 Lancôme Ô Zenith EDT 100ml
t = "Lancôme Ô Zenith Eau de Toilette 100ml"
F("3614274380392", "Lancôme", t, "Women", "100", "59.99", "76.99", 5,
  [("Heart", "Jasmine Absolute"), ("Base", "Monoï Accord")],
  "Floral · Fruity", "Sun-drenched jasmine with a warm, solar monoï glow.",
  f"{t} is a floral fragrance from the Les Ô de Lancôme collection, created by perfumer Dominique Ropion and launched in 2025. Built around jasmine absolute from Lancôme's own Domaine de la Rose in Grasse, it glows with a radiant, sunlit white-floral heart before settling into a warm, skin-like monoï accord.",
  ["Jasmine absolute from Lancôme's Domaine de la Rose", "A warm, solar monoï accord", "Part of the Les Ô de Lancôme collection", "Generous 100ml Eau de Toilette"],
  "EAN 3614274380392 matched on The Perfume Shop UK (Ô Zenith EDT 100ml) + aio.lv. EDT confirmed (Lancôme UK/CA, Sephora FR, Escentual, TPS). Only heart + base shown: no 2 sources agree on named top notes (Lancôme mentions citrus/coconut water). Floral/fruity per Lancôme, Sephora FR, TPS, Escentual. 2025 + Dominique Ropion per Lancôme UK, TPS, Parfumo, NST. Gender kept as supplier (Women), but Lancôme UK says 'for men and women' and TPS/Escentual/NST call the Les Ô line unisex. Women." + AW,
  "radiant jasmine absolute over a warm monoï accord.", ["Floral", "Fruity"], ["Floral", "Jasmine", "Fruity"],
  name="Ô Zenith", **TC)

# 9 Ralph Lauren Polo Blue EDT 125ml
t = "Ralph Lauren Polo Blue Eau de Toilette 125ml"
F("3360377022928", "Ralph Lauren", t, "Men", "125", "46.99", "60.99", 1,
  [("Top", "Melon, Cucumber, Mandarin"), ("Heart", "Basil, Sage, Geranium"), ("Base", "Suede, Musk, Patchouli")],
  "Aromatic · Fresh · Aquatic", "The classic fresh blue for men, as cool as open skies.",
  f"{t} is the original fresh aromatic fragrance for men, created by perfumers Christophe Laudamiel and Carlos Benaïm. Cool melon, cucumber and mandarin open it crisp and watery, a heart of basil, sage and geranium brings a clean aromatic lift, and it settles into a soft, masculine base of suede, musk and patchouli.",
  ["A cool melon, cucumber and mandarin opening", "An aromatic basil, sage and geranium heart", "A soft suede, musk and patchouli base", "Generous 125ml Eau de Toilette"],
  "EAN 3360377022928 matched on Superdrug (Polo Blue 125ml EDT) + WatchMaxx (EDT 125ml); original EDT, not EDP/Parfum (Superdrug copy describes the EDP, ignored). Pyramid agreed by WatchMaxx, John Lewis, Cosma, Parfumo (Notino layout differs, ignored). Aromatic/fresh per Notino, Cosma, Parfumo. Perfumers per Notino + Parfumo. Launch year disputed (2002/2003), left out. Men." + AW,
  "melon and cucumber over basil, suede and musk.", ["Aromatic", "Fresh", "Aquatic"], ["Fresh", "Aquatic", "Citrus"],
  name="Polo Blue", **TC)

# 10 Surrati Ambre Noir Extrait de Parfum 100ml (needs-review)
t = "Surrati Ambre Noir Extrait de Parfum 100ml"
F("6281085031453", "Surrati", t, "Unisex", "100", "22.49", "29.99", 5,
  [("Top", "Amber"), ("Heart", "Spices, Black Pepper, Cardamom"), ("Base", "Sandalwood, Patchouli")],
  "Oriental · Spicy · Woody", "Dark amber and warm spice, rich and long-lasting.",
  f"{t} is a rich oriental fragrance for everyone, made in extrait concentration for depth and lasting power. Warm amber opens it, a heart of spices, black pepper and cardamom adds heat and character, and it settles into a smooth, earthy base of sandalwood and patchouli.",
  ["A warm amber opening", "A spicy black pepper and cardamom heart", "A smooth sandalwood and patchouli base", "Extrait de Parfum concentration, 100ml"],
  "NEEDS REVIEW: supplier form column says Eau de Parfum but supplier name + Onarys (EAN match), Perfume Trading UK, ScentVerdict, Cosmetify say Extrait de Parfum – listed as Extrait. Only 1 page matches EAN 6281085031453 (Onarys). Notes vary widely; only agreed notes shown (Perfume Trading, FilledWithBarakah, ScentVerdict); Onarys pyramid differs. Oriental per Cosmetify, spicy/woody per ScentVerdict + FilledWithBarakah. Gender kept as supplier (Unisex; Perfume Trading + ScentVerdict); Onarys markets it for men." + AW,
  "warm amber and spice over sandalwood.", ["Oriental", "Spicy", "Woody"], ["Oriental", "Spicy", "Sandalwood"],
  name="Surrati Ambre Noir", status="needs-review", **XC)

write_outputs()
