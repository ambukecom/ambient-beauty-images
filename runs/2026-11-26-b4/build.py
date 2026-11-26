import sys; sys.path.insert(0, "/home/claude/ambient-beauty-images/workflow")
from lib import *
TC = dict(conc="Eau De Toilette", concl="Eau de Toilette")
PC = dict(conc="Eau De Parfum", concl="Eau de Parfum")
AW = " Awaiting photos."
NR = dict(status="needs-review")

# 1 Marc Jacobs Daisy Eau So Fresh EDT 125ml
t = "Marc Jacobs Daisy Eau So Fresh Eau de Toilette 125ml"
F("3607342221208", "Marc Jacobs", t, "Women", "125", "63.99", "83.99", 5,
  [("Top", "Grapefruit, Raspberry, Pear, Green Notes"), ("Heart", "Violet, Rose, Jasmine, Lychee, Apple Blossom"), ("Base", "Musk, Cedar, Plum")],
  "Floral · Fruity", "Sparkling, juicy and full of sunshine.",
  f"{t} is a youthful fruity floral fragrance for women, created by perfumer Alberto Morillas and launched in 2011. Grapefruit, raspberry and pear open fresh and sparkling, a heart of violet, rose, jasmine and lychee adds a soft floral glow, and it settles onto a light base of musk, cedar and plum.",
  ["A sparkling grapefruit, raspberry and pear opening", "A soft violet, rose and jasmine heart", "A light musk, cedar and plum finish", "Generous 125ml Eau de Toilette"],
  "EAN 3607342221208 matched on WatchMaxx (125ml EDT) and Next ingredients PDF; John Lewis + Notino UK list 125ml. Pyramid agreed by Notino, John Lewis, NST, WatchMaxx. Fruity floral per Notino + John Lewis. 2011 + Alberto Morillas per John Lewis + NST. Women." + AW,
  "grapefruit and raspberry over violet, rose and musk.", ["Floral", "Fruity"], ["Floral", "Fruity", "Rose", "Jasmine"],
  name="Daisy Eau So Fresh", **TC)

# 2 Marc Jacobs Perfect EDP 100ml
t = "Marc Jacobs Perfect Eau de Parfum 100ml"
F("3614227086227", "Marc Jacobs", t, "Women", "100", "66.99", "89.99", 5,
  [("Top", "Rhubarb, Daffodil"), ("Heart", "Almond Milk"), ("Base", "Cashmeran, Cedarwood")],
  "Floral · Musky", "A cosy, modern floral that celebrates being yourself.",
  f"{t} is a modern floral fragrance for women from Marc Jacobs, launched in 2020. Bright rhubarb and daffodil open fresh and joyful, a creamy almond milk heart softens the blend, and it settles onto a warm base of cashmeran and cedarwood.",
  ["A bright rhubarb and daffodil opening", "A creamy almond milk heart", "A warm cashmeran and cedarwood base", "Generous 100ml Eau de Parfum"],
  "EAN 3614227086227 matched on The Perfume Shop, Superdrug, WatchMaxx, Next PDF (100ml EDP). Pyramid agreed by The Perfume Shop, WatchMaxx, LookFantastic, NST (TPS lists only cashmeran in base). Floral per LookFantastic, TPS, Superdrug. 2020 per TPS + NST; perfumer single-source, left out. Women." + AW,
  "rhubarb and daffodil over almond milk and cashmeran.", ["Floral", "Musky"], ["Floral"],
  name="Perfect", **PC)

# 3 Marc Jacobs Perfect EDT 100ml
t = "Marc Jacobs Perfect Eau de Toilette 100ml"
F("3616303461881", "Marc Jacobs", t, "Women", "100", "49.49", "66.99", 1,
  [("Top", "Pink Peppercorn, Polygonum"), ("Heart", "White Daffodil"), ("Base", "Cedarwood")],
  "Floral · Fresh", "A lighter, sparkling take on Perfect.",
  f"{t} is a fresh floral fragrance for women from Marc Jacobs, launched in 2023. Sparkling pink peppercorn and polygonum open bright and lively, a heart of white daffodil brings a joyful floral note, and it settles onto a clean cedarwood base.",
  ["A sparkling pink peppercorn opening", "A joyful white daffodil heart", "A clean cedarwood base", "Lighter Eau de Toilette in 100ml"],
  "EAN 3616303461881 matched on Superdrug UK (Perfect EDT 100ml); sister EAN 3616303461874 is the 50ml, so supplier barcode = 100ml. Pyramid agreed by Superdrug, John Lewis, The Perfume Shop, Parfumo. Fresh floral per Parfumo, John Lewis, Superdrug. 2023 per TPS, Parfumo, GTR; perfumer single-source, left out. Women." + AW,
  "pink peppercorn over white daffodil and cedarwood.", ["Floral", "Fresh"], ["Floral", "Fresh"],
  name="Perfect Eau de Toilette", **TC)

# 4 Marc Jacobs Perfect Intense EDP 30ml
t = "Marc Jacobs Perfect Intense Eau de Parfum 30ml"
F("3616302025930", "Marc Jacobs", t, "Women", "30", "35.99", "46.99", 5,
  [("Base", "Sandalwood, Cashmeran")],
  "Floral · Warm · Sweet", "A richer, warmer version of Perfect.",
  f"{t} is a warm floral fragrance for women from Marc Jacobs, launched in 2021. Toasted almond and grapefruit meet jasmine and daffodil in a rich, sweet floral blend, which settles onto a creamy base of sandalwood and cashmeran.",
  ["A rich, toasted almond note", "Jasmine and daffodil florals", "A creamy sandalwood and cashmeran base", "Handy 30ml Eau de Parfum"],
  "EAN 3616302025930 matched on Superdrug UK (30ml EDP) and Next PDF. Top/heart disagree (Superdrug: jasmine + daffodil open, almond in heart; Next + LookFantastic: almond + grapefruit top, jasmine + daffodil heart), so only the agreed base tier (sandalwood, cashmeran) is shown in the pyramid. Warm/sweet floral per Kohl's + Parfumo. 2021 per Parfumo + NST. Women." + AW,
  "almond and jasmine over creamy sandalwood.", ["Floral", "Gourmand"], ["Floral", "Jasmine", "Sandalwood"],
  name="Perfect Intense", **PC)

# 5 Mercedes-Benz Club EDT 100ml
t = "Mercedes-Benz Club Eau de Toilette 100ml"
F("3595471041012", "Mercedes-Benz", t, "Men", "100", "39.99", "50.99", 4,
  [("Top", "Grapefruit, Rhubarb"), ("Heart", "Juniper Berries, Cardamom"), ("Base", "Patchouli, Woods, Tonka Bean")],
  "Woody · Aromatic", "Young, zesty and full of energy.",
  f"{t} is an energetic woody aromatic fragrance for men, created by perfumer Olivier Cresp. Zesty grapefruit and rhubarb open bright and lively, a heart of juniper berries and cardamom adds an aromatic spice, and it dries down to patchouli, woods and tonka bean.",
  ["A zesty grapefruit and rhubarb opening", "An aromatic juniper and cardamom heart", "A warm patchouli, woods and tonka base", "Generous 100ml Eau de Toilette"],
  "EAN 3595471041012 matched on Superdrug UK + Scentia.fr (100ml EDT). Not Club Black. Pyramid agreed by Superdrug, Scentia, NST (grapefruit top per Scentia + brand; Superdrug list partly garbled). Woody aromatic per brand, Superdrug, Scentia. Olivier Cresp per brand, NST, ScentAdvice; launch year (2013/2014) unclear, left out. Men." + AW,
  "grapefruit and rhubarb over cardamom, juniper and tonka.", ["Woody", "Aromatic"], ["Woody", "Fresh", "Spicy"],
  name="Mercedes-Benz Club", **TC)

# 6 Mercedes-Benz (For Men) EDT 120ml
t = "Mercedes-Benz Eau de Toilette 120ml"
F("3595471024718", "Mercedes-Benz", t, "Men", "120", "39.99", "53.99", 4,
  [("Top", "Calabrian Bergamot, Italian Mandarin"), ("Heart", "Violet, Bourbon Pepper, Nutmeg, Galbanum"), ("Base", "American Cedar, Vetiver, Patchouli")],
  "Woody · Floral · Fresh", "The original Mercedes-Benz fragrance for men.",
  f"{t} is the original Mercedes-Benz fragrance for men, created by perfumer Olivier Cresp and launched in 2012. Calabrian bergamot and Italian mandarin open fresh and bright, a heart of violet, Bourbon pepper, nutmeg and galbanum adds a spicy floral edge, and it dries down to American cedar, vetiver and patchouli.",
  ["A fresh bergamot and mandarin opening", "A peppery violet and nutmeg heart", "A dry cedar, vetiver and patchouli base", "Generous 120ml Eau de Toilette"],
  "EAN 3595471024718 matched on eCosmetics (Mercedes-Benz for Men EDT 120ml spray); Galaxus + brand list 120ml EDT. Pyramid: only notes agreed by brand, Lookfantastic, eCosmetics, TorqueNews, ScentAdvice (violet leaf/lemon/Cascalone disputed, left out). Woody floral fresh per brand + TorqueNews. 2012 + Olivier Cresp per brand, TorqueNews, ScentAdvice. Men." + AW,
  "bergamot and mandarin over violet, pepper and cedar.", ["Woody", "Floral", "Fresh"], ["Woody", "Fresh", "Citrus", "Spicy"],
  name="Mercedes-Benz Eau de Toilette", **TC)

# 7 Mercedes-Benz Intense EDT 120ml
t = "Mercedes-Benz Intense Eau de Toilette 120ml"
F("3595471024787", "Mercedes-Benz", t, "Men", "120", "33.99", "42.99", 5,
  [("Top", "Calabrian Bergamot, Italian Mandarin, Violet Leaf"), ("Heart", "Violet, Pepper, Cascalone"), ("Base", "Patchouli, Cetalox, Ambrox, American Cedar, Bourbon Vetiver")],
  "Woody · Amber · Spicy", "A warmer, deeper take on the Mercedes-Benz original.",
  f"{t} is a woody amber fragrance for men, created by perfumer Olivier Cresp and launched in 2013. Calabrian bergamot, Italian mandarin and violet leaf open fresh, a heart of violet, pepper and Cascalone adds a spicy warmth, and it dries down to patchouli, ambery woods, American cedar and Bourbon vetiver.",
  ["A fresh bergamot, mandarin and violet leaf opening", "A spicy violet and pepper heart", "A deep ambery, woody base", "Generous 120ml Eau de Toilette"],
  "EAN 3595471024787 matched on Galaxus (For Men Intense EDT 120ml). This is the 2013 'For Men Intense', not 'Man Intense'. Pyramid agreed by brand, Galaxus, Parfumo (lemon/nutmeg/galbanum Galaxus-only, left out). Woody amber per brand + NST; spicy per Parfumo. 2013 per Parfumo + NST; Olivier Cresp per brand + Parfumo. Men." + AW,
  "bergamot and violet leaf over pepper and ambery woods.", ["Woody", "Oriental", "Spicy"], ["Woody", "Spicy", "Citrus"],
  name="Mercedes-Benz Intense", **TC)

# 8 Mercedes-Benz Land EDP 100ml
t = "Mercedes-Benz Land Eau de Parfum 100ml"
F("3595471026897", "Mercedes-Benz", t, "Men", "100", "39.99", "51.99", 3,
  [("Top", "Rosemary, Black Pepper"), ("Heart", "Cacao, Fir Balsam, Geranium"), ("Base", "Patchouli, Tonka Bean, Woody Notes")],
  "Woody · Spicy", "Warm cocoa and woods with a fresh herbal lift.",
  f"{t} is a warm woody spicy fragrance for men, created by perfumer Anne Flipo and launched in 2023 as part of the Mercedes-Benz Land, Sea and Air trilogy. Rosemary and black pepper open fresh and spicy, a heart of cacao, fir balsam and geranium adds depth, and it settles onto patchouli, tonka bean and woody notes.",
  ["A fresh rosemary and black pepper opening", "A rich cacao, fir balsam and geranium heart", "A warm patchouli, tonka and woody base", "Generous 100ml Eau de Parfum"],
  "EAN 3595471026897 matched on Galaxus (Land EDP 100ml); Ferwer lists Land EDP 100ml (no EAN). Pyramid agreed by Ferwer + ScentVerdict (brand + Hypebeast same notes untiered). Woody spicy per Ferwer + ScentVerdict. 2023 + Anne Flipo per brand/Hypebeast/Ferwer. Refillable per brand/Ferwer, not stated in listing (not EAN-confirmed). Men." + AW,
  "rosemary and pepper over cacao, tonka and patchouli.", ["Woody", "Spicy"], ["Woody", "Spicy"],
  name="Mercedes-Benz Land", **PC)

# 9 Mercedes-Benz Le Parfum EDP 120ml (needs-review: splash vs spray)
t = "Mercedes-Benz Le Parfum Eau de Parfum 120ml"
F("3595471024800", "Mercedes-Benz", t, "Men", "120", "47.99", "62.99", 5,
  [("Top", "Italian Bergamot, Pink Pepper, Cascalone"), ("Heart", "Violet Leaf, Galbanum, Saffron")],
  "Woody · Chypre", "A refined, smoky-green woody chypre.",
  f"{t} is a refined woody chypre for men from Mercedes-Benz, launched in 2015 as the brand's first men's Eau de Parfum. Italian bergamot, pink pepper and Cascalone open bright and fizzy, a heart of violet leaf, galbanum and saffron adds a green, smoky elegance, and it dries down to patchouli, vetiver, oud and ambergris.",
  ["A fizzy bergamot and pink pepper opening", "A green violet leaf, galbanum and saffron heart", "A smoky patchouli, oud and vetiver dry-down", "Generous 120ml Eau de Parfum"],
  "NEEDS REVIEW: supplier calls it a 120ml Splash, but every EAN match (Superdrug UK 'Le Parfum For Him 120ml EDP Spray', Debenhams.ie, Qogita) says SPRAY – please check the bottle; spray/splash left out of title, text and product-form/dispenser metafields. EDP 120ml confirmed. Top/heart agreed by brand, FragranceReview, NST; patchouli/vetiver/oud/ambergris are heart per brand but base per FragranceReview, so mentioned in text, not tiered. Woody chypre per brand + NST. 2015 per NST + FragranceReview; perfumer single-source, left out. Men." + AW,
  "bergamot and pink pepper over violet leaf, saffron and oud.", ["Woody", "Spicy"], ["Woody", "Spicy", "Citrus"],
  name="Le Parfum", **PC, **NR)
P[-1]["mf"].pop("product-form"); P[-1]["mf"].pop("dispenser-type")

# 10 Mercedes-Benz Man EDT 100ml
t = "Mercedes-Benz Man Eau de Toilette 100ml"
F("3595471061010", "Mercedes-Benz", t, "Men", "100", "39.99", "53.99", 3,
  [("Top", "Pear, Ambrette Seed"), ("Heart", "Cedar Leaf, Geranium"), ("Base", "Rosewood, Oakmoss")],
  "Aromatic · Woody", "Juicy pear and aromatic woods with a deep mossy trail.",
  f"{t} is a modern aromatic woody fragrance for men, created by perfumer Olivier Cresp. Juicy pear and ambrette seed open smooth and fresh, a heart of cedar leaf and geranium adds an aromatic edge, and it settles onto a deep base of rosewood and oakmoss.",
  ["A juicy pear and ambrette seed opening", "An aromatic cedar leaf and geranium heart", "A deep rosewood and oakmoss base", "Generous 100ml Eau de Toilette"],
  "EAN 3595471061010 matched on Galaxus (Man EDT 100ml spray); Debenhams.ie SKU matches. Pyramid agreed by brand, Galaxus, ScentVerdict (Debenhams extra notes ignored). Aromatic woody per brand, Notino, Debenhams, ScentVerdict. Olivier Cresp per brand, ScentVerdict, ScentAdvice; launch year conflicts (2015/2016/2012), left out. Men." + AW,
  "pear and ambrette over cedar leaf, geranium and oakmoss.", ["Aromatic", "Woody"], ["Woody", "Fruity", "Fresh"],
  name="Mercedes-Benz Man", **TC)

# fix proper nouns lowercased by pyramid_answer
for p in P:
    for w in ["Calabrian","Italian","American","Bourbon","Cascalone","Cetalox","Ambrox"]:
        p["desc"]=p["desc"].replace(w.lower(), w)
P[3]["desc"]=P[3]["desc"].replace("<p>Sandalwood and cashmeran.</p>","<p>A rich floral of toasted almond, jasmine and daffodil, finishing with sandalwood and cashmeran.</p>")
P[8]["desc"]=P[8]["desc"].replace("Cascalone first, finishing with violet leaf, galbanum and saffron.","Cascalone first, then violet leaf, galbanum and saffron, drying down to patchouli, vetiver, oud and ambergris.")
write_outputs()
