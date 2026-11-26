import sys; sys.path.insert(0, "/home/claude/ambient-beauty-images/workflow")
from lib import *
TC = dict(conc="Eau De Toilette", concl="Eau de Toilette")
PC = dict(conc="Eau De Parfum", concl="Eau de Parfum")
XC = dict(conc="Extrait De Parfum", concl="Extrait de Parfum")
AW = " Awaiting photos."
NR = dict(status="needs-review")

# 1 Arabiyat Prestige Nyla Sherbet EDP 80ml
t = "Arabiyat Prestige Nyla Sherbet Eau de Parfum 80ml"
F("6290361915912", "Arabiyat Prestige", t, "Women", "80", "26.99", "34.99", 5,
  [("Top", "Strawberry, Mandarin"), ("Heart", "Plum"), ("Base", "Musk, Sandalwood")],
  "Fruity · Sweet", "A juicy, sherbet-sweet burst of berries and citrus.",
  f"{t} is a sweet, fruity fragrance for women from Arabiyat Prestige. Juicy strawberry and bright mandarin open with a playful fizz, a ripe plum heart follows, and it softens onto a creamy base of musk and sandalwood.",
  ["A juicy strawberry and mandarin opening", "A ripe, fruity plum heart", "A soft musk and sandalwood base", "Generous 80ml Eau de Parfum"],
  "EAN 6290361915912 matched on Superdrug UK + bjutip (80ml EDP). Pyramid agreed by Superdrug, Justmylook, bjutip, Arabic Parfums, Parfumo, Fragrantica. Fruity/sweet per all sources. Launch year/perfumer single-source, left out. Not the original Nyla. Women." + AW,
  "strawberry and mandarin over plum, musk and sandalwood.", ["Fruity", "Gourmand"], ["Fruity", "Sandalwood"],
  name="Nyla Sherbet", **PC)

# 2 Armaf Tres Nuit Lyric Pour Homme EDP 100ml
t = "Armaf Tres Nuit Lyric Pour Homme Eau de Parfum 100ml"
F("6294015138290", "Armaf", t, "Men", "100", "32.99", "41.99", 5,
  [("Top", "Bergamot, Watery Notes, Mandarin Orange"), ("Heart", "Rosemary, Lavender, Cypress"), ("Base", "Musk, Patchouli, Amber")],
  "Fresh · Aquatic · Aromatic", "Cool, watery citrus with a herbal, aromatic heart.",
  f"{t} is a fresh aquatic fragrance for men from Armaf. Bergamot, watery notes and mandarin orange open crisp and clean, a heart of rosemary, lavender and cypress adds an aromatic edge, and it settles onto a smooth base of musk, patchouli and amber.",
  ["A crisp bergamot, mandarin and watery opening", "An aromatic heart of rosemary, lavender and cypress", "A smooth musk, patchouli and amber base", "Generous 100ml Eau de Parfum"],
  "EAN 6294015138290 matched on Superdrug UK (100ml EDP). Pyramid agreed by Superdrug, Perfumania, MyPerfumeShop, DecantX (Scento swaps heart/base; majority tiering used). Fresh/aquatic/citrus per Perfumania, MyPerfumeShop, DecantX. Launch 2020 not stated (weak sources). EDP, not the EDT version. Men." + AW,
  "bergamot and watery notes over lavender, rosemary and amber.", ["Fresh", "Aquatic", "Aromatic"], ["Fresh", "Aquatic", "Citrus", "Lavender"],
  name="Tres Nuit Lyric", **PC)

# 3 French Avenue x Aromatix Magnetiq Extrait 100ml
t = "French Avenue x Aromatix Magnetiq Extrait de Parfum 100ml"
F("6298042001527", "French Avenue", t, "Unisex", "100", "39.99", "52.99", 2,
  [("Top", "Bergamot, Lavender, Pink Pepper"), ("Heart", "Orange Blossom, Neroli, Iris, Rosemary, Musk"), ("Base", "Cedarwood, Sandalwood, Amber, Vanilla, Myrrh, Oakmoss")],
  "Woody · Aromatic", "A magnetic woody aromatic in rich extrait strength.",
  f"{t} is a woody aromatic fragrance for everyone, created by French Avenue in collaboration with Aromatix. Bergamot, lavender and pink pepper open with a fresh, peppery lift, a heart of orange blossom, neroli, iris and rosemary adds polish, and it dries down to cedarwood, sandalwood, amber, vanilla, myrrh and oakmoss.",
  ["A fresh bergamot, lavender and pink pepper opening", "An elegant orange blossom, neroli and iris heart", "A rich base of cedarwood, sandalwood, amber and vanilla", "Long-lasting Extrait de Parfum in 100ml"],
  "EAN 6298042001527 matched on bjutip (100ml Extrait de Parfum). Concentration: Extrait per bjutip, Justmylook, Arabic Parfums (supplier form 'Parfum' consistent; Justmylook spec 'Parfum 30%'). Pyramid agreed by bjutip, Justmylook, Arabic Parfums. Woody aromatic per bjutip + Justmylook. Unisex." + AW,
  "bergamot and lavender over orange blossom, iris and cedarwood.", ["Woody", "Aromatic"], ["Woody", "Lavender", "Sandalwood", "Vanilla"],
  name="Magnetiq", **XC)

# 4 French Avenue x Aromatix Royal Taboo EDP 100ml (needs-review: concentration)
t = "French Avenue x Aromatix Royal Taboo Eau de Parfum 100ml"
F("6290360379227", "French Avenue", t, "Unisex", "100", "41.49", "51.99", 1,
  [("Top", "Cardamom, Cinnamon, Benzoin, Amber"), ("Heart", "Tobacco, Cashmere Wood, Heliotrope, Jasmine"), ("Base", "Tonka Bean, Patchouli, Vanilla, Dry Woods")],
  "Oriental · Woody · Spicy", "Warm spice and tobacco wrapped in amber and vanilla.",
  f"{t} is a warm oriental woody fragrance for everyone, created by French Avenue with Aromatix. Cardamom and cinnamon open over benzoin and amber, a heart of tobacco, cashmere wood, heliotrope and jasmine follows, and it settles onto tonka bean, patchouli, vanilla and dry woods.",
  ["A spicy cardamom and cinnamon opening", "A smooth tobacco and cashmere wood heart", "A warm tonka, vanilla and patchouli base", "Generous 100ml bottle"],
  "NEEDS REVIEW: concentration unresolved – EDP per supplier, TJ Hughes UK, Boozyshop, BestBuy.ca; but the EAN match (bjutip) and Notino FR/PL list it as Extrait de Parfum. Listed as EDP (supplier) – please check the box. Pyramid agreed by bjutip, TJ Hughes, Boozyshop. Oriental woody per bjutip, TJ Hughes, BestBuy. Parfumo page for a 2009 'Royal Taboo' is a different product, ignored. Unisex." + AW,
  "cardamom and cinnamon over tobacco, tonka and vanilla.", ["Oriental", "Woody", "Spicy"], ["Oriental", "Woody", "Spicy", "Vanilla"],
  name="Royal Taboo", **PC, **NR)

# 5 Lattafa Ajayeb Dubai EDP 100ml
t = "Lattafa Ajayeb Dubai Eau de Parfum 100ml"
F("6290360591551", "Lattafa", t, "Unisex", "100", "21.99", "28.99", 4,
  [("Top", "Saffron, Pineapple"), ("Heart", "Coffee, Violet Leaves"), ("Base", "Vanilla, Butterscotch, Sandalwood")],
  "Gourmand · Spicy · Woody", "Saffron, coffee and butterscotch for a warm, sweet trail.",
  f"{t} is a sweet, warm fragrance for everyone from Lattafa, launched in 2023. Saffron and juicy pineapple open with a spiced sweetness, a heart of coffee and violet leaves follows, and it melts onto a creamy base of vanilla, butterscotch and sandalwood.",
  ["A spiced saffron and pineapple opening", "A rich coffee and violet leaf heart", "A creamy vanilla, butterscotch and sandalwood base", "Generous 100ml Eau de Parfum"],
  "EAN 6290360591551 matched on Superdrug UK, Lyko, GiftExpress, McGrocer, Walmart (100ml EDP). Pyramid agreed by Superdrug, Lyko, GiftExpress, McGrocer, Fragrantica. 2023 per Fragrantica, GiftExpress, McGrocer. Family from notes + Fragrantica accords (no retailer states one). Not 'Ajayeb Dubai Portrait'. Unisex (Lyko files under men)." + AW,
  "saffron and coffee over vanilla, butterscotch and sandalwood.", ["Gourmand", "Spicy", "Woody"], ["Vanilla", "Spicy", "Sandalwood"],
  name="Ajayeb Dubai", **PC)

# 6 Lattafa Al Areeq Gold EDP 100ml
t = "Lattafa Al Areeq Gold Eau de Parfum 100ml"
F("6291108738696", "Lattafa", t, "Unisex", "100", "27.99", "36.99", 1,
  [("Top", "Saffron, Black Tea"), ("Heart", "Incense, Suede, Leather"), ("Base", "Amberwood, Vanilla, Musk")],
  "Oriental · Leather · Spicy", "Saffron and smoky black tea over soft suede and amber.",
  f"{t} is a warm oriental leather fragrance for everyone from the Lattafa Pride line. Saffron and black tea open rich and smoky, a heart of incense, suede and leather follows, and it settles onto amberwood, vanilla and musk.",
  ["A rich saffron and black tea opening", "A smoky incense, suede and leather heart", "A warm amberwood, vanilla and musk base", "Generous 100ml Eau de Parfum"],
  "EAN 6291108738696 matched on Superdrug UK + Galaxus (100ml EDP, Lattafa Pride). Pyramid agreed by Superdrug, TJ Hughes, Parfumo. Oriental/leather/spicy per Parfumo, TJ Hughes, Galaxus. Unisex per retailers (Parfumo lists women). Year/perfumer unconfirmed." + AW,
  "saffron and black tea over incense, suede and amberwood.", ["Oriental", "Leather", "Spicy", "Woody"], ["Oriental", "Spicy", "Vanilla"],
  name="Al Areeq Gold", **PC)

# 7 Maison Alhambra Athena EDP 100ml (needs-review: two pyramids in circulation)
t = "Maison Alhambra Athena Eau de Parfum 100ml"
F("6290360599243", "Maison Alhambra", t, "Women", "100", "27.49", "36.99", 2,
  [("Top", "Yerba Mate, Cypress, Thyme, Saffron, Fruity Notes"), ("Heart", "Jasmine, Iris, Rose"), ("Base", "Amber, Leather, Vanilla, Musk, Vetiver, Cedar")],
  "Floral", "A graceful floral with a herbal, saffron-kissed opening.",
  f"{t} is a floral fragrance for women from Maison Alhambra. Yerba mate, cypress, thyme and saffron open with fruity, herbal brightness, a heart of jasmine, iris and rose follows, and it settles onto amber, leather, vanilla, musk, vetiver and cedar.",
  ["A herbal, fruity opening with saffron", "A floral heart of jasmine, iris and rose", "A warm amber, vanilla and cedar base", "Generous 100ml Eau de Parfum"],
  "NEEDS REVIEW: two different pyramids are published for Athena. Shown: the set on the EAN-matched pages (Walmart, lcd-phone) also agreed by Emirates Oud UK + Dubai Perfume Shop. FragranceNet, JustMyLook, IntenseOud give tangerine/pink pepper/bergamot – jasmine sambac/ylang/lily – vanilla/sandalwood/patchouli. Please check the box. EAN 6290360599243 matched Galaxus, Walmart, lcd-phone (100ml EDP). Floral per Galaxus, JustMyLook, IntenseOud, Emirates Oud. Women." + AW,
  "herbal saffron over jasmine, iris and rose with amber.", ["Floral"], ["Floral", "Jasmine", "Vanilla"],
  name="Athena", **PC, **NR)

# 8 Maison Alhambra Pacific Blue EDP 100ml (needs-review: size)
t = "Maison Alhambra Pacific Blue Eau de Parfum 100ml"
F("6290362343196", "Maison Alhambra", t, "Unisex", "100", "29.49", "38.99", 1,
  [("Top", "Neroli, Bergamot, Lemon, Mandarin, Bitter Orange, Lavender, Myrtle, Rosemary"), ("Heart", "Orange Blossom, Jasmine, Neroli"), ("Base", "Amber, Ambrette, Angelica")],
  "Citrus · Fresh · Aquatic", "A sun-bright splash of Mediterranean citrus and neroli.",
  f"{t} is a fresh citrus fragrance for everyone from Maison Alhambra. Neroli, bergamot, lemon, mandarin and bitter orange open with lavender, myrtle and rosemary, a heart of orange blossom, jasmine and neroli follows, and it settles onto amber, ambrette and angelica.",
  ["A sparkling neroli and citrus opening", "A bright orange blossom and jasmine heart", "A soft amber, ambrette and angelica base", "Fresh, breezy unisex character"],
  "NEEDS REVIEW: size – supplier and Superdrug UK (EAN match) say 100ml, but eCosmetics (same EAN) and most retailers (Galaxus, Arabic Parfums, Al Manaar, FragranceNet) sell Pacific Blue as 80ml; please check the bottle. EDP confirmed. Pyramid agreed by Arabic Parfums + Emirates Oud UK (Parfumo confirms lemon, mandarin, bitter orange / orange blossom / amber). Citrus/fresh per Galaxus, Parfumo, Arabic Parfums; aquatic per Superdrug, FragranceNet, Al Manaar. Unisex." + AW,
  "neroli and citrus over orange blossom, jasmine and amber.", ["Citrus", "Fresh", "Aquatic"], ["Citrus", "Fresh", "Aquatic"],
  name="Pacific Blue", **PC, **NR)

# 9 Maison Alhambra Winsome EDP 90ml
t = "Maison Alhambra Winsome Eau de Parfum 90ml"
F("6291108736562", "Maison Alhambra", t, "Unisex", "90", "25.99", "33.99", 1,
  [("Top", "Violet Leaf, Bergamot, Coriander"), ("Heart", "Rose, Lily of the Valley, Black Pepper"), ("Base", "Ambergris, Patchouli, Bourbon Vanilla")],
  "Spicy · Amber · Floral", "Green violet leaf and peppered rose over warm vanilla.",
  f"{t} is a spicy amber fragrance for everyone from Maison Alhambra. Violet leaf, bergamot and coriander open green and bright, a heart of rose, lily of the valley and black pepper adds a spiced floral touch, and it settles onto ambergris, patchouli and bourbon vanilla.",
  ["A green violet leaf, bergamot and coriander opening", "A peppery rose and lily of the valley heart", "A warm ambergris, patchouli and vanilla base", "Generous 90ml Eau de Parfum"],
  "EAN 6291108736562 matched on Superdrug UK, Target, Triple Traders (90ml EDP). Pyramid agreed by Superdrug, Target, Triple Traders, Parfumo. Spicy per Target, Parfumo, Superdrug; amber/floral per Target, Superdrug. Unisex per Superdrug + Target (Parfumo and Triple Traders text say men)." + AW,
  "violet leaf and bergamot over peppered rose and vanilla.", ["Spicy", "Oriental", "Floral"], ["Spicy", "Floral", "Rose", "Vanilla"],
  name="Winsome", **PC)

# 10 Marc Jacobs Daisy Dream EDT 50ml
t = "Marc Jacobs Daisy Dream Eau de Toilette 50ml"
F("3607349764289", "Marc Jacobs", t, "Women", "50", "38.99", "51.99", 3,
  [("Top", "Blackberry, Grapefruit, Pear"), ("Heart", "Blue Wisteria, Jasmine, Lychee"), ("Base", "Coconut Water, White Woods, Musk")],
  "Floral · Fruity", "Light, airy and dreamy, like a sunny sky full of daisies.",
  f"{t} is a fruity floral fragrance for women, created by perfumer Alberto Morillas and launched in 2014. Blackberry, grapefruit and pear open fresh and juicy, a heart of blue wisteria, jasmine and lychee adds a soft floral glow, and it settles onto coconut water, white woods and musk.",
  ["A juicy blackberry, grapefruit and pear opening", "A luminous blue wisteria and jasmine heart", "A soft coconut water, white woods and musk base", "Handy 50ml Eau de Toilette"],
  "EAN 3607349764289 matched on WatchMaxx (50ml EDT); John Lewis UK lists 50ml EDT. Pyramid agreed by WatchMaxx, John Lewis, Sephora, Parfumo. 2014 per John Lewis + Parfumo; Alberto Morillas per Parfumo + Escentual. Not Daisy Dream Forever. Women." + AW,
  "blackberry and pear over wisteria, jasmine and white woods.", ["Floral", "Fruity"], ["Floral", "Fruity", "Jasmine"],
  name="Daisy Dream", **TC)

write_outputs()
