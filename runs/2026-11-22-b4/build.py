import sys; sys.path.insert(0, "/home/claude/ambient-beauty-images/workflow")
from lib import *
PC = dict(conc="Eau De Parfum", concl="Eau de Parfum")
TC = dict(conc="Eau De Toilette", concl="Eau de Toilette")
AW = " Awaiting photos."
PLAN = " Planned 20/11 run 2 (that run never ran); drafted 22/11 run 4."

def GS(bc, vendor, title, seo_t, gender, size, price, cmp, qty, pyr, profile, hook, intro, contents, love, note, seo_d,
       of, fr, name, conc="Eau De Parfum", concl="Eau de Parfum", status="done", form_suffix=" Gift Set", extra=()):
    """Fragrance set: fragrance standard (3 tags) plus a 'What's in the set' block (same as 2026-11-22-b2)."""
    q2 = {"Men": ("Is it for men?", "Yes, it is a men's fragrance gift set."),
          "Women": ("Is it for women?", "Yes, it is a women's fragrance gift set."),
          "Unisex": ("Is it unisex?", "Yes, it is made for everyone.")}[gender]
    qs = ([(f"What does {name} smell like?", pyramid_answer(pyr))] if pyr else []) + [("What's in the set?", "; ".join(contents) + "."), q2]
    blocks = [("What's in the set", ul(contents))] + ([("Scent pyramid", kd(pyr))] if pyr else []) + list(extra)
    add(cat_name="Fragrances", bc=bc, title=title, vendor=vendor, type=TYPE[gender], gender=gender, cat=TAXON["perfume"],
        price=price, cmp=cmp, qty=qty, tags=[vendor, gender, conc], seo=(seo_t, f"{seo_t}: {seo_d}" + FREE), status=status,
        form=concl + form_suffix, size=size, unit="ml", note=note + PLAN, gpc=GPC["fragrance"],
        mf={"age-group": ["Adults"], "product-form": ["Spray"], "dispenser-type": ["Spray"], "olfactory-family": list(of), "fragrance": list(fr)},
        desc=body(hook, intro, blocks,
                  [("Brand", vendor), ("Concentration", concl), ("Contents", " + ".join(c.split(" (")[0] for c in contents)),
                   ("Scent profile", profile), ("Wear", gender)], love, qs))

# 1 Burberry Hero EDT refill (not a spray: refill bottle)
t = "Burberry Hero Eau de Toilette 200ml Refill"
pyr = [("Top", "Bergamot"), ("Heart", "Cedarwood"), ("Base", "Black Pepper, Juniper")]
add(cat_name="Fragrances", bc="3616304679483", title=t, vendor="Burberry", type=TYPE["Men"], gender="Men", cat=TAXON["perfume"],
    price="52.99", cmp="71.99", qty=2, tags=["Burberry", "Men", "Eau De Toilette"],
    seo=("Burberry Hero Eau de Toilette 200ml Refill",
         "Burberry Hero Eau de Toilette 200ml Refill: juniper, black pepper, bergamot and cedarwood." + FREE),
    form="Eau de Toilette Refill", size="200", unit="ml", gpc=GPC["fragrance"],
    mf={"age-group": ["Adults"], "product-form": ["Liquid"],
        "olfactory-family": ["Woody", "Aromatic", "Spicy", "Fresh"], "fragrance": ["Woody", "Citrus", "Spicy", "Fresh"]},
    note="EDT 200ml refill confirmed by Boots, John Lewis, Harrods and Escentual (separate from the EDP and Parfum refills); refills the 100ml Hero EDT bottle only (Boots, John Lewis, Escentual). EAN 3616304679483 appears in Escentual's image file name for this refill (no labelled EAN found). Pyramid tiers as Boots, Harrods and Escentual; John Lewis puts juniper/pepper at the top – check. 2021. Men." + AW + PLAN,
    desc=body("Top up your Hero bottle with this 200ml refill of juniper, black pepper and cedarwood.",
              f"{t} refills your 100ml Burberry Hero Eau de Toilette bottle. Hero is a woody aromatic fragrance for men: bright bergamot opens onto a trio of cedarwood, with juniper and black pepper adding a crisp, spicy edge. The refill is not a spray and cannot be used on its own.",
              [("Scent pyramid", kd(pyr)),
               ("How to refill", ul(["Remove the cap and unscrew the pump from your Hero 100ml bottle.",
                                     "Without opening the refill's cap, screw the refill onto the bottle neck; filling stops when the bottle is full.",
                                     "Unscrew the refill, then put the pump and cap back on."]))],
              [("Brand", "Burberry"), ("Concentration", "Eau de Toilette"), ("Size", "200ml refill"),
               ("Fits", "Burberry Hero Eau de Toilette 100ml bottle"), ("Scent profile", "Woody · Aromatic · Spicy"), ("Wear", "Men")],
              ["Refills your Hero bottle with less packaging", "A bright bergamot opening", "A signature trio of cedarwood", "Juniper and black pepper for a crisp, spicy edge"],
              [("What does Hero smell like?", pyramid_answer(pyr)),
               ("Can I spray it straight from the refill?", "No, it is a refill bottle for the Burberry Hero Eau de Toilette 100ml bottle and cannot be used on its own."),
               ("Is it for men?", "Yes, it is a men's fragrance.")]))

# 2 Bvlgari Man Rain Essence set
t = "Bvlgari Man Rain Essence Eau de Parfum 100ml Gift Set with 15ml Eau de Parfum"
GS("0783320421211", "Bvlgari", t, "Bvlgari Man Rain Essence EDP 100ml & 15ml Gift Set", "Men", "100", "59.49", "75.99", 5,
   [("Top", "Green Tea, Orange"), ("Heart", "White Lotus, Crystal Musk"), ("Base", "Mineral Amber, Guaiac Wood")],
   "Fresh · Woody · Musky", "Fresh green tea and white lotus over mineral amber, with a travel spray to take along.",
   f"{t} pairs Bvlgari Man Rain Essence in the full 100ml size with a 15ml travel spray. Created by Alberto Morillas, this fresh woody musk opens with green tea and orange, white lotus and crystal musk form a clean, airy heart, and it settles on mineral amber and guaiac wood.",
   ["Bvlgari Man Rain Essence Eau de Parfum 100ml (spray)", "Bvlgari Man Rain Essence Eau de Parfum 15ml (travel spray)"],
   ["A fresh green tea and orange opening", "A clean white lotus and crystal musk heart", "A mineral amber and guaiac wood base", "15ml travel spray included"],
   "NEEDS REVIEW: barcode. Contents (EDP 100ml + EDP 15ml) agreed by Superdrug, Lookfantastic and Harrods, but EAN 0783320421211 (and supplier's 0783320422331 / 0783320423451) not found anywhere – check the box. Pyramid identical on Harrods and Dillard's (Parfumo/NST same notes). 2023, Alberto Morillas (NST, Parfumo). Men." + AW,
   "green tea and white lotus over amber, with 15ml spray.", ["Fresh", "Woody", "Musky", "Citrus"], ["Fresh", "Citrus", "Floral", "Woody"],
   name="Man Rain Essence", status="needs-review", **PC)

# 3 Bvlgari Rose Goldea Blossom Delight set
t = "Bvlgari Rose Goldea Blossom Delight Eau de Parfum 50ml Gift Set with 75ml Body Milk"
GS("0783320422393", "Bvlgari", t, "Bvlgari Rose Goldea Blossom Delight EDP 50ml Gift Set", "Women", "50", "57.99", "77.99", 3,
   [("Top", "Violet Leaf, Papaya, Jasmine"), ("Heart", "Rose Petal, Rosebud, Lily of the Valley"), ("Base", "White Musk, Ambergris, Bulgarian Rose")],
   "Floral · Rose · Musky", "Fresh rose petals and juicy papaya on a soft white musk, with a matching body milk.",
   f"{t} brings together Rose Goldea Blossom Delight Eau de Parfum and a 75ml body milk. Created by Alberto Morillas, this floral rose musk opens with green violet leaf, papaya and jasmine, rose petals, rosebud and lily of the valley bloom in the heart, and it settles on white musk, ambergris and Bulgarian rose.",
   ["Bvlgari Rose Goldea Blossom Delight Eau de Parfum 50ml (spray)", "Bvlgari Rose Goldea Blossom Delight Body Milk 75ml"],
   ["A fresh violet leaf, papaya and jasmine opening", "A bright rose and lily of the valley heart", "A soft white musk and ambergris base", "Matching body milk included"],
   "NEEDS REVIEW: barcode/edition. Contents (EDP 50ml + body milk 75ml) agreed by Superdrug and MyPerfumeShop, but EAN 0783320422393 (and 0783320423413) not confirmed (0783320423413 only in a MyPerfumeShop image name). Other editions exist (50ml + 15ml + hand cream; 75ml + 15ml; 75ml + 200ml body milk) – check the box. Pyramid agreed by Parfumo and John Lewis (Bulgari.com/Harrods give violet leaf, papaya, rose, white musk, ambergris). Alberto Morillas. Women." + AW,
   "violet leaf and papaya over rose and white musk, with body milk.", ["Floral", "Fruity", "Musky"], ["Rose", "Floral", "Fruity", "Jasmine"],
   name="Rose Goldea Blossom Delight", status="needs-review", **PC)

# 4 Cacharel Anais Anais set
t = "Cacharel Anaïs Anaïs L'Original Eau de Toilette 100ml Gift Set with 2 x 50ml Body Lotion"
GS("3614273843195", "Cacharel", t, "Cacharel Anaïs Anaïs EDT 100ml & Body Lotion Gift Set", "Women", "100", "45.49", "60.99", 5,
   [("Top", "Bergamot, Hyacinth, Orange Blossom"), ("Heart", "Lily, Jasmine, Rose"), ("Base", "Sandalwood, Amber, Musk")],
   "Floral · Soft · Powdery", "The timeless white-flower classic, with two matching body lotions.",
   f"{t} brings together Cacharel's first women's fragrance, launched in 1978, with two 50ml body lotions. Bergamot, hyacinth and orange blossom open fresh and green, a soft bouquet of lily, jasmine and rose forms the heart, and it settles on sandalwood, amber and musk.",
   ["Cacharel Anaïs Anaïs L'Original Eau de Toilette 100ml (spray)", "Cacharel Anaïs Anaïs Body Lotion 50ml", "Cacharel Anaïs Anaïs Body Lotion 50ml"],
   ["A fresh bergamot, hyacinth and orange blossom opening", "A soft lily, jasmine and rose heart", "A warm sandalwood, amber and musk base", "Two matching body lotions included"],
   "NEEDS REVIEW: barcode. Contents (EDT 100ml + 2 x 50ml body lotion) agreed by Fragrance London, Rackhams, Lily's Pharmacy and Tendance Parfums, but neither 3614273843195 nor 3614274091007 was found online – check the box. Pyramid: only notes agreed by two or more of Parfumo, Fragrance London, Lily's, Rackhams, Tendance, The Perfume Shop (orange blossom is heart on Parfumo). 1978 scent. Not the 30ml + 50ml lotion set. Women." + AW,
   "hyacinth and lily over sandalwood and musk, with 2 lotions.", ["Floral", "Powdery", "Fresh"], ["Floral", "Jasmine", "Rose", "Sandalwood"],
   name="Anaïs Anaïs", status="needs-review", **TC)

# 5 Cacharel Ella Ella EDP 100ml
t = "Cacharel Ella Ella Eau de Parfum 100ml"
F("3614274026511", "Cacharel", t, "Women", "100", "46.49", "61.99", 5,
  [("Top", "Coconut, Bergamot"), ("Heart", "Jasmine, Orange Blossom"), ("Base", "Patchouli, Bourbon Vanilla")],
  "Floral · Gourmand · Chypre", "Sunny coconut and jasmine over warm vanilla and patchouli.",
  f"{t} is a floral gourmand chypre for women by perfumer Dominique Ropion, and Cacharel's first refillable Eau de Parfum. Creamy coconut and bergamot open bright and sunny, jasmine and orange blossom form a radiant floral heart, and it settles into patchouli and Bourbon vanilla.",
  ["A creamy coconut and bergamot opening", "A radiant jasmine and orange blossom heart", "A warm patchouli and vanilla base", "Refillable 100ml bottle"],
  "EAN 3614274026511 labelled on Kruidvat (EDP 100ml) and used as Cosma's image name; 100ml EDP confirmed by Notino UK, TJ Hughes and Lyko. Refillable bottle per Sephora FR/Notino (separate refill is EAN 3614274026672). Pyramid agreed by Parfumo, Notino UK, TJ Hughes, Cosma and Walmart. 2025, Dominique Ropion. Women." + AW + PLAN,
  "coconut and jasmine over vanilla and patchouli.", ["Floral", "Gourmand", "Fruity"], ["Floral", "Jasmine", "Vanilla", "Citrus"],
  name="Ella Ella", **PC)

# 6 Calvin Klein Obsession for Men set
t = "Calvin Klein Obsession for Men Eau de Toilette 125ml Gift Set with Aftershave Balm and Deodorant Stick"
GS("3616303455309", "Calvin Klein", t, "Calvin Klein Obsession for Men EDT 125ml 3-Piece Gift Set", "Men", "125", "42.49", "55.99", 5,
   [("Top", "Mandarin, Bergamot"), ("Heart", "Myrrh, Nutmeg, Sage, Jasmine"), ("Base", "Amber, Vetiver, Patchouli, Vanilla")],
   "Oriental · Spicy · Woody", "The 1986 icon: warm spice and amber, with a balm and deodorant to match.",
   f"{t} brings together the classic Obsession for Men Eau de Toilette with a 75ml aftershave balm and a 75g deodorant stick. Mandarin and bergamot open with a bright citrus lift, myrrh, nutmeg, sage and jasmine form a warm spicy heart, and it settles into amber, vetiver, patchouli and vanilla.",
   ["Calvin Klein Obsession for Men Eau de Toilette 125ml (spray)", "Calvin Klein Obsession for Men Aftershave Balm 75ml", "Calvin Klein Obsession for Men Deodorant Stick 75g"],
   ["A bright mandarin and bergamot opening", "A warm myrrh, nutmeg and sage heart", "A rich amber, vetiver and vanilla base", "Aftershave balm and deodorant stick included"],
   "EAN 3616303455309 matched on Superdrug (exactly EDT 125ml + aftershave balm 75ml + deodorant stick 75g; no longer online); contents also confirmed by TJ Hughes and Tesco. Pyramid: only notes agreed by two or more of TJ Hughes, Flannels, The Perfume Shop, Osmoz (lavender/coriander tier disputed, left out). 1986 scent. Other editions have shower gel or 100ml balm – not this one. Men." + AW,
   "mandarin and myrrh over amber and vanilla, 3 pieces.", ["Oriental", "Spicy", "Woody"], ["Oriental", "Spicy", "Citrus", "Vanilla", "Woody"],
   name="Obsession for Men", **TC)

# 7 Carolina Herrera 212 Heroes for Her set
t = "Carolina Herrera 212 Heroes Forever Young for Her Eau de Parfum 80ml Gift Set with 100ml Body Lotion"
GS("8411061074855", "Carolina Herrera", t, "Carolina Herrera 212 Heroes for Her EDP 80ml Gift Set", "Women", "80", "68.99", "91.99", 4,
   [("Top", "Raspberry, Mandarin"), ("Heart", "Jasmine, Orange Blossom"), ("Base", "Cedarwood, Sandalwood")],
   "Floral · Fruity · Woody", "Juicy raspberry and jasmine over soft woods, with a matching body lotion.",
   f"{t} pairs 212 Heroes for Her Eau de Parfum with a 100ml body lotion. This floral fruity woody fragrance opens with juicy raspberry and mandarin, jasmine and orange blossom form a bright floral heart, and it settles on cedarwood and sandalwood.",
   ["Carolina Herrera 212 Heroes for Her Eau de Parfum 80ml (spray)", "Carolina Herrera 212 Heroes for Her Body Lotion 100ml"],
   ["A juicy raspberry and mandarin opening", "A bright jasmine and orange blossom heart", "A smooth cedarwood and sandalwood base", "Matching body lotion included"],
   "Contents (EDP 80ml + body lotion 100ml) agreed by Galaxus (GTIN 8411061101865 = supplier's second barcode), Cosmetify, deonlinedrogist.nl and designeroptics. EAN 8411061074855 not found. Fragrance is officially '212 Heroes for Her'; 'Forever Young' is the retailer set name (Cosmetify) – kept to match the supplier. Pyramid identical on carolinaherrera.com, Cosmetify, deonlinedrogist and Ascot. 2022. Women." + AW,
   "raspberry and jasmine over cedar and sandalwood, with lotion.", ["Floral", "Fruity", "Woody"], ["Fruity", "Floral", "Jasmine", "Woody", "Sandalwood"],
   name="212 Heroes for Her", **PC)

# 8 Carolina Herrera Bad Boy Cobalt set
t = "Carolina Herrera Bad Boy Cobalt Eau de Parfum Électrique 100ml Gift Set with 100ml Shower Gel"
GS("8411061027981", "Carolina Herrera", t, "Carolina Herrera Bad Boy Cobalt EDP 100ml Gift Set", "Men", "100", "82.49", "103.99", 4,
   [("Top", "Pink Pepper, Lavender"), ("Heart", "Geranium, Black Plum"), ("Base", "Truffle Accord, Vetiver")],
   "Aromatic · Woody · Fruity", "Electric pink pepper and lavender over dark plum and vetiver, with a shower gel to match.",
   f"{t} pairs Bad Boy Cobalt Eau de Parfum Électrique with a 100ml shower gel. Pink pepper and lavender open with an electric, aromatic spark, geranium and black plum form a dark fruity heart, and it settles on a truffle accord and vetiver.",
   ["Carolina Herrera Bad Boy Cobalt Eau de Parfum Électrique 100ml (spray)", "Carolina Herrera Bad Boy Cobalt Shower Gel 100ml"],
   ["An electric pink pepper and lavender opening", "A dark geranium and black plum heart", "A deep truffle and vetiver base", "Matching shower gel included"],
   "NEEDS REVIEW: barcode/edition. Contents (EDP 100ml + shower gel 100ml) confirmed by carolinaherrera.com set page and SecretSales (as Électrique), but neither 8411061027981 nor 8411061092521 found online; other Cobalt sets exist (50ml EDP + gel, 100ml + 10ml + gel, Absolute, Elixir) – check the box says Électrique. Pyramid as brand pyramid, agreed by SecretSales and TJ Hughes (cedar/oak on retailers only, left out). 2022. Men." + AW,
   "pink pepper and plum over truffle and vetiver, with gel.", ["Aromatic", "Woody", "Fruity", "Spicy"], ["Spicy", "Lavender", "Fruity", "Woody"],
   name="Bad Boy Cobalt", status="needs-review", **PC)

# 9 Cerruti 1881 Pour Homme set
t = "Cerruti 1881 Pour Homme Eau de Toilette 100ml Gift Set with 150ml Deodorant Spray"
GS("5050456007387", "Cerruti", t, "Cerruti 1881 Pour Homme EDT 100ml & Deodorant Gift Set", "Men", "100", "48.99", "65.99", 5,
   [("Top", "Juniper, Lavender, Galbanum"), ("Heart", "Vetiver, Ylang-Ylang, Cassia"), ("Base", "Oakmoss, Sandalwood, Patchouli")],
   "Woody · Aromatic · Green", "The 1990 classic: fresh lavender and juniper over oakmoss and sandalwood.",
   f"{t} brings together Cerruti 1881 Pour Homme Eau de Toilette with a matching 150ml deodorant spray. Juniper, lavender and green galbanum open fresh and aromatic, vetiver, ylang-ylang and cassia form the heart, and it settles on oakmoss, sandalwood and patchouli.",
   ["Cerruti 1881 Pour Homme Eau de Toilette 100ml (spray)", "Cerruti 1881 Pour Homme Deodorant Spray 150ml"],
   ["A fresh juniper, lavender and galbanum opening", "An aromatic vetiver and cassia heart", "A classic oakmoss, sandalwood and patchouli base", "Matching deodorant spray included"],
   "Contents (EDT 100ml + deodorant spray 150ml) agreed by Tendance Parfums, Lily's Pharmacy, gifts.ie, Tesco, MyPerfumeShop and Cosmetify. Supplier's second barcode 5050456009404 appears in Cosma's image name; 5050456007387 not found. Pyramid agreed by Lily's Pharmacy and The Perfume Shop (other sources vary). 1990 scent. Men." + AW,
   "lavender and juniper over oakmoss and sandalwood, with deo.", ["Woody", "Aromatic", "Fresh"], ["Lavender", "Woody", "Sandalwood", "Fresh"],
   name="Cerruti 1881 Pour Homme", **TC)

# 10 Cerruti 1881 Pour Femme set
t = "Cerruti 1881 Pour Femme Eau de Toilette 50ml Gift Set with 75ml Body Lotion"
GS("5050456005680", "Cerruti", t, "Cerruti 1881 Pour Femme EDT 50ml & Body Lotion Gift Set", "Women", "50", "34.99", "43.99", 5,
   [("Top", "Rose, Iris, Lily of the Valley"), ("Heart", "Tuberose, Orange Blossom, Jasmine"), ("Base", "Amber, Sandalwood, Vanilla")],
   "Floral · Woody · Soft", "A soft floral bouquet over sandalwood and vanilla, with a matching body lotion.",
   f"{t} brings together Cerruti 1881 Pour Femme Eau de Toilette with a 75ml perfumed body lotion. Rose, iris and lily of the valley open soft and fresh, tuberose, orange blossom and jasmine form a white-floral heart, and it settles on amber, sandalwood and vanilla.",
   ["Cerruti 1881 Pour Femme Eau de Toilette 50ml (spray)", "Cerruti 1881 Pour Femme Body Lotion 75ml"],
   ["A soft rose, iris and lily of the valley opening", "A white-floral tuberose and jasmine heart", "A warm amber, sandalwood and vanilla base", "Matching body lotion included"],
   "Contents (EDT 50ml + body lotion 75ml) agreed by Cosma, Tendance Parfums, McCabes, Tesco and Cosmetify; Cosma lists supplier's second barcode 5050456007394 as SKU for this set (5050456005680 itself not found). Pyramid agreed by Cosma and The Perfume Shop (other sources vary widely). 1995 (Osmoz). Women." + AW,
   "rose and tuberose over sandalwood and vanilla, with lotion.", ["Floral", "Woody"], ["Floral", "Rose", "Jasmine", "Sandalwood", "Vanilla"],
   name="Cerruti 1881 Pour Femme", **TC)

write_outputs()
