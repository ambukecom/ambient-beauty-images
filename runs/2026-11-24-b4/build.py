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

# 1 Franck Olivier Bella In Paris EDP 75ml
t = "Franck Olivier Bella In Paris Eau de Parfum 75ml"
F("3516641842321", "Franck Olivier", t, "Women", "75", "22.49", "28.99", 4,
  [("Top", "Orange, Peach, Pear"), ("Heart", "Iris, Magnolia, Rose"), ("Base", "Cedar, Musk, Sandalwood")],
  "Fruity · Floral · Woody", "A sunny Parisian bouquet of fruit and flowers.",
  f"{t} is a fruity floral fragrance for women. Juicy orange, peach and pear open it bright and sweet, a heart of iris, magnolia and rose brings an elegant floral bouquet, and it settles into a soft, warm base of cedar, musk and sandalwood.",
  ["A juicy orange, peach and pear opening", "An elegant iris, magnolia and rose heart", "A soft cedar, musk and sandalwood base", "Generous 75ml Eau de Parfum"],
  "EAN 3516641842321 matched on Walmart (2.5oz) and FrenchFragrance (75ml) as Bella In Paris EDP. Pyramid agreed by Parfumo and Ferwer on all tiers; Walmart, Nahdi and FragranceNet give different note lists (ignored). Fruity floral per Ferwer, Goldapple, Nahdi. Launch year conflicting (2016/2019) so left out. Not Bella Pour Elle. Women." + AW,
  "orange, peach and pear over iris, rose and sandalwood.", ["Fruity", "Floral", "Woody"], ["Fruity", "Floral", "Rose", "Sandalwood", "Woody"],
  name="Bella In Paris", **PC)

# 2 Franck Olivier Eau de Passion Men EDT 75ml
t = "Franck Olivier Eau de Passion Men Eau de Toilette 75ml"
F("3516642127120", "Franck Olivier", t, "Men", "75", "24.49", "32.99", 2,
  [("Top", "Amalfi Lemon, Mandarin Orange, Pineapple, Bergamot, Mint"), ("Heart", "Sage, Vetiver, Clove, Lavender, Geranium"), ("Base", "Oakmoss, Musk, Amber")],
  "Aromatic · Citrus · Woody", "Fresh citrus energy with an aromatic, masculine edge.",
  f"{t} is an aromatic fragrance for men, launched in 2008. Amalfi lemon, mandarin, pineapple, bergamot and mint open it crisp and zesty, a heart of sage, vetiver, clove, lavender and geranium adds an aromatic, slightly spicy character, and it dries down to oakmoss, musk and warm amber.",
  ["A zesty lemon, mandarin and mint opening", "An aromatic sage, lavender and vetiver heart", "A warm oakmoss, musk and amber base", "Generous 75ml Eau de Toilette"],
  "EAN 3516642127120 matched on FrenchFragrance (Eau de Passion For Men EDT 75ml); Galaxus sells same EDT 75ml under older EAN 3516640825127. Not the women's Passion EDP. Pyramid agreed by FragranceNet, Vivir and Fraganty (all tiers). Aromatic per all 3; 2008 per FragranceNet and Vivir. Men." + AW,
  "lemon, mandarin and mint over sage, lavender and amber.", ["Aromatic", "Citrus", "Woody"], ["Citrus", "Lavender", "Spicy", "Fresh", "Woody"],
  name="Eau de Passion Men", **TC)

# 3 Franck Olivier Giorgia EDP 75ml -> needs-review (pyramid conflict on the EAN-matched page; no pyramid shown)
t = "Franck Olivier Giorgia Eau de Parfum 75ml"
F("3516642044328", "Franck Olivier", t, "Women", "75", "24.49", "33.99", 3, [],
  "Fruity · Floral", "A feminine fruity floral from Franck Olivier.",
  f"{t} is a fruity floral fragrance for women from Franck Olivier's Giorgia line. It is a soft, feminine scent with a fruity sparkle and a floral heart, made for everyday wear.",
  ["A fruity floral character", "Easy, feminine everyday scent", "From Franck Olivier's Giorgia line", "Generous 75ml Eau de Parfum"],
  "NEEDS REVIEW: EAN 3516642044328 matched only on Superdrug marketplace (Giorgia Women EDP 75ml), whose notes (bergamot, pear, blackcurrant / jasmine, neroli, rose / vanilla, praline...) differ completely from Galaxus/FragranceNet/Bluesalon (pomegranate, freesia, ylang / peach, jasmine, tuberose / heliotrope, musk, vanilla, cedar – these use older EAN 3516641744328). Possible reformulation, so no pyramid shown – please check the box. Different product from Giorgia L'Impératrice (3516642045325, already live). Fruity floral per FragranceNet, Bluesalon, Superdrug. Women." + AW,
  "a soft, feminine fruity floral for everyday wear.", ["Fruity", "Floral"], ["Fruity", "Floral"],
  name="Giorgia", status="needs-review", **PC)

# 4 Franck Olivier One Kiss EDP 75ml
t = "Franck Olivier One Kiss Eau de Parfum 75ml"
F("3516641926328", "Franck Olivier", t, "Women", "75", "22.49", "29.99", 4,
  [("Top", "Pear, Mandarin"), ("Heart", "Jasmine, Lily of the Valley"), ("Base", "Vanilla, Praline")],
  "Gourmand · Floral · Fruity", "One sweet kiss of pear, jasmine and praline.",
  f"{t} is a fruity floral gourmand fragrance for women. Juicy pear and mandarin open it fresh and sweet, a heart of jasmine and lily of the valley adds a soft white-floral touch, and it settles into a cosy, delicious base of vanilla and praline.",
  ["A juicy pear and mandarin opening", "A soft jasmine and lily of the valley heart", "A cosy vanilla and praline base", "Generous 75ml Eau de Parfum"],
  "EAN 3516641926328 matched on Galaxus and Klinq (One Kiss EDP 75ml). Pyramid agreed by Klinq, Redlabel Outlet, ScentVerdict and Ferwer; Galaxus and FragranceNet give different lists (ignored). Gourmand floral per ScentVerdict, Ferwer, Redlabel. Launch year (1998) single-source, left out. Women." + AW,
  "pear and mandarin over jasmine, vanilla and praline.", ["Gourmand", "Floral", "Fruity"], ["Vanilla", "Floral", "Jasmine", "Fruity"],
  name="One Kiss", **PC)

# 5 Franck Olivier White Touch EDP 100ml -> needs-review (EAN weakly confirmed)
t = "Franck Olivier White Touch Eau de Parfum 100ml"
F("3516642117312", "Franck Olivier", t, "Women", "100", "23.99", "30.99", 5,
  [("Top", "Blackcurrant, Pear, Melon, Water Lily"), ("Heart", "Freesia, Violet, Rose, Jasmine, Artemisia"), ("Base", "Musk, Sandalwood")],
  "Fruity · Floral · Fresh", "Fresh, luminous and softly floral.",
  f"{t} is White Touch Pour Elle, a fresh fruity floral fragrance for women. Blackcurrant, pear, melon and water lily open it bright and watery, a heart of freesia, violet, rose, jasmine and a touch of artemisia brings a soft bouquet, and it settles into clean musk and creamy sandalwood.",
  ["A bright blackcurrant, pear and melon opening", "A soft freesia, violet, rose and jasmine heart", "A clean musk and sandalwood base", "Generous 100ml Eau de Parfum"],
  "NEEDS REVIEW: EAN 3516642117312 seen only as a Qogita search-result title (White Touch Pour Elle EDP 100ml), page not readable; Galaxus/Sharaf DG sell White Touch EDP 100ml under older EAN 3516640917310. Pyramid agreed by FragranceNet, Ferwer and NiceOne (artemisia in 2 of 3). Not the men's Black/Oud Touch line. Women." + AW,
  "blackcurrant and pear over freesia, rose and sandalwood.", ["Fruity", "Floral", "Fresh"], ["Fruity", "Floral", "Rose", "Jasmine", "Fresh"],
  name="White Touch", status="needs-review", **PC)

# 6 Gulf Orchid Silver Absolute EDP 100ml -> needs-review (only shared retailer copy for notes; gender)
t = "Gulf Orchid Silver Absolute Eau de Parfum 100ml"
F("6291107015941", "Gulf Orchid", t, "Unisex", "100", "23.49", "29.99", 5,
  [("Top", "Bergamot, Galbanum, Lemon"), ("Heart", "Floral Notes, Spicy Notes"), ("Base", "Ambergris, Musk, Sandalwood")],
  "Citrus · Fresh · Musky", "Crisp citrus and clean musk, polished to a silver shine.",
  f"{t} is a fresh citrus fragrance from Gulf Orchid. Bergamot, galbanum and lemon open it crisp and green, a heart of floral and spicy notes adds depth, and it settles into a smooth base of ambergris, musk and sandalwood.",
  ["A crisp bergamot, galbanum and lemon opening", "A floral, gently spicy heart", "A smooth ambergris, musk and sandalwood base", "Generous 100ml Eau de Parfum"],
  "NEEDS REVIEW: EAN 6291107015941 matched on parfuem365.de and sairam.cl (Silver Absolute EDP 100ml). Notes from aromaconcepts.pk, orioudh.com and sairam.cl agree on all tiers but share near-identical copy (may not be independent); no brand/Fragrantica entry. Supplier gender Unisex kept: aromaconcepts and orioudh sell it as men's, sairam as unisex. Not Al Qasr Silver." + AW,
  "bergamot and lemon over ambergris, musk and sandalwood.", ["Citrus", "Fresh", "Musky"], ["Citrus", "Fresh", "Sandalwood", "Spicy"],
  name="Silver Absolute", status="needs-review", **PC)

# 7 Gulf Orchid Smoky Vanilla EDP 100ml
t = "Gulf Orchid Smoky Vanilla Eau de Parfum 100ml"
F("6290362163091", "Gulf Orchid", t, "Unisex", "100", "25.99", "35.99", 5,
  [("Top", "Tobacco Leaf, Spicy Notes"), ("Heart", "Vanilla, Cacao, Tonka Bean, Tobacco Flower"), ("Base", "Dried Fruits, Woody Notes")],
  "Gourmand · Oriental · Woody", "Warm vanilla wrapped in soft tobacco smoke.",
  f"{t} is a smoky oriental gourmand fragrance for everyone. Tobacco leaf and spices open it warm and slightly smoky, a rich heart of vanilla, cacao, tonka bean and tobacco flower follows, and it settles into a deep base of dried fruits and woods.",
  ["A warm, smoky tobacco leaf and spice opening", "A rich vanilla, cacao and tonka heart", "A deep dried fruit and woody base", "Generous 100ml Eau de Parfum"],
  "EAN 6290362163091 matched on parfuem365.de and liquidomanduria.it (Smoky Vanilla EDP 100ml). Pyramid agreed by liquidomanduria.it, parfumerie-de-dubai.com and youlhamperfumes.ma (amber only on perfumeshop.co.za, left out). Oriental woody/gourmand per all three. Launch year single-source, left out. Unisex per retailers, matches supplier." + AW,
  "tobacco leaf and spice over vanilla, cacao and woods.", ["Gourmand", "Oriental", "Woody"], ["Vanilla", "Oriental", "Spicy", "Woody"],
  name="Smoky Vanilla", **PC)

# 8 Issey Miyake A Drop d'Issey EDP 50ml + 50ml hand cream
t = "Issey Miyake A Drop d'Issey Eau de Parfum 50ml Gift Set with 50ml Hand Cream"
GS("3423222092924", "Issey Miyake", t, "Issey Miyake A Drop d'Issey EDP 50ml & Hand Cream Gift Set", "Women", "50", "48.49", "61.99", 5,
   [("Top", "Damask Rose"), ("Heart", "Lilac, Orange Blossom, Almond Milk"), ("Base", "Musk, Atlas Cedarwood, Vanillin")],
   "Floral · Musky · Fresh", "A drop of solar florals, ready to give.",
   f"{t} pairs A Drop d'Issey, Issey Miyake's floral musky Eau de Parfum created by perfumer Ane Ayo in 2021, with a matching hand cream. Damask rose opens it softly, a sunny heart of lilac, orange blossom and almond milk follows, and it settles into a clean musk with Atlas cedarwood and vanillin.",
   ["A Drop d'Issey Eau de Parfum 50ml (spray)", "A Drop d'Issey Hand Cream 50ml"],
   ["A soft damask rose opening", "A sunny lilac, orange blossom and almond milk heart", "A clean musk, cedarwood and vanillin base", "A ready-made gift with matching hand cream"],
   "EAN 3423222092924 matched on ecscottgroup.com, morele.net and epocacosmeticos.com.br: EDP 50ml + ONE 50ml hand cream (not the live 2 x hand cream set, EAN 3423222047955). Pyramid agreed by Issey Miyake site, John Lewis and Epoca (jasmine/star anise/ambrox Parfumo only, left out). 2021 and perfumer Ane Ayo per Parfumo, brand, John Lewis. Women." + AW,
   "damask rose over lilac, almond milk and clean musk.", ["Floral", "Musky", "Fresh"], ["Floral", "Rose", "Fresh"],
   name="A Drop d'Issey", **PC)

# 9 Issey Miyake Fusion d'Issey IGO EDT 80ml + 20ml
t = "Issey Miyake Fusion d'Issey IGO Eau de Toilette 80ml with 20ml Travel Spray"
GS("3423222010492", "Issey Miyake", t, "Issey Miyake Fusion d'Issey IGO EDT 80ml + 20ml Travel Spray", "Men", "80", "35.49", "47.99", 5,
   [("Top", "Lemon, Coconut Water"), ("Heart", "Rosemary, Geranium, Cardamom"), ("Base", "Patchouli, Ambroxan, Woods")],
   "Fougère · Aromatic · Woody", "Fusion d'Issey at home and on the go.",
   f"{t} is the IGO set of Fusion d'Issey, Issey Miyake's aromatic fougère for men created by perfumer Nathalie Lorson in 2020. Lemon and coconut water open it fresh and bright, a heart of rosemary, geranium and cardamom adds an aromatic warmth, and it settles into patchouli, ambroxan and mineral woods.",
   ["Fusion d'Issey Eau de Toilette 80ml (spray)", "Fusion d'Issey Eau de Toilette 20ml (travel spray)"],
   ["A fresh lemon and coconut water opening", "An aromatic rosemary, geranium and cardamom heart", "A warm patchouli, ambroxan and woody base", "Full-size spray plus a 20ml travel spray"],
   "EAN 3423222010492 matched on cosmostore.org (IGO coffret EDT 80ml + EDT 20ml), eBay, Galaxus and Venera (100ml total). Original Fusion d'Issey EDT, not Extrême. 'Cap To Go' wording only in one URL, so listed as 20ml travel spray. Pyramid: notes placed in same tier by 2+ of cosmostore, Parfumo, lookincredible (sandalwood tier disputed, left out). 2020 and Nathalie Lorson per Parfumo, NST, lookincredible. Men." + AW,
   "lemon and coconut water over rosemary, patchouli and woods.", ["Fougere", "Aromatic", "Woody"], ["Citrus", "Spicy", "Woody", "Fresh"],
   name="Fusion d'Issey", **TC)

# 10 Issey Miyake L'Eau d'Issey Eau & Magnolia EDT Intense 50ml
t = "Issey Miyake L'Eau d'Issey Eau & Magnolia Eau de Toilette Intense 50ml"
F("3423222048013", "Issey Miyake", t, "Women", "50", "31.99", "41.99", 5,
  [("Top", "Bergamot, Neroli"), ("Heart", "Magnolia, Rose"), ("Base", "Sandalwood")],
  "Floral · Fresh · Woody", "L'Eau d'Issey in full magnolia bloom.",
  f"{t} is a fresh floral fragrance for women, launched in 2022 and created by perfumer Daphné Bugey. Bergamot and neroli open it bright and luminous, a heart of magnolia and rose brings a fresh, watery floral bloom, and it settles into a soft, creamy sandalwood.",
  ["A bright bergamot and neroli opening", "A fresh magnolia and rose heart", "A soft, creamy sandalwood base", "Handy 50ml Eau de Toilette Intense"],
  "EAN 3423222048013 matched on nandansons.com (Eau & Magnolia EDT Intense 1.7oz), Jomashop and Walmart Business (EDT 1.69oz). Brand site sells it only as EDT Intense, so 'Intense' added to supplier title. Pyramid agreed by Parfumo, Lookfantastic, tendance-parfums (musk Parfumo only, left out). 2022 and Daphné Bugey per Parfumo and tendance-parfums. Women." + AW,
  "bergamot and neroli over magnolia, rose and sandalwood.", ["Floral", "Fresh", "Woody"], ["Floral", "Rose", "Citrus", "Sandalwood", "Fresh"],
  name="Eau & Magnolia", conc="Eau De Toilette", concl="Eau de Toilette Intense")

P[9]["seo"] = ("Issey Miyake L'Eau d'Issey Eau & Magnolia EDT Intense 50ml", P[9]["seo"][1])
write_outputs()
