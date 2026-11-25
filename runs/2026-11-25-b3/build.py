import sys; sys.path.insert(0, "/home/claude/ambient-beauty-images/workflow")
from lib import *
TC = dict(conc="Eau De Toilette", concl="Eau de Toilette")
PC = dict(conc="Eau De Parfum", concl="Eau de Parfum")
AW = " Awaiting photos."

def GS(bc, vendor, title, seo_t, gender, size, price, cmp, qty, pyr, profile, hook, intro, contents, love, note, seo_d,
       of, fr, name, conc="Eau De Parfum", concl="Eau de Parfum", status="done", form_suffix=" Gift Set"):
    """Fragrance set: fragrance standard (3 tags) plus a 'What's in the set' block (as runs/2026-11-21-b4)."""
    q2 = {"Men": ("Is it for men?", "Yes, it is a men's fragrance gift set."),
          "Women": ("Is it for women?", "Yes, it is a women's fragrance gift set."),
          "Unisex": ("Is it unisex?", "Yes, it is made for everyone.")}[gender]
    qs = ([(f"What does {name} smell like?", pyramid_answer(pyr))] if pyr else []) + [("What's in the set?", "; ".join(contents) + "."), q2]
    blocks = [("What's in the set", ul(contents))] + ([("Scent pyramid", kd(pyr))] if pyr else [])
    add(cat_name="Fragrances", bc=bc, title=title, vendor=vendor, type=TYPE[gender], gender=gender, cat=TAXON["perfume"],
        price=price, cmp=cmp, qty=qty, tags=[vendor, gender, conc], seo=(seo_t, f"{seo_t}: {seo_d}" + FREE), status=status,
        form=concl + form_suffix, size=size, unit="ml", note=note, gpc=GPC["fragrance"],
        mf={"age-group": ["Adults"], "product-form": ["Spray"], "dispenser-type": ["Spray"], "olfactory-family": list(of), "fragrance": list(fr)},
        desc=body(hook, intro, blocks,
                  [("Brand", vendor), ("Concentration", concl), ("Contents", " + ".join(c.split(" (")[0] for c in contents)),
                   ("Scent profile", profile), ("Wear", gender)], love, qs))

# 1 Fleur d'Iris
t = "Karl Lagerfeld Fleur d'Iris Eau de Parfum 100ml"
F("3386460161565", "Karl Lagerfeld", t, "Women", "100", "27.99", "37.99", 5,
  [("Top", "Mandarin, Orange Blossom"), ("Heart", "Iris, Orchid"), ("Base", "Heliotrope, Vanilla, Musk")],
  "Floral · Amber · Powdery", "Soft, powdery iris wrapped in warm vanilla.",
  f"{t} is an amber floral fragrance for women from the Les Parfums Matières collection, launched in 2025. Mandarin and orange blossom open it bright and luminous, a heart of iris and orchid brings a soft, powdery elegance, and it settles into a warm, comforting base of heliotrope, vanilla and musk.",
  ["A bright mandarin and orange blossom opening", "A soft, powdery iris and orchid heart", "A warm heliotrope, vanilla and musk base", "Generous 100ml Eau de Parfum"],
  "EAN 3386460161565 matched on Galaxus CH (Fleur d'Iris EDP 100ml). Pyramid agreed by Sephora India, NST, ScentVerdict, ScentAdvice (PromoFarma puts orange blossom in heart; Luxplus gives a simpler list). Parfumo entry lists unrelated notes and says unisex – ignored. Amber floral per NST + PromoFarma (Sephora India: powdery floral). 2025 per NST, ScentVerdict, ScentAdvice. Perfumer single-source, left out. Women." + AW,
  "mandarin and orange blossom over iris and vanilla.", ["Floral", "Oriental", "Powdery"], ["Floral", "Citrus", "Vanilla"],
  name="Fleur d'Iris", **PC)

# 2 Fleur de Pivoine
t = "Karl Lagerfeld Fleur de Pivoine Eau de Parfum 100ml"
F("3386460133814", "Karl Lagerfeld", t, "Women", "100", "26.49", "33.99", 5,
  [("Top", "Mandarin, Green Notes"), ("Heart", "Peony, Lily of the Valley, Jasmine"), ("Base", "White Cedar, Musk, Amber")],
  "Floral · Fresh", "Fresh-cut peony with a bright, green sparkle.",
  f"{t} is a fresh floral fragrance for women from the Les Parfums Matières collection, launched in 2023 and created by perfumer Emilie Bevierre-Coppermann. Mandarin and green notes open it crisp and fresh, a heart of peony, lily of the valley and jasmine blooms soft and feminine, and it settles into a clean base of white cedar, musk and amber.",
  ["A crisp mandarin and green opening", "A blooming peony, lily of the valley and jasmine heart", "A clean white cedar, musk and amber base", "Generous 100ml Eau de Parfum"],
  "EAN 3386460133814 matched on Proshop SE (Fleur de Pivoine EDP 100ml). Pyramid agreed by Lookfantastic, ParfumPlus, JustMyLook, Parfumo, ScentAdvice; the berry top note is named differently (blackcurrant / redcurrant / gooseberry) so left out. Fresh floral per Lookfantastic + Parfumo (others: fruity floral). 2023 + Emilie Bevierre-Coppermann per Parfumo, ScentAdvice, ParfumPlus. Women." + AW,
  "mandarin and green notes over peony and white cedar.", ["Floral", "Fresh"], ["Floral", "Jasmine", "Citrus", "Fresh", "Woody"],
  name="Fleur de Pivoine", **PC)

# 3 For Him EDT 100ml
t = "Karl Lagerfeld for Him Eau de Toilette 100ml"
F("3386460059183", "Karl Lagerfeld", t, "Men", "100", "27.99", "37.99", 5,
  [("Top", "Mandarin, Lavender"), ("Heart", "Violet, Green Apple"), ("Base", "Sandalwood, Amber")],
  "Aromatic · Fougère · Woody", "Fresh, modern fougère with a crisp green twist.",
  f"{t} (also sold as Karl Lagerfeld Pour Homme) is an aromatic fougère for men, launched in 2014 and created by perfumer Jean-Christophe Hérault. Mandarin and lavender open it fresh and aromatic, a heart of violet and green apple adds a crisp, modern lift, and it dries down to a smooth base of sandalwood and amber.",
  ["A fresh mandarin and lavender opening", "A crisp violet and green apple heart", "A smooth sandalwood and amber base", "Generous 100ml Eau de Toilette"],
  "EAN 3386460059183 matched on CityPerfume AU (Karl Lagerfeld Pour Homme / for Him EDT 100ml) and Alza HU. Pyramid agreed by CityPerfume, Alza, ScentAdvice (Escentual swaps apple/lavender tiers). Aromatic fougère per Escentual + CityPerfume (NST: fougère). 2014 + Jean-Christophe Hérault per NST + ScentAdvice (CityPerfume 2014). Store already has the 50ml (different EAN) – this is the 100ml. Alza says women can wear it too. Men." + AW,
  "mandarin and lavender over violet and sandalwood.", ["Aromatic", "Fougere", "Woody"], ["Lavender", "Citrus", "Fresh", "Woody", "Sandalwood"],
  name="Karl Lagerfeld for Him", **TC)

# 4 Jeans Urban Pink
t = "Karl Lagerfeld Jeans Urban Pink Eau de Parfum 100ml"
F("3386460160193", "Karl Lagerfeld", t, "Women", "100", "28.49", "37.99", 3,
  [("Top", "Bergamot"), ("Heart", "Turkish Rose"), ("Base", "Bourbon Vanilla")],
  "Floral · Vanilla", "Rosy, sweet and full of city energy.",
  f"{t} is a floral fragrance for women from the Karl Lagerfeld Jeans line, launched in 2025. Sparkling bergamot opens it bright and fresh, a heart of Turkish rose brings a soft, romantic bloom, and it settles into a warm, sweet base of Bourbon vanilla.",
  ["A sparkling bergamot opening", "A romantic Turkish rose heart", "A warm Bourbon vanilla base", "Generous 100ml Eau de Parfum"],
  "EAN 3386460160193 matched on Drogeria VMD (Jeans Urban Pink W EDP 100ml) and Galaxus CH (Karl Lagerfeld Jeans EDP 100ml, Urban Pink in description); 60ml is a different EAN. Notes agreed by Parfumo, Lyko, Druni, VMD, NST. Floral per Lyko, NST describes floral with amber warmth. 2025 per Parfumo + NST. Perfumers single-source, left out. Women." + AW,
  "bergamot over Turkish rose and Bourbon vanilla.", ["Floral"], ["Floral", "Rose", "Citrus", "Vanilla"],
  name="Jeans Urban Pink", **PC)

# 5 Ikonik Pour Femme
t = "Karl Lagerfeld Ikonik Pour Femme Eau de Parfum 100ml"
F("3386460149822", "Karl Lagerfeld", t, "Women", "100", "35.99", "47.99", 4,
  [("Top", "Raspberry, Mandarin, Rose"), ("Heart", "Jasmine Sambac, Tuberose, Hazelnut Macaron"), ("Base", "Sandalwood, Musk, Vetiver")],
  "Floral · Amber · Woody", "Juicy raspberry, radiant jasmine and creamy sandalwood.",
  f"{t} is a floral amber woody fragrance for women, launched in 2024 and created by perfumer Marie Salamagne. Raspberry, mandarin and rose open it juicy and vibrant, a heart of jasmine sambac, tuberose and a gourmand hazelnut macaron accord brings radiant, addictive warmth, and it settles into a creamy base of sandalwood, musk and vetiver.",
  ["A juicy raspberry, mandarin and rose opening", "A radiant jasmine and tuberose heart with hazelnut macaron", "A creamy sandalwood, musk and vetiver base", "Generous 100ml Eau de Parfum"],
  "EAN 3386460149822 matched on Allegro SK (Ikonik pre ženy EDP 100ml); 60ml is a different EAN. Pyramid agreed by Ferwer + ScentVerdict (raspberry, jasmine, sandalwood in all sources incl. Lyko, Sephora India). Floral amber woody per Sephora India, Lyko, NST. 2024 per NST, ScentVerdict, Ferwer; Marie Salamagne per Lyko + Ferwer. Not Ikonik Absolu Pour Femme. Women." + AW,
  "raspberry and mandarin over jasmine and sandalwood.", ["Floral", "Oriental", "Woody", "Fruity"], ["Floral", "Fruity", "Jasmine", "Sandalwood"],
  name="Ikonik Pour Femme", **PC)

# 6 New York Mercer Street
t = "Karl Lagerfeld Karl New York Mercer Street Eau de Toilette 100ml"
F("3386460115551", "Karl Lagerfeld", t, "Men", "100", "30.99", "40.99", 3,
  [("Top", "Lime, Basil, White Pepper"), ("Heart", "Rhubarb, Jasmine, Geranium"), ("Base", "White Woods, Musk, Vetiver")],
  "Woody · Aromatic · Citrus", "Zesty, green and effortlessly downtown.",
  f"{t} is a woody aromatic fragrance for men from the Places by Karl collection, launched in 2020 and created by perfumer Aliénor Massenet. Lime, basil and white pepper open it zesty and green, a heart of rhubarb, jasmine and geranium adds a crisp, lightly floral freshness, and it settles into a clean base of white woods, musk and vetiver.",
  ["A zesty lime, basil and white pepper opening", "A crisp rhubarb, jasmine and geranium heart", "A clean white woods, musk and vetiver base", "Generous 100ml Eau de Toilette"],
  "EAN 3386460115551 matched on Superdrug UK (no longer available), Perfumes Club UK and Perfumetrader DE (Mercer Street EDT 100ml, men). Pyramid agreed by Perfumes Club, Lyko, Lookfantastic, getscentcast (mint Lookfantastic/NST only, left out). Woody aromatic per Perfumes Club, Lyko, getscentcast (Lookfantastic: woody floral). 2020 + Aliénor Massenet per Perfumes Club, NST, getscentcast. Men." + AW,
  "lime and basil over rhubarb and white woods.", ["Woody", "Aromatic", "Citrus"], ["Citrus", "Woody", "Fresh", "Spicy"],
  name="Mercer Street", **TC)
P[-1]["seo"] = ("Karl Lagerfeld New York Mercer Street EDT 100ml", P[-1]["seo"][1])

# 7 Rome Divino Amore
t = "Karl Lagerfeld Karl Rome Divino Amore Eau de Parfum 100ml"
F("3386460130011", "Karl Lagerfeld", t, "Women", "100", "26.49", "35.99", 5,
  [("Top", "Petitgrain, Orange, Neroli"), ("Heart", "Orange Blossom, Jasmine, Orchid"), ("Base", "Sandalwood, Amber, Musk")],
  "Floral · Woody · Citrus", "Sun-drenched Italian citrus and blossom.",
  f"{t} is a floral woody fragrance for women from the Places by Karl collection, launched in 2022 and created by perfumers Emilie Coppermann and Pierre-Constantin Guéros. Petitgrain, orange and neroli open it bright and sunny, a heart of orange blossom, jasmine and orchid brings a radiant floral warmth, and it settles into a soft base of sandalwood, amber and musk.",
  ["A sunny petitgrain, orange and neroli opening", "A radiant orange blossom, jasmine and orchid heart", "A soft sandalwood, amber and musk base", "Generous 100ml Eau de Parfum"],
  "EAN 3386460130011 matched on Perfumetrader DE and Nordicfeel FI (Rome Divino Amore EDP 100ml, women). Pyramid agreed by Parfumo, Sephora India, Lookfantastic (Lyko jumbles tiers). Interparfums site lists different notes and 'floral chypre' – judged a site error, ignored. Floral woody per Nordicfeel, Lyko, Ferwer. 2022 per Parfumo + Ferwer; perfumers per Parfumo, Ferwer, Interparfums. Lyko breadcrumb says men, text says feminine. Women." + AW,
  "petitgrain and orange over orange blossom and sandalwood.", ["Floral", "Woody", "Citrus"], ["Floral", "Citrus", "Jasmine", "Sandalwood"],
  name="Rome Divino Amore", **PC)

# 8 Kenzo Flower Ikebana Sakura gift set
t = "Kenzo Flower Ikebana Sakura Eau de Parfum 75ml Gift Set with 10ml Travel Spray and 75ml Body Lotion"
GS("3274872472891", "Kenzo", t, "Kenzo Flower Ikebana Sakura EDP 75ml 3-Piece Gift Set", "Women", "75", "56.99", "75.99", 3,
   [("Heart", "Cherry Blossom, Tuberose"), ("Base", "Sandalwood")],
   "Floral · Woody", "Cherry blossom and tuberose on soft sandalwood, beautifully gift-boxed.",
   f"{t} brings together Flower Ikebana by Kenzo Eau de Parfum in the 75ml size, a 10ml travel spray and a matching 75ml body lotion. Created by perfumers Alberto Morillas and Alexandra Monet, this floral woody scent pairs delicate sakura cherry blossom with creamy Indian tuberose over a warm Australian sandalwood base.",
   ["Kenzo Flower Ikebana Eau de Parfum 75ml (spray)", "Kenzo Flower Ikebana Eau de Parfum 10ml (travel spray)", "Kenzo Flower Ikebana Body Lotion 75ml"],
   ["Delicate sakura cherry blossom", "Creamy Indian tuberose", "A warm sandalwood base", "Travel spray and body lotion included"],
   "EAN 3274872472891 matched on Superdrug UK (Flower Ikebana Sakura Gift Set 75ml/10ml/75ml), Bixoto and eBay UK; contents EDP 75ml + EDP 10ml + body lotion 75ml per Superdrug, Bixoto, Galaxus. 'Sakura' is the edition name; scent is Flower Ikebana by Kenzo (2023, Morillas + Monet per Parfumo + NST). Top note disputed (sobacha tea vs sencha tea) so only heart + base shown; Superdrug and TPS info blocks list unrelated notes – ignored. Floral woody per Rustan's, TPS, NST, Bixoto. Galaxus FR shows a similar set under EAN 3274872467552 (maybe other year) – check the box. Women." + AW,
   "cherry blossom and tuberose over sandalwood, with lotion and travel spray.", ["Floral", "Woody"], ["Floral", "Sandalwood", "Woody"],
   name="Flower Ikebana", **PC)

# 9 Kenzo Homme EDP 110ml
t = "Kenzo Homme Eau de Parfum 110ml"
F("3274872423398", "Kenzo", t, "Men", "110", "52.49", "69.99", 5,
  [("Top", "Marine Accord"), ("Heart", "Leather"), ("Base", "Patchouli")],
  "Woody · Aquatic · Leather", "Deep marine freshness with a bold leather edge.",
  f"{t} is a woody marine fragrance for men, launched in 2022 and created by perfumer Quentin Bisch. A fresh marine accord opens it cool and airy, a heart of supple leather adds depth and character, and it settles into an earthy, intense patchouli base.",
  ["A fresh marine opening", "A bold leather heart", "An earthy patchouli base", "Generous 110ml Eau de Parfum"],
  "EAN 3274872423398 matched on Parfumera FR and Perfumetrader DE (Kenzo Homme EDP 110ml, men). Notes agreed by Parfumo, The Perfume Shop, Ferwer; Notino UK and Parfumera list other notes (likely older Kenzo Homme) – ignored. Woody marine per Ferwer, woody per TPS, aquatic/leather/woody accords per Parfumo. 2022 per Parfumo, TPS, Ferwer; Quentin Bisch per Parfumo + Ferwer. Not Homme Marine / Intense / Indigo. Men." + AW,
  "a marine accord over leather and patchouli.", ["Woody", "Aquatic", "Leather"], ["Aquatic", "Woody", "Fresh"],
  name="Kenzo Homme Eau de Parfum", **PC)

# 10 Kenzo Homme EDT Intense 110ml
t = "Kenzo Homme Eau de Toilette Intense 110ml"
F("3274872421554", "Kenzo", t, "Men", "110", "49.99", "65.99", 5,
  [("Top", "Pink Pepper, Calypsone"), ("Heart", "Fig Wood, Vetiver"), ("Base", "Sandalwood, Akigalawood")],
  "Woody · Aquatic · Spicy", "A deeper, woodier take on Kenzo's marine classic.",
  f"{t} is a woody marine fragrance for men, created by perfumer Quentin Bisch as part of the 2021 reinvention of Kenzo Homme. Pink pepper and a fresh, watery calypsone note open it bright and spicy, a heart of fig wood and vetiver brings green, woody depth, and it settles into a creamy base of sandalwood and akigalawood.",
  ["A spicy pink pepper and marine opening", "A green fig wood and vetiver heart", "A creamy sandalwood and akigalawood base", "Generous 110ml Eau de Toilette Intense"],
  "EAN 3274872421554 matched on Jomashop (Kenzo Homme Intense EDT 3.7oz/110ml), eBay and Maison des Fragrances FR. Pyramid agreed by Parfumo, LVMH press page, Escentual (Sephora FR close). Woody marine per LVMH + Sephora FR. Quentin Bisch per Parfumo, LVMH, Sephora FR. 2021 per Parfumo + LVMH (not 2022). EDT Intense (not EDP). Men." + AW,
  "pink pepper and calypsone over fig wood and sandalwood.", ["Woody", "Aquatic", "Spicy"], ["Woody", "Aquatic", "Spicy", "Sandalwood"],
  name="Kenzo Homme Intense", conc="Eau De Toilette", concl="Eau de Toilette Intense")

write_outputs(".")
for p in P: print(p["status"], p["seo"][0], len(p["seo"][0]), len(p["seo"][1]))
