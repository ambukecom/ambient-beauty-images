import sys; sys.path.insert(0, "/home/claude/ambient-beauty-images/workflow")
from lib import *
TC = dict(conc="Eau De Toilette", concl="Eau de Toilette")
PC = dict(conc="Eau De Parfum", concl="Eau de Parfum")
AW = " Awaiting photos."

def seo(t, d):
    """Override SEO for long titles: short SEO title + description built from it."""
    P[-1]["seo"] = (t, f"{t}: {d}" + FREE)

# 1 Lacoste L.12.12 Noir Intense EDT 100ml
t = "Lacoste Eau de Lacoste L.12.12 Noir Intense Eau de Toilette 100ml"
F("0737052662664", "Lacoste", t, "Men", "100", "44.99", "60.99", 5,
  [("Top", "Watermelon, Basil"), ("Heart", "Lavender, Verbena"), ("Base", "Dark Chocolate, Cashmeran, Patchouli")],
  "Aromatic · Fougère · Gourmand", "Cool watermelon and basil over a dark chocolate base.",
  f"{t} is an aromatic fougère fragrance for men from the Eau de Lacoste L.12.12 polo-shirt collection, launched in 2013. Juicy watermelon and green basil open it cool and fresh, a heart of lavender and verbena adds an aromatic, clean lift, and it dries down to a warm, unexpected base of dark chocolate, cashmeran and patchouli.",
  ["A cool watermelon and basil opening", "An aromatic lavender and verbena heart", "A warm dark chocolate, cashmeran and patchouli base", "Generous 100ml Eau de Toilette"],
  "NEEDS REVIEW: EAN 0737052662664 not matched on any retailer page (0737052 prefix = older P&G-licence stock, likely pre-2018 edition). 'Noir Intense' name used by FragranceNet + Aster (100ml EDT, men); most UK/EU retailers call it 'L.12.12 Noir'. Please check box name/EAN. Pyramid agreed by Osmoz, Escentual, Aster (FragranceNet/Parfumo split tiers slightly). 2013 per NST, Osmoz, Parfumo. Perfumer left out (sources disagree). Aromatic fougère per Escentual + Osmoz. Men." + AW,
  "watermelon and basil over lavender and dark chocolate.", ["Aromatic", "Fougere", "Gourmand"], ["Fruity", "Lavender", "Fresh"],
  name="L.12.12 Noir Intense", status="needs-review", **TC)
seo("Lacoste L.12.12 Noir Intense Eau de Toilette 100ml", "watermelon, lavender and dark chocolate.")

# 2 Lacoste L.12.12 French Panache Pour Lui EDT 100ml
t = "Lacoste Eau de Lacoste L.12.12 Pour Lui French Panache Eau de Toilette 100ml"
F("3614228228749", "Lacoste", t, "Men", "100", "43.99", "59.99", 5,
  [("Top", "Mandarin, Cardamom, Lemon"), ("Heart", "Red Apple, Lavandin"), ("Base", "Sandalwood, Patchouli")],
  "Aromatic · Fresh · Woody", "A bright, spicy-fresh take on French style.",
  f"{t} is a fresh aromatic fragrance for men, launched in 2019 as a celebration of French flair. Mandarin, lemon and cardamom open it sparkling and lightly spiced, a heart of crisp red apple and lavandin brings an aromatic freshness, and it settles into a smooth, woody base of sandalwood and patchouli.",
  ["A sparkling mandarin, lemon and cardamom opening", "A crisp red apple and lavandin heart", "A smooth sandalwood and patchouli base", "Generous 100ml Eau de Toilette"],
  "EAN 3614228228749 matched on Superdrug (L.12.12 French Panache Pour Lui EDT 100ml). Pyramid agreed by Superdrug, Lookfantastic, Notino (clay accord / narcissus only in some, left out). Aromatic per Lookfantastic, NST, Notino. 2019 per NST. Perfumer single-source, left out. Looks discontinued at Notino/Lookfantastic. Men." + AW,
  "mandarin, cardamom and apple over sandalwood.", ["Aromatic", "Fresh", "Woody"], ["Citrus", "Fruity", "Lavender", "Sandalwood"],
  name="L.12.12 French Panache Pour Lui", **TC)
seo("Lacoste L.12.12 French Panache Pour Lui EDT 100ml", "mandarin, apple and sandalwood.")

# 3 Lacoste L.12.12 Rose EDP 100ml
t = "Lacoste L.12.12 Rose Eau de Parfum 100ml"
F("3386460149211", "Lacoste", t, "Women", "100", "39.99", "54.99", 5,
  [("Top", "Green Mandarin, Mint"), ("Heart", "Rose, Musk"), ("Base", "Cedarwood, Amber")],
  "Floral · Fruity · Fresh", "Fresh rose with a cool green mandarin twist.",
  f"{t} is a fruity floral fragrance for women from the L.12.12 collection. Green mandarin and mint open it crisp and refreshing, a heart of rose and soft musk brings a clean, feminine bloom, and it settles into a warm base of cedarwood and amber.",
  ["A crisp green mandarin and mint opening", "A clean rose and musk heart", "A warm cedarwood and amber base", "Generous 100ml Eau de Parfum"],
  "NEEDS REVIEW: EAN 3386460149211 shown on The Perfume Shop but on its 50ml listing – please confirm the box is 100ml (supplier and Clean Variant say 100ml; OnBuy 100ml uses older Coty EAN 3614228836135). Supplier name 'L.12.12 Eau de Parfum Rose For Her' shortened to official 'L.12.12 Rose Eau de Parfum' (Lacoste.com, Boots). Pyramid agreed by The Perfume Shop, Interparfums, Parfumo (FragranceNet pyramid ignored). Fruity floral per Lacoste.com, Interparfums, Boots. Launch year disputed, left out. Women." + AW,
  "green mandarin and mint over rose and cedarwood.", ["Floral", "Fruity", "Fresh"], ["Rose", "Citrus", "Fresh", "Woody"],
  name="L.12.12 Rose", status="needs-review", **PC)

# 4 Lacoste Original EDP 100ml
t = "Lacoste Original Eau de Parfum 100ml"
F("3386460149969", "Lacoste", t, "Men", "100", "42.49", "57.99", 5,
  [("Top", "Bergamot, Pink Pepper, Cardamom"), ("Heart", "Lavender, Clary Sage"), ("Base", "Sandalwood, Patchouli, Tonka Bean")],
  "Woody · Fougère · Aromatic", "A modern woody fougère with timeless polish.",
  f"{t} is a woody fougère fragrance for men, launched in 2024 and created by perfumers Anne Flipo and Tanguy Guesnet. Bergamot, pink pepper and cardamom open it fresh and lightly spiced, a heart of lavender and clary sage gives it an aromatic, classic character, and it settles into a warm base of sandalwood, patchouli and tonka bean.",
  ["A fresh bergamot, pink pepper and cardamom opening", "An aromatic lavender and clary sage heart", "A warm sandalwood, patchouli and tonka base", "Generous 100ml Eau de Parfum"],
  "EAN 3386460149969 matched in Next ingredients PDF AE2338 (Original EDP 100ml); alt supplier EAN 3386460165969 not confirmed. Pyramid agreed by Lacoste.com, Notino UK, Manila Bulletin (TPS subset). Woody fougère per Lacoste.com + TPS. 2024 + Anne Flipo & Tanguy Guesnet per ScentAdvice, Manila Bulletin. Not the separate Original Parfum. Men." + AW,
  "bergamot and cardamom over lavender and sandalwood.", ["Woody", "Fougere", "Aromatic"], ["Lavender", "Spicy", "Citrus", "Sandalwood"],
  name="Lacoste Original", **PC)

# 5 Lalique Amethyst Eclat EDP 100ml
t = "Lalique Amethyst Éclat Eau de Parfum 100ml"
F("7640111501466", "Lalique", t, "Women", "100", "28.49", "37.99", 1,
  [("Top", "Raspberry, Blackcurrant, Nashi Pear"), ("Heart", "Peony, Magnolia, Bulgarian Rose"), ("Base", "Blackberry, Musk, Oxalis")],
  "Floral · Fruity", "Sparkling red berries and fresh, juicy florals.",
  f"{t} is a fruity floral fragrance for women, launched in 2014 and created by perfumer Nathalie Lorson as a brighter take on Amethyst. Raspberry, blackcurrant and nashi pear open it sparkling and juicy, a heart of peony, magnolia and Bulgarian rose blooms soft and radiant, and it settles into a base of blackberry, musk and oxalis.",
  ["A juicy raspberry, blackcurrant and pear opening", "A radiant peony, magnolia and rose heart", "A soft blackberry and musk base", "Generous 100ml Eau de Parfum"],
  "EAN 7640111501466 matched on Fruugo IE (Amethyst Eclat EDP 100ml) + Tendance-parfums image. Pyramid agreed by Lalique UK, Parfumo, Well.co.uk, Tendance. Fruity floral per Parfumo + Well. 2014 per Parfumo, Well, NST; Nathalie Lorson per Lalique.com, Parfumo, Well. Women." + AW,
  "raspberry and blackcurrant over peony and rose.", ["Floral", "Fruity"], ["Fruity", "Floral", "Rose"],
  name="Amethyst Éclat", **PC)

# 6 Lalique Amethyst Exquise EDP 100ml
t = "Lalique Amethyst Exquise Eau de Parfum 100ml"
F("7640171199481", "Lalique", t, "Women", "100", "33.49", "44.99", 4,
  [("Top", "Blackberry, Blackcurrant, Raspberry, Heliotrope"), ("Heart", "Orchid, Bulgarian Rose"), ("Base", "Vanilla, Sandalwood, Benzoin, Gardenia")],
  "Floral · Fruity · Oriental", "Dark berries wrapped in velvety rose and vanilla.",
  f"{t} is a fruity floral fragrance for women, launched in 2017 as a richer chapter of Lalique's Amethyst story. Blackberry, blackcurrant, raspberry and heliotrope open it dark and juicy, a heart of orchid and Bulgarian rose brings velvety elegance, and it settles into a warm, sensual base of vanilla, sandalwood, benzoin and gardenia.",
  ["A dark, juicy berry opening", "A velvety orchid and Bulgarian rose heart", "A warm vanilla, sandalwood and benzoin base", "Generous 100ml Eau de Parfum"],
  "EAN 7640171199481 matched on McGrocer (Amethyst Exquise EDP 100ml) + Tendance-parfums image. Pyramid agreed by Notino UK, McGrocer, Tendance. Fruity floral per Notino + Tendance. 2017 per McGrocer, Tendance, Parfumo. Perfumer single-source (Lalique.com), left out. Notino UK shows unavailable. Women." + AW,
  "dark berries over rose, vanilla and sandalwood.", ["Floral", "Fruity", "Oriental"], ["Fruity", "Rose", "Vanilla", "Sandalwood"],
  name="Amethyst Exquise", **PC)

# 7 Lalique Encre Noire Sport EDT 100ml (brand pyramid)
t = "Lalique Encre Noire Sport Eau de Toilette 100ml"
F("7640111500902", "Lalique", t, "Men", "100", "28.99", "36.99", 5,
  [("Top", "Grapefruit, Bergamot"), ("Base", "Cashmere Wood, Musk")],
  "Woody · Aromatic · Aquatic", "Fresh, sporty energy with a dark vetiver soul.",
  f"{t} is a fresh woody fragrance for men, launched in 2013 and created by perfumer Nathalie Lorson as the sporty sibling of Encre Noire. Grapefruit and bergamot open it zesty and energising, cypress, lavender, aquatic notes, nutmeg and vetiver bring an aromatic, watery depth, and it settles into a clean base of cashmere wood and musk.",
  ["A zesty grapefruit and bergamot opening", "Aromatic cypress, lavender and aquatic notes", "Bourbon and Haitian vetiver depth", "A clean cashmere wood and musk base"],
  "EAN 7640111500902 matched on Superdrug (Encre Noire Sport EDT 100ml) + Tendance-parfums image. Notes agreed by Lalique.com, NST, Tendance, but the middle tier differs (cypress/lavender/nutmeg/aquatic/vetiver placed differently), so pyramid shows only the agreed top and base; the other notes are named in the intro. Woody per brand/Superdrug/Tendance. 2013 + Nathalie Lorson per NST, Tendance, Lalique.com. Men." + AW,
  "grapefruit and bergamot over vetiver and cashmere wood.", ["Woody", "Aromatic", "Aquatic"], ["Citrus", "Woody", "Aquatic", "Fresh"],
  name="Encre Noire Sport", **TC)

# 8 Lalique L'Amour EDP 100ml
t = "Lalique L'Amour Eau de Parfum 100ml"
F("7640111499060", "Lalique", t, "Women", "100", "29.99", "38.99", 5,
  [("Top", "Neroli, Bergamot, Rosebud"), ("Heart", "Jasmine, Gardenia, Tuberose"), ("Base", "Musk, Sandalwood, Cedarwood")],
  "Floral · Woody · Musky", "A luminous white-floral bouquet, soft and romantic.",
  f"{t} is a floral fragrance for women, launched in 2013 and created by perfumer Nathalie Lorson. Neroli, bergamot and rosebud open it bright and fresh, a heart of jasmine, gardenia and tuberose blooms rich and romantic, and it settles into a soft base of musk, sandalwood and cedarwood.",
  ["A bright neroli, bergamot and rosebud opening", "A romantic jasmine, gardenia and tuberose heart", "A soft musk, sandalwood and cedarwood base", "Generous 100ml Eau de Parfum"],
  "EAN 7640111499060 confirmed only via Tendance-parfums 100ml image filename (30/50ml use 7640111499053) and barcode search returning L'Amour EDP 100ml listings. Pyramid agreed by Lalique.com, Parfumo, Tendance, McGrocer. Floral woody musk per Tendance + McGrocer (brand: floral). 2013 per McGrocer/Parfumo; Nathalie Lorson per Lalique.com, Parfumo, Tendance. 100ml sold at Harrods, Liberty. Women." + AW,
  "neroli and bergamot over jasmine and sandalwood.", ["Floral", "Woody", "Musky"], ["Floral", "Jasmine", "Citrus", "Sandalwood"],
  name="L'Amour", **PC)

# 9 Lalique White EDT 125ml
t = "Lalique White Eau de Toilette 125ml"
F("3454960024021", "Lalique", t, "Men", "125", "29.99", "38.99", 2,
  [("Top", "Lemon Leaf, Bergamot, Tamarind"), ("Heart", "White Pepper, Nutmeg, Cardamom, Violet"), ("Base", "Amber, Cedar, Musk")],
  "Aromatic · Citrus · Spicy", "Crisp citrus and white pepper, clean and sophisticated.",
  f"{t} is an aromatic citrus fragrance for men, launched in 2008 and created by perfumer Christine Nagel. Lemon leaf, bergamot and tamarind open it crisp and fresh, a heart of white pepper, nutmeg, cardamom and violet adds a refined spicy warmth, and it settles into a smooth base of amber, cedar and musk.",
  ["A crisp lemon leaf and bergamot opening", "A refined white pepper, nutmeg and cardamom heart", "A smooth amber, cedar and musk base", "Generous 125ml Eau de Toilette"],
  "EAN 3454960024021 matched on Superdrug (Lalique White EDT 125ml) + Tendance-parfums image. Supplier name 'Lalique Lalique White' shortened to brand name 'Lalique White'. Pyramid agreed by Superdrug, Tendance, NST (elemi + oakmoss not in all, left out). Aromatic citrus per Superdrug + Tendance. 2008 + Christine Nagel per Superdrug, Tendance, NST. Not the White in Black flanker. Men." + AW,
  "lemon leaf and bergamot over white pepper and cedar.", ["Aromatic", "Citrus", "Spicy"], ["Citrus", "Spicy", "Woody", "Fresh"],
  name="Lalique White", **TC)

# 10 Lalique Le Parfum EDP 100ml
t = "Lalique Le Parfum Eau de Parfum 100ml"
F("3454960020917", "Lalique", t, "Women", "100", "30.49", "40.99", 5,
  [("Top", "Bay Leaf, Bergamot, Pink Pepper"), ("Heart", "Jasmine, Heliotrope"), ("Base", "Vanilla, Patchouli, Sandalwood")],
  "Oriental · Floral · Spicy", "Warm, spicy vanilla with a seductive floral heart.",
  f"{t} is an oriental floral fragrance for women, launched in 2005 and created by perfumer Dominique Ropion. Bay leaf, bergamot and pink pepper open it fresh and spicy, a heart of jasmine and heliotrope brings a soft, powdery sweetness, and it settles into a warm, sensual base of vanilla, patchouli and sandalwood.",
  ["A spicy bay leaf, bergamot and pink pepper opening", "A soft jasmine and heliotrope heart", "A warm vanilla, patchouli and sandalwood base", "Generous 100ml Eau de Parfum"],
  "EAN 3454960020917 matched on Perfumesclub UK and Frenchfragrance (Le Parfum EDP 100ml). Pyramid agreed by Lalique UK, NST, Perfumesclub (tonka not in all, left out; Frenchfragrance list ignored). Oriental per NST + Perfumesclub. 2005 per NST + Perfumesclub; Dominique Ropion per brand + NST. Women." + AW,
  "bay leaf and pink pepper over jasmine and vanilla.", ["Oriental", "Floral", "Spicy"], ["Oriental", "Vanilla", "Jasmine", "Spicy"],
  name="Lalique Le Parfum", **PC)

write_outputs(".")
for p in P: print(p["status"], p["seo"][0], len(p["seo"][0]), len(p["seo"][1]))
