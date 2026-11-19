import sys; sys.path.insert(0, "/home/claude/ambient-beauty-images/workflow")
from lib import *
AF = "Abercrombie & Fitch"
TC = dict(conc="Eau De Toilette", concl="Eau de Toilette")
COLOGNE = dict(conc="Eau De Cologne", concl="Eau de Cologne")

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

# ---------------- Gift sets from the Bath and Body tab
t = "Marc Jacobs Daisy Eau de Toilette 100ml Gift Set with 75ml Body Lotion"
GS("3616305181381", "Marc Jacobs", t, "Marc Jacobs Daisy EDT 100ml & Body Lotion Gift Set", "Women", "100", "63.99", "83.99", 5,
   [("Top", "Wild Strawberry, Violet Leaf, Grapefruit"), ("Heart", "Jasmine, Gardenia, Violet"), ("Base", "White Woods, Musk, Vanilla")],
   "Floral · Fruity · Musky", "The much-loved Daisy, paired with a matching body lotion.",
   f"{t} brings together the iconic Daisy Eau de Toilette and a softly scented body lotion. Wild strawberry, violet leaf and grapefruit open brightly, a heart of jasmine, gardenia and violet follows, and it settles on white woods, musk and vanilla.",
   ["Daisy Eau de Toilette 100ml (spray)", "Daisy Body Lotion 75ml"],
   ["The iconic Daisy fragrance in a full 100ml size", "A matching body lotion to layer the scent", "Fresh, fruity and floral, easy to wear every day", "Ready to give as a gift"],
   "Contents (2 pieces, no travel spray) confirmed by EAN-matched listing (eBay UPC 3616305181381) and Tesco marketplace; the 3-piece Daisy sets with a 10ml spray have different EANs. Notes agreed by ScentVerdict, Superdrug (2 Daisy set pages), Tesco; LookFantastic gives a simpler pyramid (not used). Supplier lists it in the Bath and Body tab; listed as a fragrance gift set (product type Women's Fragrance). Awaiting photos.",
   "Daisy EDT with strawberry, jasmine and musk, plus body lotion.", ["Floral", "Fruity", "Musky"], ["Floral", "Fruity", "Jasmine", "Woody", "Vanilla"],
   name="Daisy")

t = "Police To Be Camouflage Eau de Toilette 75ml Gift Set with 100ml Shower Gel"
GS("0679602793643", "Police", t, "Police To Be Camouflage EDT 75ml & Shower Gel Gift Set", "Men", "75", "22.99", "29.99", 3,
   [("Top", "Red Apple, Mint, Cardamom, Lemon"), ("Heart", "Lavender, Cinnamon, Violet, Nutmeg, Rhubarb"), ("Base", "Tonka Bean, Vanilla, Amber, Vetiver, Cashmere Wood")],
   "Fougere · Oriental · Woody", "A spicy amber fougère with a matching shower gel.",
   f"{t} pairs the To Be Camouflage fragrance with a matching shower gel. Red apple, mint, cardamom and lemon open freshly, a spicy heart of lavender, cinnamon, violet, nutmeg and rhubarb follows, and it settles on tonka bean, vanilla, amber, vetiver and cashmere wood.",
   ["To Be Camouflage Eau de Toilette 75ml (spray)", "To Be Camouflage Shower Gel 100ml"],
   ["Fresh apple and mint over warm spices", "A cosy base of tonka, vanilla and amber", "Matching shower gel to layer the scent", "Great value gift for him"],
   "Needs review: EAN. Supplier EAN 0679602793643 could not be matched online; Superdrug's 75ml EDT + 100ml Shower Gel listing shows EAN 0679602774314, and Police also sells 75ml + 100ml lotion and body shampoo versions – please check the box contents. Contents per supplier, confirmed for the shower-gel set by Superdrug and Cosmetify. Notes agreed by Parfumo, Flannels, Perfumes Club (ozonic/solar accords left out). Superdrug files the shower-gel set under 'for her'; Parfumo/Flannels and supplier say men, so Men used. Supplier lists it in the Bath and Body tab; listed as a fragrance gift set. Awaiting photos.",
   "apple and mint over lavender, spice and tonka, with shower gel.", ["Fougere", "Oriental", "Woody"], ["Fruity", "Lavender", "Spicy", "Vanilla", "Woody"],
   name="To Be Camouflage", status="needs-review")

# ---------------- Fragrances
t = "Abercrombie & Fitch 100% Passion Man Eau de Toilette 100ml"
F("0085715166708", AF, t, "Men", "100", "35.99", "45.99", 5,
  [("Top", "Mandarin, Bergamot, Grapefruit"), ("Heart", "Black Pepper, Lavender, Apple, Plum"), ("Base", "Amber, Sandalwood, Tonka Bean, Musk")],
  "Oriental · Citrus · Spicy", "Bright citrus and black pepper over warm amber and tonka.",
  f"{t} is a warm, citrusy amber fragrance launched in 2025. Mandarin, bergamot and grapefruit open brightly, a heart of black pepper, lavender, apple and plum follows, and it settles into a smooth base of amber, sandalwood, tonka bean and musk.",
  ["A bright opening of mandarin, bergamot and grapefruit", "A spicy-fruity heart of black pepper, apple and plum", "A warm base of amber, sandalwood and tonka", "Modern and easy to wear, day or night"],
  "Full pyramid agreed by Parfumdreams and Lyko (Escentual and ScentVerdict list only mandarin, pepper, amber – consistent). 100ml EDT, men and 2025 launch confirmed by Escentual, Next, Parfumdreams, Lyko, ScentVerdict. EAN not found online. Awaiting photos.",
  "mandarin and black pepper over amber, sandalwood and tonka.", ["Oriental", "Citrus", "Spicy"], ["Citrus", "Spicy", "Lavender", "Fruity", "Sandalwood"],
  name="100% Passion Man", **TC)

t = "Abercrombie & Fitch 100% Passion Woman Eau de Parfum 100ml"
F("0085715166494", AF, t, "Women", "100", "35.99", "48.99", 5,
  [("Top", "Pear"), ("Heart", "Orange Blossom, Jasmine"), ("Base", "Amber, Labdanum, Vanilla")],
  "Floral · Oriental", "Juicy pear and white flowers over warm amber and vanilla.",
  f"{t} is a warm floral-amber fragrance. Juicy pear opens, a heart of orange blossom and jasmine follows, and it settles into a rich base of amber, labdanum and bourbon vanilla.",
  ["A juicy pear opening", "A luminous heart of orange blossom and jasmine", "A warm base of amber, labdanum and vanilla", "Eau de Parfum strength"],
  "Notes agreed by Escentual, Next, Parfumdreams, Lyko; only pear kept in the top (orange/nectarine wording differs between sources), strawberry and freesia (1 source each) left out. 100ml EDP and women confirmed by the same 4 sources. EAN not found online. Awaiting photos.",
  "juicy pear over orange blossom, jasmine, amber and vanilla.", ["Floral", "Oriental"], ["Fruity", "Floral", "Jasmine", "Vanilla", "Oriental"],
  name="100% Passion Woman")

t = "Abercrombie & Fitch Authentic Night Eau de Toilette 100ml Gift Set with 15ml Travel Spray"
GS("0085715166425", AF, t, "A&F Authentic Night EDT 100ml & 15ml Gift Set", "Men", "100", "30.99", "40.99", 5,
   [("Top", "Apple, Rhubarb, Lotus"), ("Heart", "Lavender, Vanilla"), ("Base", "Leather, Oakmoss")],
   "Oriental · Fougere", "Authentic Night at home and on the go.",
   f"{t} pairs a full-size bottle of Authentic Night with a handy travel spray. Crisp apple, rhubarb and lotus open, a heart of lavender and vanilla follows, and it settles on leather and oakmoss.",
   ["Authentic Night Eau de Toilette 100ml (spray)", "Authentic Night Eau de Toilette 15ml (travel spray)"],
   ["Crisp apple and rhubarb with lavender and vanilla", "A smooth leather and oakmoss base", "Travel spray for your bag or gym kit", "Ready to give as a gift"],
   "Contents confirmed by Superdrug (EAN page: 100ml EDT + travel spray) and Cosmetify (100ml + 15ml EDT, no body wash). Notes agreed by Parfumo and LookFantastic; tonka bean left out (sources disagree on tier), ambrox only on Parfumo. Oriental fougère per Superdrug. Awaiting photos.",
   "apple, lavender and vanilla over leather, with travel spray.", ["Oriental", "Fougere"], ["Fruity", "Lavender", "Vanilla", "Woody"],
   name="Authentic Night")

t = "Abercrombie & Fitch Authentic Woman Eau de Parfum 100ml"
F("0085715166517", AF, t, "Women", "100", "33.49", "43.99", 5,
  [("Top", "Pear, Mandarin Orange, Red Currant"), ("Heart", "Magnolia, Lily of the Valley, Nectarine"), ("Base", "Ambrette, Cedarwood, Sandalwood")],
  "Floral · Woody · Musky", "Pear and red currant over magnolia, with soft woods and ambrette.",
  f"{t} is a fresh floral-woody musk. Pear, mandarin orange and red currant open brightly, a heart of magnolia, lily of the valley and nectarine follows, and it settles on a soft base of ambrette, cedarwood and sandalwood.",
  ["A fruity opening of pear, mandarin and red currant", "A delicate heart of magnolia and lily of the valley", "A soft base of ambrette, cedar and sandalwood", "Eau de Parfum strength"],
  "Notes agreed by Superdrug, Beauty Bay, JustMyLook, LookFantastic (all tiers). 100ml EDP and women confirmed by the same sources. EAN not found online. Not the same as Authentic Moment or Authentic Night Woman. Awaiting photos.",
  "pear and red currant over magnolia, cedar and sandalwood.", ["Floral", "Woody", "Musky"], ["Fruity", "Floral", "Citrus", "Woody", "Sandalwood"],
  name="Authentic Woman")

t = "Abercrombie & Fitch Away Man Eau de Toilette 50ml Gift Set with 200ml Hair & Body Wash"
GS("0085715164179", AF, t, "A&F Away Man EDT 50ml & Hair & Body Wash Gift Set", "Men", "50", "30.99", "39.99", 5,
   [("Top", "Grapefruit, Pineapple, Violet Leaf"), ("Heart", "Ginger, White Pepper, Geranium"), ("Base", "Blonde Woods, Vetiver, Amber")],
   "Fresh · Woody · Aromatic", "A fresh, sunny escape with a matching wash.",
   f"{t} pairs Away Man with a matching hair and body wash. Grapefruit, pineapple and violet leaf open freshly, a heart of ginger, white pepper and geranium follows, and it settles on blonde woods, vetiver and amber.",
   ["Away Man Eau de Toilette 50ml (spray)", "Away Man Hair & Body Wash 200ml"],
   ["Fresh grapefruit and pineapple", "A lightly spiced heart of ginger and white pepper", "Matching wash to layer the scent", "Great value gift for him"],
   "Contents confirmed by Superdrug (EAN page, 50ml EDT + 200ml hair & body wash) and Proshop (250ml set); Superdrug's description says 'body wash', title says hair & body wash. Notes agreed by Parfumo and LookFantastic (sandalwood only on Superdrug, left out). Awaiting photos.",
   "grapefruit and ginger over woods and vetiver, with hair & body wash.", ["Fresh", "Woody", "Aromatic"], ["Fresh", "Citrus", "Fruity", "Spicy", "Woody"],
   name="Away Man")

t = "Abercrombie & Fitch Away Tonight Man Eau de Toilette 100ml"
F("0085715169303", AF, t, "Men", "100", "27.49", "36.99", 5,
  [("Top", "Bergamot, Grapefruit, Black Pepper"), ("Heart", "Carrot, Geranium"), ("Base", "Sandalwood, Patchouli, Cedarwood")],
  "Woody · Fresh · Citrus", "Sparkling citrus and black pepper over smooth woods.",
  f"{t} is a fresh, woody evening fragrance. Bergamot, grapefruit and black pepper open with sparkle, an unusual heart of carrot and geranium follows, and it settles on sandalwood, patchouli and cedarwood.",
  ["A sparkling opening of bergamot and grapefruit", "A distinctive heart of carrot and geranium", "A smooth base of sandalwood, patchouli and cedar", "Fresh enough for day, warm enough for night"],
  "Notes agreed by Parfumo, Escentual, LookFantastic, Lyko (Parfumdreams/Proshop say pink pepper; vetiver and moss disputed, left out). 100ml EDT confirmed by Proshop (EAN match), Escentual, LookFantastic, Lyko. Awaiting photos.",
  "bergamot and black pepper over sandalwood and cedar.", ["Woody", "Fresh", "Citrus"], ["Citrus", "Spicy", "Woody", "Sandalwood"],
  name="Away Tonight Man", **TC)

FP = [("Top", "Lemon, Orange, Fir, Cardamom, Petitgrain"), ("Heart", "Rosemary, Lily of the Valley, Rose, Jasmine"), ("Base", "Musk, Vetiver, Oakmoss, Sandalwood, Rosewood")]
for size, bc, price, cmp, src in [("30", "0085715169563", "21.99", "29.99", "Superdrug and Proshop (both EAN pages)"),
                                  ("50", "0085715169570", "26.49", "33.99", "Superdrug and Glam4u (both EAN pages)")]:
    t = f"Abercrombie & Fitch Fierce Eau de Cologne {size}ml"
    F(bc, AF, t, "Men", size, price, cmp, 5, FP,
      "Aromatic · Woody · Fresh", "The legendary A&F signature: citrus, fir and musk.",
      f"{t} is the iconic Abercrombie &amp; Fitch signature scent, first launched in 2002. Lemon, orange, fir, cardamom and petitgrain open freshly, a heart of rosemary, lily of the valley, rose and jasmine follows, and it settles on musk, vetiver, oakmoss, sandalwood and rosewood.",
      ["The iconic A&amp;F signature scent", "Fresh citrus and fir with a hint of cardamom", "A clean, woody-musky base", f"Handy {size}ml size"],
      f"Notes agreed by Superdrug, Parfumo, Glam4u, ScentVerdict (marine notes and sage left out). {size}ml EDC confirmed by {src}; men per Superdrug. Store already has Fierce 100ml and 200ml (different sizes, not duplicates). Awaiting photos.",
      "lemon and fir over rosemary, musk and oakmoss.", ["Aromatic", "Woody", "Fresh"], ["Citrus", "Fresh", "Floral", "Woody", "Sandalwood"],
      name="Fierce", **COLOGNE)

write_outputs()
