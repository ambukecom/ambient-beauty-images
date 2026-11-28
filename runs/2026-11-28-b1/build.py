import sys; sys.path.insert(0, "/home/claude/ambient-beauty-images/workflow")
from lib import *
TC = dict(conc="Eau De Toilette", concl="Eau de Toilette")
PC = dict(conc="Eau De Parfum", concl="Eau de Parfum")
AW = " Awaiting photos."
NR = "Narciso Rodriguez"
PH = "Paris Hilton"

def GS(bc, vendor, title, seo_t, gender, size, price, cmp, qty, pyr, profile, hook, intro, contents, love, note, seo_d,
       of, fr, name, conc="Eau De Parfum", concl="Eau de Parfum", status="done", form_suffix=" Gift Set"):
    """Fragrance set: fragrance standard (3 tags) plus a 'What's in the set' block (as runs/2026-11-27-b3)."""
    q2 = {"Men": ("Is it for men?", "Yes, it is a men's fragrance gift set."),
          "Women": ("Is it for women?", "Yes, it is a women's fragrance gift set."),
          "Unisex": ("Is it unisex?", "Yes, it is made for everyone.")}[gender]
    qs = ([(f"What does {name} smell like?", pyramid_answer(pyr))] if pyr else []) + [("What's in the set?", "; ".join(contents) + "."), q2]
    blocks = [("What's in the set", ul(contents))] + ([("Scent pyramid", kd(pyr))] if pyr else [])
    add(cat_name="Fragrances", bc=bc, title=title, vendor=vendor, type=TYPE[gender], gender=gender, cat=TAXON["perfume"],
        price=price, cmp=cmp, qty=qty, tags=[vendor, gender, conc], seo=(seo_t, f"{seo_t}: {seo_d}" + FREE), status=status,
        form=concl + form_suffix, size=size, unit="ml", note=note, gpc=GPC["fragrance"],
        mf={"age-group": ["Adults"], "product-form": ["Spray"], "dispenser-type": ["Spray"], "olfactory-family": list(of), "fragrance": list(fr)},
        desc=body(hook, intro, blocks,
                  [("Brand", vendor), ("Concentration", concl), ("Contents", " + ".join(c.split(" (")[0] for c in contents)),
                   ("Scent profile", profile), ("Wear", gender)], love, qs))

PO = "Police"

# 1 Police Amber Gold gift set
t = "Police Amber Gold Eau de Toilette 100ml Gift Set with 125ml Body Lotion"
GS("0679602549646", PO, t, "Police Amber Gold EDT 100ml + Body Lotion Gift Set", "Women", "100", "20.49", "25.99", 5,
   [("Top", "Bitter Orange, Saffron"), ("Heart", "Amber, Jasmine, Magnolia"), ("Base", "Akigalawood, Amberwood, Oakmoss")],
   "Oriental · Floral", "Golden warmth, made to share.",
   f"{t} pairs Police Amber Gold for women with a matching body lotion. It is an oriental floral fragrance: bitter orange and saffron open bright and spicy, a heart of amber, jasmine and magnolia glows warm and feminine, and it settles onto akigalawood, amberwood and oakmoss.",
   ["Police Amber Gold Eau de Toilette 100ml (spray)", "Police Amber Gold Body Lotion 125ml"],
   ["A bright bitter orange and saffron opening", "A warm amber, jasmine and magnolia heart", "A rich akigalawood and oakmoss base", "A matching body lotion to layer the scent"],
   "NEEDS REVIEW: EAN 0679602549646 found on one site only (eBay.de: Amber Gold Women gift set 100ml EDT + 125ml body lotion). Name and contents agree on Superdrug, TJ Hughes, Tesco, Flannels, Cosmetify. Pyramid agreed by TJ Hughes, Tesco, Flannels, Parfumo, Notino (Superdrug lists a different pyramid – ignored). Oriental floral per TJ Hughes, Flannels, Tesco. Launch year single-source – left out. Women's version (The Perfume Shop sets are the men's). Women." + AW,
   "a 100ml spray with matching body lotion.", ["Oriental", "Floral"], ["Oriental", "Jasmine", "Floral"],
   name="Police Amber Gold", status="needs-review", **TC)

# 2 Contemporary Deep Blue
t = "Police Contemporary Deep Blue Eau de Toilette 100ml"
F("0679602221108", PO, t, "Men", "100", "22.49", "28.99", 4,
  [("Top", "Rhubarb"), ("Heart", "Lavender, Geranium, Green Notes"), ("Base", "Vetiver, Leather")],
  "Aromatic · Aquatic", "Cool, fresh and full of energy.",
  f"{t} is a fresh aromatic fragrance for men. Tangy rhubarb opens crisp and lively, a heart of lavender, geranium and green notes brings an aromatic freshness, and it dries down to a confident base of vetiver and leather.",
  ["A crisp rhubarb opening", "An aromatic lavender and geranium heart", "A confident vetiver and leather base", "Generous 100ml Eau de Toilette"],
  "EAN 0679602221108 matched on OnBuy + Superdrug (Deep Blue EDT 100ml, men). Pyramid limited to notes agreed by Promofarma, Parfum-Centrum, The Perfume Shop, Parfumo (elemi and ambroxan not on all – left out; EAN pages give generic pyramids – ignored). Aromatic aquatic per Superdrug + OnBuy. 2019 per Parfumo + Parfum-Centrum. Men." + AW,
  "rhubarb over lavender, geranium and vetiver.", ["Aromatic", "Aquatic", "Fresh"], ["Fresh", "Aquatic", "Lavender"],
  name="Police Deep Blue", **TC)

# 3 Contemporary Extreme
t = "Police Contemporary Extreme Eau de Toilette 100ml"
F("0679602201018", PO, t, "Men", "100", "21.49", "29.99", 5,
  [("Top", "Apple, Peppermint"), ("Heart", "Lavender, Geranium, Nutmeg"), ("Base", "Patchouli, Amber, Vetiver, Musk, Cedarwood")],
  "Fresh · Aromatic", "Fresh energy with a warm woody finish.",
  f"{t} is a fresh aromatic fragrance for men. Crisp apple and cool peppermint open with a burst of energy, lavender, geranium and nutmeg give an aromatic, lightly spicy heart, and patchouli, amber, vetiver, musk and cedarwood leave a warm woody trail.",
  ["A crisp apple and peppermint opening", "An aromatic lavender and nutmeg heart", "A warm patchouli, amber and cedarwood base", "Generous 100ml Eau de Toilette"],
  "EAN 0679602201018 matched on Superdrug ('Extreme For Him EDT 100ml'), The Perfume Shop ('Police Extreme EDT 100ml'), aio.lv. Pyramid: notes agreed by Superdrug, The Perfume Shop, Perfume.com, Notino, Moodnose (top limited to apple + mint, which all list; lemon/pepper/pink berries and carrot seed not on all – left out). Fresh aromatic per Perfume.com + Superdrug/TPS; Notino aromatic woody. Year/perfumer unconfirmed. Men." + AW,
  "apple and peppermint over lavender and warm woods.", ["Fresh", "Aromatic", "Woody"], ["Fresh", "Lavender", "Woody"],
  name="Police Extreme", **TC)

# 4 Love Cherry
t = "Police Contemporary Love Cherry Eau de Toilette 100ml"
F("0679602001472", PO, t, "Women", "100", "20.49", "27.99", 5,
  [("Top", "Lemon, Cherry, Pear"), ("Heart", "Jasmine, Coffee, Lily of the Valley"), ("Base", "Patchouli, Vanilla, Cedarwood")],
  "Amber · Fruity", "Sweet, juicy and a little bit daring.",
  f"{t} is an amber fruity fragrance for women. Italian lemon, juicy cherry and pear open sweet and sparkling, a heart of jasmine, coffee and lily of the valley adds a seductive twist, and it settles onto patchouli, vanilla and cedarwood.",
  ["A juicy cherry and pear opening", "A seductive jasmine and coffee heart", "A warm patchouli and vanilla base", "Generous 100ml Eau de Toilette"],
  "EAN 0679602001472 matched on Superdrug (Love Cherry Woman EDT 100ml), The Perfume Shop (Love Cherry EDT 100ml) + brand site policelifestyle.com (Contemporary Love Cherry EDT for Woman 100ml). Pyramid agreed by brand site, Superdrug, The Perfume Shop, FragranceNet (Cosmetify differs – ignored). Amber fruity per brand + Superdrug. Launch year single-source – left out. Not Potion Love. Women." + AW,
  "cherry and pear over jasmine, coffee and vanilla.", ["Oriental", "Fruity", "Floral"], ["Fruity", "Jasmine", "Vanilla"],
  name="Police Love Cherry", **TC)

# 5 Dark Women
t = "Police Dark Women Eau de Toilette 100ml"
F("0679602161107", PO, t, "Women", "100", "19.49", "26.99", 5,
  [("Top", "Bergamot, Mandarin, Violet, Blackcurrant"), ("Heart", "Gardenia, Jasmine, Iris, Rose"), ("Base", "Sandalwood, Cedarwood, Vanilla, Resins")],
  "Floral · Oriental", "Mysterious, soft and quietly seductive.",
  f"{t} is a floral oriental fragrance for women. Bergamot, mandarin, violet and blackcurrant open fresh and fruity, a heart of gardenia, jasmine, iris and rose blooms soft and powdery, and it settles onto a warm base of sandalwood, cedarwood, vanilla and balsamic resins.",
  ["A fruity bergamot and blackcurrant opening", "A powdery gardenia, iris and rose heart", "A warm sandalwood and vanilla base", "Generous 100ml Eau de Toilette"],
  "EAN 0679602161107 matched on Perfumetrader.de + Parfuem365.de (Dark Woman/Women EDT 100ml). Pyramid agreed by Ferwer, Promofarma, Parfum-Centrum (Scentadvice same notes, untiered). Floral oriental per Parfum-Centrum; Perfumetrader oriental powdery. 2011 per Scentadvice + Parfum-Centrum. Parfumo's 2014 'Dark pour Femme' entry is a different perfume – not used. Some UK retailers call this 'Dark pour Femme'. Women." + AW,
  "blackcurrant and violet over gardenia, iris and vanilla.", ["Floral", "Oriental", "Powdery"], ["Floral", "Jasmine", "Rose", "Vanilla"],
  name="Police Dark Women", **TC)

# 6 Silver Allure
t = "Police Silver Allure Eau de Toilette 100ml"
F("0679602591010", PO, t, "Men", "100", "20.99", "27.99", 5,
  [("Top", "Bergamot, Mandarin Orange, Neroli"), ("Heart", "Lily of the Valley, Rose, Clove"), ("Base", "Amber, Tonka Bean, Cedarwood")],
  "Citrus · Woody", "Bright, polished and easy to wear.",
  f"{t} is a fresh citrus woody fragrance for men. Bergamot, mandarin orange and neroli open bright and clean, a heart of lily of the valley, rose and clove adds a smooth floral-spicy touch, and it settles onto amber, tonka bean and cedarwood.",
  ["A bright bergamot, mandarin and neroli opening", "A smooth floral heart with a touch of clove", "A warm amber, tonka and cedarwood base", "Generous 100ml Eau de Toilette"],
  "EAN 0679602591010 matched on The Perfume Shop (Silver Allure EDT 100ml); US retailers (FragranceX, Nearstore) sell it as 'Contemporary Silver Allure for Men'. Pyramid agreed by The Perfume Shop, Rackhams, ScentVerdict. Citrus woody per The Perfume Shop + Rackhams + ScentVerdict. Launch year single-source – left out. Men." + AW,
  "bergamot and neroli over rose, clove and tonka.", ["Citrus", "Woody", "Fresh"], ["Citrus", "Rose", "Woody"],
  name="Police Silver Allure", **TC)

# 7 Wild Night
t = "Police Wild Night Eau de Toilette 100ml"
F("0679602001458", PO, t, "Men", "100", "21.99", "27.99", 5,
  [("Top", "Apple, Cardamom, Grapefruit"), ("Heart", "Coffee, Lavender, Nutmeg"), ("Base", "Amber, Patchouli, Sandalwood")],
  "Spicy · Aromatic", "Dark, spicy and made for after hours.",
  f"{t} is a spicy aromatic fragrance for men. Apple, cardamom and pink grapefruit open fresh and spicy, a heart of coffee, lavender and nutmeg brings depth and warmth, and it settles onto amber, patchouli and sandalwood.",
  ["A fresh apple and cardamom opening", "A warm coffee, lavender and nutmeg heart", "A deep amber, patchouli and sandalwood base", "Generous 100ml Eau de Toilette"],
  "EAN 0679602001458 matched on The Perfume Shop (Wild Night EDT 100ml); Superdrug sells Wild Night For Men 100ml EDT. Pyramid agreed by The Perfume Shop + Parfumo (FragranceNet partly; Perfume.com differs – ignored). Family: FragranceNet oriental fougère, Superdrug spicy lavender/woody-musk – Spicy + Aromatic used. Launch year disputed (2024/2025) – left out. EDT, not the Wild Night EDP. Men." + AW,
  "apple and cardamom over coffee, lavender and amber.", ["Spicy", "Aromatic", "Oriental"], ["Spicy", "Lavender", "Sandalwood"],
  name="Police Wild Night", **TC)

# 8 Porsche Design Titan 50ml
t = "Porsche Design Titan Eau de Toilette 50ml"
F("5050456101207", "Porsche Design", t, "Men", "50", "28.99", "39.99", 5,
  [("Top", "Mint, Grapefruit, Black Pepper"), ("Heart", "Basil, Geranium, Lavender"), ("Base", "Cedarwood, Musk, Amber")],
  "Woody · Aromatic", "Clean-cut, fresh and engineered for confidence.",
  f"{t} is a woody aromatic fragrance for men, created by perfumer Véronique Nyberg and launched in 2012. Cool mint, grapefruit and black pepper open fresh and sharp, a green heart of basil, geranium and lavender adds aromatic character, and it settles onto cedarwood, musk and amber.",
  ["A cool mint and grapefruit opening", "A green basil, geranium and lavender heart", "A smooth cedarwood, musk and amber base", "Handy 50ml Eau de Toilette"],
  "Supplier name 'Porche Design Porche Titan' – corrected to Porsche Design Titan. EAN 5050456101207 matched on Jomashop (Porsche Titan EDT 1.7oz/50ml); Superdrug sells the same item under EAN 3351500802012 (check box barcode). Pyramid agreed by Superdrug, Notino UK, Fragplace, Osmoz. Woody aromatic per Notino + Superdrug. Véronique Nyberg per NST + Fragplace; 2012 per NST, Osmoz, Fragplace. Men." + AW,
  "mint and grapefruit over basil, geranium and cedarwood.", ["Woody", "Aromatic", "Fresh"], ["Woody", "Fresh", "Lavender"],
  name="Porsche Design Titan", **TC)

# 9 Polo Black 125ml
t = "Ralph Lauren Polo Black Eau de Toilette 125ml"
F("3360377032767", "Ralph Lauren", t, "Men", "125", "51.99", "70.99", 5,
  [("Top", "Iced Mango, Mandarin, Sage"), ("Heart", "Silver Armoise, Hedione"), ("Base", "Patchouli, Tonka Bean, Sandalwood")],
  "Woody · Aromatic", "Sleek, modern and effortlessly cool.",
  f"{t} is a woody aromatic fragrance for men, launched in 2005 and created by perfumer Pierre Négrin. Iced mango, mandarin and sage open cool and fruity, a heart of silver armoise and hedione adds an airy aromatic freshness, and it dries down to dark patchouli, tonka bean and sandalwood.",
  ["A cool iced mango and mandarin opening", "An airy silver armoise heart", "A smooth patchouli, tonka and sandalwood base", "Generous 125ml Eau de Toilette"],
  "EAN 3360377032767 matched on glam4u.gr, Qogita, Galaxus (Polo Black EDT 125ml). Pyramid: notes agreed by at least 2 of brand site, The Perfume Shop, Osmoz, glam4u (single-source notes – cardamom, ozone, jasmine, moss, cedar – left out). Woody aromatic per Osmoz, glam4u, The Perfume Shop. 2005 per Osmoz, glam4u, ScentAdvice, NST; Pierre Négrin per glam4u + ScentAdvice. Not Polo Double Black. Men." + AW,
  "iced mango and sage over armoise and patchouli.", ["Woody", "Aromatic"], ["Woody", "Fruity", "Citrus"],
  name="Polo Black", **TC)

# 10 Rayhaan Aquatica
t = "Rayhaan Aquatica Eau de Parfum 100ml"
F("6297001571330", "Rayhaan", t, "Men", "100", "31.49", "39.99", 5,
  [("Top", "Lime, Coconut Milk, Bergamot, Mandarin"), ("Heart", "Sugar Cane, Jasmine, Hibiscus, Gardenia"), ("Base", "Rum, Musk, Tonka Bean, Patchouli")],
  "Citrus · Tropical", "A sun-warmed tropical escape in a bottle.",
  f"{t} is a tropical citrus floral fragrance. Zesty lime, creamy coconut milk, bergamot and mandarin open bright and sunny, a heart of sugar cane, jasmine, hibiscus and gardenia adds a sweet floral glow, and it settles onto rum, musk, tonka bean and patchouli.",
  ["A zesty lime and coconut milk opening", "A sweet sugar cane and jasmine heart", "A warm rum, musk and tonka base", "Generous 100ml Eau de Parfum"],
  "EAN 6297001571330 matched on Superdrug (Rayhaan Aquatica 100ml EDP). Pyramid agreed by Superdrug, Fragrance Hub UK, Just My Look. Citrus floral fruity per Just My Look + Fragrance Hub. Not marine/aquatic despite the name. Gender: supplier says Men (kept); Superdrug + Just My Look market it as unisex. Men." + AW,
  "lime and coconut over jasmine, rum and tonka.", ["Citrus", "Floral", "Fruity"], ["Citrus", "Fruity", "Jasmine"],
  name="Rayhaan Aquatica", **PC)

write_outputs()
