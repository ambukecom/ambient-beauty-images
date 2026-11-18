import sys; sys.path.insert(0, "/home/claude/ambient-beauty-images/workflow")
from lib import *
B = "Street Origins"
X = dict(conc="Extrait De Parfum", concl="Extrait de Parfum")
EXN = " Supplier sheet lists the concentration as Eau de Parfum, but the supplier name, Superdrug (EAN page) and the other retailers all say Extrait de Parfum, so Extrait used."

t = "Street Origins Cape Town Dream Eau de Parfum 75ml"
F("6298042001251", B, t, "Unisex", "75", "32.49", "41.99", 1,
  [("Top", "Apple, Bergamot, Grapefruit"), ("Heart", "Orange Blossom"), ("Base", "Patchouli, Amber, Sea Notes")],
  "Fresh · Citrus · Aquatic", "Crisp apple and citrus over orange blossom and a salty amber breeze.",
  f"{t} is a fresh, breezy fragrance for everyone. Apple, bergamot and grapefruit open crisply, a heart of orange blossom follows, and it settles on a base of patchouli, amber and sea notes.",
  ["A crisp opening of apple, bergamot and grapefruit", "A bright heart of orange blossom", "A breezy base of patchouli, amber and sea notes", "Fresh and easy to wear every day"],
  "Notes confirmed by 3 sources (FilledWithBarakah, Parfumo, ScentVerdict), all tiers agree; trademarked accords (Pamplezest, Oceanol, Ambernat, Ambertonic) shown as grapefruit, sea notes and amber; Cristalfizz left out. 75ml EDP and unisex confirmed by Superdrug (EAN page) and ScentVerdict. Awaiting photos.",
  "apple and bergamot over orange blossom, amber and sea notes.", ["Fresh", "Citrus", "Aquatic"], ["Fresh", "Citrus", "Fruity", "Aquatic"],
  name="Cape Town Dream")

t = "Street Origins It's Giving New York Extrait de Parfum 75ml"
F("6290360379869", B, t, "Unisex", "75", "43.49", "57.99", 1,
  [("Top", "Rose, Cinnamon, Pink Pepper, Violet, Mandarin"), ("Heart", "Jasmine, Orange Blossom, Rose"), ("Base", "Honey, Vanilla, Cocoa, Tonka Bean, Patchouli, Sandalwood, Cedarwood")],
  "Floral · Gourmand · Spicy", "Spiced rose and violet over jasmine, with honey, cocoa and vanilla.",
  f"{t} is a rich floral-gourmand fragrance. Rose, cinnamon, pink pepper, violet and mandarin open with spice, a heart of jasmine, orange blossom and rose follows, and it settles into honey, vanilla, cocoa, tonka, patchouli and woods.",
  ["A spicy opening of rose, cinnamon and pink pepper", "A floral heart of jasmine and orange blossom", "A sweet base of honey, cocoa and vanilla", "Long-lasting extrait concentration"],
  "Notes confirmed by 4 sources (Zaoud, FilledWithBarakah, ScentVerdict, Parfumo), all tiers agree; heart rose in 3 sources; brown sugar left out of the description for brevity (3 sources). Extrait 75ml confirmed by Superdrug (EAN page), Zaoud, FWB, ScentVerdict. Mostly sold as unisex (Zaoud lists it under men); supplier's Unisex used." + EXN + " Awaiting photos.",
  "spiced rose and violet over jasmine, honey and vanilla.", ["Floral", "Gourmand", "Spicy"], ["Rose", "Spicy", "Floral", "Vanilla", "Jasmine"],
  name="It's Giving New York", **X)

t = "Street Origins It's Vegas, Baby! Extrait de Parfum 75ml"
F("6290360379845", B, t, "Unisex", "75", "43.49", "54.99", 1,
  [("Top", "Cognac, Plum, Cinnamon"), ("Heart", "Iris, Myrrh, Cashmeran"), ("Base", "Vanilla, Tonka Bean, Sandalwood")],
  "Spicy · Oriental · Gourmand", "Boozy cognac and plum over iris and myrrh, with vanilla and sandalwood.",
  f"{t} is a warm, boozy fragrance. Cognac, plum and cinnamon open richly, a heart of iris, myrrh and cashmeran follows, and it settles into a smooth base of vanilla, tonka bean and sandalwood.",
  ["A boozy opening of cognac, plum and cinnamon", "A soft heart of iris, myrrh and cashmeran", "A smooth base of vanilla, tonka and sandalwood", "Long-lasting extrait concentration"],
  "Notes confirmed by 2 sources (Ferwer, ScentVerdict), all tiers agree. Extrait 75ml and unisex confirmed by Superdrug (EAN page), Ferwer and ScentVerdict. Not the same as 'I Do I Do, Vegas'." + EXN + " Awaiting photos.",
  "cognac and plum over iris, myrrh, vanilla and sandalwood.", ["Spicy", "Oriental", "Gourmand"], ["Spicy", "Fruity", "Vanilla", "Sandalwood"],
  name="It's Vegas, Baby!", **X)

t = "Street Origins Mumbai Hustle Eau de Parfum 75ml"
F("6298042001459", B, t, "Unisex", "75", "32.49", "41.99", 1,
  [("Top", "Heliotrope, Candied Fruits"), ("Heart", "Gardenia, Jasmine, Sandalwood"), ("Base", "Caramel, Vanilla, Musk")],
  "Gourmand · Floral · Fruity", "Candied fruit and heliotrope over gardenia, with caramel and vanilla.",
  f"{t} is a sweet floral-gourmand fragrance. Heliotrope and candied fruits open softly, a heart of gardenia, jasmine and sandalwood follows, and it settles on a cosy base of caramel, vanilla and musk.",
  ["A sweet opening of heliotrope and candied fruits", "A creamy heart of gardenia, jasmine and sandalwood", "A cosy base of caramel, vanilla and musk", "Sweet, comforting character"],
  "Notes confirmed by 4 sources (FilledWithBarakah, Splash, ScentVerdict, Fraganty), all tiers agree. 75ml EDP confirmed by Superdrug (EAN page), FWB, Splash. Superdrug and Fraganty say unisex, Splash says women; supplier's Unisex used. Awaiting photos.",
  "candied fruit and heliotrope over gardenia, caramel and vanilla.", ["Gourmand", "Floral", "Fruity"], ["Fruity", "Floral", "Jasmine", "Vanilla", "Sandalwood"],
  name="Mumbai Hustle")

t = "Street Origins Mumbai MC Eau de Parfum 75ml"
F("6298042001329", B, t, "Unisex", "75", "32.49", "41.99", 1,
  [("Top", "Grapefruit, Cardamom, Cinnamon, Nutmeg"), ("Heart", "Lavender, Licorice"), ("Base", "Sandalwood, Patchouli, Vetiver, Amber")],
  "Spicy · Aromatic · Woody", "Spiced grapefruit and cardamom over lavender, with sandalwood and amber.",
  f"{t} is a warm, spicy fragrance. Grapefruit, cardamom, cinnamon and nutmeg open with spice, a heart of lavender and licorice follows, and it settles on a woody base of sandalwood, patchouli, vetiver and amber.",
  ["A spicy opening of grapefruit, cardamom and cinnamon", "An aromatic heart of lavender and licorice", "A woody base of sandalwood, vetiver and amber", "Warm, confident character"],
  "Notes confirmed by 3 sources (Zaoud, Perfume Oriental, ScentVerdict), all tiers agree. 75ml EDP confirmed by Superdrug (EAN page) and 3 others. Zaoud and Perfume Oriental market it for men, Superdrug as unisex; supplier's Unisex used. Supplier spells it 'Mumbai Mc'; retailers use 'MC'. Awaiting photos.",
  "spiced grapefruit and cardamom over lavender and sandalwood.", ["Spicy", "Aromatic", "Woody"], ["Spicy", "Lavender", "Citrus", "Sandalwood", "Woody"],
  name="Mumbai MC")

t = "Street Origins Oars and Yours, Venice Extrait de Parfum 75ml"
F("6290360379746", B, t, "Unisex", "75", "43.49", "58.99", 1,
  [("Top", "Sea Notes, Bergamot"), ("Heart", "Black Pepper, Geranium"), ("Base", "Patchouli, Vetiver, Cedar")],
  "Aquatic · Aromatic · Woody", "Sea air and bergamot over black pepper and geranium, with vetiver and cedar.",
  f"{t} is a fresh, aquatic-woody fragrance. Sea notes and bergamot open brightly, a heart of black pepper and geranium follows, and it settles on a polished base of patchouli, vetiver and cedar.",
  ["A breezy opening of sea notes and bergamot", "A peppery heart of black pepper and geranium", "A polished base of patchouli, vetiver and cedar", "Long-lasting extrait concentration"],
  "Notes confirmed by 4 sources (Zaoud, FilledWithBarakah, Perfume Oriental, ScentVerdict), all tiers agree. Extrait 75ml confirmed by Superdrug (EAN page) and 3 others. Unisex per Superdrug, Perfume Oriental, ScentVerdict; Zaoud says men." + EXN + " Awaiting photos.",
  "sea notes and bergamot over black pepper, vetiver and cedar.", ["Aquatic", "Aromatic", "Woody"], ["Aquatic", "Fresh", "Spicy", "Woody"],
  name="Oars and Yours, Venice", **X)

t = "Street Origins On New York Time Extrait de Parfum 75ml"
F("6290360379760", B, t, "Unisex", "75", "43.49", "57.99", 1,
  [("Top", "Lemon, Pineapple, Bergamot, Blackcurrant, Apple"), ("Heart", "Birch, Jasmine, Rose"), ("Base", "Musk, Ambergris, Patchouli, Vanilla")],
  "Fruity · Woody · Fresh", "Juicy pineapple and blackcurrant over smoky birch, with musk and ambergris.",
  f"{t} is a fruity, woody fragrance. Lemon, pineapple, bergamot, blackcurrant and apple open juicily, a heart of birch, jasmine and rose follows, and it settles on a base of musk, ambergris, patchouli and vanilla.",
  ["A juicy opening of pineapple, blackcurrant and lemon", "A smoky heart of birch with jasmine and rose", "A smooth base of musk, ambergris and vanilla", "Long-lasting extrait concentration"],
  "Notes confirmed by 4 sources (Zaoud, Splash, Perfume Oriental, ScentVerdict), all tiers agree. Extrait 75ml confirmed by Superdrug (EAN page), Zaoud, Perfume Oriental (Splash type field says EDP). Most retailers market it for men, Superdrug as unisex; supplier's Unisex used. Not the same as It's Giving New York." + EXN + " Awaiting photos.",
  "pineapple and blackcurrant over birch, musk and ambergris.", ["Fruity", "Woody", "Fresh"], ["Fruity", "Citrus", "Woody", "Fresh"],
  name="On New York Time", **X)

t = "Street Origins Rise and Bling, Dubai Extrait de Parfum 75ml"
F("6290360379838", B, t, "Unisex", "75", "43.49", "57.99", 1,
  [("Top", "Peach, Green Notes, Blackcurrant"), ("Heart", "Rose, Iris"), ("Base", "White Musk, Cedar, Pepper, Orris Root, Violet Leaf")],
  "Floral · Fruity · Powdery", "Peach and blackcurrant over rose and iris, with white musk and violet leaf.",
  f"{t} is an elegant floral fragrance. Peach, green notes and blackcurrant open freshly, a heart of rose and iris follows, and it settles on a soft base of white musk, cedar, pepper, orris root and violet leaf.",
  ["A fresh, fruity opening of peach and blackcurrant", "A rosy heart with powdery iris", "A soft base of white musk, cedar and violet leaf", "Long-lasting extrait concentration"],
  "Notes confirmed by 3 sources (Zaoud, Perfume Oriental, Ferwer; ScentVerdict agrees), all tiers agree; rose shown generally (sources list May/Turkish rose). Extrait 75ml confirmed by Superdrug (EAN page), Zaoud, Perfume Oriental, Ferwer (ScentVerdict says EDP). Unisex per Superdrug and Ferwer; Perfume Oriental and ScentVerdict say women; supplier's Unisex used. Not the same as Hot Drip Dubai." + EXN + " Awaiting photos.",
  "peach and blackcurrant over rose, iris and white musk.", ["Floral", "Fruity", "Powdery"], ["Rose", "Floral", "Fruity", "Fresh"],
  name="Rise and Bling, Dubai", **X)

t = "Street Origins Singapore Prim Eau de Parfum 75ml"
F("6298042001466", B, t, "Unisex", "75", "32.49", "43.99", 1,
  [("Top", "Tea, Bergamot, Osmanthus"), ("Heart", "Orchid, Freesia, Jasmine, Rose, Orange Blossom"), ("Base", "Patchouli, Musk, Vanilla")],
  "Floral · Fresh · Musky", "Tea and osmanthus over orchid and jasmine, with soft musk and vanilla.",
  f"{t} is a graceful floral fragrance. Tea, bergamot and osmanthus open delicately, a heart of orchid, freesia, jasmine, rose and orange blossom follows, and it settles on a soft base of patchouli, musk and vanilla.",
  ["A delicate opening of tea, bergamot and osmanthus", "A lush floral heart of orchid, jasmine and rose", "A soft base of patchouli, musk and vanilla", "Elegant everyday Eau de Parfum"],
  "Notes confirmed by 4 sources (FilledWithBarakah, Splash, ScentVerdict, Carrefour UAE with this EAN), all tiers agree (orchid and orange blossom each in 3 of 4). 75ml EDP confirmed by Superdrug (EAN page) and others. Superdrug and ScentVerdict say unisex, Splash and Carrefour say women; supplier's Unisex used. Not the same as Singapore Proper. Awaiting photos.",
  "tea and osmanthus over orchid, jasmine, musk and vanilla.", ["Floral", "Fresh", "Musky"], ["Floral", "Jasmine", "Rose", "Fresh", "Vanilla"],
  name="Singapore Prim")

t = "Street Origins Singapore Proper Eau de Parfum 75ml"
F("6298042001336", B, t, "Unisex", "75", "32.49", "43.99", 1,
  [("Top", "Pepper, Raspberry, Bergamot"), ("Heart", "Smoke, Warm Spices, Red Apple"), ("Base", "Oud, Leather, Tonka Bean, Citrus Wood")],
  "Spicy · Leather · Woody", "Peppered raspberry over smoke and spice, with oud and leather.",
  f"{t} is a bold, spicy fragrance. Pepper, raspberry and bergamot open with heat, a heart of smoke, warm spices and red apple follows, and it settles on a rich base of oud, leather, tonka bean and citrus wood.",
  ["A peppery opening of raspberry and bergamot", "A smoky heart of warm spices and red apple", "A rich base of oud, leather and tonka", "Bold, polished character"],
  "Notes confirmed by 4 sources (FilledWithBarakah, Zaoud, Perfume Oriental, ScentVerdict), all tiers agree. Parfumo's entry shows a completely different pyramid with nonsense note names – not used. 75ml EDP and unisex confirmed by Superdrug (EAN page), Zaoud, ScentVerdict. Not the same as Singapore Prim. Awaiting photos.",
  "peppered raspberry over smoke, oud and leather.", ["Spicy", "Leather", "Woody"], ["Spicy", "Fruity", "Woody", "Oriental"],
  name="Singapore Proper")

write_outputs()
