import sys; sys.path.insert(0, "/home/claude/ambient-beauty-images/workflow")
from lib import *

# ---------------- Bath & Body (body & hair mists)
t = "Ted Baker Fusion Midnight Petal Body & Hair Mist 200ml"
add(cat_name="Bath & Body", bc="5060412678872", title=t, vendor="Ted Baker", type="Bath & Body", gender="Women", cat=TAXON["hair-perfume"],
    price="19.49", cmp="26.99", qty=2, form="Body & Hair Mist", size="200", unit="ml", gpc=GPC["fragrance"],
    tags=["Ted Baker", "Women", "Bath & Body", "Body Mist", "Hair Mist", "Fusion", "Midnight Petal", "Floral", "Gourmand"],
    seo=("Ted Baker Fusion Midnight Petal Body & Hair Mist 200ml", f"{t}: vanilla and orchid over rose, brown sugar and amber." + FREE),
    mf={"age-group": ["Adults"], "product-form": ["Spray"], "dispenser-type": ["Spray"], "fragrance": ["Floral", "Vanilla", "Rose", "Jasmine"]},
    desc=body("A sweet, gourmand-floral spritz for body and hair.",
      "Ted Baker Fusion Midnight Petal Body &amp; Hair Mist 200ml is a gourmand floral mist. Vanilla, bergamot and orchid open softly, a heart of rose, jasmine and brown sugar follows, and it settles on warm amber, tonka and patchouli. Glycerin and pro-vitamin B5 leave skin feeling moisturised.",
      [("Scent", kd([("Top", "Vanilla, Bergamot, Orchid"), ("Heart", "Rose, Jasmine, Brown Sugar"), ("Base", "Amber, Tonka, Patchouli")])),
       ("Key ingredients", ul(["<strong>Glycerin</strong> for scented hydration", "<strong>Pro-vitamin B5</strong> (panthenol)"])),
       ("How to use", ul(["Spray lightly over body and hair", "Reapply through the day as you like", "Avoid the eyes"])),
       ("Good to know", ul(["Part of the Ted Baker Fusion collection", "Flammable: keep away from heat"]))],
      [("Brand", "Ted Baker"), ("Range", "Fusion"), ("Type", "Body & hair mist"), ("Scent profile", "Floral · Gourmand · Amber"), ("Size", "200ml")],
      ["Gourmand-floral scent with a warm base", "Use on body and hair", "With glycerin and pro-vitamin B5", "Light, airy mist"],
      [("What does it smell like?", "Vanilla, bergamot and orchid with rose, jasmine and brown sugar over amber, tonka and patchouli."), ("Can I use it on my hair?", "Yes, it is made for body and hair: spray lightly.")]),
    note="Facts confirmed by 2+ sources (Superdrug EAN page, Next product page and ingredient PDF with same EAN, Cosmetify; KMI Brands for the range). Notes agreed by Superdrug, Next and Cosmetify. Vegan claim left out (only KMI's range-wide statement). Awaiting photos.")

t = "Ted Baker Fusion Pink Bloom Body & Hair Mist 200ml"
add(cat_name="Bath & Body", bc="5060412678865", title=t, vendor="Ted Baker", type="Bath & Body", gender="Women", cat=TAXON["hair-perfume"],
    price="19.49", cmp="25.99", qty=1, form="Body & Hair Mist", size="200", unit="ml", gpc=GPC["fragrance"],
    tags=["Ted Baker", "Women", "Bath & Body", "Body Mist", "Hair Mist", "Fusion", "Pink Bloom", "Fruity", "Floral"],
    seo=("Ted Baker Fusion Pink Bloom Body & Hair Mist 200ml", f"{t}: pink pepper, berries and peach over jasmine and musk." + FREE),
    mf={"age-group": ["Adults"], "product-form": ["Spray"], "dispenser-type": ["Spray"], "fragrance": ["Fruity", "Floral", "Jasmine", "Vanilla"]},
    desc=body("A fruity, floral spritz for body and hair.",
      "Ted Baker Fusion Pink Bloom Body &amp; Hair Mist 200ml is a fruity-floral mist. Pink pepper, berries and peach open brightly, a heart of jasmine and orange blossom follows, and it settles on patchouli, musk and sweet vanilla. Glycerin and pro-vitamin B5 leave skin feeling moisturised.",
      [("Scent", kd([("Top", "Pink Pepper, Berries, Peach"), ("Heart", "Jasmine, Orange Blossom"), ("Base", "Patchouli, Musk, Sweet Vanilla")])),
       ("Key ingredients", ul(["<strong>Glycerin</strong> for scented hydration", "<strong>Pro-vitamin B5</strong> (panthenol)"])),
       ("How to use", ul(["Shake well, then spray lightly over body and hair", "Reapply through the day as you like", "Avoid the eyes"])),
       ("Good to know", ul(["Part of the Ted Baker Fusion collection", "Flammable: keep away from heat"]))],
      [("Brand", "Ted Baker"), ("Range", "Fusion"), ("Type", "Body & hair mist"), ("Scent profile", "Fruity · Floral · Musky"), ("Size", "200ml")],
      ["Juicy fruity-floral scent", "Use on body and hair", "With glycerin and pro-vitamin B5", "Light, airy mist"],
      [("What does it smell like?", "Pink pepper, berries and peach with jasmine and orange blossom over patchouli, musk and sweet vanilla."), ("Can I use it on my hair?", "Yes, it is made for body and hair: spray lightly.")]),
    note="Facts confirmed by 2+ sources (Superdrug EAN page, Next product page and ingredient PDF with same EAN, Cosmetify; KMI Brands for the range). Notes agreed by Superdrug, Next and Cosmetify; rose (Next only) left out. Vegan claim left out (only KMI's range-wide statement). Awaiting photos.")

# ---------------- Gulf Orchid
t = "Gulf Orchid Diwan Eau de Parfum 85ml"
F("6291107015750", "Gulf Orchid", t, "Men", "85", "19.99", "25.99", 5,
  [("Top", "Lemon, Aqueous Notes, Coconut"), ("Heart", "Anise, Lily of the Valley, Violet"), ("Base", "Cedarwood, Sandalwood, Dry Woods, Vanilla, Musk")],
  "Aquatic · Woody · Floral", "Fresh lemon and coconut over violet, sandalwood and vanilla.",
  f"{t} is a fresh, woody fragrance. Lemon, aqueous notes and coconut open brightly, a heart of anise, lily of the valley and violet follows, and it settles into a smooth base of cedarwood, sandalwood, dry woods, vanilla and musk.",
  ["A fresh lemon and coconut opening", "A soft heart of anise, lily of the valley and violet", "A smooth base of sandalwood, vanilla and musk", "Easy everyday Eau de Parfum"],
  "Notes confirmed by 2 sources (Gulf Orchid brand page, Gajanatura EAN page; Morele EAN page agrees on main notes). 85ml EDP confirmed by brand, Morele, Gajanatura, Deloox. Brand and retailers market it as unisex; supplier's Men used. Awaiting photos.",
  "lemon and coconut over violet, sandalwood and vanilla.", ["Aquatic", "Woody", "Floral"], ["Citrus", "Aquatic", "Sandalwood", "Vanilla"],
  name="Diwan")

t = "Gulf Orchid Flame Eau de Parfum 110ml"
F("6290362160588", "Gulf Orchid", t, "Unisex", "110", "21.49", "26.99", 4,
  [("Top", "Clove, Ginger"), ("Heart", "Tobacco, Incense, Cocoa"), ("Base", "Vanilla, Benzoin, Woody Notes")],
  "Spicy · Oriental · Woody", "Warm clove and ginger over tobacco, cocoa and vanilla.",
  f"{t} is a warm, spicy oriental. Clove and ginger open with heat, a heart of tobacco, incense and cocoa follows, and it settles into a rich base of vanilla, benzoin and woods.",
  ["A spicy opening of clove and ginger", "A smoky heart of tobacco, incense and cocoa", "A warm base of vanilla, benzoin and woods", "Cosy cold-weather character"],
  "Notes confirmed by 2 sources (Gulf Orchid brand page, Parfumo; Hadiyyeh agrees). EAN matches Flame 110ml EDP on Parfuem365 and eBay. Galaxus shows 100ml in its description (title 110ml); 110ml used. Awaiting photos.",
  "clove and ginger over tobacco, cocoa and vanilla.", ["Spicy", "Oriental", "Woody"], ["Spicy", "Oriental", "Vanilla", "Woody"],
  name="Flame")

t = "Gulf Orchid Mawj Eau de Parfum 110ml"
F("6290362164425", "Gulf Orchid", t, "Unisex", "110", "25.49", "34.99", 1,
  [("Top", "Orange, Mandarin, Bergamot"), ("Heart", "Grapefruit, Ginger"), ("Base", "Lily of the Valley, Musk")],
  "Citrus · Fresh · Musky", "Sparkling orange and bergamot over ginger and soft musk.",
  f"{t} is a bright, fresh citrus fragrance. Orange, mandarin and bergamot open with sparkle, a heart of grapefruit and ginger follows, and it settles on lily of the valley and clean musk.",
  ["A sparkling citrus opening", "A zesty heart of grapefruit and ginger", "A clean base of lily of the valley and musk", "Fresh, easy-wearing character"],
  "Notes confirmed by 2+ sources (Gulf Orchid brand page, Ferwer; Superdrug EAN page and Scentverdict agree; some add tea). 110ml from brand page and Superdrug EAN title, though some retailers list 100ml. Retailers split on gender; supplier's Unisex used (Superdrug agrees). Awaiting photos.",
  "orange and bergamot over ginger and soft musk.", ["Citrus", "Fresh", "Musky"], ["Citrus", "Fresh", "Floral", "Spicy"],
  name="Mawj")

t = "Gulf Orchid Perfection Eau de Parfum 105ml"
F("6290362162476", "Gulf Orchid", t, "Unisex", "105", "23.49", "30.99", 3,
  [("Top", "Bergamot, Lemon, Green Notes"), ("Heart", "Orange Blossom, Rosemary, Lavender"), ("Base", "Oakmoss, Sandalwood, Cedarwood")],
  "Aromatic · Fougere · Citrus", "Bright citrus and greens over lavender, rosemary and woods.",
  f"{t} is a fresh aromatic fragrance. Bergamot, lemon and green notes open crisply, a heart of orange blossom, rosemary and lavender follows, and it settles into a woody base of oakmoss, sandalwood and cedarwood.",
  ["A crisp opening of bergamot, lemon and greens", "An aromatic heart of lavender and rosemary", "A woody base of oakmoss, sandalwood and cedar", "Clean, versatile character"],
  "Needs review: bottle size. Supplier and Superdrug EAN page say 105ml, but Bjutip (same EAN) and Ferwer say 110ml; please check the box. Notes agreed by Bjutip, Ferwer, Emirates Oud, Scentverdict and Superdrug. 'Eau de Perfume' shown as Eau de Parfum. Retailers split on gender; supplier's Unisex used. Awaiting photos.",
  "citrus and greens over lavender, rosemary and woods.", ["Aromatic", "Fougere", "Citrus"], ["Citrus", "Lavender", "Woody", "Fresh"],
  name="Perfection", status="needs-review")

# ---------------- Lattafa Pride gift sets
def SET(no, bc, price, cmp, qty, contents, of, fr, profile, hook, note, spray=True, status="done"):
    t = f"Lattafa Pride Gift Set Collection No.{no} Eau de Parfum 5 x 20ml"
    names = [n for n, _ in contents]
    lst = ", ".join(names[:-1]) + " and " + names[-1]
    mf = {"age-group": ["Adults"], "olfactory-family": of, "fragrance": fr}
    if spray: mf.update({"product-form": ["Spray"], "dispenser-type": ["Spray"]})
    fmt = "20ml Eau de Parfum sprays" if spray else "20ml Eau de Parfum bottles"
    add(cat_name="Fragrances", bc=bc, title=t, vendor="Lattafa", type="Unisex Fragrances", gender="Unisex", cat=TAXON["perfume"],
        price=price, cmp=cmp, qty=qty, form="Eau de Parfum Gift Set", size="20", unit="ml", gpc=GPC["fragrance"],
        tags=["Lattafa", "Unisex", "Eau De Parfum"], status=status, note=note,
        seo=(f"Lattafa Pride Gift Set No.{no} Eau de Parfum 5 x 20ml", f"Lattafa Pride Gift Set No.{no}: five 20ml EDPs – {lst}."[:133] + FREE),
        mf=mf,
        desc=body(hook,
          f"The Lattafa Pride Gift Set Collection No.{no} brings together five Lattafa Pride fragrances in {fmt}: {lst}. It is an easy way to explore the range, wear a different scent each day or share as a gift.",
          [("What's in the set", ul([f"<strong>{n}</strong> – {d}" for n, d in contents]))],
          [("Brand", "Lattafa Pride"), ("Concentration", "Eau de Parfum"), ("Contents", "5 x 20ml"), ("Scent profile", profile), ("Wear", "Unisex")],
          ["Five Lattafa Pride fragrances in one box", "Handy 20ml size for travel or your bag", "A great way to find your favourite", "Ready to give as a gift"],
          [("Which fragrances are in the set?", f"{lst}, each 20ml Eau de Parfum."), ("Is it unisex?", "Yes, the set is made for everyone.")]))

SET(1, "6290362348108", "34.99", "45.99", 3,
    [("Affection", "a sweet, creamy gourmand of pistachio, hazelnut, raspberry and vanilla"),
     ("Tharwah Gold", "lavender and bergamot with orange blossom, jasmine, vanilla and amber"),
     ("Breeze", "a fresh citrus-floral musk with bergamot, cardamom, cedar and sandalwood"),
     ("Shaheen Gold", "fruity and sweet: pineapple, grapefruit, fig, vanilla and tonka"),
     ("La Collection d'Antiquités 1505", "smoky, spicy black cherry with saffron, frankincense and guaiac")],
    ["Gourmand", "Fruity", "Floral"], ["Fruity", "Vanilla", "Floral", "Citrus"], "Gourmand · Fruity · Floral",
    "Five Lattafa Pride favourites, from creamy gourmand to smoky cherry.",
    "Contents confirmed by 2+ sources (Kaufland EAN page, Triple Traders EAN page, Rackhams, Lattafa India, Intense Oud). EDP, unisex and sprays confirmed by 2+ sources. Scent summaries each from lattafa-usa plus Parfumo/retailers. Lattafa USA sells this line-up as 'Set 5'; EU No.1 numbering used. Awaiting photos.")

SET(2, "6290362348078", "30.99", "40.99", 3,
    [("Artisan Ethnique", "a boozy gourmand of rum, cinnamon, caramel, coffee and vanilla"),
     ("Natural Oud", "fruity, rosy oud with saffron, jasmine, rose and amber"),
     ("Tharwah Silver", "fresh and aromatic: mint, bergamot, lavender, cedar and musk"),
     ("Eternal Oud", "sweet, fruity-amber oud with plum, vanilla, benzoin and tonka"),
     ("Ishq Al Shuyukh Gold", "sweet leather with caramel, saffron, amber and vanilla")],
    ["Woody", "Gourmand", "Leather"], ["Woody", "Vanilla", "Oriental", "Spicy"], "Woody · Gourmand · Leather",
    "Five Lattafa Pride scents, from boozy gourmand to rich oud.",
    "Contents confirmed by 2+ sources (Kaufland and Superdrug EAN pages, Triple Traders, Rackhams, Lattafa India). EDP and unisex confirmed by 2+ sources. Spray format only stated by Triple Traders, so not claimed. Scent summaries each from lattafa-usa plus a retailer. Awaiting photos.",
    spray=False)

SET(3, "6290362348092", "34.99", "45.99", 1,
    [("Nebras", "a sweet berry-cacao gourmand with vanilla, tonka and amber"),
     ("Art of Wood", "citrus-woody: grapefruit, pink pepper, cedar, patchouli and vetiver"),
     ("Art of Universe", "fresh and fruity with mandarin, mint, pear, musk and cedar"),
     ("Ansaam Gold", "a sweet fruity floral of pear, jasmine, rose, raspberry and vanilla"),
     ("Kashan", "spicy-woody with pepper, orange, ambroxan, sandalwood and vetiver")],
    ["Fruity", "Gourmand", "Woody"], ["Fruity", "Woody", "Vanilla", "Citrus"], "Fruity · Gourmand · Woody",
    "Five Lattafa Pride scents, from berry gourmand to spicy woods.",
    "Contents confirmed by 2+ sources (Superdrug and Galaxus EAN pages, Triple Traders, Rackhams, Ferwer, Lattafa India). Superdrug's info section lists Hala instead of Kashan (its main listing says Kashan). EDP, unisex and sprays confirmed by 2+ sources. Scent summaries each from lattafa-usa plus Parfumo/Lyko. Awaiting photos.")

SET(4, "6290362348085", "41.49", "56.99", 2,
    [("Art of Arabia III", "spicy-sweet oriental with frankincense, date, tobacco and vanilla"),
     ("Ajwaa", "resinous date and liquorice with myrrh, benzoin and vanilla"),
     ("Al Qiam Gold", "fruity leather-oud with raspberry, saffron, patchouli and amber"),
     ("Masa", "fruity-spicy floral of mango, saffron, osmanthus, suede and amber"),
     ("Brioche Vanille", "a sweet bakery gourmand of brioche, heliotrope, vanilla and praline")],
    ["Oriental", "Gourmand", "Spicy"], ["Oriental", "Spicy", "Vanilla", "Fruity"], "Oriental · Gourmand · Spicy",
    "Five Lattafa Pride scents, from spiced oriental to sweet bakery gourmand.",
    "Contents confirmed by 2+ sources and match supplier list (Superdrug and Galaxus EAN pages, Triple Traders, Rackhams, Cosmetify, Lattafa India). Superdrug's info section names Sheikh Al Shuyukh instead of Brioche Vanille (main listing says Brioche Vanille). EDP, unisex and sprays confirmed by 2+ sources. Awaiting photos.")

write_outputs()
