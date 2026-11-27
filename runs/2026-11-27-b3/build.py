import sys; sys.path.insert(0, "/home/claude/ambient-beauty-images/workflow")
from lib import *
TC = dict(conc="Eau De Toilette", concl="Eau de Toilette")
PC = dict(conc="Eau De Parfum", concl="Eau de Parfum")
AW = " Awaiting photos."
MB = "Mont Blanc"

def GS(bc, vendor, title, seo_t, gender, size, price, cmp, qty, pyr, profile, hook, intro, contents, love, note, seo_d,
       of, fr, name, conc="Eau De Parfum", concl="Eau de Parfum", status="done", form_suffix=" Gift Set"):
    """Fragrance set: fragrance standard (3 tags) plus a 'What's in the set' block (as runs/2026-11-27-b2)."""
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

# 1 Explorer Infinite EDP 60ml (needs-review: pyramid + family)
t = "Mont Blanc Explorer Infinite Eau de Parfum 60ml"
F("3386460175609", MB, t, "Men", "60", "44.49", "60.99", 1,
  [("Heart", "Patchouli")],
  "Fresh · Woody", "A fresh new direction for the Explorer journey.",
  f"{t} is a fresh woody fragrance for men, created by perfumers Jordi Fernandez and Antoine Maisondieu and launched in 2026. A bright, zesty opening leads into a deep heart of patchouli, giving this newest Explorer a clean, modern character with an earthy, woody trail.",
  ["The newest addition to the Explorer family", "A deep, earthy patchouli heart", "A clean, fresh woody character", "A handy 60ml Eau de Parfum"],
  "NEEDS REVIEW: scent pyramid disputed – brand site says bergamot (top) / patchouli / vetiver (base), The Perfume Shop, parfumerie-en-ligne, Sephora FR + NST say lemon / patchouli / musk; only the agreed heart (patchouli) is shown. Olfactory family soft: 'fresh woody' per NST + brand 'fresh direction' only. EAN 3386460175609 matched on The Perfume Shop UK, Jomashop, parfumerie-en-ligne (Explorer Infinite EDP 60ml). Jordi Fernandez + Antoine Maisondieu per parfumerie-en-ligne, NST, Sephora FR; 2026 per TPS + NST. Men." + AW,
  "a fresh woody scent with a deep patchouli heart.", ["Fresh", "Woody"], ["Fresh", "Woody"],
  name="Explorer Infinite", status="needs-review", **PC)

PL_PYR = [("Top", "Violet Leaf"), ("Heart", "Clary Sage"), ("Base", "Cedarwood")]
PL_INTRO = ("Montblanc Explorer Platinum is a woody amber fragrance for men, launched in 2023. Green violet leaf opens it with a cool freshness, "
            "an aromatic heart of clary sage adds depth, and it settles onto a smooth, lasting cedarwood base.")
PL_NOTE = ("Pyramid agreed by montblanc.com UK, Parfumo, Sephora UK, Savers (grapefruit in top on NST + Escentual only – left out). "
           "Woody amber per Sephora UK + NST. 2023 per Parfumo, NST, Escentual. Perfumer unconfirmed – left out. Men.")
# 2 Explorer Platinum EDP 200ml
t = "Mont Blanc Explorer Platinum Eau de Parfum 200ml"
F("3386460146081", MB, t, "Men", "200", "51.49", "65.99", 5, PL_PYR,
  "Woody · Amber · Aromatic", "Cool, clean and quietly confident.",
  PL_INTRO.replace("Montblanc Explorer Platinum is", t + " is"),
  ["A cool green violet leaf opening", "An aromatic clary sage heart", "A smooth, lasting cedarwood base", "A generous 200ml Eau de Parfum"],
  "EAN 3386460146081 matched on Savers UK, eBay, fragranceclick.co.uk (Explorer Platinum EDP 200ml); Amazon UK also lists the 200ml. Brand UK site shows 30/60/100ml only and Savers says 'no longer available online' – 200ml may be a limited size. " + PL_NOTE + AW,
  "violet leaf over clary sage and cedarwood.", ["Woody", "Oriental", "Aromatic"], ["Woody", "Fresh"],
  name="Explorer Platinum", **PC)

# 3 Explorer Platinum gift set (needs-review: one EAN source)
t = "Mont Blanc Explorer Platinum Eau de Parfum 100ml Gift Set with 30ml Eau de Parfum"
GS("3386460139373", MB, t, "Mont Blanc Explorer Platinum EDP 100ml + 30ml Gift Set", "Men", "100", "50.49", "66.99", 5, PL_PYR,
   "Woody · Amber · Aromatic", "Two sizes of Explorer Platinum, ready to give.",
   f"{t} brings together Montblanc Explorer Platinum Eau de Parfum in the 100ml size and a 30ml Eau de Parfum to keep in your bag or take away. " + PL_INTRO,
   ["Montblanc Explorer Platinum Eau de Parfum 100ml (spray)", "Montblanc Explorer Platinum Eau de Parfum 30ml (spray)"],
   ["A cool green violet leaf opening", "An aromatic clary sage heart", "A smooth cedarwood base", "A 30ml spray for travel included"],
   "NEEDS REVIEW: EAN 3386460139373 found on one site only (envie2parfum.fr: Coffret Explorer Platinum Noël 2023, 100ml EDP + 30ml EDP) – contents match the supplier name but are not two-source confirmed; most UK Explorer Platinum sets are 100ml EDP + shower gel + 7.5ml instead. Check the box. Christmas 2023 set, likely discontinued. " + PL_NOTE + AW,
   "violet leaf over clary sage and cedarwood, with a 30ml spray.", ["Woody", "Oriental", "Aromatic"], ["Woody", "Fresh"],
   name="Explorer Platinum", status="needs-review", **PC)

# 4 Individuel EDT 75ml
t = "Mont Blanc Individuel Eau de Toilette 75ml"
F("3386460028394", MB, t, "Men", "75", "31.99", "41.99", 5,
  [("Top", "Bergamot, Juniper Berry, Lavender, Cinnamon, Coriander"), ("Heart", "Orange Blossom, Violet, Jasmine"),
   ("Base", "Sandalwood, Tonka Bean, Amber, Patchouli, Musk")],
  "Oriental · Woody", "Warm, spicy and quietly distinctive.",
  f"{t} is a woody oriental fragrance for men, created by perfumer Pierre Bourdon and launched in 2003. Bergamot, juniper berry, lavender and a touch of cinnamon and coriander open it with a fresh, spicy energy, a soft heart of orange blossom, violet and jasmine follows, and it settles onto a warm base of sandalwood, tonka bean, amber, patchouli and musk.",
  ["A fresh, spicy juniper and bergamot opening", "A soft orange blossom and violet heart", "A warm sandalwood, tonka and amber base", "A classic Montblanc since 2003"],
  "EAN 3386460028394 matched on GiftExpress, tendance-parfums (image file), eBay (Individuel EDT 75ml); upcitemdb snippet agrees; Notino UK 75ml. Pyramid notes each listed by 2+ of Parfumo, tendance-parfums, Notino UK (shortened; pineapple, mint, rosemary, geranium, oakmoss, raspberry, chocolate, vanilla, vetiver have partial support – left out). Woody oriental per Notino + tendance. Pierre Bourdon, 2003 per Parfumo, Notino, tendance. Parfumo says it appears discontinued – old/limited stock. Men (not Femme Individuelle)." + AW,
  "juniper and bergamot over orange blossom, sandalwood and tonka.", ["Oriental", "Woody", "Spicy"], ["Woody", "Spicy", "Sandalwood"],
  name="Montblanc Individuel", **TC)

LG_PYR = [("Top", "Lavender, Bergamot"), ("Heart", "Rose"), ("Base", "Sandalwood, Tonka Bean, Oakmoss Accord")]
LG_NOTE = ("Pyramid: only notes agreed across montblanc.com, Parfumo, Osmoz, NST (lists differ in detail – citrus/pineapple leaf top, cedar/jasmine/geranium/apple heart disputed – left out). "
           "Aromatic fougère per Osmoz, NST, brand ('fresh fougère'). Olivier Pescheux, 2011 per Parfumo, Osmoz, NST. Men.")
# 5 Legend Aftershave Lotion 100ml (needs-review: splash vs spray)
t = "Mont Blanc Legend Aftershave Lotion 100ml"
add(cat_name="Fragrances", bc="3386460032780", title=t, vendor=MB, type=TYPE["Men"], gender="Men", cat=TAXON["aftershave"],
    price="33.49", cmp="45.99", qty=5, tags=[MB, "Men", "Aftershave"],
    seo=(t, f"{t}: the fresh aromatic fougère Legend scent for after shaving." + FREE),
    form="Aftershave Lotion (Splash)", size="100", unit="ml", gpc=GPC["fragrance"], status="needs-review",
    mf={"product-form": ["Liquid"]},  # age-group not allowed in aftershave category
    note="NEEDS REVIEW: supplier name says Splash but supplier form says Aftershave Spray – listed as splash lotion per supplier name, eBay UK title ('Splash') and OnBuy directions ('pour into hands'); no brand page confirms – please check the bottle. EAN 3386460032780 matched on eBay UK, Galaxus BE, OnBuy UK (Legend Aftershave Lotion 100ml). Scent = Legend (2011). " + LG_NOTE + AW,
    desc=body("The fresh Legend signature, for the finishing touch after shaving.",
              f"{t} carries the fresh, aromatic fougère character of Montblanc Legend, created by perfumer Olivier Pescheux in 2011. Lavender and bergamot open it with a clean freshness, a soft rose heart follows, and it settles into warm sandalwood, tonka bean and an oakmoss accord.",
              [("Scent pyramid", kd(LG_PYR)),
               ("How to use", "<p>After shaving, pour a little into your hands and apply to the face and neck.</p>")],
              [("Brand", MB), ("Type", "Aftershave lotion"), ("Size", "100ml"),
               ("Scent profile", "Aromatic · Fougère · Fresh"), ("Wear", "Men")],
              ["The best-selling Legend scent", "Fresh lavender and bergamot", "A warm sandalwood and tonka finish", "100ml bottle"],
              [("What does Montblanc Legend Aftershave smell like?", pyramid_answer(LG_PYR)),
               ("Is it for men?", "Yes, it is a men's aftershave.")]))

# 6 Legend EDT 100ml
t = "Mont Blanc Legend Eau de Toilette 100ml"
F("3386460032681", MB, t, "Men", "100", "46.49", "62.99", 2, LG_PYR,
  "Aromatic · Fougère · Fresh", "Fresh, confident and made to last.",
  f"{t} is an aromatic fougère fragrance for men, created by perfumer Olivier Pescheux and launched in 2011. Lavender and bergamot open it with a clean, fresh lift, a soft rose heart adds smoothness, and it settles onto warm sandalwood, tonka bean and an oakmoss accord.",
  ["A modern classic since 2011", "A clean lavender and bergamot opening", "A warm sandalwood and tonka base", "The full 100ml Eau de Toilette"],
  "EAN 3386460032681 matched on penworld.eu (Legend EDT 100ml) + eBay UK title; jeancoutu URL carries the EAN (page didn't load). " + LG_NOTE + AW,
  "lavender and bergamot over rose, sandalwood and tonka.", ["Aromatic", "Fougere", "Fresh"], ["Lavender", "Fresh", "Sandalwood"],
  name="Montblanc Legend", **TC)

# 7 Legend Red EDP 200ml
t = "Mont Blanc Legend Red Eau de Parfum 200ml"
pyr = [("Top", "Blood Orange, Grapefruit, Cardamom"), ("Heart", "Cedarwood, Juniper Berry, Clary Sage"), ("Base", "Mahogany Wood, Atlas Cedarwood, Tonka Bean")]
F("3386460134965", MB, t, "Men", "200", "41.49", "55.99", 5, pyr,
  "Woody · Fruity", "Bold, vibrant and full of energy.",
  f"{t} is a woody fruity fragrance for men, launched in 2022. Juicy blood orange and grapefruit open it with a spark of cardamom, a heart of cedarwood, juniper berry and clary sage adds an aromatic depth, and it settles onto a rich base of mahogany wood, Atlas cedarwood and tonka bean.",
  ["A vibrant blood orange and cardamom opening", "An aromatic juniper and clary sage heart", "A rich mahogany wood and tonka base", "A generous 200ml Eau de Parfum"],
  "EAN 3386460134965 matched on Jomashop (Legend Red EDP 6.7oz) + fathyibrahim.com (Legend Red EDP 200ml); JustMyLook UK lists 200ml. Pyramid agreed by Interparfums, The Perfume Shop, Escentual, Tendance. Woody fruity per Interparfums, JustMyLook, TPS, Escentual. 2022 per Tendance + Escentual. Perfumer unconfirmed – left out. Men." + AW,
  "blood orange and cardamom over juniper, mahogany wood and tonka.", ["Woody", "Fruity"], ["Woody", "Citrus", "Spicy"],
  name="Montblanc Legend Red", **PC)

ST_INTRO = ("part of Mugler's Starlicious – Les Eaux Gourmandes trio, launched in 2026: light, playful gourmand Eau de Toilette sprays "
            "made to be worn on the neck, wrists, hair and clothes.")
ST_NOTE = ("Starlicious – Les Eaux Gourmandes trio, 2026 per Parfumo, Tendance, NST; Mugler UK says spray on neck, hair, wrist and clothes; Ulta US sells the same scents as 'Hair & Body Fragrance Mist' – listed as EDT perfume per UK retailers. Refill not confirmed; perfumer not found. Women (Mugler: feminine).")
# 8 Starlicious Berry Licorice
t = "Mugler Starlicious Berry Licorice Eau de Toilette 75ml"
pyr = [("Top", "Strawberry Accord, Raspberry Accord"), ("Heart", "Freesia Accord"), ("Base", "Licorice Accord")]
F("3614274797213", "Mugler", t, "Women", "75", "54.49", "68.99", 3, pyr,
  "Amber · Fruity · Gourmand", "Sweet, juicy and a little bit daring.",
  f"{t} is an ambery fruity gourmand fragrance for women, {ST_INTRO} Juicy strawberry and raspberry open it, a soft freesia heart adds a floral lift, and it dries down to a playful licorice accord.",
  ["A juicy strawberry and raspberry opening", "A soft freesia heart", "A playful licorice finish", "Light 75ml Eau de Toilette for skin and hair"],
  "EAN 3614274797213 matched on The Perfume Shop (Starlicious Berry EDT 75ml) + Tendance-parfums image (Starlicious Mist Berry Licorice EDT 75ml). Pyramid agreed by Mugler UK article, TPS, Tendance. Ambery fruity gourmand per Mugler UK, TPS, Sephora FR. " + ST_NOTE + AW,
  "strawberry and raspberry over freesia and licorice.", ["Oriental", "Fruity", "Gourmand"], ["Fruity", "Floral"],
  name="Starlicious Berry Licorice", **TC)

# 9 Starlicious Pineapple Musk
t = "Mugler Starlicious Pineapple Musk Eau de Toilette 75ml"
pyr = [("Top", "Pineapple Accord"), ("Heart", "Coconut Accord"), ("Base", "Musk")]
F("3614274797244", "Mugler", t, "Women", "75", "54.49", "68.99", 4, pyr,
  "Floral · Fruity · Gourmand", "Sunny, sweet and shimmering.",
  f"{t} is a floral fruity gourmand fragrance for women, {ST_INTRO} Juicy pineapple opens it, a creamy coconut heart brings a holiday feel, and it settles onto soft musk. Its shimmering formula catches the light, so give it a shake before use.",
  ["A juicy pineapple opening", "A creamy coconut heart", "A soft musky finish", "A shimmering 75ml Eau de Toilette"],
  "EAN 3614274797244 matched on The Perfume Shop only (Starlicious Pineapple EDT 75ml); name, size, notes agree on Mugler UK, Tendance, Ulta and EAN follows the sister products. Pyramid agreed by Mugler UK article, TPS, Ulta, Tendance. Floral fruity gourmand per Mugler UK, TPS, Ulta (Tendance: oriental vanilla). Shimmer / shake before use per Mugler + NST. " + ST_NOTE + AW,
  "pineapple over coconut and soft musk.", ["Floral", "Fruity", "Gourmand"], ["Fruity", "Floral"],
  name="Starlicious Pineapple Musk", **TC)

# 10 Starlicious Pistachio Praline
t = "Mugler Starlicious Pistachio Praline Eau de Toilette 75ml"
pyr = [("Top", "Pistachio Accord"), ("Heart", "Caramel Accord"), ("Base", "Patchouli")]
F("3614274797220", "Mugler", t, "Women", "75", "54.49", "70.99", 4, pyr,
  "Gourmand · Fruity · Woody", "Nutty, creamy and irresistibly sweet.",
  f"{t} is a gourmand fruity woody fragrance for women, {ST_INTRO} Creamy pistachio opens it, a heart of golden caramel adds a sweet, praline-like warmth, and it settles onto earthy patchouli.",
  ["A creamy pistachio opening", "A sweet caramel heart", "An earthy patchouli finish", "Light 75ml Eau de Toilette for skin and hair"],
  "EAN 3614274797220 matched on The Perfume Shop (Starlicious Pistachio EDT 75ml) + Tendance-parfums image (Starlicious Mist Pistachio Praline EDT 75ml). Pyramid agreed by Mugler UK article + TPS (Tendance adds praliné heart, woody base – left out). Gourmand fruity woody per Mugler, TPS, Sephora FR. " + ST_NOTE + AW,
  "pistachio over caramel and patchouli.", ["Gourmand", "Fruity", "Woody"], ["Woody", "Fruity"],
  name="Starlicious Pistachio Praline", **TC)

write_outputs()
for p in P: print(p["status"], p["seo"][0], len(p["seo"][0]), len(p["seo"][1]))
