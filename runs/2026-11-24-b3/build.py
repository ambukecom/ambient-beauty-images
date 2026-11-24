import sys; sys.path.insert(0, "/home/claude/ambient-beauty-images/workflow")
from lib import *
TC = dict(conc="Eau De Toilette", concl="Eau de Toilette")
PC = dict(conc="Eau De Parfum", concl="Eau de Parfum")
AW = " Awaiting photos."

def TRIO(bc, gender, title, seo_t, price, cmp, qty, frags, hook, intro, love, note, seo_d, of, fr):
    """FCUK 3 x 25ml EDT gift set. frags = [(name, character, [(tier, notes)...]), ...]"""
    who = {"Men": ("Is it for men?", "Yes, it is a men's fragrance gift set."),
           "Women": ("Is it for women?", "Yes, it is a women's fragrance gift set.")}[gender]
    contents = [f"{n} Eau de Toilette 25ml (spray)" for n, _, _ in frags]
    blocks = [("What's in the set", ul(contents))]
    for n, ch, pyr in frags:
        blocks.append((n, f"<p>{ch}</p>" + kd(pyr)))
    qs = [("What's in the set?", "; ".join(contents) + "."),
          ("What do they smell like?", " ".join(f"{n}: {ch}" for n, ch, _ in frags)), who]
    add(cat_name="Fragrances", bc=bc, title=title, vendor="FCUK", type=TYPE[gender], gender=gender, cat=TAXON["perfume"],
        price=price, cmp=cmp, qty=qty, tags=["FCUK", gender, "Eau De Toilette"], seo=(seo_t, f"{seo_t}: {seo_d}" + FREE),
        status="needs-review", form="Eau de Toilette Gift Set", size="25", unit="ml", note=note, gpc=GPC["fragrance"],
        mf={"age-group": ["Adults"], "product-form": ["Spray"], "dispenser-type": ["Spray"], "olfactory-family": list(of), "fragrance": list(fr)},
        desc=body(hook, intro, blocks,
                  [("Brand", "FCUK (French Connection)"), ("Concentration", "Eau de Toilette"),
                   ("Contents", "3 x 25ml Eau de Toilette sprays"), ("Wear", gender)], love, qs))

# 1 Elie Saab Girl of Now Rose Petal EDP 90ml
t = "Elie Saab Girl of Now Rose Petal Eau de Parfum 90ml"
F("7640233342466", "Elie Saab", t, "Women", "90", "54.49", "69.99", 4,
  [("Top", "Sichuan Pepper, Pink Peach"), ("Heart", "Magnolia, Rose"), ("Base", "Blond Woods, White Musk")],
  "Fruity · Floral · Fresh", "Girl of Now, dressed in fresh rose petals.",
  f"{t} is a fresh fruity floral fragrance for women, launched in 2024 as part of the Girl of Now family. A spark of Sichuan pepper and juicy pink peach opens it, a heart of magnolia and rose brings a soft petal bouquet, and it settles into blond woods and a clean white musk.",
  ["A sparkling Sichuan pepper and pink peach opening", "A soft magnolia and rose heart", "A clean blond woods and white musk base", "Generous 90ml Eau de Parfum"],
  "EAN 7640233342466 not found online; fits the range (The Perfume Shop 50ml = 7640233342459). Pyramid agreed by The Perfume Shop, Lookfantastic, John Lewis, Next and NST (mandarin only on NST, left out; Perfume.com conflicting list ignored). 2024 per John Lewis, The Perfume Shop, NST. Several UK retailers show it unavailable – may be winding down. Women." + AW,
  "Sichuan pepper and pink peach over magnolia, rose and white musk.", ["Fruity", "Floral", "Fresh"], ["Floral", "Rose", "Fruity", "Fresh"],
  name="Girl of Now Rose Petal", **PC)

# 2 Elie Saab L'Homme EDP 100ml
t = "Elie Saab L'Homme Eau de Parfum 100ml"
F("7640233342565", "Elie Saab", t, "Men", "100", "61.99", "79.99", 4,
  [("Top", "Bergamot, Pink Pepper, Lemon"), ("Heart", "Vetiver, Cedar"), ("Base", "Patchouli, Myrrh")],
  "Woody · Aromatic · Fresh", "Elie Saab's first signature fragrance for men.",
  f"{t} is a woody vetiver fragrance for men, launched in 2025 and created by perfumer Pierre-Constantin Guéros. Bergamot, pink pepper and lemon open bright and crisp, a heart of vetiver and cedar gives it a clean, woody backbone, and it settles into warm patchouli and myrrh.",
  ["A crisp bergamot, pink pepper and lemon opening", "A clean vetiver and cedar heart", "A warm patchouli and myrrh base", "Generous 100ml Eau de Parfum"],
  "EAN 7640233342565 seen in L'Homme EDP image filenames on tendance-parfums.com (size not stated; The Perfume Shop 50ml = 7640233342558, so fits 100ml). Not L'Homme Intense. Pyramid agreed by The Perfume Shop, Tendance, John Lewis, Notino (cedar heart per 3 sources; The Perfume Shop puts it in the base). 2025 and perfumer per Notino and NST. Men." + AW,
  "bergamot and pink pepper over vetiver, cedar and myrrh.", ["Woody", "Aromatic", "Fresh"], ["Woody", "Citrus", "Spicy", "Fresh"],
  name="Elie Saab L'Homme", **PC)

# 3 Elie Saab Le Parfum in White EDP 90ml
t = "Elie Saab Le Parfum in White Eau de Parfum 90ml"
F("3423473997658", "Elie Saab", t, "Women", "90", "59.49", "80.99", 5,
  [("Top", "Orange Blossom"), ("Heart", "Jasmine"), ("Base", "Patchouli, White Musk")],
  "Floral · Fruity · Musky", "Le Parfum, reimagined in luminous white.",
  f"{t} is a floral chypre fragrance for women from Elie Saab's Le Parfum collection, launched in 2018. Luminous orange blossom opens it, a radiant jasmine heart follows, and it settles into a soft, elegant base of patchouli and white musk.",
  ["A luminous orange blossom opening", "A radiant jasmine heart", "A soft patchouli and white musk base", "Generous 90ml Eau de Parfum"],
  "EAN 3423473997658 not found online (supplier also lists 7640233340127; 3423473 = older licence prefix, unconfirmed). Retailer pyramids differ (Lookfantastic newer list vs Notino/Beauty Bay), so only notes 3 sources agree on are shown. 2018 per Notino and NST. Perfumer not shown (1 source only). Women." + AW,
  "orange blossom over jasmine, patchouli and white musk.", ["Floral", "Fruity", "Musky"], ["Floral", "Jasmine", "Fresh"],
  name="Le Parfum in White", **PC)

# 4 Elie Saab Le Parfum Royal EDP 90ml
t = "Elie Saab Le Parfum Royal Eau de Parfum 90ml"
F("7640233340097", "Elie Saab", t, "Women", "90", "55.49", "70.99", 5,
  [("Top", "Mandarin"), ("Heart", "Rose, Neroli"), ("Base", "Patchouli, Sandalwood, Vanilla, Amber")],
  "Floral · Oriental · Woody", "A regal, ambery take on Le Parfum.",
  f"{t} is an ambery floral chypre for women, launched in 2019 and created by perfumer Maïa Lernout. Bright mandarin opens it, a heart of rose and neroli brings a rich floral glow, and it settles into a warm base of patchouli, sandalwood, vanilla and amber.",
  ["A bright mandarin opening", "A rich rose and neroli heart", "A warm patchouli, sandalwood, vanilla and amber base", "Generous 90ml Eau de Parfum"],
  "EAN 7640233340097 not found online. Pyramid agreed by Lookfantastic, John Lewis, Escentual and The Fragrance Shop (amber per NST, Escentual, The Fragrance Shop). 2019 per John Lewis and NST; perfumer per NST and Escentual. Possibly being discontinued (John Lewis, Lookfantastic, Escentual sold out; Next still sells 90ml). Women." + AW,
  "mandarin over rose, neroli, sandalwood and vanilla.", ["Floral", "Oriental", "Woody"], ["Floral", "Rose", "Vanilla", "Sandalwood", "Oriental"],
  name="Le Parfum Royal", **PC)

# 5 Elizabeth Taylor Diamonds & Sapphires EDT 100ml
t = "Elizabeth Taylor Diamonds & Sapphires Eau de Toilette 100ml"
F("0719346450409", "Elizabeth Taylor", t, "Women", "100", "22.49", "29.99", 4,
  [("Top", "Melon, Peach, Lily of the Valley, Freesia, Galbanum"), ("Heart", "Jasmine, Rose, Ylang-Ylang, Rhubarb, Spices"), ("Base", "Amber, Sandalwood, Musk, Vetiver")],
  "Floral · Fruity · Woody", "A sparkling floral classic from 1993.",
  f"{t} is a floral fruity fragrance for women, launched in 1993. Melon, peach, lily of the valley, freesia and green galbanum open fresh and bright, a heart of jasmine, rose, ylang-ylang and rhubarb adds a lush, gently spiced bouquet, and it settles into warm amber, sandalwood, musk and vetiver.",
  ["A fresh melon, peach and freesia opening", "A lush jasmine, rose and ylang-ylang heart", "A warm amber, sandalwood and musk base", "Generous 100ml Eau de Toilette"],
  "EAN 0719346450409 only in marketplace listing titles (eBay UK, Jomashop) – weak match. EDT 100ml sold by Superdrug, Fragrance Direct, FragranceNet, Notino. Pyramid agreed by FragranceNet, JustMyLook, ScentVerdict, Superdrug, Parfumo (apricot/heliotrope single-source, left out). 1993 per Parfumo, FragranceNet, ScentVerdict. Women." + AW,
  "melon and peach over jasmine, rose and sandalwood.", ["Floral", "Fruity", "Woody"], ["Floral", "Fruity", "Jasmine", "Rose", "Sandalwood"],
  name="Diamonds & Sapphires", **TC)

# 6 Elizabeth Taylor Passion EDT 74ml
t = "Elizabeth Taylor Passion Eau de Toilette 74ml"
F("0719346010115", "Elizabeth Taylor", t, "Women", "74", "24.99", "31.99", 5,
  [("Top", "Lily of the Valley, Ylang-Ylang"), ("Heart", "Spicy Notes"), ("Base", "Sandalwood, Incense, Cedar")],
  "Oriental · Spicy · Woody", "Elizabeth Taylor's original, opulent signature.",
  f"{t} is a spicy woody oriental fragrance for women, first launched in 1987. Lily of the valley and ylang-ylang open rich and floral, a warm spicy heart follows, and it settles into a deep, smoky base of sandalwood, incense and cedar.",
  ["A rich lily of the valley and ylang-ylang opening", "A warm, spicy heart", "A smoky sandalwood, incense and cedar base", "Classic 74ml Eau de Toilette"],
  "EAN 0719346010115 matched on UPCitemdb (Passion 2.5oz EDT) and Maxaroma item UP719346010115 (Passion EDT 75ml); eBay.de EDT 74ml. EDT 74ml also at JustMyLook, allbeauty, Tesco. Pyramid: only notes Parfumo and Maxaroma/JustMyLook agree on (long retailer list from a shared feed, left out). 1987 per Parfumo and NST (FragranceNet 1988). Women." + AW,
  "lily of the valley and ylang-ylang over spice, sandalwood and incense.", ["Oriental", "Spicy", "Woody"], ["Oriental", "Spicy", "Floral", "Woody", "Sandalwood"],
  name="Passion", **TC)

# 7 Elizabeth Taylor Violet Eyes EDP 100ml
t = "Elizabeth Taylor Violet Eyes Eau de Parfum 100ml"
F("0719346158046", "Elizabeth Taylor", t, "Women", "100", "23.99", "31.99", 5,
  [("Top", "White Peach"), ("Heart", "Jasmine, Purple Rose"), ("Base", "Cedarwood, Amber, Peony")],
  "Floral · Fruity · Woody", "Inspired by Elizabeth Taylor's famous violet eyes.",
  f"{t} is a sensual floral fragrance for women, launched in 2010 and created by perfumer Carlos Benaïm. Juicy white peach opens it, a heart of jasmine and purple rose brings a lush floral bouquet, and it settles into a warm base of cedarwood, amber and soft peony.",
  ["A juicy white peach opening", "A lush jasmine and purple rose heart", "A warm cedarwood and amber base", "Generous 100ml Eau de Parfum"],
  "EAN 0719346158046 only in eBay listing titles (EDP 100ml) – weak match; OnBuy shows a different EAN (0887776795923) for the same 100ml EDP. EDP 100ml at TJ Hughes, Tesco, OnBuy, FragranceNet. Pyramid agreed by FragranceNet, TJ Hughes, ScentVerdict (OnBuy puts peony in the heart). 2010 and perfumer per PR Newswire, NST, ScentVerdict. Women." + AW,
  "white peach over jasmine, purple rose and amber.", ["Floral", "Fruity", "Woody"], ["Floral", "Fruity", "Jasmine", "Rose", "Woody"],
  name="Violet Eyes", **PC)

# 8 Elizabeth Taylor White Diamonds EDT 100ml
t = "Elizabeth Taylor White Diamonds Eau de Toilette 100ml"
F("0719346022705", "Elizabeth Taylor", t, "Women", "100", "29.99", "38.99", 5,
  [("Top", "Bergamot, Neroli, Lily"), ("Heart", "Rose, Jasmine, Tuberose, Orris"), ("Base", "Sandalwood, Amber, Musk, Oakmoss, Patchouli")],
  "Floral · Woody · Musky", "The legendary white floral, since 1991.",
  f"{t} is a classic white floral fragrance for women, launched in 1991 and created by perfumer Carlos Benaïm. Bergamot, neroli and Amazon lily open bright and elegant, a heart of rose, jasmine, tuberose and orris brings a rich, glamorous bouquet, and it settles into sandalwood, amber, musk, oakmoss and patchouli.",
  ["A bright bergamot, neroli and lily opening", "A glamorous rose, jasmine and tuberose heart", "A rich sandalwood, amber and oakmoss base", "Generous 100ml Eau de Toilette"],
  "EAN 0719346022705 matched on Superdrug (White Diamonds 100ml EDT). Also at Boots, The Perfume Shop, FragranceNet. Pyramid: only notes 2+ of Superdrug, ScentVerdict, NST, Boots, FragranceNet agree on (narcissus single-source, left out). 1991 and perfumer per elizabethtaylor.com, NST, ScentVerdict. Not Brilliant White Diamonds / En Rouge / Icon. Women." + AW,
  "bergamot and neroli over rose, tuberose and sandalwood.", ["Floral", "Woody", "Musky"], ["Floral", "Rose", "Jasmine", "Citrus", "Sandalwood"],
  name="White Diamonds", **TC)

# 9 FCUK Her trio gift set (needs-review)
TRIO("0085715676726", "Women", "FCUK Her Eau de Toilette 3 x 25ml Gift Set – Original, Friction & Connect",
     "FCUK Her EDT 3 x 25ml Gift Set – Original, Friction, Connect", "21.99", "28.99", 5,
     [("FCUK Her", "A floral woody amber scent: fresh iris and citrus over a soft vanilla-wood drydown.",
       [("Top", "Iris, Citrus"), ("Heart", "Jasmine, Peony, Violet"), ("Base", "Cedar, Amber, Sandalwood, Vanilla")]),
      ("FCUK Friction Her", "A fruity, sweet floral with a warm, musky finish.",
       [("Key notes", "Red Berries, Apple Blossom, Honeysuckle, Amber, Musk, Sandalwood, Vanilla")]),
      ("FCUK Connect Her", "A fresh, clean floral woody musk for every day.",
       [("Top", "Lotus, Bergamot, Lily of the Valley"), ("Heart", "Jasmine, Violet, Peony"), ("Base", "Musk, Sandalwood, Cedar, Amber")])],
     "Three FCUK favourites for her in one handy set.",
     "This FCUK Her gift set brings together three 25ml Eau de Toilette sprays: the original FCUK Her, the fruity-sweet FCUK Friction Her and the fresh, clean FCUK Connect Her. A great way to switch scents from day to night, or to give as a gift.",
     ["Three fragrances to suit every mood", "Handy 25ml sprays for your bag", "Fresh florals to warm, musky woods", "A ready-made gift"],
     "NEEDS REVIEW: EAN 0085715676726 not found anywhere (0085715 prefix fits FCUK). Set only confirmed by one retailer (Beauty Scent UK: FCUK Her EDT 3 x 25ml Gift Set – Original, Friction, Connect); not on frenchconnection.com – may be discontinued/clearance. 'Original' taken as FCUK Her (Beauty Scent naming). Friction Her is mainly sold as EDP; EDT 25ml not confirmed. Notes: FCUK Her per Parfumo + The Perfume Shop; Friction Her per Superdrug + Fragrance Direct (tiers disagree, shown as key notes); Connect Her per Fragrance Direct + Rackhams. Women." + AW,
     "FCUK Her, Friction Her and Connect Her minis.", ["Floral", "Woody", "Musky"], ["Floral", "Fruity", "Vanilla", "Sandalwood", "Jasmine"])

# 10 FCUK Him trio gift set (needs-review)
TRIO("0085715676733", "Men", "FCUK Him Eau de Toilette 3 x 25ml Gift Set – Original, Friction & Connect",
     "FCUK Him EDT 3 x 25ml Gift Set – Original, Friction, Connect", "21.99", "28.99", 5,
     [("FCUK Him", "An aromatic, herbal and fresh scent with a vanilla and woods base.",
       [("Top", "Lavender, Basil, Sangria, Rosemary"), ("Heart", "Sage, Green Pepper, Tea"), ("Base", "Vanilla, Ebony, Patchouli")]),
      ("FCUK Friction Him", "A fresh aquatic-aromatic with fruit, spice and a warm rum, amber and leather finish.",
       [("Top", "Mandarin, Green Fruits, Lavender"), ("Heart", "Geranium, Marine Notes, Cardamom, Rum"), ("Base", "Amber, Leather, Patchouli, Musk")]),
      ("FCUK Connect Him", "An aromatic fougère: fresh and herbal at first, then warmer and darker.",
       [("Top", "Rosemary, Sangria, Lavender"), ("Heart", "Sage, Tea, Pepper"), ("Base", "Ebony Wood, Patchouli")])],
     "Three FCUK favourites for him in one handy set.",
     "This FCUK Him gift set brings together three 25ml Eau de Toilette sprays: the original FCUK Him, the fresh, spicy FCUK Friction Him and the aromatic FCUK Connect Him. Easy to carry and easy to switch between, from the office to a night out.",
     ["Three fragrances to suit every mood", "Handy 25ml sprays for your bag", "Fresh herbs to warm woods and amber", "A ready-made gift"],
     "NEEDS REVIEW: EAN 0085715676733 not found anywhere (0085715 prefix fits FCUK). Set only confirmed by one retailer (Beauty Scent UK: FCUK Him EDT 3 x 25ml Set – Original, Friction, Connect); not on frenchconnection.com – may be discontinued/clearance. 'Original' taken as FCUK Him (Beauty Scent naming); Friction (not Friction Night). Notes: FCUK Him per Parfumo + The Perfume Shop; Friction Him per Tesco + Welzo; Connect Him per Cosmetify + Rackhams. Men." + AW,
     "FCUK Him, Friction Him and Connect Him minis.", ["Aromatic", "Fougere", "Woody"], ["Lavender", "Fresh", "Spicy", "Woody", "Vanilla"])

write_outputs(".")
