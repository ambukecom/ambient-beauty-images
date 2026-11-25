import sys; sys.path.insert(0, "/home/claude/ambient-beauty-images/workflow")
from lib import *
TC = dict(conc="Eau De Toilette", concl="Eau de Toilette")
TI = dict(conc="Eau De Toilette", concl="Eau de Toilette Intense")
PC = dict(conc="Eau De Parfum", concl="Eau de Parfum")
PI = dict(conc="Eau De Parfum", concl="Eau de Parfum Intense")
AW = " Awaiting photos."

# 1 L'Eau d'Issey Eau de Parfum Intense 100ml (refillable)
t = "Issey Miyake L'Eau d'Issey Eau de Parfum Intense 100ml"
F("3423222118341", "Issey Miyake", t, "Women", "100", "52.49", "67.99", 5,
  [("Top", "Posidonia Accord"), ("Heart", "Ylang-Ylang"), ("Base", "Vanilla")],
  "Floral · Aquatic", "The iconic water fragrance, deepened and made refillable.",
  f"{t} is a floral aquatic fragrance for women, launched in 2025 and created by perfumer Amandine Clerc-Marie. A marine posidonia accord opens it with a fresh, watery glow, a heart of sunny ylang-ylang brings rich floral warmth, and it settles into a soft, enveloping vanilla. The bottle unscrews so it can be refilled from the dedicated refill.",
  ["A fresh posidonia (sea grass) accord opening", "A warm, sunny ylang-ylang heart", "A soft, enveloping vanilla base", "Refillable 100ml Eau de Parfum Intense"],
  "EAN 3423222118341 matched in Galaxus.ch page data (L'Eau d'Issey EDP Intense 100ml); sibling EANs consistent at The Perfume Shop/brand. Pyramid agreed by brand (isseymiyakeparfums.com), The Perfume Shop and Schiphol (posidonia / ylang-ylang / vanilla). Floral aquatic, 2025, Amandine Clerc-Marie per brand + Parfumo. Refillable per brand and The Perfume Shop. Do not confuse with older L'Eau d'Issey Intense. Women." + AW,
  "posidonia over ylang-ylang and vanilla.", ["Floral", "Aquatic"], ["Floral", "Aquatic", "Vanilla", "Fresh"],
  name="L'Eau d'Issey Eau de Parfum Intense", **PI)

# 2 Pour Homme Eau & Cedre EDT Intense 50ml
t = "Issey Miyake L'Eau d'Issey Pour Homme Eau & Cèdre Eau de Toilette Intense 50ml"
F("3423222048037", "Issey Miyake", t, "Men", "50", "38.49", "48.99", 5,
  [("Top", "Grapefruit, Cardamom, Cypress"), ("Heart", "Cedarwood"), ("Base", "Vetiver, Patchouli")],
  "Woody · Fresh · Aquatic", "Water meets wood in a fresh, intense cedar.",
  f"{t} is a woody fragrance for men, released in 2022 to mark 30 years of L'Eau d'Issey. Grapefruit, cardamom and cypress open it fresh and lightly spiced, a heart of cedarwood brings a clean, dry woodiness, and it settles into an earthy base of vetiver and patchouli.",
  ["A fresh grapefruit, cardamom and cypress opening", "A clean, dry cedarwood heart", "An earthy vetiver and patchouli base", "Handy 50ml Eau de Toilette Intense"],
  "EAN 3423222048037 matched on Shop-apotheke (Eau & Cèdre EDT Intense 50ml) and in brand URL. Pyramid: cardamom/cedarwood/vetiver+patchouli agreed by brand UK store, The Perfume Shop, Scento, Escentual; grapefruit+cypress top from brand UK store + Shop-apotheke (Escentual places Calone in opening; Calone left out). Woody per The Perfume Shop and brand. 2022 per The Perfume Shop + Scento. Perfumer single-source, left out. Men." + AW,
  "grapefruit and cardamom over cedarwood and vetiver.", ["Woody", "Fresh", "Aquatic"], ["Woody", "Citrus", "Spicy", "Fresh"],
  name="Eau & Cèdre", **TI)
P[-1]["seo"] = ("Issey Miyake Pour Homme Eau & Cèdre EDT Intense 50ml", P[-1]["seo"][1])

# 3 Pour Homme EDT 75ml
t = "Issey Miyake L'Eau d'Issey Pour Homme Eau de Toilette 75ml"
F("3423470311358", "Issey Miyake", t, "Men", "75", "38.49", "50.99", 5,
  [("Top", "Yuzu, Mandarin, Verbena, Cypress, Coriander, Sage"), ("Heart", "Blue Water Lily, Nutmeg, Cinnamon, Saffron, Geranium"), ("Base", "Amber, Tobacco, Musk, Sandalwood, Vetiver")],
  "Woody · Citrus · Aquatic", "The fresh, aquatic classic that defined a generation.",
  f"{t} is a woody aquatic fragrance for men, created in 1994 by perfumer Jacques Cavallier as the brand's first men's scent. Yuzu, mandarin and verbena open it zesty and bright with aromatic coriander and sage, a heart of blue water lily, nutmeg, cinnamon and saffron adds a watery, gently spiced freshness, and it dries down to warm amber, tobacco, musk, sandalwood and vetiver.",
  ["A zesty yuzu, mandarin and verbena opening", "A watery, gently spiced water lily and nutmeg heart", "A warm amber, sandalwood and vetiver base", "A modern classic since 1994"],
  "EAN 3423470311358 matched on The Perfume Shop UK (75ml variant). Pyramid agreed by brand UK store and The Perfume Shop on all tiers (Scento superset; cypriol not in Scento so left out). 1994, Jacques Cavallier per The Perfume Shop + Scento. Woody per John Lewis; citrus-aquatic per descriptions. Not the 2025 Pour Homme EDP. Men." + AW,
  "yuzu and mandarin over water lily, nutmeg and sandalwood.", ["Woody", "Citrus", "Aquatic"], ["Citrus", "Aquatic", "Spicy", "Woody", "Sandalwood", "Fresh"],
  name="L'Eau d'Issey Pour Homme", **TC)

# 4 Pour Homme Solar Lavender EDT Intense 50ml
t = "Issey Miyake L'Eau d'Issey Pour Homme Solar Lavender Eau de Toilette Intense 50ml"
F("3423222106201", "Issey Miyake", t, "Men", "50", "29.99", "39.99", 5,
  [("Top", "Sichuan Pepper"), ("Heart", "Lavender"), ("Base", "Cedarwood")],
  "Aromatic · Woody · Spicy", "Sun-warmed lavender with a spark of pepper.",
  f"{t} is an aromatic woody fragrance for men, launched in 2024 and created by perfumer Marie Salamagne. Sichuan pepper opens it with a bright, tingling spice, a heart of Provence lavender brings a sunny aromatic freshness, and it settles into a dry, woody cedarwood accord.",
  ["A bright, tingling Sichuan pepper opening", "A sunny Provence lavender heart", "A dry, woody cedarwood base", "Handy 50ml Eau de Toilette Intense"],
  "EAN 3423222106201 appears in brand (isseymiyakeparfums.com) product URL; The Perfume Shop shows sibling 3423222106225 for 100ml (no retailer page labels 106201 explicitly). Pyramid agreed by The Perfume Shop, Parfumo and Allbeauty on all tiers. 2024, Marie Salamagne per The Perfume Shop + Parfumo. Aromatic woody per brand. Men." + AW,
  "Sichuan pepper over lavender and cedarwood.", ["Aromatic", "Woody", "Spicy"], ["Lavender", "Spicy", "Woody", "Fresh"],
  name="Solar Lavender", **TI)
P[-1]["seo"] = ("Issey Miyake Pour Homme Solar Lavender EDT Intense 50ml", P[-1]["seo"][1])

# 5 Pour Homme Sport EDT 50ml
t = "Issey Miyake L'Eau d'Issey Pour Homme Sport Eau de Toilette 50ml"
F("3423474867059", "Issey Miyake", t, "Men", "50", "26.99", "33.99", 5,
  [("Top", "Bergamot, Grapefruit"), ("Heart", "Nutmeg"), ("Base", "Cedarwood, Vetiver")],
  "Citrus · Aromatic · Woody", "Energising citrus freshness for an active lifestyle.",
  f"{t} is a fresh citrus aromatic fragrance for men, created by perfumer Jacques Cavallier and launched in 2012. Bergamot and grapefruit open it crisp and energising, a heart of nutmeg adds a warm, spicy edge, and it dries down to clean cedarwood and vetiver.",
  ["A crisp bergamot and grapefruit opening", "A warm nutmeg heart", "A clean cedarwood and vetiver base", "Handy 50ml Eau de Toilette"],
  "EAN 3423474867059 matched on Kruidvat.nl (Pour Homme Sport EDT 50ml). Pyramid: bergamot+grapefruit / nutmeg / vetiver agreed by brand UK store, Osmoz, Escentual; cedarwood by brand + Osmoz (Escentual says sandalwood). Leather heart brand-only, left out. Jacques Cavallier per Osmoz + Escentual; 2012 per Osmoz (NST reported new Dec 2011). Men." + AW,
  "bergamot and grapefruit over nutmeg and cedarwood.", ["Citrus", "Aromatic", "Woody"], ["Citrus", "Spicy", "Woody", "Fresh"],
  name="L'Eau d'Issey Pour Homme Sport", **TC)

# 6 Pure Petale de Nectar EDT 50ml
t = "Issey Miyake L'Eau d'Issey Pure Pétale de Nectar Eau de Toilette 50ml"
F("3423478753754", "Issey Miyake", t, "Women", "50", "35.99", "48.99", 4,
  [("Top", "Honey, Pear"), ("Heart", "Rose"), ("Base", "Sandalwood, Ambergris, Cashmeran")],
  "Floral · Aquatic · Fruity", "A drop of rose nectar, sweet and luminous.",
  f"{t} is an aquatic floral fragrance for women, launched in 2019 as part of the L'Eau d'Issey Pure collection. Honey and juicy pear open it sweet and radiant, a heart of rose brings a soft, nectar-like bloom, and it settles into the Pure signature of sandalwood with an ambergris and cashmeran accord. It comes in a rose-gold bottle inspired by a drop of rose nectar.",
  ["A sweet honey and pear opening", "A soft, nectar-like rose heart", "A warm sandalwood, ambergris and cashmeran base", "Handy 50ml Eau de Toilette"],
  "EAN 3423478753754 matched on The Perfume Shop IE (50ml). Pyramid agreed by Escentual, FragranceNet and The Perfume Shop (cashmeran = 'cashmere wood' on FragranceNet). Aquatic floral per Escentual + NST. 2019 per The Perfume Shop, FragranceNet, NST. Perfumer single-source, left out. Looks discontinued at some retailers. Women." + AW,
  "honey and pear over rose and sandalwood.", ["Floral", "Aquatic", "Fruity"], ["Floral", "Rose", "Fruity", "Sandalwood", "Aquatic"],
  name="Pure Pétale de Nectar", **TC)
P[-1]["seo"] = ("Issey Miyake L'Eau d'Issey Pure Pétale de Nectar EDT 50ml", P[-1]["seo"][1])

# 7 Rose & Rose EDP Intense 50ml
t = "Issey Miyake L'Eau d'Issey Rose & Rose Eau de Parfum Intense 50ml"
F("3423478515857", "Issey Miyake", t, "Women", "50", "40.99", "52.99", 5,
  [("Top", "Pink Pepper, Raspberry, Pear"), ("Heart", "Bulgarian Rose, Osmanthus"), ("Base", "Patchouli, Cashmeran, Ambrox")],
  "Floral · Fruity", "Two roses, one intense floral signature.",
  f"{t} is a fruity floral fragrance for women, launched in 2019. Pink pepper, raspberry and pear open it juicy and sparkling, a heart of Bulgarian rose and osmanthus brings a rich, velvety rose bloom, and it settles into a warm base of patchouli, cashmeran and ambrox. The soft-touch cap is designed to feel like petals.",
  ["A juicy pink pepper, raspberry and pear opening", "A rich Bulgarian rose and osmanthus heart", "A warm patchouli, cashmeran and ambrox base", "Handy 50ml Eau de Parfum Intense"],
  "EAN 3423478515857 matched on Galaxus.ch (Rose & Rose EDP 50ml; Galaxus omits 'Intense', all other retailers say Intense). Pyramid agreed by Parfumo, Escentual, Lookfantastic, Lyko, FragranceNet; ambrox per Parfumo, Escentual, Lyko. Fruity floral per Parfumo + Galaxus. 2019 per Parfumo + FragranceNet. Perfumers single-source, left out. Women." + AW,
  "pink pepper and raspberry over rose and patchouli.", ["Floral", "Fruity"], ["Floral", "Rose", "Fruity", "Spicy", "Woody"],
  name="Rose & Rose", **PI)

# 8 Solar Violet EDT Intense 50ml
t = "Issey Miyake L'Eau d'Issey Solar Violet Eau de Toilette Intense 50ml"
F("3423222105860", "Issey Miyake", t, "Women", "50", "29.99", "37.99", 5,
  [("Top", "Pear"), ("Heart", "Violet Leaf Absolute"), ("Base", "Iris")],
  "Floral · Fruity · Powdery", "Sun-kissed violet with a juicy, luminous glow.",
  f"{t} is a fruity floral fragrance for women, launched in 2024 and created by perfumer Marie Salamagne. Juicy pear opens it bright and luminous, a heart of violet leaf absolute from Egypt brings a fresh, green floral note, and it settles into soft, powdery iris. It is vegan, with around 90% natural-origin ingredients, in a bottle made with 20% recycled glass and a wooden cap.",
  ["A juicy, luminous pear opening", "A fresh, green violet leaf heart", "A soft, powdery iris base", "Vegan formula with around 90% natural-origin ingredients"],
  "EAN 3423222105860 matched on The Perfume Shop UK (50ml, code 1295098). Pyramid agreed by brand UK site, The Perfume Shop, Escentual, Boots IE. Fruity floral per all. 2024 per The Perfume Shop + NST; Marie Salamagne per The Perfume Shop + Escentual. Vegan/90% natural origin/20% recycled glass/wood cap per brand, The Perfume Shop, Escentual. NST called it limited edition - permanence not claimed. Women." + AW,
  "pear over violet leaf and iris.", ["Floral", "Fruity", "Powdery"], ["Floral", "Fruity", "Fresh"],
  name="Solar Violet", **TI)

# 9 Pour Homme Vetiver EDT Intense 50ml
t = "Issey Miyake L'Eau d'Issey Pour Homme Vétiver Eau de Toilette Intense 50ml"
F("3423222090715", "Issey Miyake", t, "Men", "50", "29.99", "40.99", 5,
  [("Top", "Ginger"), ("Heart", "Clary Sage"), ("Base", "Vetiver")],
  "Woody · Aromatic · Spicy", "Powerful Haitian vetiver with a fresh, spicy kick.",
  f"{t} is a woody fragrance for men, launched in 2023. Ginger opens it with a fresh, spicy kick, a heart of clary sage adds an aromatic, herbal character, and it settles into a powerful, earthy vetiver from Haiti. It is vegan, with 93% natural-origin ingredients, in a bottle made with 20% recycled glass and a natural wood cap.",
  ["A fresh, spicy ginger opening", "An aromatic clary sage heart", "A powerful, earthy Haitian vetiver base", "Vegan formula with 93% natural-origin ingredients"],
  "EAN 3423222090715 matched on The Perfume Shop UK (50ml). Brand UK site, Escentual and The Perfume Shop sell it as EDT Intense, so 'Intense' added to supplier title (supplier name also had '?' for apostrophes). Pyramid agreed by brand UK site, The Perfume Shop, Escentual. 2023 per Escentual + NST (The Perfume Shop says 2017, ignored). Vegan/93%/Haiti vetiver per brand, The Perfume Shop, Escentual. Men." + AW,
  "ginger over clary sage and vetiver.", ["Woody", "Aromatic", "Spicy"], ["Woody", "Spicy", "Fresh"],
  name="L'Eau d'Issey Pour Homme Vétiver", **TI)
P[-1]["seo"] = ("Issey Miyake Pour Homme Vétiver EDT Intense 50ml", P[-1]["seo"][1])

# 10 Nuit d'Issey Bleu Astral EDT 125ml
t = "Issey Miyake Nuit d'Issey Bleu Astral Eau de Toilette 125ml"
F("3423474889259", "Issey Miyake", t, "Men", "125", "34.99", "46.99", 5,
  [("Top", "Lime, Coriander"), ("Heart", "Leather"), ("Base", "Amber Woods")],
  "Woody · Leather · Fresh", "A fresh, starry take on the night.",
  f"{t} is a fresh woody fragrance for men, launched in 2017 as a flanker of Nuit d'Issey. Zesty lime and coriander open it bright and aromatic, a heart of smooth leather brings depth and character, and it settles into warm amber woods.",
  ["A zesty lime and coriander opening", "A smooth leather heart", "A warm amber woods base", "Generous 125ml Eau de Toilette"],
  "EAN 3423474889259 matched on Kruidvat.nl (Nuit d'Issey Pour Homme Bleu Astral EDT 125ml). Supplier spelling 'Belu' corrected to 'Bleu'. Pyramid agreed by FragranceNet and fragrancereview (lime+coriander / leather / amber woods); vetiver untiered (NST, MightyApe), left out. Woody with leather facets. 2017 per FragranceNet, NST, fragrancereview. Men." + AW,
  "lime and coriander over leather and amber woods.", ["Woody", "Leather", "Fresh"], ["Citrus", "Spicy", "Woody", "Fresh"],
  name="Nuit d'Issey Bleu Astral", **TC)

P[4]["seo"] = ("Issey Miyake L'Eau d'Issey Pour Homme Sport EDT 50ml", P[4]["seo"][1])
P[6]["seo"] = ("Issey Miyake L'Eau d'Issey Rose & Rose EDP Intense 50ml", P[6]["seo"][1])
P[7]["seo"] = ("Issey Miyake L'Eau d'Issey Solar Violet EDT Intense 50ml", P[7]["seo"][1])
for p in P:  # SEO description should lead with the (shortened) SEO title
    st, sd = p["seo"]
    if sd.startswith(p["title"]) and st != p["title"][:60]:
        p["seo"] = (st, st + sd[len(p["title"]):])
    elif len(sd) > 160:
        p["seo"] = (st, st + sd[len(p["title"]):])
write_outputs()
