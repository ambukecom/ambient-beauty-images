import sys; sys.path.insert(0, "/home/claude/ambient-beauty-images/workflow")
from lib import *

# ---------------- Lattafa Pride gift set No.5 (same structure as batch 2 sets)
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
        seo=(f"Lattafa Pride Gift Set No.{no} Eau de Parfum 5 x 20ml", f"Lattafa Pride Gift Set No.{no}: five 20ml Eau de Parfums from the Pride range, a gift-ready box." + FREE),
        mf=mf,
        desc=body(hook,
          f"The Lattafa Pride Gift Set Collection No.{no} brings together five Lattafa Pride fragrances in {fmt}: {lst}. It is an easy way to explore the range, wear a different scent each day or share as a gift.",
          [("What's in the set", ul([f"<strong>{n}</strong> – {d}" for n, d in contents]))],
          [("Brand", "Lattafa Pride"), ("Concentration", "Eau de Parfum"), ("Contents", "5 x 20ml"), ("Scent profile", profile), ("Wear", "Unisex")],
          ["Five Lattafa Pride fragrances in one box", "Handy 20ml size for travel or your bag", "A great way to find your favourite", "Ready to give as a gift"],
          [("Which fragrances are in the set?", f"{lst}, each 20ml Eau de Parfum."), ("Is it unisex?", "Yes, the set is made for everyone.")]))

SET(5, "6290362348061", "30.99", "40.99", 1,
    [("La Collection d'Antiquités 1910", "a sweet fruity-floral gourmand of apple, rose, osmanthus, tonka and vanilla"),
     ("Shaheen Silver", "fresh and fruity: blackcurrant and bergamot over rose, patchouli, amber and oakmoss"),
     ("African Drummer", "creamy coconut and bergamot with jasmine, orange blossom, ylang-ylang and vanilla"),
     ("Ishq Al Shuyukh Silver", "fresh citrus-woody with lemon, bergamot, pineapple, cedar and vanilla"),
     ("Vintage Radio", "aromatic lavender and sage with spicy plum and black pepper over sandalwood")],
    ["Fruity", "Floral", "Woody"], ["Fruity", "Floral", "Citrus", "Vanilla"], "Fruity · Floral · Woody",
    "Five Lattafa Pride scents, from creamy coconut florals to aromatic lavender.",
    "Contents confirmed by 3 sources (Triple Traders EAN page, Almanaar UK, Intense Oud). EDP and unisex confirmed by 2+ sources. Spray format only stated by Triple Traders, so not claimed. Scent summaries each from 2 sources (Parfumo / Fragrance Hub / Arabic Parfums / Lattafa India / Gush); Vintage Radio base only sandalwood agreed. Superdrug lists other sets under similar names – not used. Awaiting photos.",
    spray=False)

# ---------------- Maison Alhambra
t = "Maison Alhambra Karat Eau de Parfum 100ml"
F("6291107459240", "Maison Alhambra", t, "Unisex", "100", "23.49", "30.99", 1,
  [("Top", "Peach, Passion Fruit, Pear"), ("Heart", "Lily of the Valley"), ("Base", "Musk, Vanilla, Heliotrope")],
  "Fruity · Floral · Musky", "Juicy peach and passion fruit over lily of the valley, vanilla and musk.",
  f"{t} is a bright, fruity fragrance. Peach, passion fruit and pear open juicily, a heart of lily of the valley follows, and it settles on a soft base of musk, vanilla and heliotrope.",
  ["A juicy opening of peach, passion fruit and pear", "A fresh floral heart of lily of the valley", "A soft, powdery base of musk, vanilla and heliotrope", "Easy everyday Eau de Parfum"],
  "Notes confirmed by 2+ sources (Bjutip EAN page, Arabic Parfums, ScentVerdict; Triple Traders EAN page lists same notes untiered). Only agreed notes shown (raspberry, blackcurrant, sandalwood, patchouli in 2 sources only, left out). 100ml EDP confirmed by Triple Traders and Bjutip (EAN). Awaiting photos.",
  "peach and passion fruit over lily of the valley, vanilla and musk.", ["Fruity", "Floral", "Musky"], ["Fruity", "Floral", "Vanilla"],
  name="Karat")

t = "Maison Alhambra La Charmante Eau de Parfum 100ml"
F("6290362340164", "Maison Alhambra", t, "Unisex", "100", "25.99", "34.99", 1,
  [("Top", "Bergamot, Pink Pepper"), ("Heart", "Cherry, Rose, Heliotrope"), ("Base", "Vanilla, Sandalwood, Musk")],
  "Fruity · Floral · Gourmand", "Bergamot and pink pepper over cherry and rose, with vanilla and sandalwood.",
  f"{t} is a sweet, fruity-floral fragrance. Bergamot and pink pepper open with sparkle, a heart of cherry, rose and heliotrope follows, and it settles into a warm base of vanilla, sandalwood and musk.",
  ["A sparkling opening of bergamot and pink pepper", "A juicy heart of cherry and rose", "A warm base of vanilla, sandalwood and musk", "Sweet, charming character"],
  "Notes confirmed by 3 sources (Triple Traders EAN page, Target UPC page, Emirates Oud UK); red fruits (2 sources) left out. Two other sites give a different pyramid – not used. 100ml EDP confirmed. Mostly sold as unisex, some 'for her'; supplier's Unisex used. Not to be confused with La Charmante Eclatant. Awaiting photos.",
  "bergamot and pink pepper over cherry, rose and vanilla.", ["Fruity", "Floral", "Gourmand"], ["Fruity", "Rose", "Vanilla", "Sandalwood"],
  name="La Charmante")

t = "Maison Alhambra Luxe Nightlife Eau de Parfum 100ml"
F("6290362341123", "Maison Alhambra", t, "Unisex", "100", "30.49", "39.99", 1,
  [("Top", "Gardenia, Carnation, Jasmine"), ("Heart", "Patchouli, Sandalwood"), ("Base", "Caramel, Coffee")],
  "Floral · Gourmand · Woody", "White florals over patchouli and sandalwood, with caramel and coffee.",
  f"{t} is a rich floral-gourmand fragrance. Gardenia, carnation and jasmine open lushly, a heart of patchouli and sandalwood follows, and it settles on a sweet base of caramel and coffee.",
  ["A lush floral opening of gardenia, carnation and jasmine", "A woody heart of patchouli and sandalwood", "A sweet base of caramel and coffee", "Made for evenings out"],
  "Notes confirmed by 3 sources (Target UPC page, Triple Traders EAN page, Arabic Parfums), all tiers agree. 100ml EDP spray confirmed. Sold as unisex by these retailers; some US sites list it as men's. Awaiting photos.",
  "gardenia and jasmine over sandalwood, caramel and coffee.", ["Floral", "Gourmand", "Woody"], ["Floral", "Jasmine", "Sandalwood", "Spicy"],
  name="Luxe Nightlife")

t = "Maison Alhambra Smoky Eau de Parfum 100ml"
F("6291108736319", "Maison Alhambra", t, "Men", "100", "28.49", "37.99", 2,
  [("Heart", "Honey, Smoke"), ("Base", "Tobacco Leaf, Amber")],
  "Smoky · Tobacco · Amber", "Smoky honey over warm tobacco leaf and amber.",
  f"{t} is a warm, smoky fragrance. A heart of honey and smoke leads into a rich base of tobacco leaf and amber.",
  ["Smoky, honeyed character", "A warm base of tobacco leaf and amber", "Rich and long-lasting feel", "Great for cooler evenings"],
  "Needs review: scent notes. Sources disagree on the top notes (Jameela EAN page, Emirates Oud and PerfumeTrading say plum/citrus; Superdrug EAN page says bergamot, peppers, elemi, grapefruit), so top notes left out. Heart honey/smoke (Jameela, Emirates Oud, PerfumeTrading) and base tobacco/amber (also matches Superdrug's description) shown. Some sites call it a renamed 'Tabac'. 100ml EDP confirmed by Superdrug and Jameela (EAN). Not the same as Smoky Touch 80ml. Retailers mostly sell it as unisex; supplier's Men used. Awaiting photos.",
  "smoky honey over tobacco leaf and amber.", ["Oriental", "Woody"], ["Oriental", "Woody"],
  name="Smoky", status="needs-review")

# ---------------- Rasasi
t = "Rasasi Daarej Pour Homme Eau de Parfum 100ml"
F("0614514178010", "Rasasi", t, "Men", "100", "21.99", "27.99", 2,
  [("Top", "Cardamom, Cumin, Artemisia"), ("Heart", "Rose, Iris"), ("Base", "Vanilla, Tonka Bean, Amber, Sandalwood, Patchouli, Musk")],
  "Spicy · Oriental · Powdery", "Spiced cardamom and cumin over rose and iris, with vanilla and amber.",
  f"{t} is a warm, spicy oriental. Cardamom, cumin and artemisia open with spice, a powdery heart of rose and iris follows, and it settles into a rich base of vanilla, tonka, amber, sandalwood, patchouli and musk.",
  ["A spicy opening of cardamom and cumin", "A powdery heart of rose and iris", "A rich base of vanilla, tonka and amber", "Warm, distinguished character"],
  "Notes confirmed by 2 sources (Parfumo, Elryan with matching product code), all tiers agree; barcode also listed on FragranceX and Perfume.com. 100ml EDP confirmed. Men's version (not Daarej Pour Femme, which is already on the site). Awaiting photos.",
  "cardamom and cumin over rose, iris, vanilla and amber.", ["Oriental", "Spicy", "Powdery"], ["Spicy", "Oriental", "Vanilla", "Rose"],
  name="Daarej Pour Homme")

t = "Rasasi Hawas Fire Eau de Parfum 100ml"
F("0614514178065", "Rasasi", t, "Unisex", "100", "38.49", "51.99", 4,
  [("Top", "Clary Sage"), ("Heart", "Jasmine, Marine Notes"), ("Base", "Amber, Ambergris")],
  "Aquatic · Aromatic · Fresh", "Clary sage over jasmine and marine notes, with amber and ambergris.",
  f"{t} is a fresh, aquatic fragrance. Clary sage opens aromatically, a heart of jasmine and marine notes follows, and it settles on a warm base of amber and ambergris.",
  ["An aromatic opening of clary sage", "A fresh heart of jasmine and marine notes", "A warm base of amber and ambergris", "Fresh, modern character"],
  "Notes confirmed by 3 sources (Sharaf DG EAN page, FragranceHub UK, Fragplace; Parfumo agrees). Extra notes on Sharaf DG only, left out. 100ml EDP confirmed by Sharaf DG (EAN). Gender split: FragranceHub UK and Notino UK say unisex, Sharaf DG and others say men ('Hawas for Him Fire'); supplier's Unisex used. Awaiting photos.",
  "clary sage over jasmine and marine notes with amber.", ["Aquatic", "Aromatic", "Fresh"], ["Aquatic", "Fresh", "Jasmine"],
  name="Hawas Fire")

t = "Rasasi Hawas Gold Digger Eau de Parfum 100ml"
F("0614514331262", "Rasasi", t, "Men", "100", "38.49", "48.99", 5,
  [("Top", "Pear, Mint, Lavender, Bergamot"), ("Heart", "Cinnamon, Sage"), ("Base", "Vanilla, Amber, Cedarwood, Patchouli")],
  "Aromatic · Woody · Spicy", "Pear, mint and lavender over cinnamon and sage, with vanilla and cedar.",
  f"{t} is an aromatic, woody fragrance. Pear, mint, lavender and bergamot open freshly, a heart of cinnamon and sage follows, and it settles into a warm base of vanilla, amber, cedarwood and patchouli.",
  ["A fresh opening of pear, mint, lavender and bergamot", "A spicy heart of cinnamon and sage", "A warm base of vanilla, amber and cedarwood", "A 2026 addition to the Hawas line"],
  "Notes confirmed by 2+ sources (Kruidvat EAN page, Ferwer, Arabic Parfums, FridayCharm), all tiers agree. 100ml EDP confirmed. Launched 2026 (Gulf Today). Parfumo's 'Hawas Gold Digger' entry has different notes and looks like a different/wrong entry – not used. Awaiting photos.",
  "pear, mint and lavender over cinnamon, vanilla and cedar.", ["Aromatic", "Woody", "Spicy"], ["Lavender", "Spicy", "Woody", "Vanilla"],
  name="Hawas Gold Digger")

# ---------------- Rue Broca
t = "Rue Broca Penthouse Ginza Eau de Parfum 80ml"
F("6290171010487", "Rue Broca", t, "Unisex", "80", "25.49", "33.99", 1,
  [("Top", "Bergamot, Grapefruit"), ("Heart", "Bay Leaf, Jasmine, Lavender"), ("Base", "Oakmoss, Patchouli, Amber")],
  "Fougere · Citrus · Aromatic", "Bergamot and grapefruit over bay leaf and lavender, with oakmoss and amber.",
  f"{t} is a fresh aromatic fragrance. Bergamot and grapefruit open brightly, a heart of bay leaf, jasmine and lavender follows, and it settles on a classic base of oakmoss, patchouli and amber.",
  ["A bright citrus opening of bergamot and grapefruit", "An aromatic heart of bay leaf, jasmine and lavender", "A classic base of oakmoss, patchouli and amber", "Clean, versatile character"],
  "Notes confirmed by 4 sources (Bjutip and Triple Traders EAN pages, Ferwer, McGrocer), all tiers agree. 80ml EDP confirmed by EAN. Rue Broca is an Afnan house. Gender split: Ferwer and McGrocer say unisex, Bjutip and Notino UK say men; supplier's Unisex used. Awaiting photos.",
  "bergamot and grapefruit over lavender, oakmoss and amber.", ["Fougere", "Citrus", "Aromatic"], ["Citrus", "Fresh", "Lavender", "Jasmine"],
  name="Penthouse Ginza")

t = "Rue Broca Penthouse Windsor Eau de Parfum 80ml"
F("6290171010456", "Rue Broca", t, "Unisex", "80", "25.49", "33.99", 1,
  [("Top", "Oud, Benzoin, Rose"), ("Heart", "Saffron, Amberwood, Leather"), ("Base", "Incense, Birch, Raspberry")],
  "Oriental · Leather · Woody", "Oud and rose over saffron and leather, with incense and birch.",
  f"{t} is a rich oriental-leather fragrance. Oud, benzoin and rose open warmly, a heart of saffron, amberwood and leather follows, and it settles on a smoky base of incense, birch and raspberry.",
  ["A warm opening of oud, benzoin and rose", "A rich heart of saffron, amberwood and leather", "A smoky base of incense, birch and raspberry", "Bold, luxurious character"],
  "Needs review: bottle size. Supplier lists 100ml, but every source shows 80ml, including Bjutip and Lyko pages with this EAN and Oasis Fashion UK (matching SKU); listed as 80ml – please check the bottle. Notes confirmed by 4 sources (Bjutip, Lyko, Oasis, Parfumo; FragranceX agrees). Mostly sold as unisex; supplier's Unisex used. Awaiting photos.",
  "oud and rose over saffron, leather and incense.", ["Oriental", "Leather", "Woody"], ["Oriental", "Woody", "Spicy", "Rose"],
  name="Penthouse Windsor", status="needs-review")

write_outputs()
