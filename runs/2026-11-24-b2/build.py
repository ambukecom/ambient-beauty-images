import sys; sys.path.insert(0, "/home/claude/ambient-beauty-images/workflow")
from lib import *
TC = dict(conc="Eau De Toilette", concl="Eau de Toilette")
PC = dict(conc="Eau De Parfum", concl="Eau de Parfum")
AW = " Awaiting photos."

def GS(bc, vendor, title, seo_t, gender, size, price, cmp, qty, pyr, profile, hook, intro, contents, love, note, seo_d,
       of, fr, name, conc="Eau De Toilette", concl="Eau de Toilette", status="done"):
    """Fragrance gift set (as runs/2026-11-23-b3)."""
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

# 1 Cerruti 1881 Pour Homme EDT 200ml
t = "Cerruti 1881 Eau de Toilette 200ml"

# 1 Davidoff Cool Water Wave EDT 40ml -> needs-review (EAN / 40ml not confirmed; 2007 vs 2017 Wave)
t = "Davidoff Cool Water Wave Eau de Toilette 40ml"
F("3614223379897", "Davidoff", t, "Men", "40", "20.49", "27.99", 5,
  [("Top", "Sea Notes, Grapefruit, Sichuan Pepper"), ("Heart", "Juniper, Birch Leaf"), ("Base", "Sandalwood, Patchouli")],
  "Aquatic · Woody · Fresh", "A bright, salty splash of Cool Water for summer.",
  f"{t} is the 2017 edition of Davidoff's Cool Water Wave, an aquatic woody fragrance for men. Sea notes, grapefruit and Sichuan pepper open fresh and tingling, a heart of juniper and birch leaf adds a green, aromatic breeze, and it dries down to smooth sandalwood and patchouli.",
  ["A fresh sea-spray and grapefruit opening", "A crisp juniper and birch leaf heart", "A smooth sandalwood and patchouli base", "Handy 40ml Eau de Toilette"],
  "NEEDS REVIEW: EAN 3614223379897 not found on any retailer page and the 40ml size is not confirmed by 2 sources (one Parfumo review mentions 40ml). There is also a different 2007 Cool Water Wave – check the box (listed as the 2017 version). Pyramid agreed by Parfumo, FragranceNet and Watsons SG (orange blossom only on Parfumo, left out). 2017 per Parfumo, FragranceNet, maximumfragrance.ca. Looks discontinued/limited (perfume.com unavailable). Men." + AW,
  "sea notes and grapefruit over juniper and sandalwood.", ["Aquatic", "Woody", "Fresh"], ["Aquatic", "Fresh", "Citrus", "Woody", "Sandalwood"],
  name="Cool Water Wave", status="needs-review", **TC)

# 2 Davidoff Cool Water Woman gift set
t = "Davidoff Cool Water Woman Eau de Toilette 30ml Gift Set with 75ml Body Lotion"
GS("3616303806101", "Davidoff", t, "Davidoff Cool Water Woman EDT 30ml & Body Lotion Gift Set", "Women", "30", "26.49", "33.99", 5,
   [("Top", "Melon, Pineapple"), ("Heart", "Lily of the Valley, Jasmine"), ("Base", "Musk")],
   "Aquatic · Floral · Fresh", "The iconic aquatic floral for her, ready to give.",
   f"{t} pairs Cool Water Woman, Davidoff's fresh aquatic floral fragrance, with a matching body lotion. Juicy melon and pineapple open bright and watery, a soft heart of lily of the valley and jasmine follows, and it settles into a clean, gentle musk.",
   ["Cool Water Woman Eau de Toilette 30ml (spray)", "Cool Water Woman Body Lotion 75ml"],
   ["A fresh, juicy melon and pineapple opening", "A soft lily of the valley and jasmine heart", "A clean musky finish", "A ready-made gift with matching body lotion"],
   "Contents 30ml EDT + 75ml body lotion agreed by Lookfantastic UK, Tesco, Superdrug, Cosmetify and Inish Pharmacy. EAN 3616303806101 not shown on retailer pages (Superdrug versions use 3614221675311 / 3614223240340; Inish SKU COOL-6101 fits); supplier lists this EAN with 3 alternates for the same set. Pyramid: only notes 2+ of Inish, Cosmetify, Lookfantastic agree on (sandalwood/amber left out). Women." + AW,
   "melon and pineapple over jasmine and a clean musk.", ["Aquatic", "Floral", "Fresh"], ["Aquatic", "Floral", "Fresh", "Fruity", "Jasmine"],
   name="Cool Water Woman")

# 3 Davidoff Cool Water Woman Sea Rose EDT 100ml
t = "Davidoff Cool Water Woman Sea Rose Eau de Toilette 100ml"
F("3607347462583", "Davidoff", t, "Women", "100", "26.99", "36.99", 5,
  [("Top", "Nashi Pear"), ("Heart", "Peony, Rose"), ("Base", "Musk")],
  "Floral · Fruity · Musky", "A sea-kissed rose, light as an ocean breeze.",
  f"{t} is a fresh floral fruity fragrance for women, launched in 2013 and created by perfumer Aurélien Guichard. Juicy nashi pear opens light and crisp, a heart of peony and rose brings a soft, dewy bouquet, and it settles into a clean, skin-like musk.",
  ["A crisp, juicy nashi pear opening", "A dewy peony and rose heart", "A clean, soft musk base", "Generous 100ml Eau de Toilette"],
  "EAN 3607347462583 matched on gadcet.com (Cool Water Woman Sea Rose 100ml EDT). Pyramid: Osmoz and gadcet agree on every tier (sandalwood only on gadcet, left out). 2013 and perfumer Aurélien Guichard per Osmoz and NST Perfume (FragranceNet 2019 = limited edition). Women." + AW,
  "nashi pear over peony, rose and a soft musk.", ["Floral", "Fruity", "Musky"], ["Floral", "Rose", "Fruity", "Fresh"],
  name="Cool Water Woman Sea Rose", **TC)

# 4 Diesel D Red EDP 50ml (supplier gender Unisex kept)
t = "Diesel D Red Eau de Parfum 50ml"
F("3614273924443", "Diesel", t, "Unisex", "50", "28.49", "36.99", 5,
  [("Top", "Red Grapefruit"), ("Heart", "Lavender"), ("Base", "Sandalwood")],
  "Fougère · Aromatic · Fresh", "Bold, fresh and refillable: D by Diesel in red.",
  f"{t} is D by Diesel Red, a fresh aromatic fougère launched in 2024 in a refillable bottle. Zesty red grapefruit opens bright and juicy, a heart of Provence lavender adds an aromatic, clean edge, and it settles into a warm, creamy sandalwood.",
  ["A zesty red grapefruit opening", "An aromatic Provence lavender heart", "A warm, creamy sandalwood base", "Refillable 50ml Eau de Parfum"],
  "EAN 3614273924443 matched on Galaxus CH (D by Diesel Red EDP 50ml); 50ml also on Escentual. Pyramid agreed by John Lewis, Escentual, FragranceNet and NST Perfume. 2024 per NST and FragranceNet. Not D Red Le Parfum (2025). Supplier gender Unisex kept: NST, Galaxus and Parfumdreams call it unisex, but John Lewis, Escentual and FragranceNet market it mainly to men. John Lewis lists it as no longer available online." + AW,
  "red grapefruit over lavender and sandalwood.", ["Fougere", "Aromatic", "Fresh"], ["Lavender", "Citrus", "Sandalwood", "Fresh", "Woody"],
  name="D Red", **PC)

# 5 Diesel Fuel For Life Homme EDT 50ml
t = "Diesel Fuel For Life Homme Eau de Toilette 50ml"
F("3605520386442", "Diesel", t, "Men", "50", "23.99", "30.99", 5,
  [("Top", "Star Anise, Grapefruit"), ("Heart", "Lavender, Raspberry"), ("Base", "Heliotrope, Dry Woods")],
  "Aromatic · Fougère · Powdery", "Diesel's cult fougère with a fruity, rebellious twist.",
  f"{t} is the original Fuel For Life for men, an aromatic fougère launched in 2007. Star anise and grapefruit open sharp and fresh, a heart of lavender and raspberry adds an unexpected fruity sweetness, and it settles into powdery heliotrope over dry woods.",
  ["A sharp star anise and grapefruit opening", "A fruity lavender and raspberry heart", "A powdery heliotrope and dry woods base", "Handy 50ml Eau de Toilette"],
  "EAN 3605520386442 matched on Superdrug (Fuel For Life Homme EDT 50ml) and eBay (EDT 50ml men); probably the older L'Oréal-era box (current 50ml uses other codes; supplier also lists 3614272608603). Pyramid agreed by diesel.com 'sensorial notes' and NST Perfume (Superdrug same notes untiered); diesel.com description text gives a different list – slight doubt. 2007 per Fragrancex and NST. Men." + AW,
  "star anise and grapefruit over lavender, raspberry and heliotrope.", ["Aromatic", "Fougere", "Powdery"], ["Lavender", "Fruity", "Fresh", "Citrus", "Woody"],
  name="Fuel For Life Homme", **TC)

# 6 Dumont Nitro Red EDP 100ml
t = "Dumont Nitro Red Eau de Parfum 100ml"
F("3760060761880", "Dumont", t, "Men", "100", "33.49", "44.99", 5,
  [("Top", "Apple, Lavender, Bergamot"), ("Heart", "Watermelon, Cedar, Calamus"), ("Base", "Amber, Patchouli, Sandalwood")],
  "Fruity · Fresh · Woody", "A juicy, energetic red to wear every day.",
  f"{t} is Nitro Red Pour Homme, a fruity fresh fragrance for men from Dumont Paris. Crisp apple, lavender and bergamot open bright and lively, a heart of juicy watermelon, cedar and calamus follows, and it settles into a warm base of amber, patchouli and sandalwood.",
  ["A crisp apple, lavender and bergamot opening", "A juicy watermelon and cedar heart", "A warm amber, patchouli and sandalwood base", "Generous 100ml Eau de Parfum"],
  "EAN (UPC 03760060761880) matched on ThePerfumeSpot (Nitro Red by Dumont 100ml EDP, men). Pyramid agreed by Parfumo, FragranceNet and ThePerfumeSpot; Perfume.com and eCosmetics give different lists (ignored). Launch year not confirmed (left out). Men." + AW,
  "apple and bergamot over watermelon, cedar and sandalwood.", ["Fruity", "Fresh", "Woody"], ["Fruity", "Fresh", "Woody", "Lavender", "Sandalwood"],
  name="Nitro Red", **PC)

# 7 Dunhill Desire Blue EDT 100ml
t = "Dunhill Desire Blue Eau de Toilette 100ml"
F("0085715801555", "Dunhill", t, "Men", "100", "35.99", "46.99", 2,
  [("Top", "Lychee, Mandarin Orange, Lotus, Bergamot"), ("Heart", "Sea Notes, Orange, Brazilian Rosewood"), ("Base", "Tonka Bean, Amber, Musk, Benzoin")],
  "Aquatic · Aromatic · Fresh", "Cool, fresh and sharply modern: Desire in blue.",
  f"{t} is a fresh aquatic fragrance for men from Dunhill London. Lychee, mandarin, lotus and bergamot open bright and juicy, a heart of sea notes, orange and Brazilian rosewood brings a cool marine breeze, and it settles into a smooth base of tonka bean, amber, musk and benzoin.",
  ["A juicy lychee and mandarin opening", "A cool sea notes and rosewood heart", "A smooth tonka, amber and musk base", "Generous 100ml Eau de Toilette"],
  "EAN 0085715801555 matched on Superdrug (Desire Blue EDT 100ml), Carrefour UAE and eBay. Pyramid: Superdrug and Interparfums (licensee) agree on every tier; Osmoz close. Launch year conflicts (2002 Superdrug / 2003 Osmoz) – left out. Family: sources say aromatic green / woody-spicy; shown as Aquatic, Aromatic, Fresh. Men." + AW,
  "lychee and mandarin over sea notes, rosewood and tonka.", ["Aquatic", "Aromatic", "Fresh"], ["Aquatic", "Fresh", "Citrus", "Fruity", "Woody"],
  name="Desire Blue", **TC)

# 8 Dunhill Driven EDT 60ml
t = "Dunhill Driven Eau de Toilette 60ml"
F("0085715807748", "Dunhill", t, "Men", "60", "20.49", "27.99", 3,
  [("Top", "Green Apple, Black Pepper"), ("Heart", "Juniper, Sage, Orange Blossom"), ("Base", "Teakwood, Vetiver, Amber")],
  "Woody · Aromatic · Fresh", "Fresh, focused and full of drive.",
  f"{t} is the blue Driven, a woody aromatic fragrance for men launched in 2021. Green apple and black pepper open crisp and lively, a heart of juniper, sage and orange blossom adds an aromatic freshness, and it settles into teakwood, vetiver and a modern amber.",
  ["A crisp green apple and black pepper opening", "An aromatic juniper and sage heart", "A modern teakwood, vetiver and amber base", "Handy 60ml Eau de Toilette"],
  "EAN 0085715807748 matched on Superdrug (Dunhill Driven EDT 60ml, marked no longer available online). Pyramid agreed by Superdrug, Parfumo and Interparfums (bergamot / Italian lemon disputed in the top, left out; amber = Ambroxan). 2021 per Superdrug and Parfumo. Men." + AW,
  "green apple and black pepper over juniper, sage and teakwood.", ["Woody", "Aromatic", "Fresh"], ["Fresh", "Woody", "Fruity", "Spicy", "Floral"],
  name="Dunhill Driven", **TC)

# 9 Dunhill Mongolian Cashmere EDP 100ml
t = "Dunhill Mongolian Cashmere Eau de Parfum 100ml"
F("0085715807595", "Dunhill", t, "Men", "100", "61.49", "79.99", 3,
  [("Top", "Mandarin Orange, Pink Pepper"), ("Heart", "Orris, Rose, Geranium"), ("Base", "Amber, Musk, Suede")],
  "Leather · Powdery · Floral", "Soft as cashmere, from the Dunhill Signature Collection.",
  f"{t} is part of the Dunhill Signature Collection, a soft leathery fragrance for men launched in 2022. Mandarin orange and pink pepper open bright and gently spiced, a powdery heart of orris, rose and geranium follows, and it settles into a warm, velvety base of amber, musk and suede.",
  ["A bright mandarin and pink pepper opening", "A powdery orris, rose and geranium heart", "A velvety amber, musk and suede base", "Generous 100ml Eau de Parfum"],
  "EAN 0085715807595 matched on Superdrug (Dunhill Signature Collection Mongolian Cashmere EDP 100ml). Pyramid: Parfumo and Fragrancenet agree on every tier. 2022 per Parfumo, Fragrancenet, NST. Men (retailers sell it for men; many reviewers find it unisex)." + AW,
  "mandarin and pink pepper over orris, rose and suede.", ["Leather", "Powdery", "Floral"], ["Floral", "Rose", "Spicy", "Citrus"],
  name="Mongolian Cashmere", **PC)

# 10 Elie Saab Girl of Now Lovely EDP 90ml
t = "Elie Saab Girl of Now Lovely Eau de Parfum 90ml"
F("7640233341070", "Elie Saab", t, "Women", "90", "52.99", "68.99", 5,
  [("Top", "Mandarin, Pear"), ("Heart", "Orange Blossom, Almond, Frangipani, Rose"), ("Base", "Tonka Bean, Patchouli")],
  "Floral · Gourmand · Fruity", "A sweeter, sunnier Girl of Now.",
  f"{t} is a floral gourmand fragrance for women, launched in 2022. Mandarin and pear open juicy and bright, a heart of orange blossom, almond, frangipani and rose brings a soft, sweet bouquet, and it settles into a warm base of tonka bean and patchouli.",
  ["A juicy mandarin and pear opening", "A sweet orange blossom, almond and rose heart", "A warm tonka bean and patchouli base", "Generous 90ml Eau de Parfum"],
  "EAN 7640233341070 matched on Shop-Apotheke (Girl of Now Lovely EDP 90ml); 90ml EDP also on Lookfantastic. Pyramid: Lookfantastic, Shop-Apotheke and Beauty Bay agree (blackcurrant bud placement and cashmeran/ambroxan disputed, left out). 2022 per Parfumo and NST. Women." + AW,
  "mandarin and pear over orange blossom, almond and tonka.", ["Gourmand", "Floral", "Fruity"], ["Floral", "Fruity", "Rose"],
  name="Girl of Now Lovely", **PC)

write_outputs(".")
