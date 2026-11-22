import sys; sys.path.insert(0, "/home/claude/ambient-beauty-images/workflow")
from lib import *
PC = dict(conc="Eau De Parfum", concl="Eau de Parfum")
XC = dict(conc="Extrait De Parfum", concl="Extrait de Parfum")
TC = dict(conc="Eau De Toilette", concl="Eau de Toilette")
AW = " Awaiting photos."

def GS(bc, vendor, title, seo_t, gender, size, price, cmp, qty, pyr, profile, hook, intro, contents, love, note, seo_d,
       of, fr, name, conc="Eau De Parfum", concl="Eau de Parfum", status="done", form_suffix=" Gift Set"):
    """Fragrance set: fragrance standard (3 tags) plus a 'What's in the set' block."""
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

# 1 Swiss Arabian Vanilla 01
t = "Swiss Arabian Vanilla 01 Extrait de Parfum 50ml"
F("6295124049910", "Swiss Arabian", t, "Women", "50", "53.49", "67.99", 2,
  [("Top", "Pink Pepper, Orange Flower, Coconut"), ("Heart", "Jasmine Sambac, Tuberose, Cappuccino, Caramel"), ("Base", "Bourbon Vanilla, Tonka Bean, Sandalwood, Musk")],
  "Floral · Gourmand · Vanilla", "Creamy white flowers and caramel coffee wrapped in Bourbon vanilla.",
  f"{t} is a rich floral gourmand from Swiss Arabian's 01 collection. Madagascar pink pepper, orange flower and coconut open, jasmine sambac and tuberose meet cappuccino and caramel in the heart, and it settles into Bourbon vanilla, tonka bean, sandalwood and musk.",
  ["A sparkling pink pepper and coconut opening", "Creamy jasmine and tuberose with cappuccino and caramel", "A warm Bourbon vanilla and tonka base", "Rich Extrait de Parfum concentration"],
  "EAN 6295124049910 matched on Bjutip (Extrait 50ml) and The Perfume Shop (which titles it EDP); JustMyLook also Extrait 50ml. Pyramid identical on all three. 2025 (The Perfume Shop). Listed as Extrait per name and 2 of 3 sources (supplier form column says EDP) – check the box. JustMyLook women, Bjutip unisex; supplier's Women kept." + AW,
  "jasmine, caramel and coffee over Bourbon vanilla.", ["Floral", "Gourmand", "Oriental"], ["Floral", "Jasmine", "Vanilla", "Sandalwood"],
  name="Vanilla 01", **XC)

# 2 Swiss Arabian Wajd
t = "Swiss Arabian Wajd Eau de Parfum 50ml"
F("6295124031298", "Swiss Arabian", t, "Unisex", "50", "41.49", "53.99", 1,
  [("Top", "Turkish Rose, Apple, Fruity Notes"), ("Heart", "Patchouli, Orris"), ("Base", "Amber, Musk, Balsams")],
  "Fruity · Floral · Amber", "Turkish rose and crisp apple over powdery orris and warm amber.",
  f"{t} is a soft, sweet fruity floral from Swiss Arabian. Turkish rose and apple open with a juicy fruitiness, patchouli and powdery orris form the heart, and it settles into amber, musk and warm balsams.",
  ["A juicy Turkish rose and apple opening", "A powdery orris and patchouli heart", "A warm amber and musk base", "Compact 50ml bottle"],
  "EDP 50ml and pyramid agreed by Nahdi (as 'Wajd 1080'), Intense Oud, Galaxus and ScentVerdict (vanilla in base on only 2, left out). EAN 6295124031298 not found online – check the box. Cosmetify lists an 'Extrait' 50ml for men – odd one out. Release year conflicts (2019 vs 2021), left out. Unisex per Nahdi/Notino; supplier's Unisex kept." + AW,
  "Turkish rose and apple over orris and warm amber.", ["Fruity", "Floral", "Oriental", "Powdery"], ["Rose", "Fruity", "Floral"],
  name="Wajd", **PC)

# 3 Ted Baker Celeste set (needs-review: barcode)
t = "Ted Baker Celeste Eau de Toilette 50ml Gift Set with 100ml Body Lotion"
GS("5060523019397", "Ted Baker", t, "Ted Baker Celeste EDT 50ml & Body Lotion Gift Set", "Women", "50", "23.49", "30.99", 5,
   [("Top", "Lily, Cardamom"), ("Heart", "Cassis, Rose"), ("Base", "Tonka Bean")],
   "Floral · Spicy · Musky", "Breezy lily and cardamom over cassis, rose and soft tonka.",
   f"{t} pairs Celeste from Ted Baker's Floret range with a matching body lotion. Lily and cardamom open with a fresh, aromatic lift, cassis and rose form the heart, and it settles on soft tonka bean. The body lotion with vitamin E layers the scent on the skin.",
   ["Ted Baker Celeste Eau de Toilette 50ml (spray)", "Ted Baker Celeste Body Lotion 100ml"],
   ["A breezy lily and cardamom opening", "A fruity cassis and rose heart", "A soft tonka bean finish", "Matching body lotion included"],
   "NEEDS REVIEW: barcode. Contents (EDT 50ml + body lotion 100ml, women) confirmed by Cosmetify, Medino and Oasis, but EAN 5060523019397 not found anywhere (Oasis's set is SKU 5060523017485, maybe an older edition) – check the box. Floret range (Boots, Oasis). Pyramid agreed by Boots, Oasis and Medino; Superdrug gives musk/sandalwood base instead." + AW,
   "lily and cardamom over cassis and rose, with body lotion.", ["Floral", "Spicy", "Musky"], ["Floral", "Rose", "Spicy", "Fruity"],
   name="Celeste", status="needs-review", **TC)

# 4 Ted Baker Kasia cracker
t = "Ted Baker Kasia Eau de Toilette 15ml Cracker Gift Set with Lip Gloss"
GS("5060523018031", "Ted Baker", t, "Ted Baker Kasia EDT 15ml & Lip Gloss Cracker Gift Set", "Women", "15", "20.49", "26.99", 5,
   [("Top", "Lychee, Orange Blossom"), ("Heart", "Jasmine, Coconut"), ("Base", "Vanilla, Amber, Sandalwood")],
   "Fruity · Floral · Warm", "A festive cracker with juicy lychee, creamy jasmine and a nude lip gloss.",
   f"{t} is a fun festive cracker holding a travel-size Kasia from Ted Baker's Floralicious collection and a nude lip gloss. Lychee and orange blossom open juicily, jasmine and coconut form a creamy floral heart, and it finishes warm and sweet with vanilla, amber and sandalwood.",
   ["Ted Baker Kasia Eau de Toilette 15ml (spray)", "Ted Baker nude lip gloss 8ml (with brush applicator)"],
   ["A juicy lychee and orange blossom opening", "A creamy jasmine and coconut heart", "A warm vanilla, amber and sandalwood base", "Festive cracker packaging, ideal stocking filler"],
   "EAN 5060523018031 matched on Superdrug Marketplace (Ted Baker Beauty); contents confirmed with Cosmetify (15ml EDT + 8ml lip gloss; Superdrug gives no gloss size). Pyramid identical on Superdrug and tedbaker.com (Kasia 50ml). Floralicious range. Women." + AW,
   "lychee and jasmine over vanilla, with a nude lip gloss.", ["Fruity", "Floral", "Gourmand"], ["Fruity", "Floral", "Jasmine", "Vanilla", "Sandalwood"],
   name="Kasia", **TC)

# 5 Ted Baker Kasia candle set
t = "Ted Baker Kasia Eau de Toilette 50ml Gift Set with 70g Candle"
GS("5060523017997", "Ted Baker", t, "Ted Baker Kasia EDT 50ml & Candle Gift Set", "Women", "50", "23.99", "30.99", 3,
   [("Top", "Lychee"), ("Heart", "Jasmine, Coconut"), ("Base", "Vanilla, Sandalwood")],
   "Fruity · Floral · Warm", "Juicy lychee and creamy jasmine for you, with a candle for your home.",
   f"{t} pairs Kasia from Ted Baker's Floralicious collection with a 70g scented candle. Lychee opens with a juicy sweetness, jasmine and coconut form a creamy floral heart, and it settles into vanilla and sandalwood.",
   ["Ted Baker Kasia Eau de Toilette 50ml (spray)", "Ted Baker scented candle 70g"],
   ["A juicy lychee opening", "A creamy jasmine and coconut heart", "A soft vanilla and sandalwood base", "Scented candle included"],
   "EAN 5060523017997 matched on Superdrug (now unavailable online); contents (EDT 50ml + 70g candle) confirmed by Cosmetify. Pyramid: only notes shared by Superdrug's set page and tedbaker.com (orange blossom/amber on tedbaker.com only, left out). Floralicious range. Women." + AW,
   "lychee and jasmine over vanilla, with a scented candle.", ["Fruity", "Floral", "Gourmand"], ["Fruity", "Floral", "Jasmine", "Vanilla", "Sandalwood"],
   name="Kasia", **TC)

# 6 Ted Baker M Active Essentials (needs-review: only one source for exact set)
t = "Ted Baker M Eau de Toilette 30ml Active Essentials Gift Set with Gym Towel"
GS("5060412679169", "Ted Baker", t, "Ted Baker M EDT 30ml & Gym Towel Gift Set", "Men", "30", "20.99", "28.99", 5,
   [("Top", "Yuzu, Roseberry, Black Pepper"), ("Heart", "Coriander, Guaiacwood"), ("Base", "Vetiver, Tonka Bean, Musk")],
   "Woody · Citrus · Spicy", "Zesty yuzu and black pepper over vetiver, with a gym towel for the workout.",
   f"{t} brings Ted Baker M together with a branded gym towel. Japanese yuzu, roseberry and black pepper open, coriander and guaiacwood form a woody, spicy heart, and it settles into vetiver, tonka bean and musk.",
   ["Ted Baker M Eau de Toilette 30ml (spray)", "Ted Baker gym towel"],
   ["A zesty yuzu and black pepper opening", "A spicy coriander and guaiacwood heart", "A smooth vetiver, tonka and musk base", "Gym towel included"],
   "NEEDS REVIEW: only Superdrug (EAN 5060412679169 match, store-only) lists this exact set; towel size not stated anywhere, so left out. Perfume Shop/Rowlands 'M Gift Set' is a different set (30ml EDT + body wash). Pyramid agreed by Rowlands and McCabes; Superdrug 75ml gives a different list – check. Men." + AW,
   "yuzu and black pepper over vetiver, with a gym towel.", ["Woody", "Citrus", "Spicy", "Aromatic"], ["Citrus", "Spicy", "Woody"],
   name="Ted Baker M", status="needs-review", **TC)

# 7 Ted Baker Original Woman set
t = "Ted Baker Original Woman Eau de Toilette 100ml Gift Set with 15ml Eau de Toilette and 150ml Body Wash"
GS("5060523017973", "Ted Baker", t, "Ted Baker Original Woman EDT 100ml 3-Piece Gift Set", "Women", "100", "23.49", "30.99", 5,
   [("Top", "Bergamot, Rum, Lemon, Tangerine, Apple, Peach"), ("Heart", "Ylang-Ylang, Jasmine, Cinnamon, Freesia, Lily"), ("Base", "Vetiver, Vanilla, Musk")],
   "Fruity · Floral · Musky", "The Ted Baker classic: sparkling citrus and peach over jasmine and soft vanilla musk.",
   f"{t} brings together Ted Baker's original women's fragrance in the full 100ml size, a 15ml travel spray and a 150ml body wash. Bergamot, lemon, tangerine, apple and peach open with a dash of rum, ylang-ylang, jasmine, freesia and lily bloom with a touch of cinnamon, and it settles into vetiver, vanilla and musk.",
   ["Ted Baker Original Woman Eau de Toilette 100ml (spray)", "Ted Baker Original Woman Eau de Toilette 15ml (travel spray)", "Ted Baker Original Woman Body Wash 150ml"],
   ["A sparkling citrus, apple and peach opening", "A floral jasmine, ylang-ylang and freesia heart", "A soft vetiver, vanilla and musk base", "Travel spray and body wash included"],
   "Contents agreed by JustMyLook, Cosmetify, Debenhams IE (SKU contains EAN 5060523017973) and McCabes. Pyramid identical on JustMyLook, Debenhams and Superdrug Original Woman 200ml. 1999 scent. Not the 2025 'Woman Limited Edition' set (EAN 5060412678643, different notes). Women." + AW,
   "citrus and peach over jasmine and vanilla musk, 3 pieces.", ["Fruity", "Floral", "Citrus", "Musky"], ["Citrus", "Fruity", "Floral", "Jasmine", "Vanilla"],
   name="Original Woman", **TC)

# 8 Versace Eros Energy set
t = "Versace Eros Energy Eau de Parfum 50ml Gift Set with Shower Gel and After Shave Balm"
GS("8011003900077", "Versace", t, "Versace Eros Energy EDP 50ml 3-Piece Gift Set", "Men", "50", "56.49", "73.99", 5,
   [("Top", "Bergamot, Blood Orange, Lime"), ("Heart", "Pink Pepper, Blackcurrant"), ("Base", "Patchouli, Oakmoss, Musk")],
   "Citrus · Spicy · Woody", "A burst of Italian citrus and pink pepper over patchouli and oakmoss.",
   f"{t} brings together Eros Energy Eau de Parfum with a matching shower gel and after shave balm. Bergamot, blood orange and lime open with a bright citrus burst, pink pepper and blackcurrant add energy in the heart, and it settles into patchouli, oakmoss and musk.",
   ["Versace Eros Energy Eau de Parfum 50ml (spray)", "Versace Eros Energy Shower Gel 50ml", "Versace Eros Energy After Shave Balm 50ml"],
   ["A vibrant bergamot, blood orange and lime opening", "A lively pink pepper and blackcurrant heart", "A woody patchouli, oakmoss and musk base", "Shower gel and after shave balm included"],
   "Contents (EDP 50ml + shower gel 50ml + after shave balm 50ml) agreed by The Perfume Shop, Next and JustMyLook; EAN 8011003900077 matched on Jomashop (Men's Eros Energy Gift Set). Supplier stockfile also lists 8011003907083 for this set. Pyramid agreed by Basenotes, Olfastory, The Perfume Shop/Next (heart); mandarin, lemon, grapefruit, white amber left out (not agreed). 2024 scent. Men." + AW,
   "citrus and pink pepper over patchouli, with gel and balm.", ["Citrus", "Spicy", "Woody", "Fresh"], ["Citrus", "Spicy", "Fruity", "Woody", "Fresh"],
   name="Eros Energy", **PC)

# 9 Zimaya Abadi Saga
t = "Zimaya Abadi Saga Eau de Parfum 100ml"
F("6290171075080", "Zimaya", t, "Men", "100", "30.99", "38.99", 1,
  [("Top", "Blackcurrant, Bergamot, Orange Blossom, Clove"), ("Heart", "Ginger, Patchouli, Cardamom, Rose, Cinnamon"), ("Base", "Vetiver, Oakmoss, Sandalwood, Tonka Bean, Pepper, Musk")],
  "Spicy · Woody · Fruity", "Blackcurrant and clove over warm spices and a deep vetiver base.",
  f"{t} is a spicy, woody fragrance for men from Zimaya. Blackcurrant, bergamot, orange blossom and clove open, ginger, patchouli, cardamom, rose and cinnamon form a warm, spiced heart, and it settles into vetiver, oakmoss, sandalwood, tonka bean and musk.",
  ["A fruity blackcurrant and bergamot opening with clove", "A warm ginger, cardamom and cinnamon heart", "A deep vetiver, oakmoss and sandalwood base", "Great value 100ml Eau de Parfum"],
  "EAN 6290171075080 matched on Bjutip (as 'Abadi Saga Black', same product) and Carrefour UAE (EDP 100ml, men). Pyramid agreed by Bjutip, Cosmetify, Parfum-Centrum and Carrefour's description (Carrefour spec box generic, ignored). 2025 (Parfum-Centrum). Zimaya is an Afnan line. Men." + AW,
  "blackcurrant and clove over warm spices and vetiver.", ["Spicy", "Woody", "Fruity"], ["Spicy", "Fruity", "Citrus", "Woody", "Sandalwood"],
  name="Abadi Saga", **PC)

# 10 Zimaya Al Embratur Intense
t = "Zimaya Al Embratur Intense Eau de Parfum 100ml"
F("6290171074847", "Zimaya", t, "Unisex", "100", "24.49", "31.99", 1,
  [("Top", "Lemon, Pink Pepper"), ("Heart", "Lavender, Saffron, Fruity Notes"), ("Base", "Amber, Tonka Bean, Vanilla, Musk")],
  "Aromatic · Fruity · Amber", "Lemon and pink pepper over lavender and saffron, finishing in warm amber and vanilla.",
  f"{t} is a warm aromatic from Zimaya. Lemon and pink pepper open brightly, lavender and saffron meet juicy fruity notes in the heart, and it settles into amber, tonka bean, vanilla and musk.",
  ["A bright lemon and pink pepper opening", "An aromatic lavender and saffron heart", "A warm amber, tonka and vanilla base", "Great value 100ml Eau de Parfum"],
  "EAN 6290171074847 matched on Superdrug UK, Bjutip and Triple Traders (EDP 100ml). Pyramid agreed by Bjutip, Triple Traders and Carrefour (Superdrug matches, no musk). 2024 (Bjutip). Superdrug/Bjutip unisex, Carrefour/Triple Traders men; supplier's Unisex kept." + AW,
  "lemon and lavender over saffron, amber and vanilla.", ["Aromatic", "Fruity", "Oriental"], ["Citrus", "Lavender", "Spicy", "Fruity", "Vanilla"],
  name="Al Embratur Intense", **PC)

write_outputs()
