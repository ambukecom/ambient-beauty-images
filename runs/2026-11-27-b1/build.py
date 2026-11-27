import sys; sys.path.insert(0, "/home/claude/ambient-beauty-images/workflow")
from lib import *
TC = dict(conc="Eau De Toilette", concl="Eau de Toilette")
PC = dict(conc="Eau De Parfum", concl="Eau de Parfum")
AW = " Awaiting photos."
NR = dict(status="needs-review")
MB = "Mercedes-Benz"

# 1 Man EDT 20ml
t = "Mercedes-Benz Man Eau de Toilette 20ml"
F("3595471061201", MB, t, "Men", "20", "19.49", "25.99", 4,
  [("Top", "Pear, Ambrette Seed"), ("Heart", "Cedar Leaf, Geranium"), ("Base", "Oakmoss, Rosewood")],
  "Woody · Aromatic", "Clean, confident and easy to wear every day.",
  f"{t} is a woody aromatic fragrance for men, created by perfumer Olivier Cresp. Juicy pear and ambrette seed open fresh and smooth, a heart of cedar leaf and geranium adds an aromatic green character, and it settles onto a refined base of oakmoss and rosewood. The 20ml size is ideal for travel or your gym bag.",
  ["A fresh pear and ambrette opening", "An aromatic cedar leaf and geranium heart", "A refined oakmoss and rosewood base", "Handy 20ml travel-size Eau de Toilette"],
  "EAN 3595471061201 matched on Jomashop + Modesens + Amazon UK (Man EDT 20ml). Pyramid agreed by brand site, Fragrancex FAQ, Scentadvice (Debenhams/Fragrancex description give other heart notes – brand version used). Woody aromatic per brand + Fragrancex. Olivier Cresp per brand, Fragrancex, Scentverdict. Launch year disputed (2015/2016) – left out. Men." + AW,
  "pear and ambrette over cedar leaf and oakmoss.", ["Woody", "Aromatic"], ["Woody", "Fresh"],
  name="Mercedes-Benz Man", **TC)

# 2 Man Private EDP 100ml
t = "Mercedes-Benz Man Private Eau de Parfum 100ml"
F("3595471061096", MB, t, "Men", "100", "39.99", "51.99", 4,
  [("Top", "Mugwort, Cardamom, Cypress"), ("Heart", "Lavender, Labdanum, Ambrox"), ("Base", "Patchouli, Cashmeran, Cedar")],
  "Amber · Woody", "A warm, intimate signature for the evening.",
  f"{t} is an amber woody fragrance for men, created by perfumer Olivier Cresp. Aromatic mugwort, cardamom and cypress open with a spicy freshness, a heart of lavender, labdanum and ambrox brings warmth and depth, and it dries down to patchouli, cashmeran and cedar.",
  ["A spicy mugwort and cardamom opening", "A warm lavender and labdanum heart", "A deep patchouli, cashmeran and cedar base", "Generous 100ml Eau de Parfum"],
  "EAN 3595471061096 matched on Al Seer & Safeer (100ml EDP; spec field says 120ml – site error) + eBay (100ml EDP spray); Jomashop wrongly says EDT. Pyramid agreed by brand site + Parfumo. Amber woody per brand + Amazon. Olivier Cresp per brand + Parfumo. Launch year single-source – left out. Men." + AW,
  "mugwort and cardamom over lavender, labdanum and patchouli.", ["Woody", "Oriental"], ["Woody", "Spicy", "Lavender"],
  name="Man Private", **PC)

# 3 Rose EDT 90ml
t = "Mercedes-Benz Rose Eau de Toilette 90ml"
F("3595471026248", MB, t, "Women", "90", "36.99", "47.99", 1,
  [("Top", "Grapefruit, Blackcurrant"), ("Heart", "Magnolia, Rosewood, Elemi"), ("Base", "Musk, Amber, Cedar")],
  "Floral · Rose", "A radiant rose with a fresh, modern twist.",
  f"{t} is a floral fragrance for women centred on rose. Sparkling grapefruit and blackcurrant open bright and juicy, a heart of magnolia, rosewood and elemi gives a soft floral elegance around the rose, and it settles onto a warm base of musk, amber and cedar.",
  ["A sparkling grapefruit and blackcurrant opening", "An elegant rose and magnolia floral heart", "A warm musk, amber and cedar base", "Generous 90ml Eau de Toilette"],
  "EAN 3595471026248 matched on tshop.bg + Samawa.ae (Rose EDT 90ml, women); Superdrug/Galaxus sell the same scent under EAN 3595471031129 (likely other packaging – check photos match stock). Pyramid agreed by Parfumo, Superdrug, Galaxus, Perfumania, Samawa; rose itself is placed in top by some and heart by others, so it is named in the text but not in a tier. Floral per Parfumo + Perfumania. Women." + AW,
  "grapefruit and blackcurrant over magnolia and musk.", ["Floral"], ["Floral", "Rose"],
  name="Mercedes-Benz Rose", **TC)

# 4 Select EDT 100ml
t = "Mercedes-Benz Select Eau de Toilette 100ml"
F("3595471081018", MB, t, "Men", "100", "33.49", "43.99", 1,
  [("Top", "Bergamot, Blackcurrant"), ("Heart", "Mint, Apple"), ("Base", "Ambroxan, Musk, Patchouli")],
  "Woody · Fresh", "Fresh, crisp and effortlessly stylish.",
  f"{t} is a fresh woody fragrance for men, created by perfumer Olivier Cresp and launched in 2018. Bergamot and blackcurrant open bright and zesty, a cool heart of mint and apple keeps it crisp, and it dries down to a smooth base of ambroxan, musk and patchouli.",
  ["A zesty bergamot and blackcurrant opening", "A cool mint and crisp apple heart", "A smooth ambroxan, musk and patchouli base", "Generous 100ml Eau de Toilette"],
  "EAN 3595471081018 matched on Ansar Gallery, GiftExpress, CreationWatches (Select EDT 100ml). Pyramid agreed by brand site, Scento, Ansar Gallery, GiftExpress. Woody chypre per brand + GiftExpress. Olivier Cresp per brand + GiftExpress; 2018 per Scento + GiftExpress. Not Select Day. Men." + AW,
  "bergamot and blackcurrant over mint, apple and musk.", ["Woody", "Fresh"], ["Woody", "Fresh", "Fruity"],
  name="Mercedes-Benz Select", **TC)

# 5 Select Night EDP 100ml
t = "Mercedes-Benz Select Night Eau de Parfum 100ml"
F("3595471081032", MB, t, "Men", "100", "39.99", "50.99", 2,
  [("Top", "Bergamot, Cardamom, Lavender"), ("Heart", "Orange Blossom, Cedar, Guaiac Wood"), ("Base", "Sandalwood, Patchouli, Vanilla")],
  "Woody · Oriental", "A sensual, warm scent made for after dark.",
  f"{t} is a woody oriental fragrance for men, created by perfumer Olivier Cresp and launched in 2019. Bergamot, cardamom and lavender open fresh and aromatic, a heart of orange blossom, cedar and guaiac wood adds warmth, and it settles onto a sensual base of sandalwood, patchouli and vanilla.",
  ["A fresh bergamot, cardamom and lavender opening", "A warm orange blossom and guaiac wood heart", "A sensual sandalwood, patchouli and vanilla base", "Generous 100ml Eau de Parfum"],
  "EAN 3595471081032 matched on Arreglatelo.es, Jomashop, eBay UK (Select Night EDP 100ml). Pyramid agreed by brand site, Scento, Scentverdict, eCosmetics, Mercedes-Benz NZ store. Woody oriental per brand + NZ store. Olivier Cresp per brand, Scentverdict, eCosmetics; 2019 per Scentverdict + Vivir. Men." + AW,
  "bergamot and cardamom over orange blossom, sandalwood and vanilla.", ["Woody", "Oriental"], ["Woody", "Vanilla", "Sandalwood"],
  name="Select Night", **PC)

SIGN_PYR = [("Top", "Cardamom, Pink Pepper"), ("Heart", "Lavender, Orange Blossom, Geranium"), ("Base", "Tonka Bean, Cashmere Wood, Patchouli")]
SIGN_NOTE = ("Pyramid: tiers agreed by brand site + FragranceX (violet leaf and white musk disputed – left out). Family: brand says fougère oriental, "
             "Galaxus + FragranceX woody spicy. 2021 per Galaxus, Ferwer, FragranceX; Olivier Cresp per brand + Ferwer. Men.")
# 6 Sign EDP 100ml
t = "Mercedes-Benz Sign Eau de Parfum 100ml"
F("3595471111012", MB, t, "Men", "100", "39.99", "53.99", 5, SIGN_PYR,
  "Woody · Spicy", "A bold, modern signature with a spicy edge.",
  f"{t} is a woody spicy fragrance for men, created by perfumer Olivier Cresp and launched in 2021. Cardamom and pink pepper open with a lively spice, a heart of lavender, orange blossom and geranium adds an aromatic floral twist, and it dries down to warm tonka bean, cashmere wood and patchouli.",
  ["A lively cardamom and pink pepper opening", "An aromatic lavender and orange blossom heart", "A warm tonka, cashmere wood and patchouli base", "Generous 100ml Eau de Parfum"],
  "EAN 3595471111012 matched on Superdrug (Sign For Him 100ml EDP) + Qogita title. " + SIGN_NOTE + AW,
  "cardamom and pink pepper over lavender and tonka bean.", ["Woody", "Spicy"], ["Woody", "Spicy", "Lavender"],
  name="Mercedes-Benz Sign", **PC)

# 7 Sign EDP 50ml
t = "Mercedes-Benz Sign Eau de Parfum 50ml"
F("3595471111029", MB, t, "Men", "50", "30.99", "39.99", 3, SIGN_PYR,
  "Woody · Spicy", "A bold, modern signature with a spicy edge.",
  f"{t} is a woody spicy fragrance for men, created by perfumer Olivier Cresp and launched in 2021. Cardamom and pink pepper open with a lively spice, a heart of lavender, orange blossom and geranium adds an aromatic floral twist, and it dries down to warm tonka bean, cashmere wood and patchouli.",
  ["A lively cardamom and pink pepper opening", "An aromatic lavender and orange blossom heart", "A warm tonka, cashmere wood and patchouli base", "Handy 50ml Eau de Parfum"],
  "EAN 3595471111029 matched on Galaxus (Sign EDP 50ml) + bb-shop.ro / kendrashop.ro titles. " + SIGN_NOTE + AW,
  "cardamom and pink pepper over lavender and tonka bean.", ["Woody", "Spicy"], ["Woody", "Spicy", "Lavender"],
  name="Mercedes-Benz Sign", **PC)

# 8 Sign Your Attitude EDT 100ml
t = "Mercedes-Benz Sign Your Attitude Eau de Toilette 100ml"
F("3595471024008", MB, t, "Men", "100", "41.49", "51.99", 3,
  [("Top", "Bergamot, Mandarin, Ginger"), ("Heart", "Lavender, Cypress, Cinnamon, Nutmeg"), ("Base", "Amberwood")],
  "Spicy · Woody", "Fresh citrus with a confident, spicy warmth.",
  f"{t} is a spicy fragrance for men, created by perfumer Fabrice Pellegrin and launched in 2022. Bergamot, mandarin and ginger open fresh and zesty, a heart of lavender, cypress, cinnamon and nutmeg adds aromatic spice, and it settles onto a warm amberwood base.",
  ["A zesty bergamot, mandarin and ginger opening", "An aromatic, spicy lavender and nutmeg heart", "A warm amberwood base", "Generous 100ml Eau de Toilette"],
  "EAN 3595471024008 matched on Maxaroma (item UP3595471024008, EDT 100ml) + eBay title only – no major UK retailer found. Pyramid agreed by Parfumo, Maxaroma, FragranceNet, brand description (Cologne.com differs – ignored). Family has no consensus (fresh citrus / amber spicy / woody spicy) – spicy + woody used. 2022 per Parfumo + FragranceNet; Fabrice Pellegrin per brand, Parfumo, Maxaroma. Men." + AW,
  "bergamot and ginger over lavender, nutmeg and amberwood.", ["Spicy", "Woody"], ["Spicy", "Citrus", "Lavender"],
  name="Sign Your Attitude", **TC)

# 9 Sign Your Power EDP Intense 100ml  (needs-review)
t = "Mercedes-Benz Sign Your Power Eau de Parfum Intense 100ml"
F("3595471028334", MB, t, "Men", "100", "39.99", "49.99", 3,
  [("Base", "Cedarwood")],
  "Woody · Amber", "Rich, warm and intensely charismatic.",
  f"{t} is a rich, intense fragrance for men, created by perfumer Fabrice Pellegrin as the third chapter of the SIGN collection. Warm spice, plum and cocoa give it a sweet, heady depth, wrapped in amber warmth and finishing on a smooth cedarwood base.",
  ["A warm, spicy opening", "Sweet plum and cocoa depth", "A smooth cedarwood finish", "Generous 100ml Eau de Parfum Intense"],
  "NEEDS REVIEW: EAN 3595471028334 matched on news-parfums.com + Perfume305 (SIGN Your Power Eau de Parfum Intense 100ml); some US retailers shorten to EDP. Note tiers disagree (brand: top cardamom/cinnamon/davana, heart plum/cocoa, base patchouli/cedar; news-parfums: cocoa top, patchouli heart, cedar base) – only agreed base (cedarwood) shown. Family not stated by 2 sources (brand: wood and amber) – Woody used. Launch year unconfirmed. Fabrice Pellegrin per brand, news-parfums, Perfume305. Men." + AW,
  "warm spice, plum and cocoa over cedarwood.", ["Woody"], ["Woody", "Spicy"],
  name="Sign Your Power", conc="Eau De Parfum", concl="Eau de Parfum Intense", **NR)

# 10 The Move EDT 20ml
t = "Mercedes-Benz The Move Eau de Toilette 20ml"
F("3595471091079", MB, t, "Men", "20", "18.99", "25.99", 4,
  [("Top", "Cardamom"), ("Heart", "Geranium, Sea Salt Notes"), ("Base", "Tonka Bean, Balsam Fir")],
  "Aromatic · Fougère", "Fresh, free-spirited and always on the go.",
  f"{t} is an aromatic fougère fragrance for men, created by perfumer Dominique Ropion and launched in 2019. Spicy cardamom opens with energy, a heart of geranium and salty marine notes brings a fresh, open-air feel, and it settles onto tonka bean and balsam fir. The 20ml size is perfect for travel.",
  ["An energetic cardamom opening", "A fresh geranium and sea salt heart", "A warm tonka bean and balsam fir base", "Handy 20ml travel-size Eau de Toilette"],
  "EAN 3595471091079 matched on Galaxus (The Move EDT 20ml) + Qogita title ('The Move (Exclusive) EDT 20ml'). Pyramid limited to notes agreed by Parfumo, Galaxus, Ferwer/Parfum-Centrum (apple blossom tier disputed, grapefruit not in Galaxus – left out). Aromatic fougère per brand, Ferwer, Galaxus. 2019 per Parfumo + Ferwer; Dominique Ropion per brand, Parfumo, Ferwer. Original The Move (not Express Yourself / Live The Moment). Men." + AW,
  "cardamom over geranium, sea salt and tonka bean.", ["Aromatic", "Fougere"], ["Fresh", "Spicy", "Aquatic"],
  name="The Move", **TC)

P[8]['desc']=P[8]['desc'].replace('<p>Cedarwood.</p>','<p>Warm spice, plum and cocoa over a smooth cedarwood base.</p>')
write_outputs()
