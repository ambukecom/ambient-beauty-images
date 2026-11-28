import sys; sys.path.insert(0, "/home/claude/ambient-beauty-images/workflow")
from lib import *
TC = dict(conc="Eau De Toilette", concl="Eau de Toilette")
PC = dict(conc="Eau De Parfum", concl="Eau de Parfum")
XP = dict(conc="Parfum", concl="Parfum")
AW = " Awaiting photos."
RB = "Reebok"
RC = "Roberto Cavalli"

def GS(bc, vendor, title, seo_t, gender, size, price, cmp, qty, pyr, profile, hook, intro, contents, love, note, seo_d,
       of, fr, name, conc="Eau De Parfum", concl="Eau de Parfum", status="done", form_suffix=" Gift Set"):
    """Fragrance set: fragrance standard (3 tags) plus a 'What's in the set' block (as runs/2026-11-28-b1)."""
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

def seo_t(t):
    P[-1]["seo"] = (t, P[-1]["seo"][1].replace(P[-1]["title"] + ":", t + ":", 1))

# 1 Reebok Cool Your Body Women gift set
t = "Reebok Cool Your Body Eau de Toilette 100ml Gift Set with 150ml Body Spray"
GS("8436581946246", RB, t, "Reebok Cool Your Body EDT 100ml + Body Spray Gift Set", "Women", "100", "19.99", "27.99", 5,
   [("Top", "Peach, Pear, Grapefruit"), ("Heart", "Bamboo, Jasmine, Gardenia"), ("Base", "Sandalwood, Musk")],
   "Fruity · Floral", "Fresh, fruity and ready to go.",
   f"{t} pairs Reebok Cool Your Body for women with a matching body spray. It is a fruity floral fragrance: juicy peach, pear and grapefruit open bright and fresh, a heart of bamboo, jasmine and gardenia keeps it light and feminine, and it settles onto soft sandalwood and musk.",
   ["Reebok Cool Your Body Eau de Toilette 100ml (spray)", "Reebok Cool Your Body Body Spray 150ml"],
   ["A juicy peach, pear and grapefruit opening", "A fresh bamboo, jasmine and gardenia heart", "A soft sandalwood and musk base", "A matching body spray for an all-over refresh"],
   "EAN 8436581946246 matched on Superdrug (Cool Your Body Women Gift Set 100ml EDT + 150ml Body Spray; marked no longer available online) + Lily's Pharmacy (100ml EDT + 150ml deodorant spray). Pyramid agreed by Lily's Pharmacy, FragranceNet, McCabes Pharmacy. Fruity floral per Superdrug. 2022 per FragranceNet + Lily's (left out of copy). Women." + AW,
   "a 100ml spray with matching 150ml body spray.", ["Floral", "Fruity"], ["Fruity", "Floral", "Jasmine"],
   name="Reebok Cool Your Body", **TC)

# 2 Reebok Inspire Your Mind Woman gift set
t = "Reebok Inspire Your Mind Eau de Toilette 100ml Gift Set with 150ml Body Spray"
GS("8436581946253", RB, t, "Reebok Inspire Your Mind EDT 100ml + Body Spray Gift Set", "Women", "100", "20.99", "27.99", 5,
   [("Top", "Pear, Pistachio, Bergamot"), ("Heart", "Magnolia, Rose, Ylang-Ylang"), ("Base", "Vanilla, Patchouli, Musk")],
   "Floral · Fruity", "Soft florals with a creamy twist.",
   f"{t} pairs Reebok Inspire Your Mind for women with a matching body spray. It is a floral fragrance: pear, pistachio and bergamot open fresh and slightly creamy, a heart of magnolia, rose and ylang-ylang blooms soft and feminine, and it settles onto warm vanilla, patchouli and musk.",
   ["Reebok Inspire Your Mind Eau de Toilette 100ml (spray)", "Reebok Inspire Your Mind Body Spray 150ml"],
   ["A fresh pear, pistachio and bergamot opening", "A soft magnolia, rose and ylang-ylang heart", "A warm vanilla, patchouli and musk base", "A matching body spray for an all-over refresh"],
   "EAN 8436581946253 matched on Superdrug (Inspire Your Mind Woman Gift Set 100ml EDT + 150ml Body Spray), eBay UK and Klarna (EDT 100ml + deo spray 150ml). Pyramid agreed by Centrepoint + FragranceNet. Floral per Centrepoint + FragranceNet. Women." + AW,
   "a 100ml spray with matching 150ml body spray.", ["Floral", "Fruity"], ["Floral", "Rose", "Vanilla"],
   name="Reebok Inspire Your Mind", **TC)

# 3 Bloodiris
t = "Roberto Cavalli Bloodiris Eau de Parfum 100ml"
F("3616302038909", RC, t, "Unisex", "100", "74.99", "97.99", 5,
  [("Top", "Blood Orange"), ("Heart", "Iris, Turmeric"), ("Base", "Cashmeran, Musk")],
  "Floral · Citrus", "Golden iris with a bright citrus glow.",
  f"{t} is part of the Roberto Cavalli Gold Collection. Sparkling blood orange opens bright and juicy, a heart of iris and turmeric brings a warm, golden, gently spicy floral, and it settles onto soft cashmeran and musk. A refined unisex scent with a luxurious feel.",
  ["A bright blood orange opening", "A warm iris and turmeric heart", "A soft cashmeran and musk base", "Part of the Roberto Cavalli Gold Collection"],
  "EAN 3616302038909 matched on Superdrug (Gold Collection Bloodiris 100ml EDP, unisex) + Jomashop. Pyramid agreed by Now Smell This (launch) + FragranceNet. Floral (iris-led) per Superdrug 'oriental floral'. 2022; perfumer single-source – left out. Unisex." + AW,
  "blood orange over iris, turmeric and cashmeran.", ["Floral", "Powdery"], ["Floral", "Citrus"],
  name="Bloodiris", **PC)

# 4 Divine Oud Intense (no confirmed pyramid)
t = "Roberto Cavalli Divine Oud Eau de Parfum Intense 100ml"
F("3616303470654", RC, t, "Unisex", "100", "74.99", "94.99", 5, [],
  "Woody · Oud", "Deep, rich oud with Cavalli glamour.",
  f"{t} is the intense edition of Divine Oud from the Roberto Cavalli Gold Collection. It is a rich, woody oud fragrance made for everyone, with a deep, long-lasting character for evenings and special occasions.",
  ["A rich, woody oud character", "Intense Eau de Parfum strength", "Part of the Roberto Cavalli Gold Collection", "Generous 100ml bottle"],
  "NEEDS REVIEW: scent pyramid not confirmed – the two sources tied to this EAN (Pariscom2030, Elryan) disagree on every tier, so no notes are shown. EAN 3616303470654 matched on eBay ('Unisex Gold Collection Divine Oud Intense EDP 3.4 oz'), Pariscom2030 + Shams ('Divine Oud Intense 100ml'); Jomashop / Elryan call it just 'Divine Oud EDP' (original Divine Oud has a different EAN 3614221031377, so this is the Intense). Woody per Interparfums / Pariscom2030. Unisex (some US retailers list the original as women's)." + AW,
  "a rich, woody unisex oud.", ["Woody", "Oriental"], ["Woody", "Oriental"],
  name="Divine Oud Intense", status="needs-review", **PC)
seo_t("Roberto Cavalli Divine Oud EDP Intense 100ml")

# 5 Just Cavalli for her 90ml
t = "Roberto Cavalli Just Cavalli Eau de Toilette 90ml"
F("8052464899104", RC, t, "Women", "90", "29.49", "38.99", 5,
  [("Top", "Neroli"), ("Heart", "Tiare Flower"), ("Base", "Rosewood")],
  "Floral · Woody", "Sensual florals with a playful edge.",
  f"{t} is the women's Just Cavalli. Fresh neroli opens bright and luminous, a heart of exotic tiare flower brings a creamy, sensual floral, and it settles onto smooth rosewood. A feminine, easy-to-wear scent for every day.",
  ["A bright neroli opening", "A creamy tiare flower heart", "A smooth rosewood base", "Generous 90ml Eau de Toilette"],
  "EAN 8052464899104 matched on Superdrug ('Just Women 90ml EDT'), Interparfums ('Just Her EDT 90ml') + Galaxus. Pyramid agreed by robertocavalli.com, Escentual, Parfumo, Nahdi (Superdrug's page for this EAN lists a different cinnamon/coffee pyramid – no other source supports it, ignored). Floral per Escentual + Parfumo. Women." + AW,
  "neroli and tiare flower over rosewood.", ["Floral", "Woody"], ["Floral", "Citrus", "Woody"],
  name="Just Cavalli", **TC)

# 6 Magnetic Guaiac
t = "Roberto Cavalli Magnetic Guaiac Eau de Parfum 100ml"
F("3616302038961", RC, t, "Unisex", "100", "74.99", "97.99", 5,
  [("Top", "Bergamot"), ("Heart", "Geranium"), ("Base", "Guaiac Wood, Animal Fur Accord")],
  "Woody · Spicy", "Smoky woods with magnetic warmth.",
  f"{t} is part of the Roberto Cavalli Gold Collection. Bright bergamot opens fresh, a heart of geranium adds an aromatic floral edge, and it settles onto smoky guaiac wood and a soft animal fur accord. A bold, warm unisex woody scent.",
  ["A fresh bergamot opening", "An aromatic geranium heart", "A smoky guaiac wood base", "Part of the Roberto Cavalli Gold Collection"],
  "EAN 3616302038961 matched on Superdrug (Magnetic Guaiac EDP 100ml) + Jomashop (unisex EDP 3.4oz). Pyramid agreed by Superdrug + Now Smell This. Spicy woody per Superdrug. Unisex per NST + Jomashop (Superdrug files it under women's but calls it unisex). A few Middle East sites say 'Parfum' – EDP per majority." + AW,
  "bergamot and geranium over smoky guaiac wood.", ["Woody", "Spicy"], ["Woody", "Spicy", "Citrus"],
  name="Magnetic Guaiac", **PC)

# 7/8 Paradiso Assoluto 100ml + 75ml
PA = [("Top", "Wisteria, Pink Pepper, Grapefruit, Bergamot, Lemon"), ("Heart", "Jasmine, Red Lily, Passionfruit"),
      ("Base", "Vanilla, Cashmeran, Sandalwood, Patchouli")]
for bc, size, price, cmp, qty, src in [
    ("3616303445232", "100", "38.49", "48.99", 4, "EAN 3616303445232 matched on Timestore.it + Bol.com (Paradiso Assoluto EDP 100ml, women). Pyramid agreed by Timestore, Superdrug and TJ Hughes."),
    ("8052464896868", "75", "35.99", "48.99", 4, "EAN 8052464896868 matched on Interparfums (brand licensee: Paradiso Assoluto EDP 75ml) + Rossmann.de (EdP 75ml); the same 75ml also sells under older EAN 3614222793496 – packaging may differ. Pyramid agreed by Superdrug, TJ Hughes, Timestore (Rossmann + Parfumo list the core notes, all included).")]:
    t = f"Roberto Cavalli Paradiso Assoluto Eau de Parfum {size}ml"
    F(bc, RC, t, "Women", size, price, cmp, qty, PA,
      "Floral · Chypre", "A sensual floral paradise.",
      f"{t} is a sensual floral fragrance for women. Wisteria, pink pepper and sparkling citrus open bright and lively, a heart of jasmine, red lily and passionfruit blooms rich and feminine, and it settles onto vanilla, cashmeran, sandalwood and patchouli.",
      ["A bright wisteria, pink pepper and citrus opening", "A lush jasmine, red lily and passionfruit heart", "A warm vanilla, sandalwood and patchouli base", f"{size}ml Eau de Parfum"],
      src + " Floral per Timestore + Superdrug (Bol says fruity). 2016; perfumer single-source – left out. Women." + AW,
      "wisteria and jasmine over vanilla and sandalwood.", ["Floral"], ["Floral", "Jasmine", "Vanilla"],
      name="Paradiso Assoluto", **PC)

# 9 Royal Soul – listed as Parfum (needs-review)
t = "Roberto Cavalli Royal Soul Parfum 100ml"
F("3616304668722", RC, t, "Unisex", "100", "74.99", "100.99", 5,
  [("Top", "Bergamot, Jasmine, Pink Pepper"), ("Heart", "Rose, Patchouli, Sandalwood"), ("Base", "Vanilla, Musk, Amber")],
  "Oriental · Floral", "Regal warmth with a floral glow.",
  f"{t} is part of the Roberto Cavalli Gold Collection. Bergamot, jasmine and pink pepper open bright and spicy, a heart of rose, patchouli and sandalwood brings depth and richness, and it settles onto warm vanilla, musk and amber. A luxurious amber floral made for everyone.",
  ["A bright bergamot, jasmine and pink pepper opening", "A rich rose, patchouli and sandalwood heart", "A warm vanilla, musk and amber base", "Part of the Roberto Cavalli Gold Collection"],
  "NEEDS REVIEW: concentration. Supplier says Eau de Parfum, but every page showing EAN 3616304668722 (Elryan; Modesens, Essenzi, Trycho-medica titles) calls it Parfum – listed as Parfum; please check the box. Only MyPerfumeShop (no EAN, tester) says EDP. Pyramid agreed by Elryan + MyPerfumeShop (cedarwood/oud on Scentadvice only – left out). Amber floral per Elryan + MyPerfumeShop. Unisex." + AW,
  "bergamot and rose over vanilla, musk and amber.", ["Oriental", "Floral"], ["Oriental", "Rose", "Vanilla"],
  name="Royal Soul", status="needs-review", **XP)

# 10 Signature Verde Assoluto 75ml
t = "Roberto Cavalli Signature Verde Assoluto Eau de Parfum 75ml"
F("8056860214660", RC, t, "Unisex", "75", "35.99", "46.99", 4,
  [("Top", "Bergamot, Pink Pepper, Mandarin"), ("Heart", "Honeysuckle, Tuberose, Gardenia"), ("Base", "Cedarwood, Amberwood, Sandalwood, Praline")],
  "Floral · Woody", "Lush white florals on a creamy woody base.",
  f"{t} is a woody floral fragrance. Bergamot, pink pepper and mandarin open fresh and sparkling, a heart of honeysuckle, tuberose and gardenia blooms creamy and radiant, and it settles onto cedarwood, amberwood, sandalwood and a touch of sweet praline.",
  ["A sparkling bergamot, pink pepper and mandarin opening", "A creamy honeysuckle, tuberose and gardenia heart", "A warm cedarwood, sandalwood and praline base", "75ml Eau de Parfum"],
  "EAN 8056860214660 matched on Glam4u.gr (Signature Verde Assoluto EDP 75ml). Pyramid agreed by Glam4u, Escentual, Parfumo. Woody floral per Escentual + Glam4u. Gender kept as supplier (Unisex), but retailers (Glam4u, Escentual, Parfumo, Notino) market it for women. Not the men's Uomo Verde Assoluto." + AW,
  "white florals over cedarwood, sandalwood and praline.", ["Floral", "Woody"], ["Floral", "Woody", "Sandalwood"],
  name="Verde Assoluto", **PC)
seo_t("Roberto Cavalli Signature Verde Assoluto EDP 75ml")

write_outputs()
