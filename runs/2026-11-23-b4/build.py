import sys; sys.path.insert(0, "/home/claude/ambient-beauty-images/workflow")
from lib import *
TC = dict(conc="Eau De Toilette", concl="Eau de Toilette")
PC = dict(conc="Eau De Parfum", concl="Eau de Parfum")
AW = " Awaiting photos."
CK = "Calvin Klein"

# 1 Britney Spears Fantasy Intense
t = "Britney Spears Fantasy Intense Eau de Parfum 100ml"
F("0719346565868", "Britney Spears", t, "Women", "100", "25.99", "33.99", 5,
  [("Top", "Pear, Red Lychee, Kiwi"), ("Heart", "Cupcake Accord, White Chocolate Orchid, Jasmine"), ("Base", "Patchouli, Tonka Bean, Sandalwood")],
  "Fruity · Floral · Gourmand", "A sweeter, deeper take on the cult Fantasy.",
  f"{t} is a fruity floral gourmand for women, launched in 2021. Juicy pear, red lychee and kiwi open bright and playful, a frosted cupcake accord with white chocolate orchid and jasmine forms the heart, and it settles into a creamy base of patchouli, tonka bean and sandalwood.",
  ["A juicy pear, lychee and kiwi opening", "A sweet cupcake and white chocolate orchid heart", "A creamy patchouli, tonka and sandalwood base", "Great value 100ml Eau de Parfum"],
  "UPC 719346565868 matched on GiftExpress and Jomashop (EDP 100ml, women); name/size also on Boots and Just My Look. Pyramid agreed by Boots, Just My Look and Parfumo (GiftExpress gives a different base). 2021 per Parfumo and GiftExpress. Women." + AW,
  "pear and lychee over cupcake accord, jasmine and tonka.", ["Gourmand", "Fruity", "Floral"], ["Fruity", "Vanilla", "Floral", "Jasmine", "Sandalwood"],
  name="Fantasy Intense", **PC)

# 2 Bujairami Agha
t = "Bujairami Agha Eau de Parfum 100ml"
F("9362014000010", "Bujairami", t, "Men", "100", "39.99", "53.99", 1,
  [("Top", "Cardamom, Orange Blossom"), ("Heart", "Bourbon Vanilla"), ("Base", "Musk, Ambroxan, Woody Notes")],
  "Amber · Gourmand · Spicy", "Creamy vanilla warmth with a spiced, ambery trail.",
  f"{t} is a warm, ambery gourmand for men. Cardamom and orange blossom open softly spiced, a rich bourbon vanilla heart follows, and it dries down to musk, ambroxan and smooth woods.",
  ["A spiced cardamom and orange blossom opening", "A rich, creamy bourbon vanilla heart", "A musky ambroxan and woody base", "Long-lasting 100ml Eau de Parfum"],
  "EAN 9362014000010 matched on Morele.net (EDP 100ml, men; title oddly prefixed 'Giordano Amaro'). Name/EDP/100ml/men also on Cosmetify, FilledWithBarakah, FragranceNet. Pyramid tiers agreed by Cosmetify and FilledWithBarakah (Morele adds more notes). Launch year not confirmed. Men." + AW,
  "cardamom and orange blossom over bourbon vanilla and musk.", ["Oriental", "Gourmand", "Spicy", "Woody"], ["Vanilla", "Spicy", "Woody", "Oriental"],
  name="Agha", **PC)

# 3 Bujairami First Class  -> needs-review (concentration conflict, barcode not found)
t = "Bujairami First Class Eau de Parfum 100ml"
F("9362014011610", "Bujairami", t, "Unisex", "100", "46.99", "60.99", 1, [],
  "Amber · Woody", "A glowing, ambery-woody signature for everyone.",
  f"{t} is a unisex amber woody fragrance from Bujairami, the bold house known for its long-lasting Eau de Parfums. Warm, luminous and ambery, it is made to be worn by anyone.",
  ["A warm, luminous amber-woody character", "Unisex – made for everyone", "Bold, long-lasting Bujairami style", "Generous 100ml bottle"],
  "NEEDS REVIEW: barcode 9362014011610 not found online. Supplier says Eau de Parfum, but UK retailers (Just My Look, Fragrance Hub, Scent of the Dunes) sell Bujairami First Class as an EXTRAIT DE PARFUM 100ml (2026, unisex; notes saffron, jasmine / amberwood, ambergris / cedar, fir resin). Only Cosmetify says EDP, with different vague notes. Check the box: if it is the Extrait, change title/tag/concentration and add that pyramid. Pyramid left out for now. Unisex (Cosmetify lists men)." + AW,
  "an ambery, woody glow.", ["Oriental", "Woody"], ["Woody", "Oriental"],
  name="First Class", status="needs-review", **PC)

# 4 Burberry London (women) EDP 50ml
t = "Burberry London Eau de Parfum 50ml"
F("3614226905192", "Burberry", t, "Women", "50", "30.49", "38.99", 5,
  [("Top", "Rose, Honeysuckle, Mandarin"), ("Heart", "Jasmine, Peony, Tiaré Flower"), ("Base", "Patchouli, Sandalwood, White Musk")],
  "Floral · Woody · Musky", "An elegant English floral with a warm, woody finish.",
  f"{t} is the classic floral London for Women, launched in 2006. Rose, honeysuckle and a sparkle of mandarin open the scent, jasmine, peony and tiaré flower form a rich floral heart, and it settles into patchouli, sandalwood and white musk.",
  ["A rose, honeysuckle and mandarin opening", "A rich jasmine, peony and tiaré heart", "A warm patchouli, sandalwood and musk base", "Handy 50ml Eau de Parfum"],
  "EAN 3614226905192 matched on GiftExpress and SoleSense (EDP 50ml, women). Pyramid agreed by Osmoz and GiftExpress (Parfumo puts the citrus in the heart). 2006 per Parfumo, Osmoz, GiftExpress. Not Her London Dream. Women." + AW,
  "rose and honeysuckle over jasmine, peony and sandalwood.", ["Floral", "Woody", "Musky"], ["Floral", "Rose", "Jasmine", "Sandalwood", "Citrus"],
  name="Burberry London", **PC)

# 5 Burberry London for Men EDT 50ml
t = "Burberry London Eau de Toilette 50ml"
F("3614226904997", "Burberry", t, "Men", "50", "29.49", "38.99", 5,
  [("Top", "Bergamot, Cinnamon, Lavender"), ("Heart", "Leather, Mimosa"), ("Base", "Tobacco, Oakmoss, Guaiac Wood, Opoponax")],
  "Spicy · Woody · Leather", "A warm, spiced classic made for cooler days.",
  f"{t} is London for Men, a warm spicy woody fragrance launched in 2006. Bergamot, cinnamon and lavender open with a cosy spice, a smooth heart of leather and mimosa follows, and it dries down to tobacco, oakmoss, guaiac wood and opoponax.",
  ["A spiced bergamot, cinnamon and lavender opening", "A smooth leather and mimosa heart", "A rich tobacco and oakmoss base", "Handy 50ml Eau de Toilette"],
  "EAN 3614226904997 matched on bestbrandsperfume.com and an eBay listing (London for Men EDT 50ml). Pyramid: top/heart and tobacco/oakmoss agreed by Parfumo and Notino UK; guaiac wood and opoponax from Notino and bestbrandsperfume (not Parfumo). 2006 per Parfumo and Notino. Men." + AW,
  "cinnamon and lavender over leather, tobacco and oakmoss.", ["Spicy", "Woody", "Leather", "Oriental"], ["Spicy", "Lavender", "Woody", "Citrus"],
  name="Burberry London for Men", **TC)

# 6 CK One 100ml
t = "Calvin Klein CK One Eau de Toilette 100ml"
F("0088300107407", CK, t, "Unisex", "100", "28.49", "37.99", 5,
  [("Top", "Pineapple, Mandarin, Bergamot, Lemon, Cardamom, Papaya"), ("Heart", "Nutmeg, Violet, Orris Root, Jasmine, Lily of the Valley, Rose"), ("Base", "Sandalwood, Amber, Musk, Cedar, Oakmoss")],
  "Citrus · Aromatic · Musky", "The clean, fresh unisex icon since 1994.",
  f"{t} is the original shared fragrance, launched in 1994. Pineapple, mandarin, bergamot, lemon, cardamom and papaya open fresh and zesty, a soft heart of nutmeg, violet, orris, jasmine, lily of the valley and rose follows, and it settles into sandalwood, amber, musk, cedar and oakmoss.",
  ["A fresh, zesty citrus and fruit opening", "A light, clean floral heart", "A soft musky, woody dry-down", "Everyday 100ml Eau de Toilette for anyone"],
  "UPC 088300107407 matched on UPCitemdb (EDT 3.4oz) and Best Buy Canada (unisex 100ml EDT). The Perfume Shop UK lists other EANs (0088300107438) for 100ml – packaging variants. Pyramid agreed by Notino and Wikipedia (Best Buy agrees). 1994 per Wikipedia, Notino, The Perfume Shop. Unisex." + AW,
  "citrus and pineapple over violet, jasmine and soft musk.", ["Citrus", "Aromatic", "Fresh", "Musky"], ["Citrus", "Fresh", "Fruity", "Floral"],
  name="CK One", **TC)

# 7 CK One Gold 100ml
t = "Calvin Klein CK One Gold Eau de Toilette 100ml"
F("3614221537763", CK, t, "Unisex", "100", "25.99", "34.99", 5,
  [("Top", "Fig, Bergamot, Sage"), ("Heart", "Neroli, Jasmine, Violet"), ("Base", "Vetiver, Patchouli, Guaiac Wood")],
  "Woody · Aromatic · Fresh", "A golden, fresh-woody twist on CK One.",
  f"{t} is a fresh woody unisex fragrance, launched in 2016. Fig, bergamot and sage open green and bright, neroli, jasmine and violet form the heart, and it dries down to warm vetiver, patchouli and guaiac wood.",
  ["A green fig, bergamot and sage opening", "A soft neroli, jasmine and violet heart", "A warm vetiver and guaiac wood base", "Generous 100ml Eau de Toilette for anyone"],
  "EAN 3614221537763 matched on UPCitemdb (seen in search results) and eBay (EDT 3.4oz, unisex). Pyramid identical on Notino UK and Escentual (Now Smell This agrees; Parfumo's pyramid is different and ignored). 2016 per Notino and Now Smell This; originally a limited edition. Unisex." + AW,
  "fig and bergamot over neroli, jasmine and vetiver.", ["Woody", "Aromatic", "Fresh"], ["Woody", "Fruity", "Citrus", "Jasmine", "Fresh"],
  name="CK One Gold", **TC)

# 8 CK Euphoria Men EDT 100ml
t = "Calvin Klein Euphoria Men Eau de Toilette 100ml"
F("0088300178278", CK, t, "Men", "100", "32.49", "43.99", 5,
  [("Top", "Pepper, Ginger"), ("Heart", "Sage, Cedar Leaf, Black Basil"), ("Base", "Amber, Patchouli, Suede")],
  "Spicy · Woody · Aromatic", "Fresh spice and soft suede for modern sensuality.",
  f"{t} is a spicy woody fragrance for men, launched in 2006. Pepper and ginger open fresh and lively, sage, cedar leaf and black basil form an aromatic heart, and it warms into amber, patchouli and creamy suede.",
  ["A lively pepper and ginger opening", "An aromatic sage, cedar leaf and basil heart", "A sensual amber, patchouli and suede base", "Generous 100ml Eau de Toilette"],
  "Barcode 0088300178278 shown on The Perfume Shop UK's Euphoria Men EDT page; also Sharaf DG and United Perfumes (Euphoria EDT Men 100ml). Supplier name lacks 'Men' – this is the men's version, not women's Euphoria. Pyramid agreed by Parfumo and Notino UK (redwood/rosewood disagree, left out). 2006 per Parfumo and Notino. Men." + AW,
  "pepper and ginger over basil, amber and suede.", ["Spicy", "Woody", "Aromatic", "Leather"], ["Spicy", "Woody", "Fresh"],
  name="Euphoria Men", **TC)

# 9 CK Truth for Men EDT 100ml (only the agreed base tier shown)
t = "Calvin Klein Truth for Men Eau de Toilette 100ml"
F("0088300073627", CK, t, "Men", "100", "29.49", "37.99", 5,
  [("Base", "Cedarwood, Patchouli")],
  "Aromatic · Fougère · Woody", "A fresh, green aromatic with a calm, woody depth.",
  f"{t} is a fresh aromatic fougère for men, launched in 2002. Cardamom, basil and green notes give it a crisp, herbal freshness, and it settles into a clean woody base of cedarwood and patchouli.",
  ["Crisp cardamom and basil freshness", "Fresh green, aromatic character", "A clean cedarwood and patchouli base", "Generous 100ml Eau de Toilette"],
  "Barcode 0088300073627 shown on The Perfume Shop UK's Truth for Men EDT page; eBay listings agree (Truth EDT 3.4oz men). Supplier name lacks 'for Men' – not the women's Truth EDP. Top/heart tiers disagree (TPS/Notino put cardamom+basil in top, Osmoz/Parfumo in heart), so only the agreed base (cedar, patchouli) is shown as a pyramid. Aromatic fougère per TPS and Osmoz. 2002 per Parfumo, Osmoz, Notino. Men." + AW,
  "cardamom and basil over cedarwood and patchouli.", ["Aromatic", "Fougere", "Woody", "Fresh"], ["Spicy", "Fresh", "Woody"],
  name="Truth for Men", **TC)

# 10 CK Women EDP 100ml
t = "Calvin Klein Women Eau de Parfum 100ml"
F("3614225358463", CK, t, "Women", "100", "37.49", "50.99", 5,
  [("Top", "Eucalyptus"), ("Heart", "Orange Blossom"), ("Base", "Cedarwood")],
  "Woody · Floral · Fresh", "A modern, minimal woody floral.",
  f"{t} is a modern woody floral for women, launched in 2018. Fresh eucalyptus opens the scent, a luminous orange blossom heart follows, and it settles into warm cedarwood.",
  ["A fresh eucalyptus opening", "A luminous orange blossom heart", "A warm cedarwood base", "Generous 100ml Eau de Parfum"],
  "EAN 3614225358463 matched on Perfumeria Ana (CK Women EDP 100ml) and eBay; also in Drogerie Natura URL. Pyramid agreed by Parfumo and Lookfantastic UK (Perfumeria Ana's longer list not confirmed, left out). 2018 per Parfumo and Now Smell This. Not CK Women Intense. Women." + AW,
  "eucalyptus over orange blossom and cedarwood.", ["Woody", "Floral", "Fresh"], ["Woody", "Floral", "Fresh", "Citrus"],
  name="Calvin Klein Women", **PC)

P[8]["desc"] = P[8]["desc"].replace("<p>Cedarwood and patchouli.</p>", "<p>Crisp cardamom, basil and green notes over a woody base of cedarwood and patchouli.</p>")
write_outputs()
