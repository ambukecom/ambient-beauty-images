import sys; sys.path.insert(0, "/home/claude/ambient-beauty-images/workflow")
from lib import *
PC = dict(conc="Eau De Parfum", concl="Eau de Parfum")
XC = dict(conc="Extrait De Parfum", concl="Extrait de Parfum")
AW = " Awaiting photos."

# 1 Rue Broca Penthouse Larvotto
t = "Rue Broca Penthouse Larvotto Eau de Parfum 80ml"
F("6290171010470", "Rue Broca", t, "Unisex", "80", "25.49", "32.99", 1,
  [("Top", "Bergamot, Violet Leaf, Coriander"), ("Heart", "Rose, Black Pepper"), ("Base", "Vanilla, Patchouli, Amber")],
  "Aromatic · Spicy · Amber", "Riviera glamour: bergamot and violet leaf over warm vanilla and amber.",
  f"{t} is inspired by the penthouses above Monaco's Larvotto beach. Fresh bergamot, violet leaf and coriander open, a heart of rose and black pepper adds a spicy edge, and it settles into a warm, powdery base of vanilla, patchouli and amber.",
  ["A fresh bergamot and violet leaf opening", "A spicy rose and black pepper heart", "A warm vanilla, patchouli and amber base", "Great value for a long-wearing Eau de Parfum"],
  "EAN 6290171010470 matched on Walmart (its spec says 3.4oz but URL/title 2.7oz – data error) and Amazon.ae/.sa (80ml). EDP 80ml and pyramid agreed by Lyko, Parfum-Centrum and FragranceNet; Parfum-Centrum lists 'spices, black currant, rose' in the heart, so heart shown is the 3-of-4 majority (rose, black pepper). 2020. Rue Broca is an Afnan line (Notino lists it under Afnan). Retailers mostly market it for men (Parfum-Centrum unisex); supplier's Unisex kept." + AW,
  "bergamot and violet leaf over warm vanilla and amber.", ["Aromatic", "Spicy", "Oriental", "Powdery"], ["Citrus", "Spicy", "Rose", "Vanilla", "Oriental"],
  name="Penthouse Larvotto", **PC)

# 2 Surrati Cuban Latte
t = "Surrati Cuban Latte Extrait de Parfum 150ml"
F("6281085040011", "Surrati", t, "Unisex", "150", "44.49", "57.99", 1,
  [("Top", "Coffee, Vanilla"), ("Heart", "Caramel, Suede"), ("Base", "Roasted Woods, Musk")],
  "Gourmand · Woody · Oriental", "Fresh espresso and vanilla melting into caramel and soft suede.",
  f"{t} is a rich gourmand from Surrati's 1929 Collection. Coffee and vanilla open like a freshly made latte, caramel and smooth suede form the heart, and it dries down to roasted woods and musk.",
  ["A rich coffee and vanilla opening", "Sweet caramel softened by suede", "A warm roasted woods and musk base", "Long-lasting Extrait in a generous 150ml bottle"],
  "Extrait 150ml and pyramid agreed by JustMyLook + Perfume Trading UK (Cosmetify's looser note list ignored). EAN 6281085040011 not found online – check the box. Supplier form column says EDP but name and all sources say Extrait – listed as Extrait. JustMyLook unisex, Cosmetify men; supplier's Unisex kept." + AW,
  "coffee and vanilla over caramel, suede and roasted woods.", ["Gourmand", "Woody", "Oriental"], ["Vanilla", "Woody", "Oriental"],
  name="Cuban Latte", **XC)

# 3 Surrati Omniyat
t = "Surrati Omniyat Eau de Parfum 140ml"
F("6281085039657", "Surrati", t, "Unisex", "140", "26.99", "34.99", 1,
  [("Top", "Black Currant, Green Tangerine, Peach, Passionfruit"), ("Heart", "Strawberry, Caramel, Gardenia"), ("Base", "Vanilla, Musk, Amber, Sandalwood")],
  "Fruity · Gourmand · Musky", "A basket of juicy fruits drizzled with caramel over creamy vanilla.",
  f"{t} is a sweet, fruity gourmand from Surrati's Heritage Collection. Black currant, green tangerine, peach and passionfruit open, strawberry, caramel and gardenia form the heart, and it finishes on vanilla, musk, amber and sandalwood.",
  ["A juicy black currant, peach and passionfruit opening", "Strawberry and caramel with a touch of gardenia", "A creamy vanilla, amber and sandalwood base", "Generous 140ml bottle"],
  "EAN 6281085039657 matched on Perfumeria Esencja and Triple Traders (EDP 140ml); pyramid identical on Esencja, Perfume Trading UK, Intense Oud and FilledWithBarakah. Unisex per Perfume Trading/Esencja (Cosmetify files under men)." + AW,
  "black currant, peach and caramel over creamy vanilla.", ["Fruity", "Gourmand", "Musky"], ["Fruity", "Citrus", "Floral", "Vanilla", "Sandalwood"],
  name="Omniyat", **PC)

# 4 Surrati Purple Candy
t = "Surrati Purple Candy Extrait de Parfum 150ml"
F("6281085040059", "Surrati", t, "Unisex", "150", "42.49", "55.99", 1,
  [("Top", "Tea, Osmanthus, Bergamot"), ("Heart", "Jasmine, Freesia, Orchid, Rose, Orange Blossom"), ("Base", "Vanilla, Patchouli, Musk")],
  "Fruity · Floral · Sweet", "Tea and osmanthus over a candy-sweet bouquet and soft vanilla.",
  f"{t} is a sweet floral extrait from Surrati. Tea, osmanthus and bergamot open, a bouquet of jasmine, freesia, orchid, rose and orange blossom blooms in the heart, and it settles into vanilla, patchouli and musk.",
  ["A delicate tea, osmanthus and bergamot opening", "A lush jasmine, orchid and rose bouquet", "A soft vanilla, patchouli and musk base", "Long-lasting Extrait in a generous 150ml bottle"],
  "EAN 6281085040059 matched on eBay UK (Extrait 150ml); pyramid agreed by JustMyLook, Cosmetify and ScentVerdict. Supplier form column says EDP but name and all sources say Extrait – listed as Extrait. JustMyLook unisex, Cosmetify men, ScentVerdict women; supplier's Unisex kept." + AW,
  "tea and osmanthus over jasmine, orchid and vanilla.", ["Floral", "Fruity", "Gourmand"], ["Floral", "Jasmine", "Rose", "Fruity", "Vanilla"],
  name="Purple Candy", **XC)

# 5 Swiss Arabian Kashkha
t = "Swiss Arabian Kashkha Eau de Parfum 50ml"
F("6295124002236", "Swiss Arabian", t, "Women", "50", "39.99", "51.99", 1,
  [("Top", "Bergamot, Apple, Cinnamon"), ("Heart", "Saffron, Cardamom, Oud"), ("Base", "Cedarwood, Amber, Musk")],
  "Oriental · Spicy · Woody", "Apple and cinnamon warmed by saffron, oud and amber.",
  f"{t} is a warm, spicy oriental from Swiss Arabian. Bergamot, apple and cinnamon open, saffron, cardamom and oud form a rich heart, and it settles into cedarwood, amber and musk.",
  ["A bright bergamot and apple opening with cinnamon", "A rich saffron, cardamom and oud heart", "A warm cedarwood, amber and musk base", "Compact 50ml bottle"],
  "EAN 6295124002236 matched on Desertcart (EDP 1.7oz, women); EDP 50ml confirmed by Notino UK, Nahdi and TJ Hughes. Pyramid agreed by swissarabian.com (written for the 20ml perfume oil), Nahdi and Scento; extra notes on Notino/TJ Hughes left out. Notino, Nahdi and FragranceNet market it as unisex; supplier's Women kept." + AW,
  "apple and cinnamon warmed by saffron, oud and amber.", ["Oriental", "Spicy", "Woody", "Fruity"], ["Spicy", "Fruity", "Woody", "Oriental"],
  name="Kashkha", **PC)

# 6 Swiss Arabian Patchouli 01 (needs-review: size)
t = "Swiss Arabian Patchouli 01 Extrait de Parfum 50ml"
F("6295124051456", "Swiss Arabian", t, "Unisex", "50", "53.49", "71.99", 2,
  [("Top", "Lavender, Bergamot, Blackcurrant, Pink Pepper, Grapefruit"), ("Heart", "Geranium, Orange Blossom, Elemi, Lily of the Valley"), ("Base", "Patchouli, Labdanum, Olibanum, Vanilla, Tonka")],
  "Woody · Aromatic · Oriental", "A modern fougère: lavender and pink pepper over rich patchouli and labdanum.",
  f"{t} is a modern, woody patchouli. Lavender, bergamot, blackcurrant and pink pepper open, geranium, orange blossom and elemi form an aromatic heart, and it settles into patchouli, labdanum, olibanum, vanilla and tonka.",
  ["A fresh lavender and pink pepper opening", "An aromatic geranium and elemi heart", "A deep patchouli, labdanum and olibanum base", "Rich Extrait de Parfum concentration"],
  "NEEDS REVIEW: size. Supplier says 100ml, but EAN 6295124051456 is listed as 50ml on Bjutip and eCosmetics, every retailer sells only 50ml, and the supplier price equals Vanilla 01 50ml – listed as 50ml, check the box (and size/price with supplier). Extrait confirmed by Bjutip, FilledWithBarakah, Gold Apple, JustMyLook (supplier form says EDP). Pyramid agreed by Bjutip, Centrepoint, Gold Apple, JustMyLook (shown shortened). Unisex." + AW,
  "lavender and pink pepper over rich patchouli and labdanum.", ["Woody", "Aromatic", "Fougere"], ["Lavender", "Citrus", "Spicy", "Woody", "Vanilla"],
  name="Patchouli 01", status="needs-review", **XC)

# 7 Swiss Arabian Pure Instinct
t = "Swiss Arabian Pure Instinct Eau de Parfum 100ml"
F("6295124030581", "Swiss Arabian", t, "Men", "100", "44.99", "57.99", 1,
  [("Top", "Grapefruit, Apple, Pineapple, Pepper, Rosemary"), ("Heart", "Tuberose, Rose, Cardamom, Galbanum, Patchouli"), ("Base", "Amber, Cedarwood, Vanilla, Vetiver, Leather")],
  "Woody · Aromatic · Fresh", "Zesty grapefruit and pineapple over cedar, vetiver and leather.",
  f"{t} is a fresh, woody aromatic for men. Grapefruit, apple, pineapple, pepper and rosemary open, tuberose, rose, cardamom and galbanum add depth in the heart, and it settles into amber, cedarwood, vanilla, vetiver and leather.",
  ["A zesty grapefruit and pineapple opening", "A spiced cardamom and floral heart", "A masculine cedar, vetiver and leather base", "Versatile for day and evening"],
  "EAN 6295124030581 matched on Superdrug Marketplace, Triple Traders and Faire (EDP 100ml, men); pyramid agreed by all three plus Parfoom (Faire/Parfoom say 'green notes' for galbanum). 2018 (Parfoom)." + AW,
  "grapefruit and pineapple over cedar, vetiver and leather.", ["Woody", "Aromatic", "Fresh", "Fruity"], ["Citrus", "Fruity", "Spicy", "Woody", "Fresh"],
  name="Pure Instinct", **PC)

# 8 Sapil Bound for Women
t = "Swiss Arabian Sapil Bound for Women Eau de Parfum 100ml"
F("6295124030253", "Swiss Arabian", t, "Women", "100", "24.49", "31.99", 4,
  [("Top", "Passion Fruit, Raspberry, Violet Leaf"), ("Heart", "Passion Flower, Orange Blossom, Jasmine"), ("Base", "Musk, Cedar, Benzoin")],
  "Fruity · Floral · Woody", "Passion fruit and raspberry over orange blossom and soft musk.",
  f"{t} is a bright fruity floral from Sapil, part of the Swiss Arabian group. Passion fruit, raspberry and violet leaf open, passion flower, orange blossom and jasmine form the heart, and it settles into musk, cedar and benzoin.",
  ["A juicy passion fruit and raspberry opening", "A pretty orange blossom and jasmine heart", "A soft musk, cedar and benzoin base", "Great value 100ml Eau de Parfum"],
  "EAN 6295124030253 matched on Faire (brand Swiss Arabian, titled Sapil Bound) and Debenhams IE SKU. Bottle brand is Sapil (Swiss Arabian Perfumes Group) – vendor kept as Swiss Arabian per supplier. EDP 100ml and pyramid agreed by Notino UK, Faire, Parfumo and Debenhams. 2019. Not to be confused with Bound for Men EDT. Women." + AW,
  "passion fruit and raspberry over orange blossom and musk.", ["Fruity", "Floral", "Woody"], ["Fruity", "Floral", "Jasmine", "Woody"],
  name="Sapil Bound for Women", **PC)

# 9 Shaghaf Oud Marine
t = "Swiss Arabian Shaghaf Oud Marine Eau de Parfum 75ml"
F("6295124053269", "Swiss Arabian", t, "Unisex", "75", "53.49", "72.99", 2,
  [("Top", "Sea Notes, Bergamot, Black Pepper"), ("Heart", "Geranium, Mahonial, Petalia, Rosyfolia"), ("Base", "Oud, Akigalawood, Cypriol, Amber")],
  "Aquatic · Woody · Oud", "A fresh sea breeze over smoky oud and amber.",
  f"{t} is a marine twist on Swiss Arabian's Shaghaf Oud line. Sea notes, bergamot and black pepper open, a floral heart of geranium and modern rose accords follows, and it settles into oud, akigalawood, cypriol and amber.",
  ["A fresh sea notes and bergamot opening", "A peppery, airy floral heart", "A smoky oud, cypriol and amber base", "A fresh take on the Shaghaf Oud collection"],
  "EAN 6295124053269 matched on Jomashop and Parfumerie de Dubai (EDP 75ml/2.5oz, unisex); pyramid agreed by Parfumerie de Dubai and Vivir (ScentAdvice consistent). New 2026 release – no swissarabian.com or UK page yet. Not the original Shaghaf Oud or Oud Azraq." + AW,
  "sea notes and bergamot over smoky oud and amber.", ["Aquatic", "Woody", "Fresh", "Spicy"], ["Aquatic", "Citrus", "Spicy", "Woody"],
  name="Shaghaf Oud Marine", **PC)

# 10 Spirit of Valencia
t = "Swiss Arabian Spirit of Valencia Extrait de Parfum 100ml"
F("6295124042799", "Swiss Arabian", t, "Unisex", "100", "57.49", "77.99", 2,
  [("Top", "Lemon, Bergamot, Apple"), ("Heart", "Rose, Jasmine, Gardenia, Peony"), ("Base", "Amber, Sandalwood, Musk")],
  "Fruity · Floral · Amber", "Sunny Spanish citrus and apple over a rose and jasmine bouquet.",
  f"{t} captures a sunny day in Valencia. Lemon, bergamot and apple open with a bright sparkle, rose, jasmine, gardenia and peony bloom in the heart, and it settles into warm amber, sandalwood and musk.",
  ["A bright lemon, bergamot and apple opening", "A lush rose, jasmine and peony heart", "A warm amber, sandalwood and musk base", "Rich Extrait de Parfum concentration"],
  "Extrait per swissarabian (KSA site), FragranceNet and FilledWithBarakah; Faire (EAN 6295124042799 match) titles it EDP, as does the supplier form column – listed as Extrait per brand, check the box. 100ml and pyramid agreed by brand site, Faire, Parfumo, Nahdi. 2023. Unisex (some reviewers say it leans feminine)." + AW,
  "lemon and apple over rose, jasmine and warm amber.", ["Fruity", "Floral", "Oriental", "Citrus"], ["Citrus", "Fruity", "Rose", "Jasmine", "Sandalwood"],
  name="Spirit of Valencia", **XC)

write_outputs()
