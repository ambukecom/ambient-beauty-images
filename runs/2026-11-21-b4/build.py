import sys; sys.path.insert(0, "/home/claude/ambient-beauty-images/workflow")
from lib import *
PC = dict(conc="Eau De Parfum", concl="Eau de Parfum")
XC = dict(conc="Extrait De Parfum", concl="Extrait de Parfum")
AW = " Awaiting photos."

def GS(bc, vendor, title, seo_t, gender, size, price, cmp, qty, pyr, profile, hook, intro, contents, love, note, seo_d,
       of, fr, name, conc="Eau De Parfum", concl="Eau de Parfum", status="done", form_suffix=" Gift Set", show_size=False):
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

# ---------------- 1 Signorina Misteriosa set
t = "Salvatore Ferragamo Signorina Misteriosa Eau de Parfum 100ml Gift Set with Body Lotion and 10ml Travel Spray"
GS("8052464893447", "Salvatore Ferragamo", t, "Ferragamo Signorina Misteriosa EDP 100ml 3-Piece Gift Set", "Women", "100", "50.49", "63.99", 5,
   [("Top", "Blackberry, Neroli"), ("Heart", "Tuberose, Orange Blossom"), ("Base", "Vanilla, Patchouli")],
   "Fruity · Floral · Oriental", "Blackberry and tuberose wrapped in dark vanilla: Signorina's mysterious side.",
   f"{t} brings together Signorina Misteriosa Eau de Parfum in the full 100ml size, a 10ml travel spray and a matching body lotion. Wild blackberry and neroli open, creamy tuberose and orange blossom form the heart, and it settles into black vanilla and patchouli.",
   ["Salvatore Ferragamo Signorina Misteriosa Eau de Parfum 100ml (spray)", "Salvatore Ferragamo Signorina Misteriosa Eau de Parfum 10ml (travel spray)", "Salvatore Ferragamo Signorina Misteriosa Body Lotion 50ml"],
   ["A juicy blackberry and neroli opening", "A creamy tuberose and orange blossom heart", "A dark, warm vanilla and patchouli base", "Travel spray and body lotion included"],
   "Set contents (EDP 100ml + body lotion 50ml + EDP 10ml, women) confirmed by Flannels and Cosmetify; EAN 8052464893447 not found online (Superdrug sells 100ml sets under other EANs) – check the box, and that it has the 10ml (some editions have a 5ml mini). Pyramid agreed by Escentual + L'Etoile (Superdrug consistent); Flannels' different list ignored. 2016." + AW,
   "blackberry and tuberose over black vanilla, with lotion and travel spray.", ["Oriental", "Fruity", "Floral"], ["Fruity", "Floral", "Vanilla", "Oriental"],
   name="Signorina Misteriosa", **PC)

# ---------------- 2 Street Origins Skin, Sand & Santorini
t = "Street Origins Skin, Sand and Santorini Extrait de Parfum 75ml"
F("6290360379821", "Street Origins", t, "Unisex", "75", "43.49", "56.99", 1,
  [("Top", "Marigold, Bergamot, Praline"), ("Heart", "Iris, Violet, Jasmine"), ("Base", "Amber, Ambergris, Patchouli")],
  "Floral · Amber · Gourmand", "Sun-warmed skin and Aegean sand: marigold, praline and iris over amber.",
  f"{t} captures a warm evening on a Santorini beach. Marigold, bergamot and a touch of praline open, a powdery heart of iris, violet and jasmine follows, and it dries down to amber, ambergris and patchouli.",
  ["A sunny marigold and bergamot opening with sweet praline", "A soft, powdery iris and violet heart", "A warm amber and ambergris base", "Rich Extrait de Parfum concentration"],
  "EAN 6290360379821 matched on Superdrug (now unavailable) and Carrefour UAE (75ml Extrait); Cosmetify agrees. Supplier form column says Eau de Parfum but name and all sources say Extrait – listed as Extrait. Pyramid agreed by Carrefour + Cosmetify. Gender: Superdrug unisex, Carrefour women ('Venus'), Cosmetify men – supplier's Unisex kept." + AW,
  "marigold, praline and iris over warm amber.", ["Floral", "Oriental", "Gourmand", "Powdery"], ["Floral", "Jasmine", "Oriental", "Woody"],
  name="Skin, Sand and Santorini", **XC)
_st = "Street Origins Skin, Sand & Santorini Extrait de Parfum 75ml"
P[-1]["seo"] = (_st, f"{_st}: marigold, praline and iris over warm amber." + FREE)

# ---------------- 3 Surrati 1929 Collection 1 discovery set
t = "Surrati 1929 Collection 1 Extrait de Parfum Discovery Set 5 x 10ml"
GS("6281085042275", "Surrati", t, "Surrati 1929 Collection 1 Extrait Discovery Set 5 x 10ml", "Unisex", "10", "26.99", "34.99", 1,
   [], "Woody · Floral · Oriental", "Five Surrati extraits from the 1929 Collection in one discovery box.",
   f"{t} is the easy way to explore Surrati's 1929 Collection. It holds five 10ml Extrait de Parfum sprays, from the sweet musk of Gold Musk and the fruity-floral Miss World Charisma to the woody Rosso Ombre, the amber-floral Fabrica 1929 and the leathery Italian Tobacco.",
   ["Surrati Gold Musk Extrait de Parfum 10ml", "Surrati Rosso Ombre Extrait de Parfum 10ml", "Surrati Miss World Charisma Extrait de Parfum 10ml", "Surrati Fabrica 1929 Extrait de Parfum 10ml", "Surrati Italian Tobacco Extrait de Parfum 10ml"],
   ["Five full-strength extraits to try", "Handy 10ml sizes for travel and layering", "From soft musk and florals to tobacco and leather", "A great gift or way to find a new favourite"],
   "Contents (5 x 10ml Extrait: Gold Musk, Rosso Ombre, Miss World Charisma, Fabrica 1929, Italian Tobacco) confirmed by JustMyLook + Cosmetify; EAN 6281085042275 not found online – check the box (not Collection 2). Per-scent notes disagree between the two sources, so no pyramid shown. JustMyLook says unisex, breadcrumbs say men – supplier's Unisex kept." + AW,
   "five 10ml extraits from Surrati's 1929 Collection.", ["Woody", "Oriental", "Floral", "Musky"], ["Woody", "Floral", "Oriental"],
   name="Surrati 1929 Collection 1", form_suffix=" Discovery Set", **XC)

# ---------------- 4 Arabian Jackpot (needs-review: concentration)
t = "Surrati Arabian Jackpot Eau de Parfum 100ml"
F("6281085041391", "Surrati", t, "Unisex", "100", "31.99", "40.99", 1,
  [("Top", "Bergamot, Lemon, Sea Accord"), ("Heart", "Lavender, Jasmine, Marine Notes"), ("Base", "Amber, Musk, Driftwood")],
  "Aquatic · Citrus · Aromatic", "A fresh sea breeze of citrus and lavender over warm driftwood.",
  f"{t} is a fresh, aquatic scent for everyday wear. Bergamot, lemon and a sea accord open brightly, lavender, jasmine and marine notes form the heart, and it settles into amber, musk and driftwood.",
  ["A bright bergamot and lemon opening", "A breezy sea accord and marine heart", "Lavender and jasmine for a clean, aromatic feel", "A warm amber, musk and driftwood base"],
  "NEEDS REVIEW: concentration. Asrar-co (EAN 6281085041391 match), JustMyLook, SOTD and Iconic Perfumes call it 'Eau de Extrait'; Rackhams and Cosmetify say EDP, as does the supplier – listed as Eau de Parfum, check the box. Pyramid identical on Rackhams, JustMyLook, SOTD and Iconic; Cosmetify's oriental pyramid ignored. Cosmetify markets it for men; supplier's Unisex kept." + AW,
  "citrus, sea accord and lavender over amber and driftwood.", ["Aquatic", "Citrus", "Aromatic", "Fresh"], ["Citrus", "Aquatic", "Fresh", "Jasmine", "Lavender", "Woody"],
  name="Arabian Jackpot", status="needs-review", **PC)

# ---------------- 5 Gray Oud
t = "Surrati Gray Oud Extrait de Parfum 150ml"
F("6281085040035", "Surrati", t, "Unisex", "150", "42.49", "57.99", 1,
  [("Top", "Oud, Saffron"), ("Heart", "Aromatic Woods, Patchouli"), ("Base", "Amber, Leather")],
  "Woody · Oud · Leather", "Smoky oud and saffron over a deep amber and leather base.",
  f"{t} is a rich, woody oud from Surrati's 1929 Collection. Oud and saffron open boldly, aromatic woods and patchouli build the heart, and it finishes on warm amber and smooth leather.",
  ["A bold oud and saffron opening", "Aromatic woods and earthy patchouli", "A warm amber and leather finish", "Long-lasting Extrait in a generous 150ml bottle"],
  "Extrait 150ml and pyramid agreed by JustMyLook + MyRoyalMusk (Cosmetify, as 'Grey Oud', agrees on oud/leather/spicy). EAN 6281085040035 not found online – check the box. MyRoyalMusk and Cosmetify market it for men, JustMyLook unisex; supplier's Unisex kept." + AW,
  "oud and saffron over amber and leather.", ["Woody", "Oriental", "Leather", "Spicy"], ["Woody", "Spicy", "Oriental"],
  name="Gray Oud", **XC)

# ---------------- 6 Honey Oud
t = "Surrati Honey Oud Eau de Parfum 140ml"
F("6281085036915", "Surrati", t, "Unisex", "140", "27.49", "34.99", 1,
  [("Top", "Cardamom"), ("Heart", "Rose, Jasmine"), ("Base", "Oud, Amber, Vanilla")],
  "Oriental · Spicy · Floral", "Spiced cardamom and rose melting into oud, amber and vanilla.",
  f"{t} comes from Surrati's Heritage Collection. Warm cardamom opens, a floral heart of rose and jasmine follows, and it settles into a smooth base of oud, amber and vanilla.",
  ["A warm cardamom opening", "A rich rose and jasmine heart", "A smooth oud, amber and vanilla base", "Generous 140ml bottle"],
  "EAN 6281085036915 matched on Asrar-co and Debenhams (EDP 140ml); JustMyLook, Perfume Trading, Fragrance Hub and FilledWithBarakah agree on size and pyramid (Iconic Perfumes/Almanaar list a different pyramid, ignored). Asrar-co names it 'Honey Oud Marina' and Debenhams shows 148ml in its size selector – check the box. Unisex." + AW,
  "cardamom and rose over oud, amber and vanilla.", ["Oriental", "Spicy", "Floral", "Woody"], ["Spicy", "Rose", "Jasmine", "Woody", "Vanilla", "Oriental"],
  name="Honey Oud", **PC)

# ---------------- 7 Miss World Charisma
t = "Surrati Miss World Charisma Extrait de Parfum 150ml"
F("6281085039978", "Surrati", t, "Women", "150", "42.49", "57.99", 1,
  [("Top", "Orange, Strawberry"), ("Heart", "Jasmine, White Flowers"), ("Base", "Amber, Vanilla")],
  "Fruity · Floral · Oriental", "Juicy strawberry and orange over jasmine and creamy vanilla.",
  f"{t} is a sweet, feminine extrait from Surrati's 1929 Collection. Orange and strawberry open with a juicy sparkle, jasmine and white flowers bloom in the heart, and it dries down to warm amber and vanilla.",
  ["A juicy orange and strawberry opening", "A soft jasmine and white flower heart", "A warm amber and vanilla base", "Long-lasting Extrait in a generous 150ml bottle"],
  "Extrait 150ml (women) and identical pyramid on JustMyLook, Beauty Base, FilledWithBarakah and Arabia Scents; Cosmetify agrees on fruity/floral/oriental. EAN 6281085039978 not found online – check the box." + AW,
  "orange and strawberry over jasmine, amber and vanilla.", ["Fruity", "Floral", "Oriental"], ["Fruity", "Citrus", "Floral", "Jasmine", "Vanilla"],
  name="Miss World Charisma", **XC)

# ---------------- 8 Miss World (needs-review: notes)
t = "Surrati Miss World Extrait de Parfum 150ml"
F("6281085039992", "Surrati", t, "Women", "150", "42.49", "56.99", 2,
  [("Top", "Jasmine, Citrus"), ("Heart", "Musk, Rose"), ("Base", "White Flowers, Bergamot")],
  "Floral · Citrus · Musky", "A soft, romantic bouquet of jasmine, rose and musk with a citrus glow.",
  f"{t} is a fresh, feminine floral from Surrati. Jasmine and citrus open, musk and rose form a soft, romantic heart, and white flowers with a touch of bergamot linger on the skin.",
  ["A bright jasmine and citrus opening", "A romantic rose and musk heart", "Delicate white flowers that linger", "Long-lasting Extrait in a generous 150ml bottle"],
  "NEEDS REVIEW: notes. EAN 6281085039992 matched on Jomashop (Ladies Extrait 150ml). Pyramid shown is the one Fragrance Viking, Eastern Perfume UK and Crepslocker agree on (JustMyLook set summary consistent), but other sites give quite different pyramids (Cosmetify; uksurrati/MyRoyalMusk copy Italian Tobacco's notes) – check the box. Perfume Trading and surrati.ae say EDP; listed as Extrait per the EAN source and supplier. Some sites say unisex; supplier's Women kept." + AW,
  "jasmine, rose and musk with a citrus glow.", ["Floral", "Citrus", "Musky"], ["Floral", "Jasmine", "Rose", "Citrus", "Fresh"],
  name="Miss World", status="needs-review", **XC)

# ---------------- 9 Hamrah
t = "Surrati Hamrah Eau de Parfum 100ml"
F("6281085040271", "Surrati", t, "Unisex", "100", "31.49", "40.99", 1,
  [("Top", "Cognac, Apple"), ("Heart", "Cinnamon, Tonka Bean, Oak, Hedione"), ("Base", "Vanilla, Praline, Sandalwood")],
  "Gourmand · Spicy · Woody", "Cognac and apple warmed by cinnamon, praline and vanilla.",
  f"{t} is a warm, boozy gourmand. Cognac and apple open, cinnamon, tonka bean, oak and Hedione give a spicy, glowing heart, and it melts into vanilla, praline and sandalwood.",
  ["A rich cognac and apple opening", "Warm cinnamon and tonka", "A sweet vanilla, praline and sandalwood base", "Cosy and long-lasting for cooler days"],
  "EAN 6281085040271 matched on Times Perfumes AU (EDP 100ml, unisex); pyramid agreed by FilledWithBarakah + Intense Oud (Times Perfumes description matches; its structured note fields differ and were ignored)." + AW,
  "cognac and apple over cinnamon, praline and vanilla.", ["Gourmand", "Spicy", "Woody", "Oriental"], ["Vanilla", "Spicy", "Fruity", "Woody", "Sandalwood", "Oriental"],
  name="Hamrah", **PC)

# ---------------- 10 Royal 777 (needs-review: notes/gender)
t = "Surrati Royal 777 Eau de Parfum 100ml"
F("6281085041377", "Surrati", t, "Women", "100", "29.49", "38.99", 1,
  [], "Woody · Spicy · Musky", "A refined Surrati Eau de Parfum with a warm, woody-musky trail.",
  f"{t} is a modern Surrati Eau de Parfum in a 100ml spray. It has a bright opening and a warm, woody-musky finish, made for everyday elegance.",
  ["A bright, uplifting opening", "A warm, woody-musky trail", "Eau de Parfum strength", "Generous 100ml bottle"],
  "NEEDS REVIEW: notes and gender. EDP 100ml per Cosmetify, Fragranza, surrati.com.pk and Perfume Click (JustMyLook says Extrait); EAN 6281085041377 not found online. The three published pyramids largely disagree (only bergamot, musk and sandalwood recur), so no pyramid shown – please add notes from the box. Gender varies (Cosmetify men, Perfume Click for her, others unisex); supplier's Women kept." + AW,
  "a refined, warm woody-musky Eau de Parfum.", ["Woody", "Musky"], ["Woody", "Sandalwood"],
  name="Royal 777", status="needs-review", **PC)

write_outputs()
