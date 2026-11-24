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
F("5050456522781", "Cerruti", t, "Men", "200", "52.99", "72.99", 5,
  [("Top", "Bergamot, Lavender, Juniper, Cypress, Galbanum"), ("Heart", "Rose, Ylang-Ylang, Lily of the Valley, Vetiver"),
   ("Base", "Sandalwood, Cedar, Oakmoss, Patchouli, Musk")],
  "Woody · Aromatic · Fresh", "The timeless Cerruti 1881 for men, in a generous 200ml bottle.",
  f"{t} is the classic 1881 Pour Homme, a woody aromatic fragrance first launched in 1990. Bergamot, lavender, juniper and cypress open crisp and green, a refined heart of rose, ylang-ylang and lily of the valley over vetiver follows, and it settles into sandalwood, cedar, oakmoss and a soft musk.",
  ["A crisp bergamot, lavender and juniper opening", "A refined floral heart over vetiver", "A smooth sandalwood, cedar and oakmoss base", "Great-value 200ml Eau de Toilette"],
  "EAN 5050456522781 matched on Superdrug (Cerruti 1881 Homme EDT 200ml, marked 'DNR' / no longer online); 100ml in the same barcode series on The Perfume Shop; 200ml also on Parfumdreams. Pyramid shown is a subset of notes The Perfume Shop and Parfumo (2018 EDT) agree on in every tier; Cerruti.com and Osmoz give older/different lists. 1990 per TPS, Osmoz, ScentAdvice. Men." + AW,
  "bergamot, lavender and juniper over rose, sandalwood and oakmoss.", ["Woody", "Aromatic", "Fresh"], ["Woody", "Lavender", "Floral", "Sandalwood", "Fresh"],
  name="Cerruti 1881", **TC)

# 2 Clinique Aromatics In Black
t = "Clinique Aromatics In Black Eau de Parfum 100ml"
F("0020714769987", "Clinique", t, "Women", "100", "45.49", "59.99", 5,
  [("Top", "Pink Grapefruit, Plum Leaf, Italian Bergamot"), ("Heart", "Jasmine Sambac, Osmanthus, Neroli"), ("Base", "Myrrh, Tonka Bean, Vetiver")],
  "Floral · Oriental · Woody", "A dark, sensual twist on the Aromatics legend.",
  f"{t} is a floral oriental fragrance for women, launched in 2015. Pink grapefruit, plum leaf and Italian bergamot open with a bright sparkle, a heart of jasmine sambac, osmanthus and neroli follows, and it deepens into a smoky, warm base of myrrh, tonka bean and vetiver.",
  ["A bright pink grapefruit and bergamot opening", "A rich jasmine sambac and osmanthus heart", "A smoky myrrh, tonka and vetiver base", "Generous 100ml Eau de Parfum"],
  "EAN (GTIN 20714769987) matched on Galaxus (Aromatics in Black EDP 100ml); 100ml EDP also on John Lewis and Harrods. Pyramid: Parfumo and The Perfume Girl agree on every tier (Lookfantastic shorter list fits). 2015 per John Lewis, Parfumo, The Perfume Girl. Women." + AW,
  "grapefruit and plum leaf over jasmine, myrrh and tonka.", ["Floral", "Oriental", "Woody"], ["Floral", "Jasmine", "Oriental", "Citrus", "Woody"],
  name="Aromatics In Black", **PC)

# 3 Clinique Aromatics in White
t = "Clinique Aromatics in White Eau de Parfum 100ml"
F("0020714711740", "Clinique", t, "Women", "100", "45.49", "56.99", 5,
  [("Top", "Violet Leaves, Sichuan Pepper, Labdanum"), ("Heart", "Rose, Orange Blossom"), ("Base", "Amber, Benzoin, Musk")],
  "Floral · Spicy · Musky", "Luminous florals with a warm, ambery glow.",
  f"{t} is a radiant floral fragrance for women, launched in 2014. Violet leaves, Sichuan pepper and labdanum open with a fresh, gently spiced edge, a heart of rose and orange blossom follows, and it settles into a soft, warm base of amber, benzoin and musk.",
  ["A fresh violet leaf and Sichuan pepper opening", "A luminous rose and orange blossom heart", "A warm amber, benzoin and musk base", "Generous 100ml Eau de Parfum"],
  "EAN (GTIN 20714711740) matched on Galaxus (Aromatics in White EDP 100ml); 100ml EDP also on Boots IE and Harrods. Pyramid: top agreed by Osmoz, The Perfume Girl and Galaxus; heart rose + orange blossom agreed (patchouli only in 2 of 3, left out); base amber/benzoin/musk agreed by Osmoz and The Perfume Girl. 2014, perfumer Nicolas Beaulieu. Family varies by source (chypre floral / floral oriental): shown as Floral. Women." + AW,
  "violet leaves and pepper over rose, orange blossom and amber.", ["Floral", "Spicy", "Musky"], ["Floral", "Rose", "Spicy", "Oriental"],
  name="Aromatics in White", **PC)

# 4 Clinique Happy for Men Cologne -> needs-review (concentration)
t = "Clinique Happy for Men Cologne Spray 100ml"
F("0020714080310", "Clinique", t, "Men", "100", "31.49", "42.99", 5,
  [("Top", "Lime, Mandarin, Green Notes, Marine Notes"), ("Heart", "Freesia, Jasmine, Lily of the Valley, Rose"), ("Base", "Cedarwood, Cypress, Guaiac Wood, Musk")],
  "Citrus · Fresh · Aromatic", "A bright, upbeat citrus for every day.",
  f"{t} is Clinique's fresh citrus fragrance for men, launched in 1999. Zesty lime and mandarin with green and marine notes open bright and energising, a light floral heart of freesia, jasmine, lily of the valley and rose follows, and it dries down to cedarwood, cypress, guaiac wood and musk.",
  ["A zesty lime and mandarin opening", "Fresh green and marine notes", "A clean cedar, cypress and musk base", "Easy everyday freshness in a 100ml spray"],
  "NEEDS REVIEW: concentration. Supplier name says 'Cologne Spray Eau de Toilette', supplier form says Eau de Cologne. Clinique and UK retailers (Boots, Harrods, Lookfantastic) sell it as 'Happy For Men Cologne Spray' with no concentration; Carrefour UAE says Eau de Cologne; Kruidvat and Parfumo class it as EDT. Titled 'Cologne Spray', tagged Eau De Cologne – check the box. EAN match indirect: Carrefour UAE product code DJ20714080310 (Happy Cologne Spray for Men 100ml). Pyramid: Parfumo and Osmoz agree on every tier (Boots gives a different heart). 1999 per Parfumo, Osmoz. Men." + AW,
  "lime and mandarin over freesia, cedar and cypress.", ["Citrus", "Fresh", "Aromatic"], ["Citrus", "Fresh", "Floral", "Woody"],
  name="Happy for Men", conc="Eau De Cologne", concl="Cologne Spray", status="needs-review")

HAPPY = [("Top", "Grapefruit, Mandarin, Bergamot"), ("Heart", "Morning Dew Orchid"), ("Base", "Mimosa")]
HN = ("Pyramid: notes Clinique.com and CaFleureBon agree on (Hawaiian wedding flower left out: heart on Clinique, base on CaFleureBon). "
      "Clinique.com sells it as Eau de Parfum Spray (Clinique UK says 'Perfume Spray'). 1997 per ScentAdvice and CaFleureBon. Women.")
# 5 Clinique Happy EDP 100ml
t = "Clinique Happy Eau de Parfum 100ml"
F("0020714156893", "Clinique", t, "Women", "100", "30.49", "41.99", 5, HAPPY,
  "Citrus · Floral · Fruity", "Bright, sunny citrus that lifts your mood.",
  f"{t} is Clinique's iconic feel-good fragrance for women, launched in 1997. Juicy grapefruit, mandarin and bergamot open with a burst of sunshine, a soft morning dew orchid heart follows, and it settles on a delicate touch of mimosa.",
  ["A sparkling grapefruit, mandarin and bergamot opening", "A fresh morning dew orchid heart", "A soft mimosa finish", "Generous 100ml Eau de Parfum"],
  "EAN 0020714156893 matched on Kruidvat (Happy For Women EDP 100ml) and Cocooncenter UK (Happy Parfum Spray 100ml). " + HN + AW,
  "grapefruit and mandarin over orchid and mimosa.", ["Citrus", "Floral", "Fruity"], ["Citrus", "Floral", "Fruity", "Fresh"],
  name="Clinique Happy", **PC)

# 6 Clinique Happy EDP 50ml
t = "Clinique Happy Eau de Parfum 50ml"
F("0020714052959", "Clinique", t, "Women", "50", "25.49", "32.99", 5, HAPPY,
  "Citrus · Floral · Fruity", "Bright, sunny citrus that lifts your mood.",
  f"{t} is Clinique's iconic feel-good fragrance for women, launched in 1997. Juicy grapefruit, mandarin and bergamot open with a burst of sunshine, a soft morning dew orchid heart follows, and it settles on a delicate touch of mimosa.",
  ["A sparkling grapefruit, mandarin and bergamot opening", "A fresh morning dew orchid heart", "A soft mimosa finish", "Handy 50ml size"],
  "EAN 0020714052959 matched on Cocooncenter UK (Happy Perfume Spray 50ml) and Kruidvat (Happy For Women Parfum 50ml) – both say 'Perfume/Parfum spray'; Clinique.com sells 50ml as Eau de Parfum Spray, supplier says EDP. " + HN + AW,
  "grapefruit and mandarin over orchid and mimosa.", ["Citrus", "Floral", "Fruity"], ["Citrus", "Floral", "Fruity", "Fresh"],
  name="Clinique Happy", **PC)

# 7 Clinique Happy Heart EDP 50ml
t = "Clinique Happy Heart Eau de Parfum 50ml"
F("0020714170479", "Clinique", t, "Women", "50", "27.99", "35.99", 5,
  [("Top", "Mandarin, Cucumber"), ("Heart", "Water Hyacinth"), ("Base", "Blond Woods")],
  "Floral · Fresh · Woody", "A soft, fresh floral with a feel-good warmth.",
  f"{t} is a fresh floral fragrance for women, launched in 2003. Juicy mandarin and cool cucumber open crisp and refreshing, a delicate water hyacinth heart follows, and it settles on a soft, warm base of blond woods.",
  ["A crisp mandarin and cucumber opening", "A delicate water hyacinth heart", "A soft blond woods finish", "Handy 50ml Eau de Parfum"],
  "EAN 0020714170479 matched on Jomashop (Happy Heart Perfume Spray 50ml, code in URL) and eBay (UPC, Happy Heart EDP 1.7oz); supplier stockfile lists it with the newer code 0020714881436 (Kruidvat, Bluemercury). Clinique.com sells it as Eau de Parfum Spray. Pyramid: Clinique.com and Osmoz agree on mandarin, cucumber / water hyacinth / blond woods (Osmoz adds rose, sandalwood). 2003 per Osmoz and ScentAdvice. Women." + AW,
  "mandarin and cucumber over water hyacinth and blond woods.", ["Floral", "Fresh", "Woody"], ["Floral", "Fresh", "Citrus", "Woody"],
  name="Happy Heart", **PC)

# 8 Davidoff Cool Elixir gift set -> needs-review (EAN/contents only weakly confirmed)
t = "Davidoff Cool Elixir Parfum Intense 50ml Gift Set with 75ml Hair & Body Wash"
GS("3616306130777", "Davidoff", t, "Davidoff Cool Elixir Parfum Intense 50ml & Body Wash Set", "Men", "50", "39.49", "52.99", 5,
   [("Top", "Rose Oxide"), ("Heart", "Lavandin Absolute"), ("Base", "Oud Accord")],
   "Woody · Aromatic · Spicy", "Davidoff's intense new Cool Elixir, gift-ready.",
   f"{t} pairs Cool Elixir, Davidoff's intense woody fragrance for men launched in 2025, with a matching hair and body wash. Rose oxide opens with a cool, sparkling edge, a heart of lavandin absolute adds aromatic depth, and it settles into a rich, smooth oud accord.",
   ["Cool Elixir Parfum Intense 50ml (spray)", "Cool Elixir Hair & Body Wash 75ml"],
   ["A cool, sparkling rose oxide opening", "An aromatic lavandin absolute heart", "A rich, smooth oud accord base", "A ready-made gift with a 50ml spray"],
   "NEEDS REVIEW: EAN 3616306130777 only matched on Galaxus CH, which says 100ml EDP (contradicts supplier and others). Contents 50ml + 75ml wash from Cosmetify UK ('Cool Elixir Parfum Intense 50ml Gift Set') and Zalando DE (50ml + 75ml shower gel). Supplier form says Eau de Parfum; brand calls it Parfum, UK retailers (TJ Hughes, Cosmetify) 'Parfum Intense' – used Parfum Intense. Check box and contents. Pyramid agreed by brand site, Very, Parfumo, TJ Hughes. 2025 per Parfumo, TJ Hughes, Moodie Davitt. Men." + AW,
   "rose oxide and lavandin over a rich oud accord.", ["Woody", "Aromatic", "Spicy"], ["Woody", "Lavender", "Rose", "Spicy"],
   name="Cool Elixir", conc="Parfum Intense", concl="Parfum Intense", status="needs-review")

# 9 Davidoff Cool Water aftershave splash 125ml (not a spray)
t = "Davidoff Cool Water Aftershave Lotion 125ml"
pyr = [("Top", "Lavender, Mint"), ("Heart", "Geranium, Sandalwood"), ("Base", "Amber, Musk")]
add(cat_name="Fragrances", bc="3414202000664", title=t, vendor="Davidoff", type=TYPE["Men"], gender="Men", cat=TAXON["aftershave"],
    price="26.49", cmp="34.99", qty=5, tags=["Davidoff", "Men", "Aftershave"],
    seo=("Davidoff Cool Water Aftershave Lotion 125ml Splash",
         "Davidoff Cool Water Aftershave Lotion 125ml: the classic aromatic scent that soothes skin after shaving." + FREE),
    form="Aftershave Lotion (Splash)", size="125", unit="ml", gpc=GPC["fragrance"],
    mf={"age-group": ["Adults"], "product-form": ["Liquid"]},
    note="EAN 3414202000664 matched on Argos (Cool Water Splash Aftershave 125ml) and Galaxus (Cool Water aftershave lotion 125ml); Boots and Studio list the same 125ml after shave. Splash, not spray (Argos spec field says spray – ignored). Soothing/calming claim agreed by Boots, Studio, Galaxus. Pyramid is the Cool Water Man scent: notes Argos (aftershave page) and Parfumo agree on (oakmoss left out: tier differs). Category set to Aftershave (hb-3-14-1). 1988 (Cool Water Man). Men." + AW,
    desc=body("The iconic Cool Water scent in a cooling after-shave splash.",
              f"{t} brings the classic aromatic freshness of Cool Water, first launched in 1988, to your shaving routine. This splash lotion soothes and calms skin after shaving, leaving it lightly scented with lavender and mint, geranium and sandalwood, over warm amber and musk.",
              [("Scent pyramid", kd(pyr)),
               ("How to use", "<p>After shaving, pour a little into your hands and massage onto the face and neck.</p>")],
              [("Brand", "Davidoff"), ("Type", "Aftershave lotion (splash)"), ("Size", "125ml"),
               ("Scent profile", "Aromatic · Fresh · Aquatic"), ("Wear", "Men")],
              ["Soothes and calms skin after shaving", "The classic Cool Water scent", "Fresh lavender and mint over amber and musk", "Generous 125ml bottle"],
              [("What does Cool Water Aftershave smell like?", pyramid_answer(pyr)),
               ("Is it a spray?", "No, it is a splash lotion: pour a little into your hands and apply after shaving."),
               ("Is it for men?", "Yes, it is a men's aftershave.")]))

# 10 Davidoff Cool Water Reborn EDT 75ml
t = "Davidoff Cool Water Reborn Eau de Toilette 75ml"
F("3616302038794", "Davidoff", t, "Men", "75", "24.49", "31.99", 5,
  [("Top", "Rosemary"), ("Heart", "Galbanum"), ("Base", "Haitian Vetiver")],
  "Aromatic · Fougère · Woody", "A fresh, green rebirth of the Cool Water spirit.",
  f"{t} is a modern aromatic fougère for men, launched in 2022. Tunisian rosemary opens fresh and herbal, a green galbanum heart follows, and it settles into a clean, earthy base of Haitian vetiver.",
  ["A fresh, herbal rosemary opening", "A crisp green galbanum heart", "A clean Haitian vetiver base", "Versatile 75ml Eau de Toilette"],
  "EAN 3616302038794 matched on Superdrug (Cool Water For Men Reborn 75ml EDT) and Galaxus (Reborn EDT 75ml). Pyramid agreed by Superdrug, The Perfume Shop and Vivir (brand names rosemary and vetiver). 2022 per Vivir, TJ Hughes, FragranceNet (EDP is a separate 2023 release). Men." + AW,
  "rosemary over galbanum and Haitian vetiver.", ["Aromatic", "Fougere", "Woody", "Fresh"], ["Fresh", "Woody"],
  name="Cool Water Reborn", **TC)

write_outputs(".")
