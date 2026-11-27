import sys; sys.path.insert(0, "/home/claude/ambient-beauty-images/workflow")
from lib import *
TC = dict(conc="Eau De Toilette", concl="Eau de Toilette")
PC = dict(conc="Eau De Parfum", concl="Eau de Parfum")
XP = dict(conc="Parfum", concl="Parfum")
AW = " Awaiting photos."
NR = dict(status="needs-review")
MB = "Mercedes-Benz"

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

# 1 The Move EDT 60ml
t = "Mercedes-Benz The Move Eau de Toilette 60ml"
F("3595471091024", MB, t, "Men", "60", "32.99", "41.99", 1,
  [("Top", "Cardamom"), ("Heart", "Geranium, Sea Salt Notes"), ("Base", "Tonka Bean, Balsam Fir")],
  "Aromatic · Fougère", "Fresh, free-spirited and always on the go.",
  f"{t} is an aromatic fougère fragrance for men, created by perfumer Dominique Ropion. Spicy cardamom opens with energy, a heart of geranium and salty marine notes brings a fresh, open-air feel, and it settles onto tonka bean and balsam fir.",
  ["An energetic cardamom opening", "A fresh geranium and sea salt heart", "A warm tonka bean and balsam fir base", "A handy 60ml Eau de Toilette"],
  "EAN 3595471091024 matched on Galaxus CH + eBay.de catalogue (The Move EDT 60ml). Pyramid as the 20ml (27/11 b1): Notino, Galaxus, Ferwer, whatscent agree; apple blossom/grapefruit tier disputed (eBay puts apple blossom in heart) – left out. Aromatic fougère per brand + Ferwer (Notino: aromatic aquatic). Dominique Ropion per brand, Ferwer, whatscent. Year left out (EDT and EDP versions both 2019-ish, not checked). Men." + AW,
  "cardamom over geranium, sea salt and tonka bean.", ["Aromatic", "Fougere"], ["Fresh", "Spicy", "Aquatic"],
  name="The Move", **TC)

# 2 Ultimate EDP 75ml
t = "Mercedes-Benz Ultimate Eau de Parfum 75ml"
F("3595471023001", MB, t, "Men", "75", "33.49", "42.99", 1,
  [("Top", "Lavender, Cedar Leaf"), ("Heart", "Apple, Mandarin, Nutmeg"), ("Base", "Sandalwood, Cypress, Patchouli, Amber")],
  "Amber · Aromatic · Woody", "Warm, aromatic and quietly powerful.",
  f"{t} is an amber aromatic woody fragrance for men, created by perfumer Olivier Cresp and launched in 2022. Lavender and cedar leaf open fresh and aromatic, a heart of crisp apple, mandarin and nutmeg adds a juicy, spicy warmth, and it settles onto a rich base of sandalwood, cypress, patchouli and amber.",
  ["A fresh lavender and cedar leaf opening", "A juicy apple, mandarin and nutmeg heart", "A rich sandalwood, patchouli and amber base", "A generous 75ml Eau de Parfum"],
  "EAN 3595471023001 matched on Tripletraders (For Men Ultimate EDP 75ml) – only one EAN page found (Qogita page would not load). EDP 75ml per brand, Tata CLiQ, FirstCry, Tripletraders (brand page header says EDT – title says EDP). Pyramid agreed by Tripletraders, FirstCry, Ferwer, Parfumo, Scentverdict. Ambery aromatic woody per brand + Ferwer. Olivier Cresp per brand, Ferwer, Parfumo; 2022 per Ferwer, Parfumo, Scentverdict. Men." + AW,
  "lavender and cedar leaf over apple, nutmeg and amber.", ["Oriental", "Aromatic", "Woody"], ["Woody", "Lavender", "Sandalwood"],
  name="Mercedes-Benz Ultimate", **PC)

WIR_PYR = [("Top", "Mandarin, Pear"), ("Heart", "Jasmine Sambac, Gardenia"), ("Base", "Tonka Bean, Benzoin, Patchouli, Sandalwood")]
WIR_INTRO = ("is an oriental floral fragrance for women, created by perfumer Honorine Blanc and launched in 2021. Juicy mandarin and pear open bright and sweet, "
             "touches of pistachio and cherry blossom add a gourmand softness, a heart of jasmine sambac and gardenia brings rich white florals, and it settles onto a warm base of tonka bean, benzoin, patchouli and sandalwood.")
WIR_NOTE = ("Pyramid agreed by Superdrug, Parfumo, brand site; pistachio and cherry blossom tier disputed (top vs heart) – named in text, not in a tier. "
            "Oriental floral per Superdrug + brand (woody oriental floral). Honorine Blanc per brand + Parfumo; 2021 per Parfumo + Scentverdict. Women.")
# 3 Woman In Red EDP 20ml
t = "Mercedes-Benz Woman In Red Eau de Parfum 20ml"
F("3595471071156", MB, t, "Women", "20", "21.49", "27.99", 5, WIR_PYR,
  "Floral · Oriental", "Bold, sensual and impossible to ignore.",
  f"{t} {WIR_INTRO} The 20ml size is perfect for your handbag or travel.",
  ["A juicy mandarin and pear opening", "A rich jasmine and gardenia heart", "A warm tonka, benzoin and sandalwood base", "Handy 20ml travel-size Eau de Parfum"],
  "EAN 3595471071156 matched on Superdrug (Woman In Red EDP 20ml) – one EAN page; 20ml travel size also on Tira + Nykaa (brand site lists 30/60/90ml only). " + WIR_NOTE + AW,
  "mandarin and pear over jasmine, gardenia and tonka.", ["Floral", "Oriental"], ["Floral", "Jasmine", "Oriental"],
  name="Woman In Red", **PC)

# 4 Woman In Red EDP 90ml
t = "Mercedes-Benz Woman In Red Eau de Parfum 90ml"
F("3595471071125", MB, t, "Women", "90", "43.99", "57.99", 1, WIR_PYR,
  "Floral · Oriental", "Bold, sensual and impossible to ignore.",
  f"{t} {WIR_INTRO}",
  ["A juicy mandarin and pear opening", "A rich jasmine and gardenia heart", "A warm tonka, benzoin and sandalwood base", "Generous 90ml Eau de Parfum"],
  "EAN 3595471071125 matched on Superdrug + eBay (Woman In Red EDP 90ml). " + WIR_NOTE + AW,
  "mandarin and pear over jasmine, gardenia and tonka.", ["Floral", "Oriental"], ["Floral", "Jasmine", "Oriental"],
  name="Woman In Red", **PC)

# 5 Michael Kors Pour Homme gift set
t = "Michael Kors Pour Homme Eau de Parfum 50ml Gift Set with Shower Gel and Aftershave Balm"
GS("0850050174691", "Michael Kors", t, "Michael Kors Pour Homme EDP 50ml 3-Piece Gift Set", "Men", "50", "48.99", "62.99", 5,
   [("Top", "Bergamot, Pink Peppercorn, Lavandin"), ("Heart", "Sea Wave Accord, Clary Sage, Geranium"), ("Base", "Patchouli, Vetiver, Grey Amber")],
   "Woody · Spicy · Citrus", "A fresh, spicy signature in a ready-to-give set.",
   f"{t} brings together Michael Kors Pour Homme Eau de Parfum in the 50ml size with a matching 50ml shower gel and 50ml aftershave balm. This woody spicy citrus scent opens with bergamot, pink peppercorn and lavandin, flows into a fresh heart of sea wave accord, clary sage and geranium, and settles onto patchouli, vetiver and grey amber.",
   ["Michael Kors Pour Homme Eau de Parfum 50ml (spray)", "Michael Kors Pour Homme Shower Gel 50ml", "Michael Kors Pour Homme Aftershave Balm 50ml"],
   ["A zesty bergamot and pink peppercorn opening", "A fresh sea wave and clary sage heart", "A warm patchouli, vetiver and grey amber base", "Shower gel and aftershave balm included"],
   "EAN 0850050174691 matched on Kruidvat NL (Pour Homme Giftset 150ml) – one EAN page; contents EDP 50ml + shower gel 50ml + aftershave balm 50ml per Kruidvat, Lyko, Debenhams. Other MK Pour Homme sets use other EANs (Superdrug 0850050174967, Harvey Nichols 0850050174356, a body-lotion version) – check box. Pyramid agreed by Superdrug, Lyko, Debenhams, Harvey Nichols. Woody spicy citrus per Lyko, Superdrug, michaelkors.com. Perfumer/year unconfirmed – left out. Men." + AW,
   "bergamot and pink pepper over sea notes and vetiver.", ["Woody", "Spicy", "Citrus"], ["Woody", "Spicy", "Citrus"],
   name="Michael Kors Pour Homme", **PC)

# 6 Molton Brown Sunlit Clementine & Vetiver EDT 100ml (needs-review: EAN not found)
t = "Molton Brown Sunlit Clementine & Vetiver Eau de Toilette 100ml"
F("5030805024111", "Molton Brown", t, "Unisex", "100", "71.49", "95.99", 5,
  [("Top", "Clementine, Mandarin"), ("Heart", "Fig Leaves"), ("Base", "Bourbon Vetiver")],
  "Citrus · Woody", "Sun-warmed citrus on a smooth vetiver base.",
  f"{t} is a citrus woody fragrance for everyone, created by perfumer Julie Massé and launched in 2024. Juicy clementine and mandarin open bright and sunny, a green heart of fig leaves adds a fresh, leafy note, and it settles onto an earthy, elegant base of Bourbon vetiver.",
  ["A bright clementine and mandarin opening", "A green fig leaf heart", "An earthy Bourbon vetiver base", "Generous 100ml Eau de Toilette"],
  "NEEDS REVIEW: no web page found listing EAN 5030805024111, and an EDP 100ml of this scent also exists – check the box says Eau de Toilette 100ml. EDT 100ml per John Lewis, Cult Beauty, Brown Thomas, Woolworths ZA. Pyramid agreed by Cult Beauty, FragranceNet, Scentverdict, Woolworths, Parfumdreams (hazelnut/moss single-tier sources – left out). Citrus woody per John Lewis + NST. Julie Massé per Parfumdreams + Scentverdict; 2024 per John Lewis, NST, Parfumdreams. Unisex kept (Parfumdreams/FragranceNet unisex; John Lewis + Brown Thomas file it under Women)." + AW,
  "clementine and mandarin over fig leaves and vetiver.", ["Citrus", "Woody"], ["Citrus", "Fresh", "Woody"],
  name="Sunlit Clementine & Vetiver", status="needs-review", **TC)

EXP_PYR = [("Top", "Bergamot, Pomarose, Sage"), ("Heart", "Vetiver, Leather, Sandalwood"), ("Base", "Patchouli, Ambrofix, Akigalawood")]
EXP_INTRO = ("is a woody aromatic leather fragrance for men, launched in 2019 and created by perfumers Jordi Fernandez, Antoine Maisondieu and Olivier Pescheux. "
             "Bergamot, Pomarose and sage open fresh and adventurous, a heart of vetiver, leather and sandalwood brings depth, and it settles onto a warm base of patchouli, Ambrofix and Akigalawood.")
EXP_NOTE = ("Pyramid agreed by Very, OnBuy, Superdrug, Harvey Nichols (Shop-Apotheke has pink pepper for Pomarose – ignored). Woody aromatic leather per Very, Moodie Davitt, FashionNetwork, Superdrug, Harvey Nichols. "
            "Perfumers per Moodie Davitt, FashionNetwork, Scentverdict; 2019 per FashionNetwork + Scentverdict. Men.")
# 7 Explorer EDP 200ml
t = "Mont Blanc Explorer Eau de Parfum 200ml"
F("3386460118675", "Mont Blanc", t, "Men", "200", "79.99", "101.99", 5, EXP_PYR,
  "Woody · Aromatic · Leather", "A bold call to adventure.",
  f"{t} {EXP_INTRO} The 200ml bottle is great value for a daily signature.",
  ["A fresh bergamot, Pomarose and sage opening", "A deep vetiver and leather heart", "A warm patchouli and Akigalawood base", "Large 200ml Eau de Parfum"],
  "EAN 3386460118675 matched on Very + OnBuy (Explorer EDP 200ml). " + EXP_NOTE + AW,
  "bergamot and sage over vetiver, leather and patchouli.", ["Woody", "Aromatic", "Leather"], ["Woody", "Citrus", "Fresh"],
  name="Montblanc Explorer", **PC)

# 8 Explorer EDP 60ml
t = "Mont Blanc Explorer Eau de Parfum 60ml"
F("3386460101042", "Mont Blanc", t, "Men", "60", "45.49", "61.99", 5, EXP_PYR,
  "Woody · Aromatic · Leather", "A bold call to adventure.",
  f"{t} {EXP_INTRO}",
  ["A fresh bergamot, Pomarose and sage opening", "A deep vetiver and leather heart", "A warm patchouli and Akigalawood base", "A handy 60ml Eau de Parfum"],
  "EAN 3386460101042 matched on Superdrug + Shop-Apotheke (Explorer EDP 60ml). " + EXP_NOTE + AW,
  "bergamot and sage over vetiver, leather and patchouli.", ["Woody", "Aromatic", "Leather"], ["Woody", "Citrus", "Fresh"],
  name="Montblanc Explorer", **PC)

XX_PYR = [("Top", "Bergamot"), ("Heart", "Patchouli"), ("Base", "Amber Accord")]
XX_INTRO = ("Montblanc Explorer Extreme is a woody ambery leather fragrance for men in the intense Parfum concentration, launched in 2025. "
            "Bright bergamot opens it, a heart of deep patchouli gives it character, and it settles onto a warm, lasting amber accord.")
XX_NOTE = ("Pyramid agreed by montblanc.com, Harvey Nichols, The Perfume Shop, Escentual (Brown Thomas swaps heart/base; Next + Parfumo add leather in base). "
           "Woody ambery leather per Brown Thomas + NST (Escentual woody amber). 2025 per Parfumo + NST. Perfumer unconfirmed – left out. Men.")
# 9 Explorer Extreme gift set (needs-review)
t = "Mont Blanc Explorer Extreme Parfum 100ml Gift Set with Shower Gel and 2 Travel Sprays"
GS("3386460167048", "Mont Blanc", t, "Mont Blanc Explorer Extreme Parfum 100ml 4-Piece Gift Set", "Men", "100", "74.49", "96.99", 5, XX_PYR,
   "Woody · Amber · Leather", "An intense new chapter of Explorer, ready to give.",
   f"{t} brings together Montblanc Explorer Extreme Parfum in the 100ml size, a 100ml shower gel and two 7.5ml Parfum travel sprays. " + XX_INTRO,
   ["Montblanc Explorer Extreme Parfum 100ml (spray)", "Montblanc Explorer Extreme Shower Gel 100ml", "Montblanc Explorer Extreme Parfum 7.5ml (travel spray)", "Montblanc Explorer Extreme Parfum 7.5ml (travel spray)"],
   ["A bright bergamot opening", "A deep patchouli heart", "A warm, lasting amber base", "Shower gel and two travel sprays included"],
   "NEEDS REVIEW: no web page found listing EAN 3386460167048, and a similar set with a 60ml Parfum exists (Brown Thomas, Harvey Nichols, TPS) – check box is the 100ml version. Supplier name says EDP, form says Parfum: listed as Parfum per Next, Justmylook, Escentual title, Montblanc naming. Contents 100ml Parfum + 100ml shower gel + 2 x 7.5ml Parfum per Next, Justmylook, Escentual. " + XX_NOTE + AW,
   "bergamot over patchouli and amber, with shower gel and travel sprays.", ["Woody", "Oriental", "Leather"], ["Woody", "Oriental"],
   name="Explorer Extreme", status="needs-review", **XP)

# 10 Explorer Extreme Parfum 60ml
t = "Mont Blanc Explorer Extreme Parfum 60ml"
F("3386460153737", "Mont Blanc", t, "Men", "60", "48.49", "62.99", 2, XX_PYR,
  "Woody · Amber · Leather", "An intense new chapter of Explorer.",
  XX_INTRO.replace("Montblanc Explorer Extreme is", t + " is"),
  ["A bright bergamot opening", "A deep patchouli heart", "A warm, lasting amber base", "Intense 60ml Parfum concentration"],
  "EAN 3386460153737 matched on Harvey Nichols + The Perfume Shop (Explorer Extreme Parfum 60ml). Supplier form says Eau de Parfum but name, montblanc.com, Harvey Nichols, TPS say Parfum – listed as Parfum. " + XX_NOTE + AW,
  "bergamot over patchouli and a warm amber accord.", ["Woody", "Oriental", "Leather"], ["Woody", "Oriental"],
  name="Explorer Extreme", **XP)

_st = "Molton Brown Sunlit Clementine & Vetiver EDT 100ml"
P[5]["seo"] = (_st, f"{_st}: clementine and mandarin over fig leaves and vetiver." + FREE)
write_outputs()
