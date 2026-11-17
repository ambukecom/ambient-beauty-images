import sys; sys.path.insert(0, "/home/claude/ambient-beauty-images/workflow")
from lib import *

# ---------------- Fragrances
t = "Ahmed Al Maghribi Kaaf Noir Extrait de Parfum 100ml"
F("6290360617756", "Ahmed Al Maghribi", t, "Unisex", "100", "38.49", "49.99", 4,
  [("Top", "Blood Orange, Sicilian Lemon, Juniper Berries"), ("Base", "Cedarwood, Ambroxan, Vetiver")],
  "Citrus · Aromatic · Woody", "Blood orange and juniper over clean cedar and vetiver.",
  f"{t} is a fresh, woody-aromatic extrait. Blood orange, Sicilian lemon and juniper berries open with a bright, gin-like sparkle, and it dries down to a clean, modern base of cedarwood, ambroxan and vetiver.",
  ["A zesty opening of blood orange and Sicilian lemon", "Juniper berries for a crisp, gin-like edge", "A clean base of cedarwood, ambroxan and vetiver", "Rich extrait concentration"],
  "Needs review: sellers publish two different pyramids. Shown notes are those agreed by Dubai Perfume Shop and PerfumeBox (also ArabicParfums, Vivir); their heart notes differ (clary sage, geranium, Hedione vs lavender, Iso E Super), so the heart is not shown. Superdrug (EAN page), FragranceHub and FilledWithBarakah describe an oud/rose/amber scent instead; please check the box. Dubai Perfume Shop markets it for men; supplier's Unisex used. Awaiting photos.",
  "blood orange and juniper over cedar and vetiver.", ["Citrus", "Aromatic", "Woody"], ["Citrus", "Woody", "Fresh"],
  name="Kaaf Noir", conc="Extrait De Parfum", concl="Extrait de Parfum", status="needs-review")

t = "Ajmal Cuir Musc Eau de Parfum 100ml"
F("6293708007479", "Ajmal", t, "Unisex", "100", "57.99", "78.99", 1,
  [("Top", "Watermelon, Raspberry"), ("Heart", "Leather, Tobacco"), ("Base", "Musk, Oakmoss")],
  "Leather · Musky · Fruity", "Juicy watermelon and raspberry over soft leather and musk.",
  f"{t} is a musky leather fragrance with a sweet, fruity twist. Watermelon and raspberry open juicily, a smooth heart of leather and tobacco follows, and it settles into a soft base of musk and oakmoss.",
  ["A juicy opening of watermelon and raspberry", "A smooth heart of leather and tobacco", "A soft base of musk and oakmoss", "Part of Ajmal's musk collection"],
  "Notes confirmed by 2 sources (Almanaar UK, Ajmal Perfume USA store; Maxaroma EAN listing matches). Almanaar describes it as masculine; supplier's Unisex used. Awaiting photos.",
  "watermelon and raspberry over leather, tobacco and musk.", ["Leather", "Musky", "Fruity"], ["Fruity"],
  name="Cuir Musc")

t = "Ajmal Patchouli Wood Eau de Parfum 50ml"
F("6293708019458", "Ajmal", t, "Unisex", "50", "60.99", "79.99", 1,
  [("Top", "Pink Pepper, Spices"), ("Base", "Oud, Patchouli, Woody Notes")],
  "Woody · Spicy · Earthy", "Spiced pink pepper over deep oud and patchouli.",
  f"{t} is a rich, woody-spicy fragrance. Pink pepper and spices open warmly, and it settles into a deep, earthy base of oud, patchouli and woods, ideal for autumn and winter evenings.",
  ["A warm opening of pink pepper and spices", "A deep base of oud and patchouli", "Earthy, woody character", "Ideal for cooler evenings"],
  "Top and base confirmed by 2 sources (Ajmal official site, Perfumania; Superdrug EAN page agrees on pink pepper, oud and patchouli). Heart notes differ (jasmine/floral vs cardamom and mace), so the heart is not shown. Cosmetify files it under men's; supplier's Unisex used. Awaiting photos.",
  "pink pepper over oud, patchouli and woods.", ["Woody", "Spicy"], ["Spicy", "Woody"],
  name="Patchouli Wood")

t = "Arabiyat Prestige Aristo Eau de Parfum 100ml"
F("6290361917183", "Arabiyat Prestige", t, "Men", "100", "43.99", "59.99", 5,
  [("Top", "Lemon, Ginger Blossom, Mandarin, Orange"), ("Heart", "Magnolia, Jasmine, Patchouli"), ("Base", "Sandalwood, Musk, Vanilla")],
  "Citrus · Floral · Woody", "Bright citrus and ginger blossom over creamy sandalwood and vanilla.",
  f"{t} is a bright citrus-floral fragrance. Lemon, ginger blossom, mandarin and orange open with a sparkling zest, a heart of magnolia, jasmine and patchouli follows, and it dries down to a creamy base of sandalwood, musk and vanilla.",
  ["A sparkling opening of citrus and ginger blossom", "A smooth heart of magnolia and jasmine", "A creamy base of sandalwood and vanilla", "Fresh enough for every day"],
  "Notes confirmed by 2 sources (Bjutip EAN page, FragranceHub UK; ArabicParfums agrees). Bjutip, JustMyLook, Notino and ArabicParfums market it as unisex; supplier's Men used. Awaiting photos.",
  "citrus and ginger blossom over sandalwood and vanilla.", ["Citrus", "Floral", "Woody"], ["Citrus", "Floral", "Jasmine", "Sandalwood", "Vanilla"],
  name="Aristo")

t = "Arabiyat Prestige Marasi For Her Eau de Parfum 100ml"
F("6295156400222", "Arabiyat Prestige", t, "Women", "100", "42.49", "57.99", 4,
  [("Top", "Hazelnut, Mango, Raspberry, Bergamot"), ("Heart", "Violet, Patchouli, Orange Blossom, Cotton Candy"), ("Base", "Tonka Bean, Vanilla, Caramel, Musk")],
  "Fruity · Gourmand · Sweet", "Mango and raspberry with cotton candy over caramel and vanilla.",
  f"{t} is a sweet, fruity-gourmand fragrance. Hazelnut, mango, raspberry and bergamot open juicily, a heart of violet, patchouli, orange blossom and cotton candy follows, and it settles into a creamy base of tonka bean, vanilla, caramel and musk.",
  ["A juicy opening of mango and raspberry", "A playful cotton candy heart", "A creamy base of caramel and vanilla", "Sweet and long-lasting"],
  "Notes confirmed by 2 sources (FilledWithBarakah, Boozyshop; ScentVerdict agrees). Awaiting photos.",
  "mango and cotton candy over caramel and vanilla.", ["Fruity", "Gourmand"], ["Fruity", "Floral", "Vanilla"],
  name="Marasi For Her")

t = "Arabiyat Prestige Marasi For Him Eau de Parfum 100ml"
F("6295156400215", "Arabiyat Prestige", t, "Men", "100", "42.49", "56.99", 4,
  [("Top", "Lavender, Mandarin, Jasmine Sambac"), ("Heart", "Orris, Cinnamon, Nutmeg, Olibanum"), ("Base", "Tarragon, Benzoin, Labdanum, Patchouli")],
  "Aromatic · Spicy · Woody", "Lavender and mandarin over warm spice and resin.",
  f"{t} is an aromatic, spicy fragrance. Lavender, mandarin and jasmine sambac open freshly, a warm heart of orris, cinnamon, nutmeg and olibanum follows, and it settles into a resinous base of tarragon, benzoin, labdanum and patchouli.",
  ["A fresh opening of lavender and mandarin", "A warm spiced heart of cinnamon and nutmeg", "A resinous base of benzoin and labdanum", "Sophisticated and long-lasting"],
  "Notes confirmed by 2 sources (FilledWithBarakah, OrientFragance; FridayCharm and ScentVerdict agree). Boozyshop lists a different pyramid, so it was not used. Awaiting photos.",
  "lavender and mandarin over spice and warm resins.", ["Aromatic", "Spicy", "Woody"], ["Lavender", "Spicy", "Woody"],
  name="Marasi For Him")

# ---------------- Haircare
t = "L'Oréal Professionnel Serie Expert Vitamino Color Mask 250ml"
add(cat_name="Haircare", bc="3474636976058", title=t, vendor="L'Oréal", type="Haircare", gender="Women", cat=TAXON["hair-mask"],
    price="22.99", cmp="29.99", qty=5, form="Hair Mask", size="250", unit="ml", gpc=GPC["hair-care"],
    tags=["L'Oréal", "Women", "Haircare", "Hair Mask", "Vitamino Color", "Coloured Hair", "Colour Protection", "Professional"],
    seo=("L'Oréal Professionnel Vitamino Color Mask 250ml", f"{t}: resveratrol mask for radiant, shiny coloured hair." + FREE),
    mf={"product-form": ["Cream"], "suitable-for-hair-type": ["Colored"], "conditioner-effect": ["Color protection", "Shine"]},
    desc=body("Radiant, glossy colour with a professional mask.",
      "L'Oréal Professionnel Serie Expert Vitamino Color Mask 250ml is a creamy professional mask for coloured hair. Powered by antioxidant resveratrol, it nourishes hair and helps colour look brighter, more radiant and shinier, leaving hair feeling soft.",
      [("Key ingredients", ul(["<strong>Resveratrol:</strong> a skincare-inspired antioxidant", "<strong>Niacinamide</strong>", "<strong>Glycerin</strong>"])),
       ("Suits", ul(["Coloured hair", "Normal to thick hair (on fine hair, use on the ends only)"])),
       ("How to use", ul(["After shampooing, apply to wet lengths and ends", "Leave for 3 minutes", "Rinse thoroughly"]))],
      [("Brand", "L'Oréal Professionnel"), ("Range", "Serie Expert Vitamino Color"), ("Type", "Hair mask"), ("Hair type", "Coloured, normal to thick hair"), ("Size", "250ml")],
      ["Brighter, more radiant colour", "Glossy shine", "Soft, nourished hair", "Salon-professional formula"],
      [("Which hair is it for?", "Coloured hair, normal to thick. On very fine hair, use it on the ends only."), ("How long do I leave it on?", "Leave it for 3 minutes, then rinse thoroughly.")]),
    note="Facts confirmed by 2 sources (L'Oréal Professionnel UK, French Beauty Hub EAN page; Feelunique agrees). This EAN is the Resveratrol formula (not Vitamino Color Spectrum). Supplier's Women used. Awaiting photos.")

# ---------------- Makeup
t = "Clarins Wonder Perfect Mascara 4D Waterproof 8ml - 01 Perfect Black"
add(cat_name="Makeup", bc="3666057157417", title=t, vendor="Clarins", type="Makeup", gender="Unisex", cat=TAXON["mascara"],
    price="28.49", cmp="37.99", qty=5, form="Mascara", size="8", unit="ml", gpc=GPC["mascara"],
    tags=["Clarins", "Unisex", "Makeup", "Mascara", "Wonder Perfect", "Waterproof", "Volume", "Black"],
    seo=("Clarins Wonder Perfect 4D Waterproof Mascara 8ml", f"Clarins Wonder Perfect Mascara 4D Waterproof 01 Perfect Black: long, curled, defined lashes." + FREE),
    mf={"color-pattern": ["Black"]},
    desc=body("Longer, curled, defined lashes that stay put.",
      "Clarins Wonder Perfect Mascara 4D Waterproof 8ml in 01 Perfect Black takes lashes to bold new dimensions: visibly lengthened, curled, defined and volumised. The waterproof formula resists humidity, sweat and watery eyes, with intense, flake-proof and smudge-proof colour that is gentle on eyes.",
      [("Key ingredients", ul(["<strong>Blue lotus wax:</strong> forms a flexible, waterproof film", "<strong>Lash Boosting Complex:</strong> with panthenol", "<strong>Mineral pigments</strong> for intense colour"])),
       ("Brush", ul(["Clarins' precision brush balances volume and definition so no lash goes unnoticed"])),
       ("Shade", ul(["01 Perfect Black"])),
       ("How to apply", ul(["Apply from roots to tips of lashes", "Remove with an oil-based eye make-up remover"]))],
      [("Brand", "Clarins"), ("Product", "Wonder Perfect Mascara 4D Waterproof"), ("Shade", "01 Perfect Black"), ("Size", "8ml")],
      ["Lengthens, curls, defines and volumises", "Waterproof: resists humidity, sweat and watery eyes", "Flake-proof, smudge-proof colour", "Gentle on eyes"],
      [("Is it waterproof?", "Yes, it resists humidity, sweat and watery eyes."), ("How do I remove it?", "Use an oil-based eye make-up remover.")]),
    note="Facts confirmed by 2 sources (Clarins brand site, Lintons Beauty EAN page; Escentual agrees on 8ml). Clarins' clinical volume claim (1 source) and any sensitive-eye/contact-lens claims left out. Awaiting photos.")

# ---------------- Bath & Body
t = "Lacoste L.12.12 Pour Elle Sparkling Shower Gel 150ml"
add(cat_name="Bath & Body", bc="8005610477053", title=t, vendor="Lacoste", type="Bath & Body", gender="Women", cat=TAXON["body-wash"],
    price="16.99", cmp="22.99", qty=1, form="Shower Gel", size="150", unit="ml", gpc=GPC["body-wash"],
    tags=["Lacoste", "Women", "Bath & Body", "Shower Gel", "L.12.12 Pour Elle Sparkling", "Fruity", "Gourmand"],
    seo=("Lacoste L.12.12 Pour Elle Sparkling Shower Gel 150ml", f"{t}: fruity, sweet shower gel with apple and candyfloss." + FREE),
    mf={"age-group": ["Adults"], "product-form": ["Gel"], "fragrance": ["Fruity"]},
    desc=body("A fizz of fruit and candyfloss in the shower.",
      "Lacoste L.12.12 Pour Elle Sparkling Shower Gel 150ml is a lightly foaming shower gel scented with the playful L.12.12 Pour Elle Sparkling fragrance: juicy red apple, mandarin and blackberry, a sweet heart of macaron accord and candyfloss, and a warm base of vetiver and cashmere woods.",
      [("Scent", kd([("Top", "Red Apple, Mandarin, Blackberry"), ("Heart", "Macaron Accord, Candyfloss"), ("Base", "Vetiver, Cashmere Woods")])),
       ("How to use", ul(["Work into a lather on wet skin", "Rinse thoroughly"]))],
      [("Brand", "Lacoste"), ("Product", "L.12.12 Pour Elle Sparkling Shower Gel"), ("Scent profile", "Fruity · Floral · Gourmand"), ("Size", "150ml")],
      ["Fruity, sweet scent", "Matches the L.12.12 Pour Elle Sparkling fragrance", "Easy lather", "Great for layering with the perfume"],
      [("What does it smell like?", "Red apple, mandarin and blackberry with macaron and candyfloss over vetiver."), ("Is it for women?", "Yes, it is a women's shower gel.")]),
    note="Facts confirmed by 2 sources (Galaxus EAN page, Cosmetify). Scent notes are from the matching Eau de Toilette (Escentual, Druni). Awaiting photos.")

t = "Molton Brown Heavenly Gingerlily Bath & Shower Gel 300ml"
add(cat_name="Bath & Body", bc="0008080151445", title=t, vendor="Molton Brown", type="Bath & Body", gender="Women", cat=TAXON["body-wash"],
    price="27.99", cmp="35.99", qty=1, form="Bath & Shower Gel", size="300", unit="ml", gpc=GPC["body-wash"], status="needs-review",
    tags=["Molton Brown", "Women", "Bath & Body", "Shower Gel", "Heavenly Gingerlily", "Floral", "Spicy"],
    seo=("Molton Brown Heavenly Gingerlily Shower Gel 300ml", f"{t}: spiced ginger and exotic lily over warm woods." + FREE),
    mf={"age-group": ["Adults"], "product-form": ["Gel"], "fragrance": ["Floral", "Spicy", "Sandalwood"]},
    desc=body("Spiced ginger and exotic lily, inspired by Tahiti.",
      "Molton Brown Heavenly Gingerlily Bath &amp; Shower Gel 300ml is an exotic, floral body wash inspired by the beaches and lagoons of Tahiti. Warm ginger, cardamom and clove meet lily, tuberose and tagetes over a base of cedarwood, sandalwood and musk.",
      [("Scent", kd([("Top", "Ginger, Cardamom, Clove"), ("Heart", "Lily, Tuberose, Tagetes"), ("Base", "Cedarwood, Sandalwood, Musk")])),
       ("How to use", ul(["Shower: apply to damp skin", "Bath: pour under warm running water"])),
       ("Good to know", ul(["Perfumer: Jacques Chabert", "Made in England"]))],
      [("Brand", "Molton Brown"), ("Product", "Heavenly Gingerlily Bath & Shower Gel"), ("Scent profile", "Floral · Spicy · Woody"), ("Size", "300ml")],
      ["Exotic spiced-floral scent", "Use in the bath or shower", "Iconic Molton Brown fragrance", "Made in England"],
      [("What does it smell like?", "Spiced ginger, cardamom and clove with lily and tuberose over sandalwood and musk."), ("Is it for women?", "Yes, though its spiced-floral scent suits anyone.")]),
    note="Needs review: barcode. Supplier's 0008080151445 is not the usual Molton Brown EAN (5030805...); it appears only in John Bell & Croyden image file names, while Austins' images carry 5030805002607. Supplier barcode used; please check the pack. Facts confirmed by 2+ sources (Niche Beauty, Austins, Sephora UK). Vegan/paraben-free claims (1 source) left out. Awaiting photos.")

for p in P:
    p["desc"] = p["desc"].replace("sicilian lemon", "Sicilian lemon")
write_outputs()
