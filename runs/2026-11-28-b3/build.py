import sys; sys.path.insert(0, "/home/claude/ambient-beauty-images/workflow")
from lib import *
TC = dict(conc="Eau De Toilette", concl="Eau de Toilette")
PC = dict(conc="Eau De Parfum", concl="Eau de Parfum")
AW = " Awaiting photos."
RC, RO, SF = "Roberto Cavalli", "Rochas", "Salvatore Ferragamo"

def seo_t(t):
    P[-1]["seo"] = (t, P[-1]["seo"][1].replace(P[-1]["title"] + ":", t + ":", 1))

def GS(bc, vendor, title, seo_title, gender, size, price, cmp, qty, pyr, profile, hook, intro, contents, love, note, seo_d,
       of, fr, name, conc="Eau De Parfum", concl="Eau de Parfum", status="done", form_suffix=" Gift Set"):
    """Fragrance set (as runs/2026-11-28-b2)."""
    q2 = {"Men": ("Is it for men?", "Yes, it is a men's fragrance gift set."),
          "Women": ("Is it for women?", "Yes, it is a women's fragrance gift set."),
          "Unisex": ("Is it unisex?", "Yes, it is made for everyone.")}[gender]
    qs = ([(f"What does {name} smell like?", pyramid_answer(pyr))] if pyr else []) + [("What's in the set?", "; ".join(contents) + "."), q2]
    blocks = [("What's in the set", ul(contents))] + ([("Scent pyramid", kd(pyr))] if pyr else [])
    add(cat_name="Fragrances", bc=bc, title=title, vendor=vendor, type=TYPE[gender], gender=gender, cat=TAXON["perfume"],
        price=price, cmp=cmp, qty=qty, tags=[vendor, gender, conc], seo=(seo_title, f"{seo_title}: {seo_d}" + FREE), status=status,
        form=concl + form_suffix, size=size, unit="ml", note=note, gpc=GPC["fragrance"],
        mf={"age-group": ["Adults"], "product-form": ["Spray"], "dispenser-type": ["Spray"], "olfactory-family": list(of), "fragrance": list(fr)},
        desc=body(hook, intro, blocks,
                  [("Brand", vendor), ("Concentration", concl), ("Contents", " + ".join(c.split(" (")[0] for c in contents)),
                   ("Scent profile", profile), ("Wear", gender)], love, qs))

# 1 Sublime Tonka
t = "Roberto Cavalli Sublime Tonka Eau de Parfum 100ml"
F("3614228890137", RC, t, "Unisex", "100", "74.99", "99.99", 5,
  [("Top", "Cinnamon, Elemi, Geranium"), ("Heart", "Clary Sage, Tobacco, Frankincense"), ("Base", "Tonka Bean, Wheat Bran")],
  "Amber · Spicy", "Warm spice wrapped in golden tonka.",
  f"{t} is part of the Roberto Cavalli Gold Collection. Cinnamon, elemi and geranium open warm and spicy, a heart of clary sage, tobacco and frankincense adds smoky depth, and it settles onto rich tonka bean and toasty wheat bran. A warm amber scent made for everyone.",
  ["A warm cinnamon, elemi and geranium opening", "A smoky clary sage, tobacco and frankincense heart", "A rich tonka bean base", "Part of the Roberto Cavalli Gold Collection"],
  "NEEDS REVIEW: scent pyramid. ScentVerdict + MyPerfumeShop agree on the pyramid shown, but the Interparfums (licensee) page lists different notes (plum, leather, jasmine…) – please check against the box. EAN 3614228890137 matched on Superdrug (Sublime Tonka EDP 100ml Spray, unisex) + Arreglatelo.es. Amber per Interparfums + MyPerfumeShop. Unisex kept (FragranceNet markets it for women). Launch year conflicting – left out." + AW,
  "spicy cinnamon and tobacco over rich tonka.", ["Oriental", "Spicy"], ["Oriental", "Spicy"],
  name="Sublime Tonka", status="needs-review", **PC)

# 2 Woodiris
t = "Roberto Cavalli Woodiris Eau de Parfum 100ml"
F("3616302038916", RC, t, "Unisex", "100", "74.99", "100.99", 5,
  [("Top", "Bitter Orange, Mandora"), ("Heart", "Iris"), ("Base", "Sandalwood, Patchouli, Musk")],
  "Woody · Powdery", "Velvety iris on a bed of woods.",
  f"{t} is part of the Roberto Cavalli Gold Collection. Bitter orange and mandora open bright and zesty, a heart of iris brings a soft, powdery elegance, and it settles onto creamy sandalwood, patchouli and musk. A refined woody scent made for everyone.",
  ["A zesty bitter orange and mandora opening", "A soft, powdery iris heart", "A creamy sandalwood, patchouli and musk base", "Part of the Roberto Cavalli Gold Collection"],
  "EAN 3616302038916 matched on Jomashop (Unisex Gold Collection Woodiris EDP 3.4oz) + Allegro.pl (EDP 100ml U). Pyramid agreed by MyPerfumeShop, Allegro, NST. Woody per MyPerfumeShop. 2022 per FragranceNet + Parfumo (left out of copy). Unisex." + AW,
  "bitter orange and iris over sandalwood.", ["Woody", "Powdery"], ["Woody", "Floral", "Sandalwood"],
  name="Woodiris", **PC)

# 3 Girl Life Refill
t = "Rochas Girl Life Eau de Parfum 150ml Refill"
F("3386460137386", RO, t, "Women", "150", "46.99", "63.99", 5,
  [("Top", "Blackcurrant"), ("Heart", "Jasmine, Tuberose, Rose"), ("Base", "Vanilla, Musk, Cedarwood")],
  "Floral · Fruity", "Refill your joy of life.",
  f"{t} is the large refill for the Rochas Girl Life refillable bottle. Juicy blackcurrant opens bright and playful, a heart of jasmine, tuberose and rose blooms radiant and feminine, and it settles onto warm vanilla, musk and cedarwood. A thoughtful way to keep your favourite scent topped up.",
  ["A juicy blackcurrant opening", "A radiant jasmine, tuberose and rose heart", "A warm vanilla, musk and cedarwood base", "A 150ml refill for the Girl Life refillable bottle"],
  "NEEDS REVIEW: refill format. EAN 3386460137386 matched on Superdrug (Girl Life EDP 150ml Refill) + Marionnaud FR (Recharge 150ml); Rochas.com: 150ml refill for the 75ml refillable bottle. No source says whether it has a spray or is pour-in – listed as a refill (product form Liquid, no spray dispenser); please check the stock. Pyramid agreed by Marionnaud, Printemps, Olfastory (pink pepper/mandarin only some – left out). Floral fruity amber per Rochas.com + Marionnaud. Women." + AW,
  "blackcurrant and white florals over vanilla. A 150ml refill.", ["Floral", "Fruity"], ["Floral", "Fruity", "Jasmine"],
  name="Rochas Girl Life", status="needs-review", **PC)
P[-1]["form"] = "Eau de Parfum Refill"
P[-1]["mf"]["product-form"] = ["Liquid"]; del P[-1]["mf"]["dispenser-type"]

# 4 Rochas Man Intense
t = "Rochas Man Intense Eau de Parfum 100ml"
F("3386460136754", RO, t, "Men", "100", "38.49", "49.99", 5,
  [("Top", "Citrus, Lavender"), ("Heart", "Coffee, Cedarwood"), ("Base", "Vanilla")],
  "Woody · Gourmand", "A deeper, richer Rochas Man.",
  f"{t} is the intense take on the classic Rochas Man. Fresh citrus and lavender open clean and aromatic, a heart of creamy coffee and cedarwood adds warmth and depth, and it settles onto smooth vanilla. A woody gourmand fragrance for evenings and cooler days.",
  ["A fresh citrus and lavender opening", "A rich coffee and cedarwood heart", "A smooth vanilla base", "Intense Eau de Parfum strength"],
  "EAN 3386460136754 matched on Perfumetrader.de (Man Intense EDP 100ml) + Jomashop (Men's Intense EDP Spray 3.4oz). Pyramid agreed by Rochas.com, Parfumo, Cosma (tonka brand site only – left out). Woody gourmand per Rochas + Perfumetrader. Perfumer Maurice Roucel (Rochas + Parfumo; left out of copy). Men." + AW,
  "citrus and lavender over coffee and vanilla.", ["Gourmand", "Woody"], ["Woody", "Vanilla"],
  name="Rochas Man Intense", **PC)

FLW = [("Top", "Yuzu, Blackcurrant"), ("Heart", "Peony, Jasmine, Plum Blossom"), ("Base", "Blond Woods, Musk, Vanilla")]
# 5 Amo Flowerful EDT 100ml
t = "Salvatore Ferragamo Amo Ferragamo Flowerful Eau de Toilette 100ml"
F("8052086376496", SF, t, "Women", "100", "39.99", "52.99", 2, FLW,
  "Fruity · Floral", "A joyful burst of flowers and fruit.",
  f"{t} is a fruity floral fragrance for women. Zesty yuzu and juicy blackcurrant open bright and playful, a heart of peony, jasmine and plum blossom blooms soft and feminine, and it settles onto blond woods, musk and vanilla.",
  ["A zesty yuzu and blackcurrant opening", "A soft peony, jasmine and plum blossom heart", "A warm blond woods, musk and vanilla base", "Generous 100ml bottle"],
  "EAN 8052086376496 matched on Superdrug (Amo Ferragamo Flowerful EDT 100ml) + Jomashop + Perfumetrader.de. Pyramid agreed by Interparfums (licensee) + Parfumo + Perfumetrader (Mazzolari has hyacinth instead of jasmine). Fruity floral per Interparfums + Lookfantastic. Women." + AW,
  "yuzu and peony over blond woods and vanilla.", ["Fruity", "Floral"], ["Fruity", "Floral", "Jasmine"],
  name="Amo Ferragamo Flowerful", **TC)
seo_t("Salvatore Ferragamo Amo Flowerful Eau de Toilette 100ml")

# 6 Amo Flowerful gift set (EDT)
t = "Salvatore Ferragamo Amo Ferragamo Flowerful Eau de Toilette 50ml Gift Set with 100ml Body Lotion"
GS("8052086376533", SF, t, "Ferragamo Amo Flowerful EDT 50ml + Body Lotion Gift Set", "Women", "50", "30.99", "40.99", 5, FLW,
   "Fruity · Floral", "Fruity florals, head to toe.",
   f"{t} pairs Amo Ferragamo Flowerful with a matching shimmering body lotion. Zesty yuzu and juicy blackcurrant open bright and playful, a heart of peony, jasmine and plum blossom blooms soft and feminine, and it settles onto blond woods, musk and vanilla.",
   ["Amo Ferragamo Flowerful Eau de Toilette 50ml (spray)", "Amo Ferragamo Flowerful Shimmer Body Lotion 100ml"],
   ["A zesty yuzu and blackcurrant opening", "A soft peony, jasmine and plum blossom heart", "A warm blond woods, musk and vanilla base", "A matching shimmer body lotion to layer the scent"],
   "NEEDS REVIEW: concentration. Supplier form column says Eau de Parfum, but the supplier name and every EAN page say EDT – listed as Eau de Toilette. EAN 8052086376533 matched on Morele.net (2-piece: Flowerful EDT 50ml + Flowerful Shimmer Day & Night Body Lotion 100ml), Pilulka.cz (EDT 50ml + body lotion 100ml), Kendrashop.ro. Not the 3-piece shower-gel set (ACTIVE 16002149613908, EAN 8052086379220). Pyramid agreed by Interparfums + Parfumo. Women." + AW,
   "a 50ml spray with matching 100ml shimmer body lotion.", ["Fruity", "Floral"], ["Fruity", "Floral", "Jasmine"],
   name="Amo Ferragamo Flowerful", status="needs-review", **TC)

# 7 Amo Oriental Wood
t = "Salvatore Ferragamo Amo Ferragamo Oriental Wood Eau de Parfum 100ml"
F("8052464892174", SF, t, "Women", "100", "39.99", "54.99", 4,
  [("Top", "Lemon, Red Apple, Cardamom"), ("Heart", "Rose, Jasmine, Saffron"), ("Base", "Vanilla, Musk")],
  "Woody · Amber", "Warm, sensual woods with a floral glow.",
  f"{t} is a warm woody amber fragrance for women. Lemon, red apple and cardamom open fresh and gently spicy, a heart of rose, jasmine and saffron brings rich, glowing florals, and it settles onto creamy vanilla and musk.",
  ["A fresh lemon, red apple and cardamom opening", "A rich rose, jasmine and saffron heart", "A creamy vanilla and musk base", "Generous 100ml bottle"],
  "EAN 8052464892174 matched on Interparfums (Amo Oriental Wood EDP 100ml), Jomashop (Ladies EDP 3.4oz), bol.com. Pyramid agreed by Profumerie Fusco, Mazzolari, eSun (oud on two only – left out). Woody amber per Fusco + bol.com + eSun. 2022 per NST + ScentAdvice (left out of copy). Parfumo page looks mixed up – ignored. Women." + AW,
  "apple and cardamom over rose, saffron and vanilla.", ["Woody", "Oriental"], ["Woody", "Oriental", "Rose"],
  name="Amo Ferragamo Oriental Wood", **PC)
seo_t("Salvatore Ferragamo Amo Oriental Wood Eau de Parfum 100ml")

# 8 F by Ferragamo Free Time
t = "Salvatore Ferragamo F by Ferragamo Free Time Eau de Toilette 100ml"
F("8034097950025", SF, t, "Men", "100", "31.99", "40.99", 2,
  [("Top", "Ginger, Lemon"), ("Heart", "Cardamom"), ("Base", "Vetiver, Musk")],
  "Woody · Spicy", "Relaxed, fresh and easy to wear.",
  f"{t} is a fresh, woody spicy fragrance for men. Zingy ginger and lemon open bright and energising, a heart of cardamom adds a warm aromatic spice, and it settles onto earthy vetiver and clean musk. A relaxed scent for weekends and every day.",
  ["A zingy ginger and lemon opening", "A warm cardamom heart", "An earthy vetiver and musk base", "Generous 100ml bottle"],
  "EAN 8034097950025 matched on WatchMaxx (EDT 3.4oz, men) + UPCitemdb (Free Time EDT Spray 100ml) + eBay. Pyramid agreed by WatchMaxx + Osmoz (cedar and pink pepper placed differently – left out). Woody spicy per Osmoz + WatchMaxx. 2011 (left out of copy). Men." + AW,
  "ginger and lemon over cardamom and vetiver.", ["Woody", "Spicy"], ["Woody", "Spicy", "Citrus"],
  name="F by Ferragamo Free Time", **TC)
seo_t("Ferragamo F by Ferragamo Free Time Eau de Toilette 100ml")

# 9 Intense Leather
t = "Salvatore Ferragamo Ferragamo Intense Leather Eau de Parfum 100ml"
F("8056860210853", SF, t, "Men", "100", "47.99", "61.99", 4,
  [("Top", "Mandarin, Pink Pepper, Clary Sage"), ("Heart", "Apple, Lily of the Valley, Iris"), ("Base", "Leather, Musk, Oakmoss")],
  "Leather · Spicy", "Smooth leather with a bright, spicy edge.",
  f"{t} is a refined leather fragrance for men. Mandarin, pink pepper and clary sage open bright and spicy, a heart of crisp apple, lily of the valley and iris adds a smooth, elegant touch, and it settles onto rich leather, musk and oakmoss.",
  ["A bright mandarin, pink pepper and clary sage opening", "A smooth apple, lily of the valley and iris heart", "A rich leather, musk and oakmoss base", "Generous 100ml bottle"],
  "EAN 8056860210853 matched on Interparfums (FE Intense Leather EDP 100ml) + Jomashop (Men's Intense Leather EDP 3.4oz). Pyramid agreed by Parfumo + Escentual (NST same notes untiered). Leather per Parfumo (Escentual: aromatic-oriental). 2021 (left out of copy). Men (Escentual says anyone can wear it)." + AW,
  "pink pepper and iris over rich leather.", ["Leather", "Spicy"], ["Spicy", "Woody"],
  name="Ferragamo Intense Leather", **PC)
seo_t("Salvatore Ferragamo Intense Leather Eau de Parfum 100ml")

# 10 Incanto Bloom 2014
t = "Salvatore Ferragamo Incanto Bloom Eau de Toilette 100ml"
F("8034097956027", SF, t, "Women", "100", "28.49", "37.99", 3,
  [("Top", "Grapefruit Blossom, Freesia"), ("Heart", "Tea Rose, Champaca, Raspberry"), ("Base", "Musk, Cashmere Wood")],
  "Floral · Fruity", "Fresh, blooming and feminine.",
  f"{t} (2014 edition) is a floral fruity fragrance for women. Grapefruit blossom and freesia open fresh and sparkling, a heart of tea rose, champaca and juicy raspberry blooms soft and romantic, and it settles onto clean musk and cashmere wood.",
  ["A fresh grapefruit blossom and freesia opening", "A romantic tea rose, champaca and raspberry heart", "A soft musk and cashmere wood base", "Generous 100ml bottle"],
  "Supplier name 'Incanto Bloom (2014)' – '2014' edition mentioned in copy, left out of title. EAN 8034097956027 matched on Direct Fragrance UK (Incanto Bloom 100ml EDT) + Profumeria Mancino (EDT 100ml, women) + Hala Perfumes. Pyramid agreed by Mancino, Hala, ScentVerdict (Direct Fragrance omits raspberry). Floral fruity per Direct Fragrance + Hala. Women." + AW,
  "grapefruit blossom and tea rose over musk.", ["Floral", "Fruity"], ["Floral", "Fruity", "Rose"],
  name="Incanto Bloom", **TC)

write_outputs()
