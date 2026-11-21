import sys; sys.path.insert(0, "/home/claude/ambient-beauty-images/workflow")
from lib import *
TC = dict(conc="Eau De Toilette", concl="Eau de Toilette")
PC = dict(conc="Eau De Parfum", concl="Eau de Parfum")

def GS(bc, vendor, title, seo_t, gender, size, price, cmp, qty, pyr, profile, hook, intro, contents, love, note, seo_d,
       of, fr, name, conc="Eau De Toilette", concl="Eau de Toilette", status="done"):
    """Fragrance gift set: fragrance standard (3 tags) plus a 'What's in the set' block."""
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

DG = "Dolce & Gabbana"

def MSET(bc, vendor, title, seo_t, gender, price, cmp, qty, scents, of, fr, profile, hook, intro, love, note, size="20", status="done"):
    """Multi-scent fragrance set (no single pyramid): 'What's in the set' block with per-scent notes."""
    names = [n for n, _ in scents]
    lst = ", ".join(names[:-1]) + " and " + names[-1]
    add(cat_name="Fragrances", bc=bc, title=title, vendor=vendor, type=TYPE[gender], gender=gender, cat=TAXON["perfume"],
        price=price, cmp=cmp, qty=qty, form="Eau de Toilette Gift Set", size=size, unit="ml", gpc=GPC["fragrance"],
        tags=[vendor, gender, "Eau De Toilette"], status=status, note=note,
        seo=(seo_t, f"{seo_t}: {lst}, four 20ml EDT sprays."[:133] + FREE),
        mf={"age-group": ["Adults"], "product-form": ["Spray"], "dispenser-type": ["Spray"], "olfactory-family": of, "fragrance": fr},
        desc=body(hook, intro, [("What's in the set", ul([f"<strong>{n}</strong> – {d}" for n, d in scents]))],
                  [("Brand", vendor), ("Concentration", "Eau de Toilette"), ("Contents", "4 x 20ml"), ("Scent profile", profile), ("Wear", gender)],
                  love, [("Which fragrances are in the set?", f"{lst}, each a 20ml Eau de Toilette spray."), ("Is it for men?", "Yes, it is a men's fragrance gift set.")]))

# ---------------- Hugo Boss The Scent for Her 30ml set
t = "Hugo Boss The Scent for Her Eau de Parfum 30ml Gift Set with 50ml Body Lotion"
GS("3616304197994", "Hugo Boss", t, "Hugo Boss The Scent for Her EDP 30ml & Lotion Gift Set", "Women", "30", "56.49", "71.99", 5,
   [("Top", "Peach"), ("Heart", "Osmanthus"), ("Base", "White Musk")],
   "Fruity · Floral · Musky", "Warm peach and osmanthus in a seductive, easy-to-gift set.",
   f"{t} pairs BOSS The Scent for Her Eau de Parfum with a matching body lotion. Juicy peach opens, a floral heart of osmanthus follows, and it settles on soft white musk.",
   ["BOSS The Scent for Her Eau de Parfum 30ml (spray)", "BOSS The Scent for Her Body Lotion 50ml"],
   ["A sweet, juicy peach opening", "A floral osmanthus heart", "A soft, sensual white musk finish", "Matching body lotion to layer the scent"],
   "EAN 3616304197994 matched on Monparle (EDP 30ml + body lotion 50ml, women) and Drogerie Natura (same contents, but it wrongly gives the men's The Scent notes); Amazon UK, DocMorris and Dr.Max titles also say The Scent For Her 30ml + 50ml. Pyramid agreed by The Perfume Shop and Sephora UK (freesia on The Perfume Shop only, left out). 2016 per The Perfume Shop and NST. Not the men's The Scent set – check the box. Store already has the 50ml EDP + 75ml lotion version as a separate draft. Awaiting photos.",
   "peach over osmanthus and white musk, with body lotion.", ["Fruity", "Floral", "Musky"], ["Fruity", "Floral"],
   name="The Scent for Her", **PC)

MK = "Michael Kors"
# ---------------- Michael Kors Gorgeous! 4-piece set
t = "Michael Kors Gorgeous! Eau de Parfum 100ml Gift Set with Body Lotion, Shower Gel and 10ml Spray"
GS("0850050174301", MK, t, "Michael Kors Gorgeous! EDP 100ml 4-Piece Gift Set", "Women", "100", "58.49", "73.99", 5,
   [("Top", "Pink Pepper, Mandarin"), ("Heart", "Tuberose, Tobacco, Orange Blossom, Jasmine Sambac, Ylang-Ylang"), ("Base", "Guaiac Wood, Tonka Bean, Cedar, Cashmeran")],
   "Floral · Woody · Spicy", "A radiant white floral, warmed with tobacco and soft woods.",
   f"{t} brings together Gorgeous! Eau de Parfum, a matching body lotion and shower gel, and a 10ml spray for your bag. Pink pepper and mandarin open brightly, a lush heart of tuberose, orange blossom, jasmine sambac, ylang-ylang and a touch of tobacco follows, and it settles on guaiac wood, tonka, cedar and cashmeran.",
   ["Gorgeous! Eau de Parfum 100ml (spray)", "Gorgeous! Body Lotion 100ml", "Gorgeous! Shower Gel 100ml", "Gorgeous! Eau de Parfum 10ml (spray)"],
   ["A sparkling opening of pink pepper and mandarin", "A lush white-floral heart of tuberose and jasmine", "A warm base of guaiac wood, tonka and cashmeran", "Four pieces, including a 10ml travel spray"],
   "EAN 0850050174301 matched on Superdrug and The Fragrance Counter (EDP 100ml + body lotion + shower gel + travel spray); 100ml/100ml/100ml/10ml sizes per michaelkors.com and Escentual. Pyramid agreed by The Fragrance Counter and Parfumo. 2021 per Fragrance Counter, Parfumo, Escentual. Supplier lists a second barcode 0850050174646 (other edition) for the same set. Awaiting photos.",
   "tuberose and orange blossom over guaiac wood, plus 10ml.", ["Floral", "Woody", "Spicy"], ["Floral", "Jasmine", "Spicy", "Woody"],
   name="Gorgeous!", **PC)

# ---------------- Michael Kors Pour Femme 4-piece set
t = "Michael Kors Pour Femme Eau de Parfum 100ml Gift Set with Body Lotion, Shower Gel and 10ml Spray"
GS("0850050174349", MK, t, "Michael Kors Pour Femme EDP 100ml 4-Piece Gift Set", "Women", "100", "74.99", "96.99", 5,
   [("Top", "Mandarin, Blackcurrant, Pink Pepper"), ("Heart", "Jasmine, Rose"), ("Base", "Vanilla, Musk, Patchouli")],
   "Floral · Fruity · Musky", "A bright, modern floral with a soft vanilla glow.",
   f"{t} brings together Michael Kors Pour Femme Eau de Parfum, a matching body lotion and shower gel, and a 10ml spray. Mandarin, blackcurrant and pink pepper open with sparkle, a heart of jasmine and rose follows, and it settles on vanilla, musk and patchouli.",
   ["Pour Femme Eau de Parfum 100ml (spray)", "Pour Femme Body Lotion 100ml", "Pour Femme Shower Gel 100ml", "Pour Femme Eau de Parfum 10ml (spray)"],
   ["A juicy opening of mandarin, blackcurrant and pink pepper", "A feminine heart of jasmine and rose", "A soft base of vanilla, musk and patchouli", "Four pieces, including a 10ml travel spray"],
   "EAN 0850050174349 matched on bol.com (100ml EDP + 10ml EDP + 100ml shower gel + 100ml body lotion, women) and Zenetic-parfum (EAN in URL, 310ml set title); contents also per michaelkors.co.uk and Escentual. Pyramid agreed by Escentual and Xpressions (WWD and michaelkors.co.uk agree; lily of the valley on two only, left out). Launched in Europe 2024 per WWD only, so not stated. Other years of this set carry other EANs (supplier also lists 0850050174684) – check the box. Awaiting photos.",
   "mandarin and blackcurrant over jasmine, rose and vanilla.", ["Floral", "Fruity", "Musky"], ["Fruity", "Floral", "Jasmine", "Rose", "Vanilla"],
   name="Michael Kors Pour Femme", **PC)

# ---------------- Missoni Pour Homme set
t = "Missoni Parfum Pour Homme Eau de Parfum 100ml Gift Set with 30ml Eau de Parfum"
GS("8011003877225", "Missoni", t, "Missoni Parfum Pour Homme EDP 100ml & 30ml Gift Set", "Men", "100", "50.49", "64.99", 5,
   [("Top", "Grapefruit, Lavender"), ("Heart", "Ginger, Jasmine"), ("Base", "Oak, Birch, Patchouli, Sandalwood, Musk")],
   "Citrus · Aromatic · Woody", "Zesty, aromatic and woody, with a 30ml spray to carry.",
   f"{t} pairs Missoni Parfum Pour Homme with a 30ml Eau de Parfum for travel. Grapefruit and lavender open fresh, a heart of ginger and jasmine follows, and it settles on oak, birch, patchouli, sandalwood and musk.",
   ["Missoni Parfum Pour Homme Eau de Parfum 100ml (spray)", "Missoni Parfum Pour Homme Eau de Parfum 30ml (spray)"],
   ["A fresh opening of grapefruit and lavender", "A spicy heart of ginger and jasmine", "A warm woody base of oak, sandalwood and musk", "30ml size for travel or the gym bag"],
   "NEEDS REVIEW: EAN 8011003877225 found only on a ModeSens title ('Missoni Mens Gift Set'), page unreadable; the 100ml EDP + 30ml EDP set is confirmed by Superdrug (under EAN 8011003870622) and US retailers (3.4oz + 1oz). Please check the box barcode/contents. Pyramid agreed by Flannels, Cosmetify, ScentAdvice (lime on two only, left out). 2017 per Flannels and ScentAdvice. Awaiting photos.",
   "grapefruit and lavender over ginger, oak and sandalwood.", ["Citrus", "Aromatic", "Woody"], ["Citrus", "Lavender", "Woody", "Sandalwood", "Spicy"],
   name="Missoni Parfum Pour Homme", status="needs-review", **PC)

MB = "Mont Blanc"
# ---------------- Montblanc Legend EDT set
t = "Mont Blanc Legend Eau de Toilette 100ml Gift Set with 100ml Shower Gel and 7.5ml Eau de Toilette"
GS("3386460130349", MB, t, "Mont Blanc Legend EDT 100ml 3-Piece Gift Set", "Men", "100", "50.99", "69.99", 5,
   [("Top", "Pineapple, Bergamot, Lavender, Lemon Verbena"), ("Heart", "Red Apple, Rose, Geranium, Dried Fruits, Oakmoss"), ("Base", "Tonka Bean, Sandalwood")],
   "Aromatic · Fougere · Fruity", "A modern fougère classic: fresh, fruity and confident.",
   f"{t} pairs the best-selling Legend Eau de Toilette with a matching shower gel and a 7.5ml mini. Pineapple, bergamot, lavender and lemon verbena open fresh, a heart of red apple, rose, geranium, dried fruits and oakmoss follows, and it settles on tonka bean and sandalwood.",
   ["Legend Eau de Toilette 100ml (spray)", "Legend Shower Gel 100ml", "Legend Eau de Toilette 7.5ml (mini)"],
   ["A fresh opening of pineapple, bergamot and lavender", "A fruity-floral heart of red apple and rose", "A smooth base of tonka and sandalwood", "Three pieces, including a 7.5ml mini"],
   "EAN 3386460130349 matched on Walmart (100ml EDT + 100ml shower gel + 7.5ml EDT) and Jomashop (3-piece EDT set). Pyramid agreed by MightyApe and LookFantastic. 2011 per ScentAdvice and NST. Supplier lists several barcodes for this set (yearly editions). Awaiting photos.",
   "pineapple and lavender over red apple, tonka and sandalwood.", ["Aromatic", "Fougere", "Fruity"], ["Fruity", "Lavender", "Floral", "Sandalwood"],
   name="Montblanc Legend", **TC)

# ---------------- Montblanc Legend Red set
t = "Mont Blanc Legend Red Eau de Parfum 50ml Gift Set with 100ml Shower Gel"
GS("3386460133777", MB, t, "Mont Blanc Legend Red EDP 50ml & Shower Gel Gift Set", "Men", "50", "34.99", "43.99", 5,
   [("Top", "Blood Orange"), ("Heart", "Cedarwood"), ("Base", "Mahogany")],
   "Citrus · Woody", "Bright blood orange over warm, glowing woods.",
   f"{t} pairs Legend Red Eau de Parfum with a matching shower gel. Juicy blood orange opens, a heart of cedarwood follows, and it settles on rich mahogany wood.",
   ["Legend Red Eau de Parfum 50ml (spray)", "Legend Red Shower Gel 100ml"],
   ["A vibrant blood orange opening", "A warm cedarwood heart", "A rich mahogany wood finish", "Matching shower gel to layer the scent"],
   "NEEDS REVIEW: EAN 3386460133777 not found online; the 50ml EDP + 100ml shower gel set is confirmed by LookFantastic and Galaxus (under EAN 3386460139076; supplier also lists 3386460139069). Please check the box barcode. Pyramid agreed by LookFantastic, Galaxus, Escentual (grapefruit/tonka on two only, left out). Supplier gender Men kept (Galaxus says unisex). Awaiting photos.",
   "blood orange over cedarwood and mahogany, with shower gel.", ["Citrus", "Woody"], ["Citrus", "Woody"],
   name="Legend Red", status="needs-review", **PC)

FM = "Ford Mustang"
# ---------------- Ford Mustang Legacy 4 x 20ml set
t = "Ford Mustang Legacy Eau de Toilette Gift Set 4 x 20ml"
MSET("0849017015566", FM, t, "Ford Mustang Legacy EDT Gift Set 4 x 20ml", "Men", "21.99", "29.99", 5,
     [("Cougar", "grapefruit and lemon over lavender and cinnamon, finishing with amber and musk"),
      ("Gran Torino", "green apple and lemon over rosemary and clove, finishing with sandalwood and musk"),
      ("Falcon", "bergamot and blackcurrant over cardamom and geranium, finishing with patchouli and cedarwood"),
      ("Thunderbird", "ginger and orange zest over lavender and black pepper, finishing with leather and amber")],
     ["Aromatic", "Woody", "Spicy", "Citrus"], ["Citrus", "Lavender", "Spicy", "Woody"], "Aromatic · Woody · Spicy",
     "Four Ford Legacy classics in handy 20ml sprays.",
     f"{t} brings together four Ford Legacy fragrances – Cougar, Gran Torino, Falcon and Thunderbird – each in a 20ml Eau de Toilette pocket spray. It's an easy way to try them all, switch scents through the week or give as a gift.",
     ["Four Ford Legacy fragrances in one box", "Pocket-size 20ml sprays for travel or the car", "From fresh citrus to warm leather and amber", "Ready to give as a gift"],
     "NEEDS REVIEW: EAN 0849017015566 not found on any web page. Contents (4 x 20ml EDT: Cougar, Gran Torino, Falcon, Thunderbird) agreed by TJ Hughes, Flannels and Cosmetify (title matches supplier). Per-scent notes from TJ Hughes and Flannels, which share the same wording (probably one source text). Supplier brand 'Mustang'; vendor set to Ford Mustang to match the store's other Mustang products. Please check the box barcode. Awaiting photos.",
     status="needs-review")

# ---------------- Ford Mustang Blue set
t = "Ford Mustang Blue Eau de Toilette 100ml Gift Set with Aftershave Balm and Hair & Body Wash"
GS("0849017007639", FM, t, "Ford Mustang Blue EDT 100ml 3-Piece Gift Set", "Men", "100", "22.99", "29.99", 5,
   [("Top", "Bergamot, Lemon, Mint, Basil"), ("Heart", "Lavender, Geranium, Clary Sage, Clove, Pine, Artemisia, Pepper, Cardamom")],
   "Aromatic · Fresh · Citrus", "Fresh, aromatic and full of open-road energy.",
   f"{t} brings together Mustang Blue Eau de Toilette with a matching aftershave balm and hair & body wash. Bergamot, lemon, mint and basil open crisp and fresh, followed by an aromatic heart of lavender, geranium, clary sage, clove, pine and cardamom, over a warm woody base.",
   ["Mustang Blue Eau de Toilette 100ml (spray)", "Mustang Blue Aftershave Balm 100ml", "Mustang Blue Hair & Body Wash 100ml"],
   ["A crisp opening of bergamot, lemon and mint", "An aromatic heart of lavender, sage and spice", "A complete grooming set for him", "Great value with a full-size 100ml spray"],
   "EAN 0849017007639 matched on Welzo and MyGiftStop (100ml EDT + 100ml aftershave balm + 100ml hair & body wash); contents also per Superdrug. Top and heart agreed by MyGiftStop and FragranceX; base notes on FragranceX only, so only top and heart shown (Superdrug: 'warm woody base'). Supplier brand 'Mustang'; vendor set to Ford Mustang to match the store. Awaiting photos.",
   "bergamot, lemon and mint over lavender, sage and clove.", ["Aromatic", "Fresh", "Citrus"], ["Citrus", "Lavender", "Fresh", "Spicy"],
   name="Mustang Blue", **TC)

NR = "Narciso Rodriguez"
# ---------------- Narciso Rodriguez All Of Me Intense set
t = "Narciso Rodriguez All Of Me Eau de Parfum Intense 50ml Gift Set with Body Lotion and Shower Gel"
GS("3423222133849", NR, t, "Narciso Rodriguez All Of Me Intense EDP 50ml Gift Set", "Women", "50", "44.99", "58.99", 1,
   [("Top", "Black Iris, Jasmine Sambac"), ("Heart", "Rose, Geranium, Tuberose"), ("Base", "Musk, Vanilla, Sandalwood")],
   "Floral · Musky", "A deeper, more sensual take on All Of Me.",
   f"{t} pairs All Of Me Eau de Parfum Intense with a matching body lotion and shower gel. Black iris and jasmine sambac open, a heart of rose, geranium and tuberose follows, and it settles on Narciso Rodriguez's signature musk with vanilla and sandalwood.",
   ["All Of Me Eau de Parfum Intense 50ml (spray)", "All Of Me Body Lotion 50ml", "All Of Me Shower Gel 50ml"],
   ["An intriguing opening of black iris and jasmine", "A rich floral heart of rose and tuberose", "Signature musk warmed with vanilla and sandalwood", "Matching body lotion and shower gel to layer the scent"],
   "EAN 3423222133849 matched on The Perfume Shop UK and IE (50ml EDP Intense + 50ml body lotion + 50ml shower gel) – same retailer, so contents also checked on Lookfantastic. Pyramid agreed by The Perfume Shop, Lookfantastic, John Lewis, Parfumo (pink pepper/heliotrope on Parfumo only, left out). Launch year disagrees (2024 vs 2025), not stated. Awaiting photos.",
   "black iris and jasmine over rose, tuberose and musk.", ["Floral", "Musky"], ["Floral", "Jasmine", "Rose", "Vanilla", "Sandalwood"],
   name="All Of Me Intense", conc="Eau De Parfum", concl="Eau de Parfum Intense")

# ---------------- Narciso Rodriguez Bleu Noir EDP set
t = "Narciso Rodriguez For Him Bleu Noir Eau de Parfum 100ml Gift Set with 10ml Spray and Shower Gel"
GS("3423222092726", NR, t, "Narciso Rodriguez Bleu Noir EDP 100ml 3-Piece Gift Set", "Men", "100", "73.99", "92.99", 2,
   [("Top", "Bergamot, Black Pepper"), ("Heart", "Musk"), ("Base", "Cedar, Ebony")],
   "Woody · Musky · Spicy", "Dark, magnetic and refined: musk wrapped in woods.",
   f"{t} brings together For Him Bleu Noir Eau de Parfum, a 10ml spray for your bag and a matching shower gel. Bergamot and black pepper open, a heart of Narciso Rodriguez's signature musk follows, and it settles on cedar and ebony wood.",
   ["For Him Bleu Noir Eau de Parfum 100ml (spray)", "For Him Bleu Noir Eau de Parfum 10ml (spray)", "For Him Bleu Noir Shower Gel 50ml"],
   ["A crisp opening of bergamot and black pepper", "A heart of signature musk", "A deep, dark base of cedar and ebony", "Three pieces, including a 10ml travel spray"],
   "EAN 3423222092726 matched on Nandansons (100ml EDP + 50ml shower gel + 10ml EDP) and El Corte Inglés (lists only 100ml EDP + 50ml shower gel); 3-piece contents also per Escentual and Tesco. Pyramid agreed by Parfumo, Escentual, Extrafarma (amber/vetiver on fewer sources, left out). Launch year on one source only, not stated. Awaiting photos.",
   "bergamot and black pepper over musk, cedar and ebony.", ["Woody", "Musky", "Spicy"], ["Citrus", "Spicy", "Woody"],
   name="Bleu Noir Eau de Parfum", **PC)

write_outputs()
