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

# ---- All Of Me (shared) ----
AOM_PYR = [("Top", "Magnolia"), ("Heart", "Rose Centifolia, Geranium Bourbon"), ("Base", "Musk, Sandalwood")]
AOM_INTRO = ("Narciso Rodriguez All Of Me is a floral musky fragrance for women, launched in 2023 and created by perfumers "
             "Dora Baghriche and Daphné Bugey. Fresh magnolia opens onto a radiant heart of rose centifolia and geranium bourbon, "
             "wrapped in the signature Narciso musk and a soft, creamy sandalwood base.")
AOM_NOTE = ("Pyramid agreed by The Perfume Shop, Lookfantastic, Jean Coutu (Parfumo lists extra untiered notes – left out). "
            "Floral musky per Lookfantastic + John Lewis. 2023 per The Perfume Shop, John Lewis, Parfumo, NST. "
            "Dora Baghriche + Daphné Bugey per The Perfume Shop, Parfumo, NST. Women.")
AOM_LOVE = ["A fresh magnolia opening", "A radiant rose and geranium heart", "The signature Narciso Rodriguez musk"]

# 1 All Of Me EDP 50ml
t = "Narciso Rodriguez All Of Me Eau de Parfum 50ml"
F("3423222080952", NR, t, "Women", "50", "32.99", "44.99", 5, AOM_PYR,
  "Floral · Musky", "Every facet of femininity, in one bottle.",
  AOM_INTRO.replace("Narciso Rodriguez All Of Me is", t + " is"),
  AOM_LOVE + ["A 50ml Eau de Parfum"],
  "EAN 3423222080952 matched on Kruidvat NL, Jean Coutu, Fruugo IE (All of Me EDP 50ml). " + AOM_NOTE + AW,
  "magnolia, rose and geranium over musk and sandalwood.", ["Floral", "Musky"], ["Floral", "Rose"],
  name="All Of Me", **PC)

# 2 All Of Me set 30ml + 50ml lotion (needs-review: EAN on one site)
t = "Narciso Rodriguez All Of Me Eau de Parfum 30ml Gift Set with 50ml Body Lotion"
GS("3423222108373", NR, t, "Narciso Rodriguez All Of Me EDP 30ml + Body Lotion Gift Set", "Women", "30", "37.49", "50.99", 3, AOM_PYR,
   "Floral · Musky", "All Of Me, ready to give.",
   f"{t} pairs a 30ml All Of Me Eau de Parfum spray with a matching scented body lotion to layer the fragrance. " + AOM_INTRO,
   ["Narciso Rodriguez All Of Me Eau de Parfum 30ml (spray)", "Narciso Rodriguez All Of Me Body Lotion 50ml"],
   AOM_LOVE + ["A matching body lotion to layer the scent"],
   "NEEDS REVIEW: EAN 3423222108373 found on one site only (Superdrug: All Of Me Gift Set 30ml EDP + 50ml Body Lotion). Contents (30ml EDP + 50ml body lotion) confirmed by Superdrug, Lookfantastic, Justmylook, Zalando. Other editions with the same contents carry different EANs (e.g. Valentine's set 3423222121730) – check the box barcode. " + AOM_NOTE + AW,
   "a 30ml spray with a matching body lotion.", ["Floral", "Musky"], ["Floral", "Rose"],
   name="All Of Me", status="needs-review", **PC)

# 3 All Of Me set 50ml + lotion + shower gel
t = "Narciso Rodriguez All Of Me Eau de Parfum 50ml Gift Set with 50ml Body Lotion and 50ml Shower Gel"
GS("3423222092528", NR, t, "Narciso Rodriguez All Of Me EDP 50ml Gift Set", "Women", "50", "54.49", "73.99", 5, AOM_PYR,
   "Floral · Musky", "The complete All Of Me ritual.",
   f"{t} brings together All Of Me Eau de Parfum with a matching body lotion and shower gel, so the scent can be layered from shower to spray. " + AOM_INTRO,
   ["Narciso Rodriguez All Of Me Eau de Parfum 50ml (spray)", "Narciso Rodriguez All Of Me Body Lotion 50ml", "Narciso Rodriguez All Of Me Shower Gel 50ml"],
   AOM_LOVE + ["A matching body lotion and shower gel"],
   "EAN 3423222092528 matched on Galaxus AT (Christmas 2023 All of Me EDP 50 + Body Lotion + Shower Gel) and Cosma Parfumeries (Giftset All of Me EDP 50ml + 2 products). Regular EDP, not Intense (Intense set is 3423222133849). Contents confirmed by both EAN pages + Tesco UK, Escentual, The Fragrance Shop. Christmas 2023 edition. " + AOM_NOTE + AW,
   "a 50ml spray with body lotion and shower gel.", ["Floral", "Musky"], ["Floral", "Rose"],
   name="All Of Me", **PC)

# 4 For Her EDT 30ml (needs-review: pyramid disputed)
t = "Narciso Rodriguez For Her Eau de Toilette 30ml"
F("3423478925557", NR, t, "Women", "30", "36.99", "49.99", 5,
  [("Top", "Water Flowers, Lily of the Valley"), ("Heart", "Musk"), ("Base", "Patchouli")],
  "Floral · Musky", "The musk that started it all.",
  f"{t} is a floral musky fragrance for women and the scent that defined the Narciso Rodriguez signature. Fresh water flowers and lily of the valley open onto the house's famous sensual musk heart, which settles onto a warm, lingering patchouli base.",
  ["The iconic Narciso Rodriguez musk heart", "A fresh, delicate floral opening", "A warm patchouli base", "A handy 30ml Eau de Toilette"],
  "NEEDS REVIEW: scent pyramid disputed – current brand copy at The Perfume Shop + Escentual agrees on water flowers, lily of the valley / musk / patchouli (amber note named differently – left out), but older sources (CaFleureBon, Parfumo, Escentual's own description) give osmanthus, orange blossom, bergamot / musk, amber / vetiver, vanilla, patchouli. Launch year conflicts (2003 vs 2005 at TPS) – left out. EAN 3423478925557 matched on Superdrug (for her EDT 30ml) and The Perfume Shop (For Her EDT page). Floral per Escentual + Parfumo. Women." + AW,
  "a floral musky scent with the iconic Narciso musk heart.", ["Floral", "Musky"], ["Floral"],
  name="Narciso Rodriguez For Her", status="needs-review", **TC)

# 5 Musc Nude EDP 50ml
t = "Narciso Rodriguez For Her Musc Nude Eau de Parfum 50ml"
F("3423222107611", NR, t, "Women", "50", "43.49", "55.99", 1,
  [("Top", "Pink Peppercorn, Floral Bouquet, Jasmine"), ("Heart", "Musk, Rose Oil, Orange Flower"), ("Base", "Tonka Bean, Cashmeran, Patchouli")],
  "Floral · Musky", "Musk, laid bare.",
  f"{t} is a floral musky fragrance for women, created by perfumer Sonia Constant. Pink peppercorn and jasmine open onto a sensual heart of musk, rose oil and orange flower, before a warm, skin-like base of tonka bean, cashmeran and patchouli.",
  ["A sparkling pink peppercorn opening", "A sensual musk and rose heart", "A warm tonka and cashmeran base", "A 50ml Eau de Parfum"],
  "EAN 3423222107611 matched on The Perfume Shop IE (Musc Nude EDP 50ml) and Kruidvat NL. Pyramid agreed by Lookfantastic, The Perfume Shop, The Fragrance Shop (Tesco has cedarwood instead of cashmeran – not used). Floral musky per The Fragrance Shop + Lookfantastic (TPS/Boots call it a chypre interpretation). Sonia Constant per TPS, The Fragrance Shop, NST. Launch year conflicts (2023 vs 2024) – left out. Women." + AW,
  "pink pepper and jasmine over musk, rose and tonka.", ["Floral", "Musky"], ["Floral", "Rose", "Jasmine"],
  name="For Her Musc Nude", **PC)

# 6 For Him Vetiver Musc EDT 50ml
t = "Narciso Rodriguez For Him Vetiver Musc Eau de Toilette 50ml"
F("3423222107727", NR, t, "Men", "50", "42.49", "55.99", 1,
  [("Top", "Cardamom, Cypress, Nutmeg"), ("Heart", "Musk, Bourbon Geranium, Red Seaweed"), ("Base", "Vetiver, Cedarwood, Patchouli")],
  "Woody · Aromatic", "Green, woody and quietly magnetic.",
  f"{t} is a woody aromatic fragrance for men. Cardamom, cypress and nutmeg give it a fresh, spicy start, the heart pairs the signature Narciso musk with bourbon geranium and red seaweed, and it dries down to an earthy base of vetiver, cedarwood and patchouli.",
  ["A fresh, spicy cardamom and nutmeg opening", "The signature Narciso musk heart", "An earthy vetiver and cedarwood base", "A 50ml Eau de Toilette"],
  "EAN 3423222107727 matched on Kruidvat NL, Parfuma, Boozt, The Perfume Shop (Vetiver Musc EDT 50ml). Pyramid agreed by brand site, The Perfume Shop, Tesco, Notino (lavandin on brand site + Tesco only – left out). Woody aromatic per Notino, Parfuma, Boozt. Launch year conflicts (2023 vs Jan 2024) and perfumer on one source only – both left out. Men." + AW,
  "cardamom and musk over vetiver and cedarwood.", ["Woody", "Aromatic"], ["Woody", "Spicy"],
  name="For Him Vetiver Musc", **TC)

# 7 Love Rush EDP 100ml
t = "Paris Hilton Love Rush Eau de Parfum 100ml"
F("0608940583562", PH, t, "Women", "100", "30.99", "39.99", 5,
  [("Top", "Bergamot, Mandarin, Apricot"), ("Heart", "Gardenia, Orange Blossom, Dahlia"), ("Base", "Sandalwood, Musk, Vanilla Orchid")],
  "Floral · Fruity", "A sweet, sunny rush of florals.",
  f"{t} is a floral fragrance for women, launched in 2022. Bright bergamot, mandarin and apricot nectar open onto a heart of gardenia, orange blossom and dahlia, settling onto a soft base of sandalwood, musk and vanilla orchid.",
  ["A juicy bergamot, mandarin and apricot opening", "A lush gardenia and orange blossom heart", "A soft sandalwood and vanilla orchid base", "A generous 100ml Eau de Parfum"],
  "EAN 0608940583562 matched on The Perfume Spot (Love Rush EDP 100ml for women) only; product identity also confirmed by the brand press release (PR Newswire, 100ml EDP) and Cosmetify UK. Pyramid agreed by PR Newswire + The Perfume Spot (shop.parishilton.com backs bergamot, gardenia, sandalwood, vanilla orchid; Perfume.com lists a different pyramid – ignored). Floral per PR Newswire, shop.parishilton.com, Cosmetify. 2022 per PR Newswire + Happi. Women." + AW,
  "bergamot and apricot over gardenia and vanilla orchid.", ["Floral", "Fruity"], ["Floral", "Fruity", "Citrus"],
  name="Love Rush", **PC)

# 8 Platinum Rush EDP 100ml
t = "Paris Hilton Platinum Rush Eau de Parfum 100ml"
F("0608940575307", PH, t, "Women", "100", "30.99", "40.99", 3,
  [("Top", "Pear, Red Apple, Mango"), ("Heart", "Green Florals, Lily of the Valley"), ("Base", "Vanilla, Musk, Liquidambar, Patchouli")],
  "Fruity · Floral", "Juicy, glossy and full of fun.",
  f"{t} is a fruity floral fragrance for women, launched in 2018. Crisp pear, red apple and mango open onto green florals and lily of the valley, before a warm base of vanilla, musk, liquidambar and patchouli.",
  ["A juicy pear, apple and mango opening", "A fresh lily of the valley heart", "A warm vanilla and musk base", "A generous 100ml Eau de Parfum"],
  "EAN 0608940575307 matched on Superdrug UK, Newegg, GiftExpress (Platinum Rush EDP 100ml for women). Pyramid agreed by Parfumo + The Star (launch article). Fruity floral per Parfumo + Superdrug. 2018 per Parfumo, FragranceNet, The Star; perfumer on one source only – left out. Women." + AW,
  "pear, apple and mango over lily of the valley and vanilla.", ["Fruity", "Floral"], ["Fruity", "Floral", "Vanilla"],
  name="Platinum Rush", **PC)

write_outputs()
