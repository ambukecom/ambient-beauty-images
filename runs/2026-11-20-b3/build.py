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

DG = "Dolce & Gabbana"
# ---------------- Dolce & Gabbana K EDP set
t = "Dolce & Gabbana K Eau de Parfum 100ml Gift Set with After Shave Balm and Shower Gel"
GS("8054754400618", DG, t, "Dolce & Gabbana K EDP 100ml 3-Piece Gift Set", "Men", "100", "61.99", "82.99", 5,
   [("Top", "Sicilian Lemon, Blood Orange, Juniper Berries, Cardamom"), ("Heart", "Fig, Lavender, Geranium, Clary Sage"), ("Base", "Cedar, Patchouli, Vetiver, Cypriol")],
   "Citrus · Aromatic · Woody", "A regal, citrus-bright K with grooming essentials to match.",
   f"{t} brings together K by Dolce & Gabbana Eau de Parfum with a matching after shave balm and shower gel. Sicilian lemon, blood orange, juniper and cardamom open brightly, a heart of fig, lavender, geranium and clary sage follows, and it settles on cedar, patchouli, vetiver and cypriol.",
   ["K Eau de Parfum 100ml (spray)", "K After Shave Balm 50ml", "K Shower Gel 50ml"],
   ["A sparkling citrus opening of lemon and blood orange", "An aromatic heart of fig, lavender and sage", "A deep woody base of cedar, vetiver and patchouli", "A complete grooming gift for him"],
   "EAN 8054754400618 matched on El Corte Inglés and eBay (EDP 100ml + 50ml after shave balm + 50ml shower gel); contents also per Amazon UK and ScentsWorld. Pyramid agreed by El Corte Inglés, Olfastory, Parfumistas (chilli/pimento placed in different tiers, left out). EDP launched 2020 per Olfastory and Parfumistas. Not the K EDT gift set. Awaiting photos.",
   "lemon and blood orange over fig, lavender and cedar.", ["Citrus", "Aromatic", "Woody"], ["Citrus", "Lavender", "Woody", "Spicy"],
   name="K by Dolce & Gabbana", **PC)

# ---------------- Dolce & Gabbana K Intense set
t = "Dolce & Gabbana K Eau de Parfum Intense 100ml Gift Set with 10ml Travel Spray"
GS("8054754400625", DG, t, "Dolce & Gabbana K EDP Intense 100ml & 10ml Gift Set", "Men", "100", "57.99", "73.99", 5,
   [("Top", "Saffron"), ("Heart", "Fig"), ("Base", "Leather")],
   "Leather · Spicy · Fruity", "K turned up: saffron, fig and leather in an intense eau de parfum.",
   f"{t} pairs the full-size K Eau de Parfum Intense with a handy 10ml travel spray. Warm saffron opens, a rich fig heart follows, and it settles on a smooth, sensual leather base.",
   ["K Eau de Parfum Intense 100ml (spray)", "Travel spray 10ml"],
   ["A warm, spicy saffron opening", "A rich, fruity fig heart", "A sensual leather finish", "Travel spray for on-the-go top-ups"],
   "EAN 8054754400625 matched on News-Parfums and Farmacia Loreto (K EDP Intense 100ml + 10ml travel spray); Jomashop also carries it. Notes agreed by News-Parfums and Nordstrom (Parfumo and D&G site list the same three). 2024 per Parfumo. Supplier says '+10ml EDP'; Escentual calls the mini 'EDP Intense travel spray' – listed simply as a 10ml travel spray. Awaiting photos.",
   "saffron, fig and leather, with 10ml travel spray.", ["Leather", "Spicy", "Fruity"], ["Spicy", "Fruity", "Woody"],
   name="K Eau de Parfum Intense", conc="Eau De Parfum", concl="Eau de Parfum Intense")

ES = "Elie Saab"
# ---------------- Elie Saab Girl of Now set
t = "Elie Saab Girl of Now Eau de Parfum 50ml Gift Set with 75ml Body Lotion"
GS("7640233340561", ES, t, "Elie Saab Girl of Now EDP 50ml & Body Lotion Gift Set", "Women", "50", "42.49", "55.99", 5,
   [("Top", "Pistachio, Pear, Mandarin"), ("Heart", "Almond, Orange Blossom, Magnolia"), ("Base", "Almond Milk, Cashmeran, Tonka Bean, Patchouli")],
   "Gourmand · Floral · Fruity", "A nutty, creamy floral for the modern woman.",
   f"{t} pairs Girl of Now Eau de Parfum with a matching body lotion. Pistachio, pear and mandarin open playfully, a heart of almond, orange blossom and magnolia follows, and it settles on almond milk, cashmeran, tonka bean and patchouli.",
   ["Girl of Now Eau de Parfum 50ml (spray)", "Girl of Now Body Lotion 75ml"],
   ["A playful opening of pistachio and pear", "A creamy heart of almond and orange blossom", "A soft, warm base of tonka and almond milk", "Matching body lotion to layer the scent"],
   "EAN 7640233340561 matched only on two eBay UK listings (50ml EDP + 75ml body lotion); contents also per Amazon UK, Cosmetify, Welzo. Pyramid agreed by Parfumo, Perfumes Club UK, Olfastory. 2017 per Parfumo and Perfumes Club. Not the Girl of Now Lovely or Shine sets. Awaiting photos.",
   "pistachio and pear over almond, orange blossom and tonka.", ["Gourmand", "Floral", "Fruity"], ["Fruity", "Citrus", "Floral"],
   name="Girl of Now", **PC)

# ---------------- Elie Saab Le Parfum Lumière set
t = "Elie Saab Le Parfum Lumière Eau de Parfum 50ml Gift Set with 10ml Eau de Parfum"
GS("7640233340745", ES, t, "Elie Saab Le Parfum Lumière EDP 50ml & 10ml Gift Set", "Women", "50", "46.49", "62.99", 5,
   [("Top", "Orange Blossom, Mandarin, Ylang-Ylang"), ("Heart", "Jasmine Sambac, Tuberose, Gardenia"), ("Base", "Patchouli, Musk, Amber, Woody Notes")],
   "Floral · Woody · Musky", "A luminous white floral that glows like light on silk.",
   f"{t} pairs Le Parfum Lumière with a 10ml Eau de Parfum for your bag. Orange blossom, mandarin and ylang-ylang open with radiance, a heart of jasmine sambac, tuberose and gardenia follows, and it settles on patchouli, musk, amber and woods.",
   ["Le Parfum Lumière Eau de Parfum 50ml (spray)", "Le Parfum Lumière Eau de Parfum 10ml (spray)"],
   ["A radiant opening of orange blossom and mandarin", "A lush white-floral heart of jasmine, tuberose and gardenia", "A warm base of patchouli, amber and musk", "10ml size to carry with you"],
   "EAN 7640233340745 matched on an eBay UK listing and a (de-listed) CH Tralee page (50ml EDP set); 50ml + 10ml EDP contents per Perfume-Click, Half Price Perfumes, Amazon.es. Pyramid agreed by Coral Perfumes, Perfume Centre UK, BellaZofia (Perfume-Click same notes untiered). 2021 per Perfume-Click and Perfume Centre. A different set with body lotion exists – check the box shows the 10ml EDP. Awaiting photos.",
   "orange blossom over jasmine, tuberose and amber, plus 10ml.", ["Floral", "Woody", "Musky"], ["Floral", "Jasmine", "Citrus", "Woody"],
   name="Le Parfum Lumière", **PC)

# ---------------- Elizabeth Arden Sunflowers set
t = "Elizabeth Arden Sunflowers Eau de Toilette 100ml Gift Set with 100ml Body Lotion"
GS("0085805255824", "Elizabeth Arden", t, "Elizabeth Arden Sunflowers EDT 100ml & Body Lotion Set", "Women", "100", "23.99", "31.99", 2,
   [("Top", "Bergamot, Lemon, Mandarin, Melon, Peach, Orange Blossom, Rosewood"), ("Heart", "Cyclamen, Jasmine, Rose, Orris Root"), ("Base", "Sandalwood, Cedar, Musk, Amber, Oakmoss")],
   "Fruity · Floral · Fresh", "Sunshine in a bottle: a fresh, fruity floral classic.",
   f"{t} pairs the much-loved Sunflowers Eau de Toilette with a matching body lotion. Bergamot, lemon, melon and peach open with sunny freshness, a heart of cyclamen, jasmine, rose and orris follows, and it settles on sandalwood, cedar, musk and amber.",
   ["Sunflowers Eau de Toilette 100ml (spray)", "Sunflowers Body Lotion 100ml"],
   ["A sunny opening of citrus, melon and peach", "A soft floral heart of jasmine and rose", "A warm base of sandalwood, cedar and amber", "Great-value gift with a full-size 100ml spray"],
   "EAN 0085805255824 matched on Walmart (UPC), Shop-Apotheke and eBay UK – EDT 100ml + body lotion 100ml. Pyramid agreed by The Perfume Shop, FragranceX, South Beach Perfumes, Walmart (osmanthus placed in different tiers, left out). 1993 per The Perfume Shop, FragranceX, South Beach. Awaiting photos.",
   "citrus, melon and peach over jasmine and sandalwood.", ["Fruity", "Floral", "Fresh"], ["Citrus", "Fruity", "Floral", "Jasmine", "Sandalwood"],
   name="Sunflowers", **TC)

# ---------------- Estée Lauder Beautiful set
t = "Estée Lauder Beautiful Eau de Parfum 75ml Gift Set with 10ml Eau de Parfum and 75ml Body Lotion"
GS("0887167697232", "Estée Lauder", t, "Estée Lauder Beautiful EDP 75ml 3-Piece Gift Set", "Women", "75", "69.99", "88.99", 5,
   [("Top", "Rose, Mandarin, Lily, Tuberose, Marigold"), ("Heart", "Orange Flower, Muguet, Jasmine, Ylang-Ylang"), ("Base", "Sandalwood, Vetiver, Amber")],
   "Floral · Woody · Citrus", "A romantic bouquet of a thousand flowers.",
   f"{t} brings together the iconic Beautiful Eau de Parfum, a 10ml spray for your bag and a perfumed body lotion. Rose, mandarin, lily and tuberose open in full bloom, a heart of orange flower, muguet, jasmine and ylang-ylang follows, and it settles on sandalwood, vetiver and amber.",
   ["Beautiful Eau de Parfum 75ml (spray)", "Beautiful Eau de Parfum 10ml (spray)", "Beautiful Perfumed Body Lotion 75ml"],
   ["A lush floral opening of rose, lily and tuberose", "A heart of orange flower, jasmine and ylang-ylang", "A warm base of sandalwood, vetiver and amber", "Three pieces, including a 10ml travel spray"],
   "EAN 0887167697232 matched on samawa.ae (75ml EDP + 10ml EDP + 75ml body lotion); contents also per Fragrance Direct and Cosmetify (eBay may call it 'Beautiful Favorites Trio'). Pyramid agreed on every tier by The Perfume Shop, John Lewis, Fragrance Direct. 1985 per The Perfume Shop and John Lewis. A version with 100ml lotion exists – check the box. Awaiting photos.",
   "rose, lily and orange flower over sandalwood and amber.", ["Floral", "Woody", "Citrus"], ["Floral", "Rose", "Jasmine", "Citrus", "Sandalwood"],
   name="Beautiful", **PC)

# ---------------- French Avenue Black Kabul
t = "French Avenue Black Kabul Eau de Parfum 60ml"
F("6291106484434", "French Avenue", t, "Unisex", "60", "25.49", "32.99", 1,
  [("Top", "Green Notes, Coffee"), ("Heart", "Tobacco, Resins, Incense"), ("Base", "Oud, Dark Woods")],
  "Woody · Spicy · Oriental", "Smoky, dark and resinous, with a jolt of coffee.",
  f"{t} is a dark, smoky oriental from French Avenue. Green notes and coffee open with an intriguing twist, a heart of tobacco, resins and incense follows, and it settles on oud and dark woods.",
  ["A distinctive opening of green notes and coffee", "A smoky heart of tobacco, resins and incense", "A deep base of oud and dark woods", "Eau de Parfum strength in a 60ml size"],
  "NEEDS REVIEW: EAN 6291106484434 matched on Superdrug (60ml EDP) and Jomashop/eBay; Lovenmour ties it to the 'New Edition'. Notes: Arabicparfums and Lovenmour agree on the pyramid shown; ScentVerdict (New Edition) puts coffee in the heart and incense in the base; TJ Hughes lists a completely different pyramid (possibly the original version) – please check the box. Supplier gender Unisex kept (Jomashop/TJ Hughes say men, Superdrug files under women). Awaiting photos.",
  "green notes and coffee over tobacco, incense and oud.", ["Woody", "Spicy", "Oriental"], ["Woody", "Spicy", "Oriental"],
  name="Black Kabul", status="needs-review")

# ---------------- Gisada Ambassador Women set
t = "Gisada Ambassador Women Eau de Parfum 50ml Gift Set with 100ml Shower Gel"
GS("7640164030616", "Gisada", t, "Gisada Ambassador Women EDP 50ml & Shower Gel Gift Set", "Women", "50", "56.99", "71.99", 2,
   [("Top", "Pear, Bergamot, Violet Leaves, Marigold"), ("Heart", "Freesia, Rose, Tuberose, Raspberry, Plum"), ("Base", "Musk, Patchouli, Sandalwood, Cedar, Vanilla, Tonka Bean")],
   "Fruity · Floral · Woody", "A juicy, elegant floral from Switzerland's Gisada.",
   f"{t} pairs Ambassador Women Eau de Parfum with a matching shower gel. Pear, bergamot, violet leaves and marigold open brightly, a heart of freesia, rose, tuberose, raspberry and plum follows, and it settles on musk, patchouli, sandalwood, cedar, vanilla and tonka.",
   ["Ambassador Women Eau de Parfum 50ml (spray)", "Ambassador Women Shower Gel 100ml"],
   ["A juicy opening of pear and bergamot", "A rich floral-fruity heart of rose, tuberose and raspberry", "A warm base of sandalwood, vanilla and tonka", "Matching shower gel to layer the scent"],
   "EAN 7640164030616 matched on Solippy and Jomashop (50ml EDP + 100ml shower gel); contents also per Perfume-Click, Amazon, eBay UK. Pyramid agreed by The Perfume Shop, Justmylook, Lyko, ScentVerdict (Solippy's different list ignored). Launch year disagrees (2019 vs 2024), not stated. Not the Ambassadora set. Awaiting photos.",
   "pear and bergamot over rose, tuberose and sandalwood.", ["Fruity", "Floral", "Woody"], ["Fruity", "Floral", "Rose", "Sandalwood", "Vanilla"],
   name="Ambassador Women", **PC)

# ---------------- Hermès Terre d'Hermès set
t = "Hermès Terre d'Hermès Eau de Toilette 100ml Gift Set with 80ml Shower Gel"
GS("3346130010630", "Hermès", t, "Hermès Terre d'Hermès EDT 100ml & Shower Gel Gift Set", "Men", "100", "70.99", "95.99", 2,
   [("Top", "Orange, Grapefruit"), ("Heart", "Pepper, Pelargonium, Flint"), ("Base", "Vetiver, Cedar, Patchouli, Benzoin")],
   "Woody · Citrus · Spicy", "An earthy, mineral classic rooted in the land.",
   f"{t} pairs the celebrated Terre d'Hermès Eau de Toilette, created by Jean-Claude Ellena in 2006, with a matching shower gel. Orange and grapefruit open brightly, a mineral heart of pepper, pelargonium and flint follows, and it settles on vetiver, cedar, patchouli and benzoin.",
   ["Terre d'Hermès Eau de Toilette 100ml (spray)", "Terre d'Hermès Shower Gel 80ml"],
   ["A bright opening of orange and grapefruit", "A distinctive mineral heart of flint and pepper", "An earthy base of vetiver, cedar and patchouli", "A refined gift with a full-size 100ml spray"],
   "EAN 3346130010630 matched on Superdrug and DLG International (EDT 100ml + shower gel 80ml). Pyramid agreed by Wikipedia and Tendance-Parfums (Parfumo same notes untiered). 2006, Jean-Claude Ellena per Wikipedia and Tendance-Parfums. New Hermès brand collection created. Awaiting photos.",
   "orange and grapefruit over flint, pepper and vetiver.", ["Woody", "Citrus", "Spicy"], ["Woody", "Citrus", "Spicy"],
   name="Terre d'Hermès", **TC)

# ---------------- Hugo Boss The Scent for Her set
t = "Hugo Boss The Scent for Her Eau de Parfum 50ml Gift Set with 75ml Body Lotion"
GS("3616304198007", "Hugo Boss", t, "Hugo Boss The Scent for Her EDP 50ml & Lotion Gift Set", "Women", "50", "50.99", "67.99", 5,
   [("Top", "Honeyed Peach, Freesia"), ("Heart", "Osmanthus"), ("Base", "Roasted Cocoa")],
   "Fruity · Floral · Gourmand", "Seductive peach, osmanthus and roasted cocoa.",
   f"{t} pairs BOSS The Scent for Her Eau de Parfum with a matching body lotion. Honeyed peach and freesia open warmly, a heart of osmanthus follows, and it settles on a rich roasted cocoa base.",
   ["BOSS The Scent for Her Eau de Parfum 50ml (spray)", "BOSS The Scent for Her Body Lotion 75ml"],
   ["A sweet opening of honeyed peach and freesia", "A floral heart of osmanthus", "A seductive roasted cocoa finish", "Matching body lotion to layer the scent"],
   "EAN 3616304198007 matched on Mellericks.ie and Envie2parfum.fr (EDP 50ml + body lotion 75ml); contents also per Scentsational and Excalibur. Pyramid agreed by The Perfume Shop and LookFantastic. Launch year on one source only, not stated. Store has a separate draft for the 50ml EDP alone (not this set). Awaiting photos.",
   "honeyed peach over osmanthus and roasted cocoa, with lotion.", ["Fruity", "Floral", "Gourmand"], ["Fruity", "Floral"],
   name="The Scent for Her", **PC)

write_outputs()
