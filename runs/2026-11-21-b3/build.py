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


AW = " Awaiting photos."
# ---------------- 1 Narciso Rodriguez For Her EDT set
t = "Narciso Rodriguez For Her Eau de Toilette 100ml Gift Set with 75ml Body Lotion"
GS("3423478559752", "Narciso Rodriguez", t, "Narciso Rodriguez For Her EDT 100ml & Body Lotion Set", "Women", "100", "54.99", "70.99", 5,
   [("Top", "Osmanthus, Bergamot"), ("Heart", "Musk, Amber"), ("Base", "Vetiver, Patchouli, Vanilla")],
   "Floral · Musky · Woody", "The modern musk classic, paired with its silky body lotion.",
   f"{t} brings together the original For Her Eau de Toilette and a matching body lotion. Osmanthus and bergamot open onto the famous musk heart warmed by amber, before vetiver, patchouli and vanilla settle on the skin.",
   ["Narciso Rodriguez For Her Eau de Toilette 100ml (spray)", "Narciso Rodriguez For Her Body Lotion 75ml"],
   ["The signature Narciso Rodriguez musk heart", "Soft osmanthus and bergamot opening", "A warm vetiver, patchouli and vanilla base", "Matching body lotion to layer and prolong the scent"],
   "EAN 3423478559752 matched on Paco Perfumerias UK and LoveNmour (EDT 100ml + body lotion 75ml, women). Pyramid from CaFleurEbon + LoveNmour: top tier differs (orange blossom vs wildflowers left out), only agreed notes shown. Launch 2003 per Parfumo and CaFleurEbon (not stated). This is the EDT, not the For Her EDP – check the box." + AW,
   "osmanthus, musk and amber over vetiver, with body lotion.", ["Floral", "Musky", "Woody"], ["Floral", "Woody"],
   name="Narciso Rodriguez For Her", **TC)

# ---------------- 2 Police Original set
t = "Police Original Eau de Toilette 100ml Gift Set with 100ml Shower Gel"
GS("0679602596190", "Police", t, "Police Original EDT 100ml & Shower Gel Gift Set", "Men", "100", "22.99", "29.99", 5,
   [("Top", "Lavender, Mint, Bergamot"), ("Heart", "Geranium, Violet"), ("Base", "Cedar, Musk, Sandalwood")],
   "Aromatic · Fougère · Fresh", "The original Police fougère: fresh, clean and easy to wear every day.",
   f"{t} pairs the 1998 Police Original Eau de Toilette with a matching shower gel. Lavender, mint and bergamot give a crisp start, geranium and violet follow, and it dries down to cedar, musk and sandalwood.",
   ["Police Original Eau de Toilette 100ml (spray)", "Police Original Shower Gel 100ml"],
   ["A crisp lavender and mint opening", "A classic aromatic fougère character", "A clean cedar, musk and sandalwood finish", "Matching shower gel for a complete routine"],
   "EAN 0679602596190 only found on two eBay UK listings (100ml EDT + 100ml shower gel, men); contents also confirmed by Perfume-Click and Cosmetify. Superdrug sells the same set under EAN 5055654031370. Some sellers list a 'shower shampoo' version – check the box says shower gel. Pyramid agreed by Fragrantica + ScentVerdict (Perfume-Click flat list matches); Parfumo gives a different pyramid. 1998." + AW,
   "lavender, mint and bergamot over cedar and musk, with shower gel.", ["Aromatic", "Fougere", "Fresh"], ["Lavender", "Fresh", "Woody"],
   name="Police Original", **TC)

# ---------------- 3 Police Potion for Her set
t = "Police Potion for Her Eau de Parfum 30ml Gift Set with 100ml Body Lotion"
GS("0679602142939", "Police", t, "Police Potion for Her EDP 30ml & Body Lotion Gift Set", "Women", "30", "19.49", "25.99", 5,
   [("Top", "Red Apple, Red Berries, Bergamot"), ("Heart", "Damask Rose, Magnolia, Orange Blossom, White Peach"), ("Base", "Vanilla, Salted Caramel, Amber, Benzoin")],
   "Floral · Fruity · Gourmand", "Red apple, rose and salted caramel in a sweet, seductive set.",
   f"{t} pairs Potion for Her Eau de Parfum with a perfumed body lotion. Red apple and berries open brightly, a bouquet of damask rose, magnolia, orange blossom and white peach follows, and it melts into vanilla, salted caramel, amber and benzoin.",
   ["Police Potion for Her Eau de Parfum 30ml (spray)", "Police Potion for Her Body Lotion 100ml"],
   ["A juicy red apple and berry opening", "A rich floral heart of rose and magnolia", "A warm gourmand base of vanilla and salted caramel", "Matching body lotion to layer the scent"],
   "EAN 0679602142939 matched on Welzo and BeautyBuys (EDP 30ml + body lotion 100ml, women); Superdrug and Cosma confirm contents. Pyramid agreed by Fragrantica + Flannels. Launch year not confirmed (2022 vs 2023), left out." + AW,
   "red apple, rose and salted caramel, with body lotion.", ["Floral", "Fruity", "Gourmand"], ["Fruity", "Floral", "Rose", "Vanilla"],
   name="Police Potion for Her", **PC)

# ---------------- 4 Police To Be #Freetodare Woman set
t = "Police To Be #Freetodare Woman Eau de Parfum 40ml Gift Set with 100ml Body Lotion"
GS("0679602153935", "Police", t, "Police To Be Freetodare Woman EDP 40ml Gift Set", "Women", "40", "20.49", "27.99", 5,
   [("Top", "Pear, Raspberry, Mandarin"), ("Heart", "Freesia, Jasmine"), ("Base", "Vanilla, Sandalwood, Cocoa")],
   "Fruity · Floral · Gourmand", "Playful pear and raspberry over a cocoa-vanilla glow.",
   f"{t} pairs To Be #Freetodare for Woman Eau de Parfum with a matching body lotion. Pear, raspberry and mandarin open, freesia and jasmine form the heart, and a sweet base of vanilla, sandalwood and cocoa finishes it.",
   ["Police To Be #Freetodare Woman Eau de Parfum 40ml (spray)", "Police To Be #Freetodare Body Lotion 100ml"],
   ["A juicy pear and raspberry opening", "A soft freesia and jasmine heart", "A cosy vanilla, sandalwood and cocoa base", "Matching body lotion to layer the scent"],
   "EAN 0679602153935 found on Gadcet only (40ml EDP gift set, women); contents (EDP 40ml + body lotion 100ml) confirmed by Superdrug, Cosmetify, The Perfume Shop and Flannels. Pyramid from The Perfume Shop + Fragrantica; heliotrope (heart) on one side only, left out. Superdrug lists men's-looking notes and calls it unisex – ignored; supplier gender Women kept. Launch year not confirmed." + AW,
   "pear and raspberry over vanilla and cocoa, with body lotion.", ["Fruity", "Floral", "Gourmand"], ["Fruity", "Floral", "Jasmine", "Vanilla"],
   name="To Be #Freetodare Woman", **PC)

# ---------------- 5 Police To Be Born To Shine Woman set (needs-review: EDT vs EDP)
t = "Police To Be Born To Shine Woman Eau de Parfum 40ml Gift Set with 100ml Body Lotion"
GS("0679602159968", "Police", t, "Police To Be Born To Shine Woman EDP 40ml Gift Set", "Women", "40", "20.49", "27.99", 5,
   [("Top", "Mandarin, Bergamot, Apple Blossom, Cinnamon"), ("Heart", "Jasmine, Coffee, Damask Rose"), ("Base", "Vanilla, Patchouli, Sandalwood, Cashmere Wood")],
   "Oriental · Gourmand · Fruity", "Sparkling citrus, coffee and rose over a warm vanilla base.",
   f"{t} pairs To Be Born To Shine for Woman with a matching body lotion. Mandarin, bergamot and apple blossom with a touch of cinnamon open, jasmine, coffee and damask rose follow, and vanilla, patchouli, sandalwood and cashmere wood finish it.",
   ["Police To Be Born To Shine Woman Eau de Parfum 40ml (spray)", "Police To Be Born To Shine Body Lotion 100ml"],
   ["A bright mandarin and apple blossom opening", "A rich jasmine, coffee and rose heart", "A warm vanilla and cashmere wood base", "Matching body lotion to layer the scent"],
   "NEEDS REVIEW: supplier name says 40ml EDT, but Branded Household (EAN 679602159968 match), Superdrug and Lyko all sell this set as EDP 40ml + body lotion 100ml, so listed as Eau de Parfum – check the box before publishing. Pyramid Branded Household + Parfumo (Lyko agrees); plum vs pomarose (heart) and cedarwood (base) disagree, left out. 2022." + AW,
   "mandarin, coffee and rose over vanilla, with body lotion.", ["Oriental", "Gourmand", "Fruity"], ["Vanilla", "Jasmine", "Rose", "Oriental"],
   name="To Be Born To Shine Woman", status="needs-review", **PC)

# ---------------- 6 Police To Be My Avatar for Woman set
t = "Police To Be My Avatar for Woman Eau de Parfum 40ml Gift Set with 100ml Body Lotion"
GS("0679602133937", "Police", t, "Police To Be My Avatar Woman EDP 40ml Gift Set", "Women", "40", "20.49", "26.99", 5,
   [("Top", "Lemon, Mandarin, Mango"), ("Heart", "White Musk, Osmanthus, Lotus Flower"), ("Base", "Cedarwood, Sugar Cane, Clearwood")],
   "Fruity · Musky · Woody", "Juicy mango and citrus wrapped in soft white musk.",
   f"{t} pairs To Be My Avatar for Woman Eau de Parfum with a matching body lotion. Lemon, mandarin and mango open, white musk, osmanthus and lotus form the heart, and cedarwood, sugar cane and clearwood give a smooth woody finish.",
   ["Police To Be My Avatar for Woman Eau de Parfum 40ml (spray)", "Police To Be My Avatar Body Lotion 100ml"],
   ["A juicy mango and citrus opening", "A soft white musk and osmanthus heart", "A smooth, sweet woody base", "Matching body lotion to layer the scent"],
   "EAN 0679602133937 matched on Rossmann.de (EAN as product ID; My Avatar for Woman EDP 40ml + body lotion 100ml); The Perfume Shop and Superdrug confirm contents. Women's version (the men's My Avatar set is EDT). Pyramid Rossmann + Lyko (agree fully). Launch 2024 per The Perfume Shop only, left out." + AW,
   "mango and citrus over white musk and woods, with body lotion.", ["Fruity", "Musky", "Woody"], ["Fruity", "Citrus", "Woody"],
   name="To Be My Avatar for Woman", **PC)

# ---------------- 7 Reebok Move Your Spirit for Women set
t = "Reebok Move Your Spirit for Women Eau de Toilette 100ml Gift Set with 150ml Body Spray"
GS("8436581946239", "Reebok", t, "Reebok Move Your Spirit Women EDT 100ml & Body Spray Set", "Women", "100", "20.99", "27.99", 5,
   [("Top", "Pink Pepper, Red Fruits"), ("Heart", "Freesia, Peony"), ("Base", "Vanilla, Musk")],
   "Fruity · Floral · Musky", "Red fruits and peony with a soft vanilla-musk finish.",
   f"{t} pairs Move Your Spirit for Women Eau de Toilette with a matching deodorant body spray. Pink pepper and red fruits give an energetic start, freesia and peony bloom in the heart, and it settles on vanilla and musk.",
   ["Reebok Move Your Spirit for Women Eau de Toilette 100ml (spray)", "Reebok Move Your Spirit Deodorant Body Spray 150ml"],
   ["A lively pink pepper and red fruit opening", "A fresh freesia and peony heart", "A soft vanilla and musk finish", "Matching body spray for an all-over refresh"],
   "EAN 8436581946239 matched on Ratans Online and Tienda La Fe: EDT 100ml + 150ml deodorant body spray (supplier '150ml Body' = body spray, as in the stockfile name). Pyramid FragranceNet + eCosmetics: cherry blossom/pineapple (top), orchid (heart), whipped cream/woods (base) disagree, left out. 2022." + AW,
   "red fruits and peony over vanilla musk, with body spray.", ["Fruity", "Floral", "Musky"], ["Fruity", "Floral", "Vanilla"],
   name="Move Your Spirit for Women", **TC)

# ---------------- 8 Rochas Girl set
t = "Rochas Girl Eau de Toilette 60ml Gift Set with 100ml Shower Gel"
GS("3386460127608", "Rochas", t, "Rochas Girl EDT 60ml & Shower Gel Gift Set", "Women", "60", "22.49", "28.99", 5,
   [("Top", "Neroli, Blackcurrant, Pink Pepper"), ("Heart", "Orange Blossom, Jasmine, Orchid"), ("Base", "Vanilla, Sandalwood, Cedar")],
   "Floral · Woody · Citrus", "A bright, joyful floral with a soft woody heart.",
   f"{t} pairs Rochas Girl Eau de Toilette, created by Anne Flipo in 2021, with a matching exfoliating shower gel. Neroli, blackcurrant and pink pepper sparkle first, orange blossom, jasmine and orchid follow, and vanilla, sandalwood and cedar round it off.",
   ["Rochas Girl Eau de Toilette 60ml (spray)", "Rochas Girl Exfoliating Shower Gel 100ml"],
   ["A sparkling neroli and blackcurrant opening", "A sunny orange blossom and jasmine heart", "A soft vanilla and sandalwood base", "Matching shower gel for a complete routine"],
   "EAN 3386460127608 matched on Paris Parfums and Envie2Parfum (EDT 60ml + exfoliating shower gel 100ml, women). Supplier stockfile lists two EANs for this line (3386460127608, 3386460133647 – Superdrug uses the second). Pyramid Superdrug + Interparfums (agree fully). Anne Flipo, 2021 (Superdrug + NST)." + AW,
   "neroli and blackcurrant over orange blossom and vanilla, with shower gel.", ["Floral", "Woody", "Citrus"], ["Floral", "Citrus", "Jasmine", "Sandalwood"],
   name="Rochas Girl", **TC)

# ---------------- 9 L'Homme Rochas set (needs-review: 3rd item)
t = "Rochas L'Homme Rochas Eau de Toilette 100ml Gift Set with Shower Gel and Aftershave Balm"
GS("3386460115223", "Rochas", t, "L'Homme Rochas EDT 100ml 3-Piece Gift Set", "Men", "100", "39.99", "51.99", 5,
   [("Top", "Blood Orange, Pineapple, Cardamom"), ("Heart", "Juniper Berries, Geranium, Basil"), ("Base", "Patchouli, Tonka Bean")],
   "Fougère · Oriental · Aromatic", "Zesty blood orange and juniper over warm tonka.",
   f"{t} brings together L'Homme Rochas Eau de Toilette, a shower gel and an aftershave balm. Blood orange, pineapple and cardamom open, juniper, geranium and basil give an aromatic heart, and patchouli and tonka bean warm the base.",
   ["L'Homme Rochas Eau de Toilette 100ml (spray)", "L'Homme Rochas Shower Gel 100ml", "L'Homme Rochas Aftershave Balm 100ml"],
   ["A zesty blood orange and pineapple opening", "An aromatic juniper and basil heart", "A warm patchouli and tonka finish", "Shower gel and aftershave balm for a complete routine"],
   "NEEDS REVIEW: supplier name says the third item is 100ml body lotion, but Welzo, eBay and Envie2Parfum (all EAN 3386460115223) say 100ml AFTERSHAVE BALM; listed as aftershave balm – check the box. Superdrug and bol.com also match the EAN. Pyramid Superdrug + Notino; moss/musk (base) on one side only, left out. Oriental fougère, 2020." + AW,
   "blood orange and juniper over tonka, with shower gel and balm.", ["Fougere", "Oriental", "Aromatic"], ["Citrus", "Spicy", "Oriental"],
   name="L'Homme Rochas", status="needs-review", **TC)

# ---------------- 10 Amo Ferragamo Flowerful set
t = "Salvatore Ferragamo Amo Ferragamo Flowerful Eau de Toilette 50ml Gift Set with Body Lotion and Shower Gel"
GS("8052086379220", "Salvatore Ferragamo", t, "Amo Ferragamo Flowerful EDT 50ml 3-Piece Gift Set", "Women", "50", "30.99", "38.99", 5,
   [("Top", "Yuzu Blossom, Blackcurrant, Bitter Accord"), ("Heart", "Pink Peony, Jasmine, Plum Blossom"), ("Base", "Blond Woods, Musk, Vanilla")],
   "Fruity · Floral · Woody", "A joyful bouquet of peony and jasmine with a sparkling yuzu twist.",
   f"{t} brings together Amo Ferragamo Flowerful Eau de Toilette, created by Marie Salamagne in 2019, with a body lotion and shower gel. Yuzu blossom, blackcurrant and a bitter accord open, pink peony, jasmine and plum blossom bloom in the heart, and blond woods, musk and vanilla finish it.",
   ["Amo Ferragamo Flowerful Eau de Toilette 50ml (spray)", "Amo Ferragamo Flowerful Body Lotion 50ml", "Amo Ferragamo Flowerful Shower Gel 50ml"],
   ["A sparkling yuzu and blackcurrant opening", "A fresh peony and jasmine bouquet", "A soft blond wood, musk and vanilla base", "Body lotion and shower gel for a complete routine"],
   "EAN 8052086379220 matched on Superdrug and Beautyol (EDT 50ml + body lotion 50ml + shower gel 50ml, women). Supplier form column says Eau de Parfum but Flowerful exists only as EDT (NST, Lookfantastic, Flannels; supplier name also says EDT) – listed as EDT. Pyramid Parfumo + Interparfums; Superdrug's different pyramid ignored. Marie Salamagne, 2019." + AW,
   "yuzu and peony over blond woods and vanilla, with lotion and gel.", ["Floral", "Fruity", "Woody"], ["Floral", "Fruity", "Jasmine", "Vanilla"],
   name="Amo Ferragamo Flowerful", **TC)

write_outputs()
