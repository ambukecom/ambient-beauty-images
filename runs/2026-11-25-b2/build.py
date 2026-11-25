import sys; sys.path.insert(0, "/home/claude/ambient-beauty-images/workflow")
from lib import *
TC = dict(conc="Eau De Toilette", concl="Eau de Toilette")
PC = dict(conc="Eau De Parfum", concl="Eau de Parfum")
AW = " Awaiting photos."

# 1 Jaguar Era Reloaded EDP 100ml
t = "Jaguar Era Reloaded Eau de Parfum 100ml"
F("7640171194455", "Jaguar", t, "Men", "100", "28.49", "38.99", 5,
  [("Top", "Lemon, Orange, Apple"), ("Heart", "Jasmine, Pink Pepper, Nutmeg"), ("Base", "Cedarwood, Vanilla, Sandalwood, Amber")],
  "Amber · Citrus · Spicy", "Bright citrus over a warm, spiced amber trail.",
  f"{t} is an amber fragrance for men with a fresh citrus opening, launched in 2024. Sicilian lemon, Brazilian orange and crisp apple open it bright and juicy, a heart of jasmine, pink pepper and nutmeg adds a lively spice, and it settles into a warm base of cedarwood, vanilla, sandalwood and amber.",
  ["A bright lemon, orange and apple opening", "A lively jasmine, pink pepper and nutmeg heart", "A warm cedarwood, vanilla and amber base", "Generous 100ml Eau de Parfum"],
  "EAN 7640171194455 matched on Drogerie Natura, Dolce.pl, Allegro (PL) and Jomashop (Era Reloaded EDP 100ml, men). Pyramid agreed by the three PL retailers (ScentVerdict partly; puts apple in heart). Amber/oriental with fresh citrus per Natura + Allegro. 2024 per Natura, Dolce, Allegro, ScentVerdict. Parfumo entry lists different notes and says unisex – judged unreliable, ignored. Perfumer unconfirmed. Not the older Era EDT. Men." + AW,
  "lemon and orange over pink pepper and amber.", ["Oriental", "Citrus", "Spicy"], ["Oriental", "Citrus", "Spicy", "Woody", "Vanilla"],
  name="Era Reloaded", **PC)

# 2 Jaguar Ultimate Power EDT 100ml
t = "Jaguar Ultimate Power Eau de Toilette 100ml"
F("7640171193069", "Jaguar", t, "Men", "100", "20.49", "25.99", 5,
  [("Top", "Lemon, Bergamot, Mint"), ("Heart", "Apple, Ginger, Green Leaves"), ("Base", "Patchouli, Oakmoss, Woods")],
  "Aromatic · Fougère · Woody", "Crisp, minty citrus with a confident aromatic edge.",
  f"{t} is an aromatic fougère for men from the Jaguar For Men line, launched in 2019. Lemon, bergamot and mint open it crisp and invigorating, a heart of apple, ginger and green leaves adds a fresh, gently spicy lift, and it dries down to earthy patchouli, oakmoss and woods.",
  ["A crisp lemon, bergamot and mint opening", "A fresh apple and ginger heart", "An earthy patchouli, oakmoss and woods base", "Great-value 100ml Eau de Toilette"],
  "EAN 7640171193069 matched on Superdrug UK (Jaguar For Men Ultimate Power EDT 100ml, no longer online), Scentia, OnBuy, French Fragrance. Supplier name 'Men's Ultimate Power' – same product (aka 'For Men Ultimate Power'). Pyramid from Superdrug + Scentia (both EAN-matched) + FragranceNet + ScentVerdict; OnBuy/Perfume.com give a different pyramid (grapefruit/lavender/cedar) – minority, not used. Aromatic fougère per Scentia + Perfume.com. 2019 per Superdrug, FragranceNet, ScentVerdict. Perfumer single-source, left out. Men." + AW,
  "lemon and mint over ginger and patchouli.", ["Aromatic", "Fougere", "Woody", "Fresh"], ["Citrus", "Fresh", "Spicy", "Woody"],
  name="Ultimate Power", **TC)

# 3 J.Lo Miami Glow EDT 100ml
t = "Jennifer Lopez Miami Glow Eau de Toilette 100ml"
F("5050456110018", "Jennifer Lopez", t, "Women", "100", "25.49", "33.99", 5,
  [("Top", "Pink Grapefruit, Coconut Water, Passion Fruit"), ("Heart", "Orange Blossom, Heliotrope, Cyclamen"), ("Base", "Amber, Musk, Vanilla")],
  "Fruity · Floral", "Sun-kissed tropical glow, straight from South Beach.",
  f"{t} is a fruity floral fragrance for women, launched in 2005 and created by perfumer Caroline Sabas. Pink grapefruit, coconut water and passion fruit open it juicy and tropical, a heart of orange blossom, heliotrope and cyclamen adds a soft, sunny bloom, and it settles into warm amber, musk and vanilla.",
  ["A juicy grapefruit, coconut water and passion fruit opening", "A sunny orange blossom and heliotrope heart", "A warm amber, musk and vanilla base", "Generous 100ml Eau de Toilette"],
  "EAN 5050456110018 matched on The Perfume Shop UK, Superdrug UK (no longer online) and Perfume Forever (Miami Glow EDT 100ml, women). Pyramid agreed by The Perfume Shop, Superdrug, Parfumo, Osmoz (cyclamen by Parfumo/Osmoz/Perfume Forever; blackcurrant and blond wood database-only, left out). Fruity floral per TPS, Superdrug, Perfume Forever. 2005 per TPS, Osmoz, Perfume Forever (Parfumo 2004). Caroline Sabas per Parfumo + Perfume Forever. Not Miami Glow Sunset. Women." + AW,
  "grapefruit and coconut water over orange blossom and vanilla.", ["Fruity", "Floral"], ["Fruity", "Floral", "Citrus", "Vanilla"],
  name="Miami Glow", **TC)

# 4 Jimmy Choo L'Eau EDT 90ml
t = "Jimmy Choo L'Eau Eau de Toilette 90ml"
F("3386460073868", "Jimmy Choo", t, "Women", "90", "46.49", "60.99", 5,
  [("Top", "Hibiscus, Bergamot"), ("Heart", "Nectarine, Peony"), ("Base", "Cedarwood, Musk")],
  "Floral · Fruity · Musky", "Light, luminous and effortlessly feminine.",
  f"{t} is a floral fruity fragrance for women, launched in 2017 and created by perfumer Juliette Karagueuzoglou. Hibiscus and bergamot open it fresh and airy, a heart of juicy nectarine and peony brings a soft, radiant femininity, and it settles into a clean base of cedarwood and musk.",
  ["A fresh hibiscus and bergamot opening", "A juicy nectarine and peony heart", "A clean cedarwood and musk base", "Generous 90ml Eau de Toilette"],
  "EAN 3386460073868 matched on Superdrug UK (Jimmy Choo L'eau EDT 90ml, women, in store only). Pyramid agreed by Interparfums (licence holder), Notino UK, Escentual, Superdrug, TJ Hughes. Floral fruity per Interparfums, Notino, TJ Hughes. 2017 + Juliette Karagueuzoglou per Notino + TJ Hughes. Not the 60ml (already in store). Women." + AW,
  "hibiscus and bergamot over nectarine and musk.", ["Floral", "Fruity", "Musky"], ["Floral", "Fruity", "Citrus", "Fresh"],
  name="Jimmy Choo L'Eau", **TC)

# 5 Jimmy Choo Rose Passion EDP 100ml
t = "Jimmy Choo Rose Passion Eau de Parfum 100ml"
F("3386460136549", "Jimmy Choo", t, "Women", "100", "41.49", "55.99", 5,
  [("Top", "Coconut Water, Frangipani"), ("Heart", "Orchid, Jasmine"), ("Base", "Sandalwood, Vanilla")],
  "Floral · Amber · Solar", "A sun-warmed, sensual floral glow.",
  f"{t} is a solar floral amber fragrance for women, launched in 2023. Coconut water and frangipani open it with a sunny, tropical softness, a heart of orchid and jasmine brings a rich floral sensuality, and it settles into a creamy base of sandalwood and vanilla.",
  ["A sunny coconut water and frangipani opening", "A sensual orchid and jasmine heart", "A creamy sandalwood and vanilla base", "Generous 100ml Eau de Parfum"],
  "EAN 3386460136549 matched on Proshop and Kruidvat (Rose Passion EDP 100ml, women); Escentual image files carry the EAN. Pyramid agreed by Escentual, John Lewis, Well Pharmacy. No rose note in any source despite the name. Floral amber/solar per John Lewis, Well, Escentual. 2023 per John Lewis, Well, Escentual. Perfumer single-source, left out. Not the 40ml (already in store). Women." + AW,
  "coconut water and frangipani over jasmine and vanilla.", ["Floral", "Oriental"], ["Floral", "Jasmine", "Sandalwood", "Vanilla"],
  name="Rose Passion", **PC)

# 6 Jimmy Choo Urban Hero EDP 100ml
t = "Jimmy Choo Urban Hero Eau de Parfum 100ml"
F("3386460109369", "Jimmy Choo", t, "Men", "100", "42.99", "54.99", 5,
  [("Top", "Lemon Caviar, Black Pepper"), ("Heart", "Rosewood, Vetiver"), ("Base", "Leather, Grey Amber")],
  "Woody · Aromatic · Leather", "Bold, magnetic and made for the city.",
  f"{t} is a woody aromatic fragrance for men, launched in 2019 and created by perfumers Antoine Maisondieu and Marion Costero. Zesty lemon caviar and black pepper open it with a bright, spicy energy, a heart of rosewood and vetiver brings smooth woody depth, and it settles into a magnetic base of leather and grey amber.",
  ["A zesty lemon caviar and black pepper opening", "A smooth rosewood and vetiver heart", "A magnetic leather and grey amber base", "Generous 100ml Eau de Parfum"],
  "EAN 3386460109369 matched on Al Seer & Safeer (Urban Hero EDP 100ml, men). Original 2019 Urban Hero, not the Gold Edition (already in store). Pyramid agreed by Lookfantastic UK, The Perfume Shop, Escentual, FashionUnited (lemon caviar = finger lime; grey amber = ambergris). Woody aromatic per Lookfantastic, TPS, NST. 2019 + Maisondieu/Costero per NST, ScentAdvice, FashionUnited. Men." + AW,
  "lemon caviar and black pepper over vetiver and leather.", ["Woody", "Aromatic", "Leather"], ["Woody", "Citrus", "Spicy"],
  name="Urban Hero", **PC)

# 7 Karl Lagerfeld Bois d'Ambre EDT 100ml
t = "Karl Lagerfeld Bois d'Ambre Eau de Toilette 100ml"
F("3386460124867", "Karl Lagerfeld", t, "Men", "100", "27.99", "36.99", 5,
  [("Top", "Bergamot, Plum, Bitter Orange"), ("Heart", "Clary Sage, Geranium"), ("Base", "Amber, Tonka Bean")],
  "Woody · Amber · Aromatic", "Warm amber woods with a fruity, aromatic twist.",
  f"{t} is an amber woody fragrance for men from the Les Parfums Matières collection, launched in 2021. Bergamot, plum and bitter orange open it juicy and bright, a heart of clary sage and geranium adds an aromatic freshness, and it settles into a warm, sweet base of amber and tonka bean.",
  ["A juicy bergamot, plum and bitter orange opening", "An aromatic clary sage and geranium heart", "A warm amber and tonka bean base", "Generous 100ml Eau de Toilette"],
  "EAN 3386460124867 matched on Kruidvat NL (Bois d'Ambre EDT 100ml, herenparfum). Pyramid agreed by Parfumo + Lyko (Fragrancenet confirms bergamot/clary sage/amber); cedar and guaiac wood tier-labelled by Parfumo only, left out. Amber woody per Lyko, woody per Fragrancenet/Parfumo. 2021 per Parfumo, Fragrancenet, ScentAdvice. Perfumer (Emilie Bevierre-Coppermann) aggregator-only, left out. Perfume.com lists different notes (likely older product) – ignored. Fragrancenet labels it unisex, description says men. Men." + AW,
  "bergamot and plum over clary sage and amber.", ["Woody", "Oriental", "Aromatic"], ["Woody", "Fruity", "Citrus", "Oriental"],
  name="Bois d'Ambre", **TC)

# 8 Karl Lagerfeld Bois de Cypres EDT 100ml
t = "Karl Lagerfeld Bois de Cyprès Eau de Toilette 100ml"
F("3386460133869", "Karl Lagerfeld", t, "Men", "100", "26.49", "35.99", 5,
  [("Top", "Mandarin, Cardamom, Lemon"), ("Heart", "Lavender, Cypress, Water Mint"), ("Base", "Cashmere Wood, Vetiver, Clary Sage")],
  "Aromatic · Woody · Fresh", "Cool cypress and lavender, crisp as a Mediterranean breeze.",
  f"{t} is an aromatic woody fragrance for men from the Les Parfums Matières collection, launched in 2023. Mandarin, cardamom and lemon open it zesty and lightly spiced, a heart of lavender, cypress and water mint brings a cool, green freshness, and it settles into a smooth base of cashmere wood, vetiver and clary sage.",
  ["A zesty mandarin, cardamom and lemon opening", "A cool lavender, cypress and mint heart", "A smooth cashmere wood and vetiver base", "Generous 100ml Eau de Toilette"],
  "EAN 3386460133869 matched on Proshop NL (Bois de Cypres EDT 100ml, men; its generic note list ignored). Pyramid agreed by Lookfantastic UK, Lyko, ScentAdvice, Fragplace (NST same notes untiered). Aromatic woody per Lookfantastic + Lyko. 2023 per NST, ScentAdvice, Fragplace. Perfumer (Alexandra Carlin) aggregator-only, left out. Some sites call it EDP – EAN page says EDT. Men." + AW,
  "mandarin and cardamom over lavender, cypress and vetiver.", ["Aromatic", "Woody", "Fresh"], ["Lavender", "Citrus", "Woody", "Fresh"],
  name="Bois de Cyprès", **TC)

# 9 Karl Lagerfeld Bois de Vetiver EDT 100ml
t = "Karl Lagerfeld Bois de Vetiver Eau de Toilette 100ml"
F("3386460087261", "Karl Lagerfeld", t, "Men", "100", "28.99", "37.99", 5,
  [("Top", "Blood Orange, Pink Grapefruit, Mint"), ("Heart", "Vetiver, Rose, Geranium"), ("Base", "Ambroxan, Musk, Patchouli")],
  "Woody · Aromatic · Fresh", "Fresh, zesty vetiver with a modern woody edge.",
  f"{t} is a fresh woody aromatic fragrance for men, launched in 2017 as the first men's scent of the Les Parfums Matières collection and created by perfumer Christophe Raynaud. Blood orange, pink grapefruit and mint open it zesty and cool, a heart of vetiver, rose and geranium brings earthy, green depth, and it settles into a clean base of ambroxan, musk and patchouli.",
  ["A zesty blood orange, grapefruit and mint opening", "An earthy vetiver heart with rose and geranium", "A clean ambroxan, musk and patchouli base", "Generous 100ml Eau de Toilette"],
  "EAN 3386460087261 matched on Galaxus CH and Alza SK (Bois de Vetiver EDT 100ml, men). Pyramid agreed by Beauty Bay, Alza, Fragplace (Lyko differs; cedar Lyko-only, left out). Woody aromatic per Beauty Bay, fresh woody per Lyko + NST. 2017 + Christophe Raynaud per NST + Fragplace. Brand site says 'Eau de parfum' for 100ml – retailers, EAN pages and supplier say EDT; kept EDT. Lyko files it under women in breadcrumb only. Men." + AW,
  "blood orange and grapefruit over vetiver and musk.", ["Woody", "Aromatic", "Fresh"], ["Woody", "Citrus", "Fresh"],
  name="Bois de Vetiver", **TC)

# 10 Karl Lagerfeld Classic Aftershave Lotion 100ml
t = "Karl Lagerfeld Classic Aftershave Lotion 100ml"
pyr = [("Top", "Bergamot"), ("Heart", "Patchouli, Orris, Rose, Tobacco"), ("Base", "Amber, Tonka Bean")]
add(cat_name="Fragrances", bc="3386460094542", title=t, vendor="Karl Lagerfeld", type=TYPE["Men"], gender="Men", cat=TAXON["aftershave"],
    price="29.49", cmp="37.99", qty=5, tags=["Karl Lagerfeld", "Men", "Aftershave"],
    seo=("Karl Lagerfeld Classic Aftershave Lotion 100ml",
         "Karl Lagerfeld Classic Aftershave Lotion 100ml: the warm, woody oriental Lagerfeld Classic scent for after shaving." + FREE),
    form="Aftershave Lotion (Splash)", size="100", unit="ml", gpc=GPC["fragrance"], status="needs-review",
    mf={"product-form": ["Liquid"]},  # age-group not allowed in aftershave category
    note="EAN 3386460094542 matched on Superdrug UK (Lagerfeld Classic After Shave Lotion 100ml), Galaxus DE and Parfumtrend (100ml, male, Inter Parfums). Scent = Lagerfeld Classic (1978) by name; no page ties this EAN to the 1978 entry directly. NEEDS REVIEW: supplier says splash, Galaxus says spray, Parfumtrend says bottle – listing says splash per supplier, please check the bottle. Full pyramids differ (Parfumo/JustMyLook vs Lyko): only notes common to all lists shown. Skin-care claims single-source (JustMyLook), left out. Oriental woody per JustMyLook, Lyko, Galaxus. Men." + AW,
    desc=body("The timeless Lagerfeld Classic scent, for the finishing touch after shaving.",
              f"{t} carries the warm, woody oriental character of Lagerfeld Classic, the house's signature men's scent first launched in 1978. Fresh bergamot leads into a rich heart of patchouli, orris, rose and tobacco, settling into warm amber and tonka bean.",
              [("Scent pyramid", kd(pyr)),
               ("How to use", "<p>After shaving, apply a little to the face and neck.</p>")],
              [("Brand", "Karl Lagerfeld"), ("Type", "Aftershave lotion"), ("Size", "100ml"),
               ("Scent profile", "Oriental · Woody · Powdery"), ("Wear", "Men")],
              ["The classic Lagerfeld scent since 1978", "Warm patchouli, tobacco and orris", "A rich amber and tonka finish", "100ml bottle"],
              [("What does Karl Lagerfeld Classic Aftershave smell like?", pyramid_answer(pyr)),
               ("Is it for men?", "Yes, it is a men's aftershave.")]))

write_outputs(".")
for p in P: print(p["status"], p["seo"][0], len(p["seo"][0]), len(p["seo"][1]))
