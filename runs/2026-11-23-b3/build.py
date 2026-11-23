import sys; sys.path.insert(0, "/home/claude/ambient-beauty-images/workflow")
from lib import *
TC = dict(conc="Eau De Toilette", concl="Eau de Toilette")
PC = dict(conc="Eau De Parfum", concl="Eau de Parfum")
AW = " Awaiting photos."
AF = "Abercrombie & Fitch"

def GS(bc, vendor, title, seo_t, gender, size, price, cmp, qty, pyr, profile, hook, intro, contents, love, note, seo_d,
       of, fr, name, conc="Eau De Toilette", concl="Eau de Toilette", status="done"):
    """Fragrance gift set: fragrance standard (3 tags) plus a 'What's in the set' block (as runs/2026-11-20-b3)."""
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

# 1 Davidoff Cool Water gift set (supplier tab: Bath and Body)
t = "Davidoff Cool Water Eau de Toilette 75ml Gift Set with 70g Deodorant Stick"
GS("3616304197420", "Davidoff", t, "Davidoff Cool Water EDT 75ml & Deodorant Stick Gift Set", "Men", "75", "32.49", "42.99", 5,
   [("Top", "Mint, Coriander, Lavender, Rosemary, Green Notes"), ("Heart", "Geranium, Neroli, Jasmine, Sandalwood"), ("Base", "Oakmoss, Cedarwood, Musk, Amber, Tobacco")],
   "Aromatic · Aquatic · Fresh", "The cool, aromatic classic that defined fresh men's fragrance.",
   f"{t} pairs the iconic Cool Water Eau de Toilette, first launched in 1988, with a matching deodorant stick. Mint, coriander, lavender and rosemary open with a cool, aromatic freshness, a heart of geranium, neroli, jasmine and sandalwood follows, and it settles on oakmoss, cedarwood, musk, amber and tobacco.",
   ["Cool Water Eau de Toilette 75ml (spray)", "Cool Water Deodorant Stick 70g"],
   ["A cool opening of mint, coriander and lavender", "A fresh aromatic fougère heart", "A warm base of oakmoss, cedar, amber and musk", "A ready-made gift with a 75ml spray"],
   "Supplier lists this in the Bath and Body tab; built as a fragrance gift set like earlier sets. EAN 3616304197420 matched on Jomashop (title) and Bonherre (EDT 75ml + Deostick 70g). Superdrug's 75ml + 75ml stick duo has another EAN (3616307511537), probably another year's set. Pyramid agreed by Parfumo and Bonherre (The Perfume Shop gives a shorter list with lavender in the heart). 1988 per Parfumo and The Perfume Shop. Men." + AW,
   "mint and lavender over geranium, oakmoss and amber.", ["Aromatic", "Aquatic", "Fougere", "Fresh"], ["Fresh", "Lavender", "Aquatic", "Woody"],
   name="Cool Water")

# 2 A&F Away Weekend Women
t = "Abercrombie & Fitch Away Weekend Women Eau de Parfum 100ml"
F("0085715169952", AF, t, "Women", "100", "28.49", "38.99", 5,
  [("Top", "Fig, Rhubarb, White Tea"), ("Heart", "Clary Sage, Lavender, Jasmine"), ("Base", "Musk, Ambroxan, Tonka Bean")],
  "Floral · Aromatic · Musky", "A light, carefree floral for slow weekend mornings.",
  f"{t} is a soft aromatic floral for women, launched in 2023. Fig, rhubarb and white tea open fresh and airy, a heart of clary sage, lavender and jasmine follows, and it settles into a smooth, powdery base of musk, ambroxan and tonka bean.",
  ["A fresh fig, rhubarb and white tea opening", "A calm clary sage, lavender and jasmine heart", "A soft musk, ambroxan and tonka base", "Generous 100ml Eau de Parfum"],
  "EAN 0085715169952 matched on Galaxus.ch (Weekend EDP 100ml). Pyramid identical on Bloom's The Chemist and Moodnose; Parfumdreams agrees (omits white tea/ambroxan from its list). 2023 per Bloom's, Moodnose, Parfumo. Not the older 'Away Women'. Women." + AW,
  "fig and white tea over lavender, jasmine and soft musk.", ["Floral", "Aromatic", "Musky", "Powdery"], ["Floral", "Fruity", "Lavender", "Jasmine", "Fresh"],
  name="Away Weekend Women", **PC)

# 3 A&F Away Weekend Man
t = "Abercrombie & Fitch Away Weekend Man Eau de Toilette 100ml"
F("0085715169402", AF, t, "Men", "100", "26.49", "35.99", 5,
  [("Top", "Bergamot, Cardamom, Apple, Clementine"), ("Heart", "Lavender, Clary Sage, Rosemary, Cypress"), ("Base", "Cedarwood, Patchouli, Cocoa")],
  "Aromatic · Woody · Citrus", "An easy, sun-warmed aromatic for days off.",
  f"{t} is a fresh woody aromatic for men, launched in 2023. Bergamot, cardamom, apple and clementine open bright and lightly spiced, a heart of lavender, clary sage, rosemary and cypress follows, and it dries down to Atlas cedarwood, patchouli and a touch of cocoa.",
  ["A bright bergamot, apple and clementine opening", "An aromatic lavender, sage and rosemary heart", "A warm cedarwood, patchouli and cocoa base", "Generous 100ml Eau de Toilette"],
  "EAN 0085715169402 matched on Galaxus.ch and Triple Traders (EDT 100ml, men). Pyramid agreed by Triple Traders, Parfumdreams and Scentadvice. 2023 per Triple Traders and Scentadvice. Also stocked by Superdrug UK. Men." + AW,
  "bergamot and apple over lavender, sage and cedarwood.", ["Aromatic", "Woody", "Citrus", "Fougere"], ["Citrus", "Fruity", "Lavender", "Woody", "Spicy"],
  name="Away Weekend Man", **TC)

# 4 A&F First Instinct Blue for Her 50ml
t = "Abercrombie & Fitch First Instinct Blue for Her Eau de Parfum 50ml"
F("0085715167217", AF, t, "Women", "50", "19.49", "24.99", 5,
  [("Top", "Salted Sea Air, Bergamot, Blackberry"), ("Heart", "Apricot Nectar, Peony, Jasmine"), ("Base", "Patchouli, Vanilla, Sandalwood")],
  "Fruity · Floral · Woody", "Fresh sea air meets a warm, golden heart.",
  f"{t} is a fruity, uplifting fragrance for women. Salted sea air, bergamot and blackberry open fresh and luminous, apricot nectar, peony and jasmine form a warm floral heart, and it settles into patchouli, vanilla and sandalwood.",
  ["A fresh sea-air, bergamot and blackberry opening", "A juicy apricot, peony and jasmine heart", "A warm patchouli, vanilla and sandalwood base", "Handy 50ml Eau de Parfum"],
  "Barcode 85715167217 used in Carrefour UAE's 50ml EDP product URL (not labelled EAN); Superdrug 100ml has sibling EAN 0085715167224. Pyramid identical on Lookfantastic, Carrefour UAE and Fragrancecart (Superdrug's 100ml page gives a different list, ignored). Release year not confirmed. Women." + AW,
  "sea air and blackberry over apricot, peony and vanilla.", ["Fruity", "Floral", "Woody", "Aquatic"], ["Fruity", "Floral", "Jasmine", "Vanilla", "Aquatic"],
  name="First Instinct Blue for Her", **PC)
P[-1]["seo"] = ("A&F First Instinct Blue for Her Eau de Parfum 50ml", P[-1]["seo"][1])

# 5 A&F First Instinct Sheer 50ml
t = "Abercrombie & Fitch First Instinct Sheer Eau de Parfum 50ml"
F("0085715167620", AF, t, "Women", "50", "19.49", "25.99", 5,
  [("Top", "Air Accord, Bergamot, Pink Pepper"), ("Heart", "Orange Blossom, Lily of the Valley, Hibiscus"), ("Base", "Musk, Amber, Creamy Woods")],
  "Floral · Amber · Fresh", "A luminous, sunny floral with a soft, warm glow.",
  f"{t} is a light, luminous floral for women. A fresh air accord, bergamot and pink pepper open bright and airy, orange blossom, lily of the valley and hibiscus form the floral heart, and it settles into musk, sweet amber and creamy woods.",
  ["An airy bergamot and pink pepper opening", "A sunny orange blossom, lily of the valley and hibiscus heart", "A soft musk, amber and creamy woods base", "Handy 50ml Eau de Parfum"],
  "EAN 0085715167620 matched on Galaxus.ch and Triple Traders (EDP 50ml). Pyramid agreed by Triple Traders and Lookfantastic (Superdrug adds pear, raspberry, peony, jasmine, freesia – not confirmed, left out). Not the original First Instinct for Her. Release year not confirmed. Women." + AW,
  "bergamot and pink pepper over orange blossom and musk.", ["Floral", "Oriental", "Fresh", "Musky"], ["Floral", "Citrus", "Fresh", "Woody"],
  name="First Instinct Sheer", **PC)

# 6/7 A&F Naturally Fierce 30ml / 50ml
NF_PYR = [("Top", "Cactus Water, Agave"), ("Heart", "Coconut, Orange Blossom, Plumeria"), ("Base", "Sandalwood, Vetiver, Moss")]
for bc, size, price, cmp, src in [
    ("0085715167828", "30", "16.99", "22.99", "EAN 0085715167828 matched on aio.lv (EDP 30ml, women)."),
    ("0085715167804", "50", "21.99", "27.99", "Barcode 085715167804 shown on Walmart's 1.7oz (50ml) EDP page; no UK EAN page found.")]:
    t = f"Abercrombie & Fitch Naturally Fierce Eau de Parfum {size}ml"
    F(bc, AF, t, "Women", size, price, cmp, 5, NF_PYR,
      "Floral · Woody · Musky", "Sunny desert blooms, warm sand and a vacation glow.",
      f"{t} is a sunny floral woody musk for women. Cactus water and sweet agave open fresh and bright, creamy coconut, orange blossom and plumeria form a warm floral heart, and it settles into sandalwood, vetiver and moss.",
      ["A fresh cactus water and agave opening", "A creamy coconut, orange blossom and plumeria heart", "A warm sandalwood, vetiver and moss base", f"{size}ml Eau de Parfum"],
      src + " Pyramid agreed by Lookfantastic, Superdrug and Escentual (moss not on Escentual). Floral woody musk per Escentual, Superdrug, Walmart. Release year not confirmed (Parfumo page unreliable). Not A&F Fierce (men's). Women." + AW,
      "cactus water and agave over coconut, plumeria and sandalwood.", ["Floral", "Woody", "Musky"], ["Floral", "Fruity", "Sandalwood", "Woody"],
      name="Naturally Fierce", **PC)

# 8 Antonio Banderas The Icon Splendid
t = "Antonio Banderas The Icon Splendid Eau de Parfum 100ml"
F("8411061084922", "Antonio Banderas", t, "Women", "100", "23.49", "29.99", 5,
  [("Top", "Tangerine, Black Pepper, Pear"), ("Heart", "Peony, Orange Blossom, Guaiac Wood"), ("Base", "Sandalwood, Vanilla, Praline, Rose, Musk")],
  "Floral · Fruity · Gourmand", "A radiant, sparkling floral with a sweet, warm glow.",
  f"{t} is a radiant floral for women from Antonio Banderas, launched in 2024. Tangerine, black pepper and pear open juicy and lightly spiced, peony, orange blossom and guaiac wood form the heart, and it settles into sandalwood, vanilla, praline, rose and musk.",
  ["A juicy tangerine and pear opening with black pepper", "A floral peony and orange blossom heart", "A sweet sandalwood, vanilla and praline base", "Great value 100ml Eau de Parfum"],
  "EAN 8411061084922 not found online. 100ml EDP for women confirmed by Woolworths SA and FragranceNet; pyramid identical on both (Fuschia gift set agrees). 2024 per FragranceNet. Perfume.com calls it a men's fragrance with different notes (ignored); supplier's Women kept." + AW,
  "tangerine and pear over peony, vanilla and praline.", ["Floral", "Fruity", "Gourmand", "Spicy"], ["Floral", "Fruity", "Citrus", "Vanilla", "Rose"],
  name="The Icon Splendid", **PC)

# 9 Antonio Banderas The Secret
t = "Antonio Banderas The Secret Eau de Toilette 100ml"
F("8411061080641", "Antonio Banderas", t, "Men", "100", "22.49", "30.99", 2,
  [("Top", "Grapefruit, Bergamot, Mint"), ("Heart", "Apple Liqueur Accord, Cinnamon, Cardamom, Pepper"), ("Base", "Leather, Musk, Vanilla, Tonka Bean")],
  "Spicy · Oriental · Fresh", "A fresh, spiced seduction with a smooth leather finish.",
  f"{t} is a fresh spicy oriental for men, launched in 2010. Grapefruit, bergamot and mint open crisp and cool, an apple liqueur accord with cinnamon, cardamom and pepper warms the heart, and it settles into leather, musk, vanilla and tonka bean.",
  ["A crisp grapefruit, bergamot and mint opening", "A spiced apple liqueur heart", "A smooth leather, vanilla and tonka base", "Great value 100ml Eau de Toilette"],
  "Supplier barcode 8411061080641 not found online, but the supplier stockfile lists it together with 8411061701034 on the same line; 8411061701034 is matched to The Secret EDT 100ml on aio.lv and Galaxus. Not Golden Secret / Secret Temptation. Pyramid agreed by Ferwer and Schiphol shop (aio.lv agrees). 2010 per Ferwer. Men." + AW,
  "grapefruit and mint over cinnamon, leather and vanilla.", ["Spicy", "Oriental", "Fresh", "Leather"], ["Spicy", "Citrus", "Fresh", "Vanilla", "Fruity"],
  name="The Secret", **TC)

# 10 Ariana Grande Cloud Body Mist
t = "Ariana Grande Cloud Body Mist 236ml"
F("0812256024194", "Ariana Grande", t, "Women", "236", "23.49", "31.99", 5,
  [("Top", "Lavender, Pear, Bergamot"), ("Heart", "Coconut Cream, Praline, Vanilla Orchid"), ("Base", "Musk, Woody Notes")],
  "Gourmand · Floral · Musky", "A dreamy, creamy cloud of scent to spritz all over.",
  f"{t} is a light body mist version of Ariana Grande's Cloud. Lavender, pear and bergamot open soft and airy, creamy coconut, praline and vanilla orchid form a sweet heart, and it settles into a cosy base of musk and woods. Spray onto skin as often as you like.",
  ["An airy lavender, pear and bergamot opening", "A creamy coconut, praline and vanilla orchid heart", "A soft musk and woody base", "Big 236ml bottle for all-over spritzing"],
  "EAN 0812256024194 matched on Superdrug (Body Mist 236ml, women; no longer online) and OnBuy. Notes agreed by Parfumo and Food4Less (Argos lists Ari's notes – ignored). Body mist, not hair mist. Women." + AW,
  "lavender and pear over coconut cream, praline and musk.", ["Gourmand", "Floral", "Musky"], ["Vanilla", "Fruity", "Lavender", "Floral"],
  name="Cloud Body Mist", conc="Body Mist", concl="Body Mist")

write_outputs()
