import sys; sys.path.insert(0, "/home/claude/ambient-beauty-images/workflow")
from lib import *
PC = dict(conc="Eau De Parfum", concl="Eau de Parfum")
AW = " Awaiting photos."

# 1 Zimaya Anhaar Valley
t = "Zimaya Anhaar Valley Eau de Parfum 100ml"
F("6290171074885", "Zimaya", t, "Unisex", "100", "26.49", "34.99", 1,
  [("Top", "Aquatic Notes, Melon, Apple, Peach"), ("Heart", "Ozonic Notes, Rose"), ("Base", "Ambergris, Musk")],
  "Aquatic · Fruity · Floral", "Juicy melon and peach on a cool sea breeze, softened by rose and musk.",
  f"{t} is a fresh floral aquatic from Zimaya. Watery notes, melon, apple and peach open with a juicy, airy brightness, ozonic notes and rose form the heart, and it settles into a soft base of ambergris and musk.",
  ["A juicy melon, apple and peach opening", "An airy ozonic and rose heart", "A soft ambergris and musk base", "Great value 100ml Eau de Parfum"],
  "EAN 6290171074885 matched on Superdrug, Bjutip and Triple Traders (EDP 100ml). Pyramid identical on Bjutip and Triple Traders; Superdrug's description names the same notes. 2024 (Bjutip). Superdrug/Bjutip unisex, Cosmetify men; supplier's Unisex kept." + AW,
  "melon and peach with sea notes, rose and musk.", ["Aquatic", "Fruity", "Floral", "Fresh"], ["Aquatic", "Fruity", "Rose", "Fresh"],
  name="Anhaar Valley", **PC)

# 2 Zimaya Awatif Blue
t = "Zimaya Awatif Blue Eau de Parfum 100ml"
F("6290171074991", "Zimaya", t, "Men", "100", "28.49", "38.99", 1,
  [("Top", "Blackcurrant, Orange, Citron, Mint, Coriander"), ("Heart", "Apricot, Basil, Rose"), ("Base", "Fig, Dates, Ambrette")],
  "Fruity · Aromatic · Fresh", "Blackcurrant, citrus and cool mint over apricot, basil and a warm fig and date base.",
  f"{t} is a fresh fruity aromatic for men from Zimaya. Blackcurrant, orange, citron, mint and coriander open crisp and lively, apricot, basil and rose form the heart, and it dries down to fig, dates and musky ambrette.",
  ["A lively blackcurrant, citrus and mint opening", "A fruity apricot, basil and rose heart", "A warm fig, date and ambrette base", "Great value 100ml Eau de Parfum"],
  "EAN 6290171074991 matched on Superdrug and Bjutip (EDP 100ml, men). Pyramid identical on Bjutip and FilledWithBarakah ('Awatif Blue Pour Homme'); Superdrug and Cosmetify name the same notes. Cosmetify files it under women's; supplier's Men kept. Release year not found." + AW,
  "blackcurrant and mint over apricot, fig and dates.", ["Fruity", "Aromatic", "Citrus", "Fresh"], ["Fruity", "Citrus", "Fresh", "Rose"],
  name="Awatif Blue", **PC)

# 3 Zimaya Khafaya Blue
t = "Zimaya Khafaya Blue Eau de Parfum 100ml"
F("6290171074151", "Zimaya", t, "Men", "100", "28.99", "36.99", 1,
  [("Top", "Cinnamon, Grapefruit, Nutmeg"), ("Heart", "Lavender, Woody Notes"), ("Base", "Amber, Liquorice, Sandalwood")],
  "Spicy · Aromatic · Woody", "Spiced grapefruit and lavender over warm amber, liquorice and sandalwood.",
  f"{t} is a warm, spicy woody fragrance for men from Zimaya. Cinnamon, grapefruit and nutmeg open with a bright spiced zest, lavender and woody notes form an aromatic heart, and it settles into amber, liquorice and sandalwood.",
  ["A zesty grapefruit opening spiced with cinnamon and nutmeg", "An aromatic lavender and woody heart", "A warm amber, liquorice and sandalwood base", "Great value 100ml Eau de Parfum"],
  "EAN 6290171074151 matched on Superdrug and Bjutip (EDP 100ml, men). Pyramid identical on Bjutip and Dubai Perfume Shop; Superdrug gives the same top/lavender/sandalwood/amber but no liquorice or woody notes. 2023 (Bjutip). Men." + AW,
  "spiced grapefruit and lavender over amber and sandalwood.", ["Spicy", "Aromatic", "Woody", "Oriental"], ["Spicy", "Citrus", "Lavender", "Woody", "Sandalwood"],
  name="Khafaya Blue", **PC)

# 4 Zimaya Khafaya Pink
t = "Zimaya Khafaya Pink Eau de Parfum 100ml"
F("6290171074168", "Zimaya", t, "Women", "100", "28.99", "37.99", 1,
  [("Top", "Pear, Bergamot, Vanilla"), ("Heart", "Indian Tuberose, Orange, Jasmine"), ("Base", "Vetiver, Musk, Ambroxan")],
  "Floral · Fruity · Musky", "Juicy pear and vanilla over a bouquet of tuberose and jasmine.",
  f"{t} is a sweet floral fragrance for women from Zimaya. Pear, bergamot and vanilla open soft and juicy, Indian tuberose, orange and jasmine form a lush white-floral heart, and it settles into vetiver, musk and ambroxan.",
  ["A juicy pear, bergamot and vanilla opening", "A lush tuberose, orange and jasmine heart", "A clean vetiver, musk and ambroxan base", "Great value 100ml Eau de Parfum"],
  "EAN 6290171074168 matched on Bjutip (EDP 100ml, women). Pyramid identical on Bjutip, Lyko and Dubai Perfume Shop (Oasis gives a different list, ignored). Not Hawwa Pink (different perfume). Release year not found. Women." + AW,
  "pear and vanilla over tuberose and jasmine.", ["Floral", "Fruity", "Musky"], ["Floral", "Fruity", "Jasmine", "Vanilla", "Citrus"],
  name="Khafaya Pink", **PC)

write_outputs()
