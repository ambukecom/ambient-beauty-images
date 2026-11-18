import sys; sys.path.insert(0, "/home/claude/ambient-beauty-images/workflow")
from lib import *

# ---------------- Bath & Body
t = "Ted Baker Fusion Electric Hair & Body Wash 250ml"
add(cat_name="Bath & Body", bc="5060412679022", title=t, vendor="Ted Baker", type="Bath & Body", gender="Men", cat=TAXON["body-wash"],
    price="16.99", cmp="22.99", qty=5, form="Hair & Body Wash", size="250", unit="ml", gpc=GPC["body-wash"],
    tags=["Ted Baker", "Men", "Bath & Body", "Body Wash", "Hair & Body Wash", "Fusion", "Electric", "Spicy", "Vegan"],
    seo=("Ted Baker Fusion Electric Hair & Body Wash 250ml", f"{t}: spicy cinnamon and grapefruit over sandalwood." + FREE),
    mf={"age-group": ["Adults"], "product-form": ["Gel"], "fragrance": ["Spicy", "Citrus", "Lavender", "Sandalwood"]},
    desc=body("A bold, energising 2-in-1 wash for hair and body.",
      "Ted Baker Fusion Electric Hair &amp; Body Wash 250ml cleanses skin and hair in one easy step. Spicy cinnamon, nutmeg and grapefruit open brightly, a heart of lavender, liquorice and amber follows, and it settles on sandalwood, patchouli and vetiver. Lactic acid and mulberry leaf extract help leave skin feeling fresh.",
      [("Scent", kd([("Top", "Cinnamon, Nutmeg, Grapefruit"), ("Heart", "Lavender, Liquorice, Amber"), ("Base", "Sandalwood, Patchouli, Vetiver")])),
       ("Key ingredients", ul(["<strong>Lactic acid</strong>", "<strong>Mulberry leaf extract</strong> (Morus alba), an antioxidant"])),
       ("How to use", ul(["Apply to wet skin and hair", "Massage into a lather, then rinse thoroughly", "Avoid contact with the eyes"])),
       ("Good to know", ul(["Vegan friendly", "Part of the Ted Baker Fusion collection"]))],
      [("Brand", "Ted Baker"), ("Range", "Fusion"), ("Type", "Hair & body wash"), ("Scent profile", "Spicy · Citrus · Woody"), ("Size", "250ml")],
      ["One wash for hair and body", "Spicy, citrusy and woody scent", "With lactic acid and mulberry leaf extract", "Vegan friendly"],
      [("What does it smell like?", "Cinnamon, nutmeg and grapefruit with lavender and liquorice over sandalwood, patchouli and vetiver."), ("Is it for men?", "Yes, it is part of the Ted Baker Fusion men's range.")]),
    note="Facts confirmed by 2+ sources (Superdrug EAN page, Next product page and ingredient PDF, Cosmetify; KMI Brands for the range). Notes agreed by Superdrug, Next and Cosmetify. Vegan friendly from Cosmetify and KMI Brands. Supplier's 'Body & Hair Wash' shown as retailers' 'Hair & Body Wash'. Awaiting photos.")

t = "Ted Baker Fusion Enigmatic Hair & Body Wash 250ml"
add(cat_name="Bath & Body", bc="5060412679015", title=t, vendor="Ted Baker", type="Bath & Body", gender="Men", cat=TAXON["body-wash"],
    price="16.99", cmp="21.99", qty=1, form="Hair & Body Wash", size="250", unit="ml", gpc=GPC["body-wash"],
    tags=["Ted Baker", "Men", "Bath & Body", "Body Wash", "Hair & Body Wash", "Fusion", "Enigmatic", "Citrus", "Vegan"],
    seo=("Ted Baker Fusion Enigmatic Hair & Body Wash 250ml", f"{t}: lemon and blackberry over patchouli and amber." + FREE),
    mf={"age-group": ["Adults"], "product-form": ["Gel"], "fragrance": ["Citrus", "Fruity", "Woody", "Spicy"]},
    desc=body("A fresh, fruity 2-in-1 wash with a warm woody finish.",
      "Ted Baker Fusion Enigmatic Hair &amp; Body Wash 250ml cleanses skin and hair in one easy step. Zesty lemon, blackberry and grapefruit open brightly, a heart of cardamom, plum and sandalwood follows, and it dries down to patchouli, tree moss and dry amber. Lactic acid and orange fruit extract help leave skin feeling fresh.",
      [("Scent", kd([("Top", "Lemon, Blackberry, Grapefruit"), ("Heart", "Cardamom, Plum, Sandalwood"), ("Base", "Patchouli, Tree Moss, Dry Amber")])),
       ("Key ingredients", ul(["<strong>Lactic acid</strong>", "<strong>Orange fruit extract</strong>"])),
       ("How to use", ul(["Apply to wet skin and hair", "Massage into a lather, then rinse thoroughly", "Avoid contact with the eyes"])),
       ("Good to know", ul(["Vegan friendly", "Part of the Ted Baker Fusion collection"]))],
      [("Brand", "Ted Baker"), ("Range", "Fusion"), ("Type", "Hair & body wash"), ("Scent profile", "Citrus · Fruity · Woody"), ("Size", "250ml")],
      ["One wash for hair and body", "Zesty citrus and blackberry scent", "With lactic acid and orange fruit extract", "Vegan friendly"],
      [("What does it smell like?", "Lemon, blackberry and grapefruit with cardamom and plum over patchouli, tree moss and dry amber."), ("Is it for men?", "Yes, it is part of the Ted Baker Fusion men's range.")]),
    note="Facts confirmed by 2+ sources (Superdrug EAN page, Next product page and ingredient PDF, Cosmetify; KMI Brands for the range). Notes from Superdrug and Next (Cosmetify omits grapefruit and sandalwood). Vegan friendly from Cosmetify and KMI Brands. Awaiting photos.")

# ---------------- Fragrances
t = "Armaf Club De Nuit Intense Overdose Extrait de Parfum 100ml"
F("6295199823941", "Armaf", t, "Men", "100", "43.99", "58.99", 2,
  [("Top", "Pineapple, Bergamot, Mandarin, Blue Crystal Accord"), ("Heart", "Oakmoss, Vanilla Flower, Plum"), ("Base", "Patchouli, Amber, Tonka Bean, White Powder Accord")],
  "Fruity · Woody · Oriental", "Juicy pineapple and bergamot over plum, patchouli and tonka.",
  f"{t} is a bold, fruity-woody extrait from the Club de Nuit Intense family. Pineapple, bergamot and mandarin open with a sparkling blue crystal accord, a heart of oakmoss, vanilla flower and plum follows, and it settles into a rich base of patchouli, amber, tonka bean and a soft powdery accord.",
  ["A juicy pineapple and bergamot opening", "A smooth heart of plum and vanilla flower", "A rich base of patchouli, amber and tonka", "Extrait de Parfum strength"],
  "Needs review: bottle size. Supplier says 100ml (Fragrance Hub UK, AAR Fragrances, Ferwer agree) but JustMyLook and IntenseOud list 105ml; please check the box. Extrait concentration confirmed by 4 sources (supplier form column said EDP). EAN on GiftExpress. Notes agreed by 6 sources. Awaiting photos.",
  "pineapple and bergamot over plum, patchouli and tonka.", ["Fruity", "Woody", "Oriental"], ["Fruity", "Citrus", "Woody", "Oriental"],
  name="Club De Nuit Intense Overdose", conc="Extrait De Parfum", concl="Extrait de Parfum", status="needs-review")

t = "Armaf Club de Nuit Precieux I Extrait de Parfum 55ml"
F("6294015181913", "Armaf", t, "Unisex", "55", "47.99", "64.99", 5,
  [("Top", "Bergamot, Lemon, Pink Pepper, Black Pepper, Pineapple, Pear, Caramel"), ("Heart", "Anise, Lily of the Valley, Jasmine, Woody Notes, Oakmoss"), ("Base", "Ambroxan, Vanilla, Leather, White Musk, Amber, Patchouli, Cedar")],
  "Woody · Oriental · Spicy", "Peppery citrus and pear over leather, vanilla and ambroxan.",
  f"{t} is a rich, woody-amber extrait. Bergamot, lemon, pink and black pepper, pineapple, pear and caramel open vividly, a heart of anise, lily of the valley, jasmine and oakmoss follows, and it settles into a deep base of ambroxan, vanilla, leather, white musk, amber, patchouli and cedar.",
  ["A vivid opening of citrus, pepper and pear", "A floral-aromatic heart of anise and jasmine", "A deep base of leather, vanilla and ambroxan", "Concentrated Extrait de Parfum in a 55ml bottle"],
  "Notes confirmed by 2 sources (Bjutip EAN page, JustMyLook; Walmart EAN page agrees on top notes but lists fewer). EAN identifies Precieux I (Precieux 1), so 'I' added to the title. JustMyLook and Bjutip code list it as unisex but Bjutip specs, Walmart and others market it for men; supplier's Unisex used. Awaiting photos.",
  "peppery citrus and pear over leather, vanilla and ambroxan.", ["Woody", "Oriental", "Spicy"], ["Woody", "Citrus", "Spicy", "Fruity"],
  name="Club de Nuit Precieux I", conc="Extrait De Parfum", concl="Extrait de Parfum")

t = "Armaf Le Parfait Pour Femme Mon Amour Eau de Parfum 100ml"
F("6295199803332", "Armaf", t, "Women", "100", "26.99", "34.99", 1,
  [("Top", "Pear, Orange Blossom, Pink Pepper"), ("Base", "Cedar, Cashmere Wood")],
  "Gourmand · Floral · Fruity", "Juicy pear and orange blossom over soft cashmere wood.",
  f"{t} is a sweet floral-fruity fragrance. Juicy pear, orange blossom and a touch of pink pepper open softly, with warm touches of vanilla and patchouli, before it settles into a smooth base of cedar and cashmere wood.",
  ["A juicy pear and orange blossom opening", "A hint of pink pepper", "A smooth base of cedar and cashmere wood", "Easy, feminine everyday scent"],
  "Notes confirmed by 2+ sources (Bjutip EAN page, Lyko; Ferwer and Scento agree on top and base). Heart not shown: Bjutip/Lyko list vanilla and patchouli, Ferwer/Scento list almond, liquorice, jasmine and coffee. Vanilla and patchouli appear in all sources, so mentioned in the intro only. Awaiting photos.",
  "pear and orange blossom over cedar and cashmere wood.", ["Gourmand", "Floral", "Fruity"], ["Fruity", "Floral", "Vanilla", "Woody"],
  name="Le Parfait Pour Femme Mon Amour")

t = "Armaf Le Parfait Pour Femme Opus Eau de Parfum 100ml"
F("6295199803349", "Armaf", t, "Women", "100", "28.49", "37.99", 1,
  [("Top", "Mandarin Orange, Blackcurrant, Petitgrain, Lavender"), ("Heart", "Orange Blossom, Lavender, Jasmine"), ("Base", "Vanilla, Cedar, Amber, Musk")],
  "Fougere · Oriental · Floral", "Mandarin and lavender over orange blossom, jasmine and vanilla.",
  f"{t} is an elegant floral fougère. Mandarin, blackcurrant, petitgrain and lavender open freshly, a heart of orange blossom, lavender and jasmine follows, and it settles into a warm base of vanilla, cedar, amber and musk.",
  ["A fresh opening of mandarin and blackcurrant", "A floral heart of orange blossom and jasmine", "A warm base of vanilla, amber and musk", "Elegant floral fougère character"],
  "Notes confirmed by 2+ sources (Armaf brand page 'Le Parfait Opus', Bjutip EAN page; Lyko and Ferwer agree). Supplier size missing ('100m'); 100ml confirmed by Bjutip, Lyko, Ferwer and Parfum-Centrum. Full name Le Parfait Pour Femme Opus used. Awaiting photos.",
  "mandarin and lavender over orange blossom, jasmine and vanilla.", ["Fougere", "Oriental", "Floral"], ["Floral", "Lavender", "Vanilla", "Citrus"],
  name="Le Parfait Pour Femme Opus")

t = "Armaf Le Parfait Pour Femme Eau de Parfum 100ml"
F("6294015102246", "Armaf", t, "Women", "100", "23.49", "31.99", 5,
  [("Top", "Jasmine, Neroli, Mandarin Orange"), ("Heart", "Honeysuckle, Tuberose, Lily of the Valley"), ("Base", "Amber, Patchouli, Musk")],
  "Floral · Musky · Citrus", "Jasmine and neroli over tuberose, honeysuckle and musk.",
  f"{t} is a graceful white-floral fragrance. Jasmine, neroli and mandarin open brightly, a heart of honeysuckle, tuberose and lily of the valley follows, and it settles into a soft base of amber, patchouli and musk.",
  ["A bright opening of jasmine, neroli and mandarin", "A lush white-floral heart of tuberose and honeysuckle", "A soft base of amber, patchouli and musk", "Elegant day-to-night floral"],
  "Notes confirmed by 2+ sources (Desertcart EAN page, The Perfume Spot EAN page; Perfumania and Dubai Perfume Shop agree). Awaiting photos.",
  "jasmine and neroli over tuberose, honeysuckle and musk.", ["Floral", "Musky", "Citrus"], ["Floral", "Jasmine", "Citrus", "Fresh"],
  name="Le Parfait Pour Femme")

t = "Armaf Le Parfait Pour Homme Eau de Toilette 100ml"
F("6294015102239", "Armaf", t, "Men", "100", "23.99", "31.99", 5,
  [("Top", "Bergamot, Blackcurrant, Pineapple, Lemon"), ("Heart", "Rose, Spicy Notes, Jasmine"), ("Base", "Musk, Vanilla, Amber")],
  "Oriental · Fruity · Spicy", "Pineapple and bergamot over spiced rose, vanilla and musk.",
  f"{t} is a fresh, fruity-oriental fragrance. Bergamot, blackcurrant, pineapple and lemon open brightly, a heart of rose, spices and jasmine follows, and it settles into a warm base of musk, vanilla and amber.",
  ["A bright opening of pineapple and bergamot", "A spiced heart of rose and jasmine", "A warm base of musk, vanilla and amber", "Easy-wearing Eau de Toilette"],
  "Notes confirmed by 3 sources (Superdrug, Shop-Apotheke and The Perfume Spot EAN pages). Patchouli (2 of 3 sources) left out of the base. EDT confirmed; a separate Le Parfait Pour Homme EDP exists, so check photos are of the EDT. Awaiting photos.",
  "pineapple and bergamot over spiced rose, vanilla and musk.", ["Oriental", "Fruity", "Spicy"], ["Fruity", "Citrus", "Spicy", "Oriental"],
  name="Le Parfait Pour Homme", conc="Eau De Toilette", concl="Eau de Toilette")

t = "French Avenue Divin Aoud Eau de Parfum 100ml"
F("6291108322093", "French Avenue", t, "Unisex", "100", "35.99", "47.99", 1,
  [("Top", "Bergamot, Lemon, Lime"), ("Heart", "Rose, Jasmine, Fig"), ("Base", "Musk, Sandalwood, Amber, Patchouli")],
  "Woody · Oriental · Spicy · Oud", "Bright citrus over rose and fig, wrapped in rich oud.",
  f"{t} is a rich oud fragrance from French Avenue by Fragrance World. Bergamot, lemon and lime open with a spicy sparkle, a heart of rose, jasmine and fig follows, and precious oud runs through a warm base of musk, sandalwood, amber and patchouli.",
  ["A bright citrus opening with a spicy edge", "A floral heart of rose, jasmine and fig", "Rich oud over sandalwood, amber and musk", "Unisex oriental-woody character"],
  "Notes confirmed by 2+ sources (Superdrug and Bjutip EAN pages; TJ Hughes, Scentverdict, Emirates Oud agree). Oud placed in the heart by some and the base by others, so it is described in the text rather than in a tier. Awaiting photos.",
  "citrus over rose and fig with rich oud and sandalwood.", ["Woody", "Oriental", "Spicy"], ["Woody", "Oriental", "Spicy", "Rose"],
  name="Divin Aoud")

t = "Gulf Orchid Cherry Vibe Eau de Parfum 100ml"
F("6290362163077", "Gulf Orchid", t, "Women", "100", "25.99", "33.99", 5,
  [("Top", "Cherry"), ("Heart", "Jasmine, Rose"), ("Base", "Sandalwood, Tonka Bean")],
  "Gourmand · Fruity · Floral", "Juicy cherry over jasmine and rose with creamy sandalwood.",
  f"{t} is a sweet, fruity-floral gourmand. Juicy cherry opens playfully, a heart of jasmine and rose follows, and it settles into a creamy base of sandalwood and tonka bean.",
  ["A juicy cherry opening", "A floral heart of jasmine and rose", "A creamy base of sandalwood and tonka", "Sweet, playful gourmand character"],
  "Needs review: EAN not found on any page (brand does not publish EANs), and two different note lists circulate (Luxurious-Fragrances/Emaratiscents vs Scentaura/o2morny). Only the notes both lists share are shown. Retailers split between women's and unisex; supplier's Women used. Please check the box barcode and notes. Awaiting photos.",
  "juicy cherry over jasmine, rose and sandalwood.", ["Gourmand", "Fruity", "Floral"], ["Fruity", "Floral", "Rose", "Jasmine"],
  name="Cherry Vibe", status="needs-review")

write_outputs()
