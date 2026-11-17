import json
LOC="gid://shopify/Location/93812949332"; FREE=" Free UK delivery over £40."
def ul(i): return "<ul>"+"".join(f"<li>{x}</li>" for x in i)+"</ul>"
def kd(p): return ul([f"<strong>{a}:</strong> {b}" for a,b in p])
def body(hook,intro,blocks,details,love,qs):
    h=f"<p><em>{hook}</em></p><p>{intro}</p>"
    for t,c in blocks: h+=f"<h2>{t}</h2>{c}"
    return h+"<h2>Key details</h2>"+kd(details)+"<h2>Why you'll love it</h2>"+ul(love)+"<h2>FAQ</h2>"+"".join(f"<h3>{q}</h3><p>{a}</p>" for q,a in qs)
P=[]
def add(**k): P.append(k)
TYPE={"Men":"Men's Fragrance","Women":"Women's Fragrance","Unisex":"Unisex Fragrances"}
def frag(bc,vendor,title,handle,gender,size,price,cmp,qty,pyr,profile,hook,intro,love,faq,note,seo_d,conc="Eau De Parfum",concl="Eau de Parfum",status="done",of=(),fr=()):
    add(cat_name="Fragrances",bc=bc,title=title,handle=handle,vendor=vendor,type=TYPE[gender],gender=gender,cat="hb-3-2-8",price=price,cmp=cmp,qty=qty,
        tags=[vendor,gender,conc],seo=(title,f"{title}: {seo_d}"+FREE),status=status,form=concl,size=size,unit="ml",of=list(of),fr=list(fr),
        desc=body(hook,intro,[("Scent pyramid",kd(pyr))] if pyr else [],[("Brand",vendor),("Concentration",concl),("Size",f"{size}ml"),("Scent profile",profile),("Wear",gender)],love,faq),note=note)
def faq(name,pyr):
    a=[" and ".join(v.lower().rsplit(", ",1)) for k,v in pyr]
    if len(a)==3: return f"{a[0][0].upper()+a[0][1:]} first, then {a[1]}, finishing with {a[2]}."
    return f"{a[0][0].upper()+a[0][1:]} first, finishing with {a[1]}."
def F(bc,vendor,title,gender,size,price,cmp,qty,pyr,profile,hook,intro,love,note,seo_d,of,fr,conc="Eau De Parfum",concl="Eau de Parfum",name=None,status="done"):
    h=title.lower().replace(" & ","-").replace(".","").replace(" ","-")
    q2=("Is it unisex?","Yes, it is made for everyone.") if gender=="Unisex" else (("Is it for men?","Yes, it is a men's fragrance.") if gender=="Men" else ("Is it for women?","Yes, it is a women's fragrance."))
    frag(bc,vendor,title,h,gender,size,price,cmp,qty,pyr,profile,hook,intro,love,[(f"What does {name} smell like?",faq(name,pyr)),q2] if pyr else [q2],note,seo_d,conc=conc,concl=concl,of=of,fr=fr,status=status)
def SO(bc,name,cmp,pyr,profile,hook,mid,love,note,seo_d,of,fr):
    t=f"Street Origins {name} Eau de Parfum 75ml"
    F(bc,"Street Origins",t,"Unisex","75","32.49",cmp,1,pyr,profile,hook,f"{t} is {mid}",love,note,seo_d,of,fr,name=name)
SO("6298042001398","Hanoi Sizzle","42.99",[("Top","Coffee, Hazelnut, Cardamom, Rum"),("Heart","Cacao, Salted Caramel, Iris, Myrrh"),("Base","Smoky Tonka Bean, Vetiver, Vanilla")],
 "Gourmand · Boozy · Smoky","Coffee, rum and salted caramel over smoky tonka and vanilla.",
 "a rich, smoky gourmand fragrance. Coffee, hazelnut, cardamom and rum open warmly, a heart of cacao, salted caramel, iris and myrrh follows, and it settles into smoky tonka bean, vetiver and vanilla.",
 ["A rich opening of coffee, hazelnut and rum","A decadent heart of cacao and salted caramel","A smoky base of tonka, vetiver and vanilla","Cosy and long-lasting for cooler days"],
 "Notes confirmed by 2 sources (ScentVerdict, FilledWithBarakah). Splash and Carrefour market it for women; supplier's Unisex used. Awaiting photos.",
 "coffee, rum and salted caramel over smoky vanilla.",["Gourmand","Oriental","Spicy"],["Spicy","Vanilla","Woody"])
SO("6298042001282","Ibiza Boom","41.99",[("Top","Sea Notes, Bergamot, Dry Woods"),("Heart","Apple, Black Pepper, Saffron, Geranium"),("Base","Patchouli, Cedar, Ylang-Ylang, Vetiver, Musk")],
 "Fresh · Aquatic · Woody","Sea air and bergamot over spiced apple and woods.",
 "a fresh, woody fragrance. Sea notes, bergamot and dry woods open crisply, a heart of apple, black pepper, saffron and geranium follows, and it settles into patchouli, cedar, ylang-ylang, vetiver and musk.",
 ["A fresh, salty opening of sea notes and bergamot","A spiced heart of apple and black pepper","A woody base of cedar, vetiver and musk","Fresh and easy to wear every day"],
 "Notes confirmed by 2 sources (FilledWithBarakah, Perfume Oriental). Perfume Oriental and Centrepoint market it for men; supplier's Unisex used. Awaiting photos.",
 "sea notes and bergamot over spiced apple and cedar.",["Fresh","Aquatic","Woody","Spicy"],["Aquatic","Citrus","Fruity","Spicy","Woody"])
SO("6298042001411","Ibiza Trap","41.99",[("Top","Cardamom, Coffee"),("Heart","Jasmine"),("Base","Incense, Oud, Vanilla")],
 "Gourmand · Spicy · Woody","Coffee and cardamom with jasmine over oud, incense and vanilla.",
 "a warm, spicy-gourmand fragrance. Cardamom and coffee open richly, a jasmine heart softens it, and it settles into incense, oud and vanilla.",
 ["A rich opening of cardamom and coffee","A soft jasmine heart","A deep base of oud, incense and vanilla","Great for evenings"],
 "Notes confirmed by 2 sources (ScentVerdict, FilledWithBarakah). Splash and Carrefour market it for women; supplier's Unisex used. Awaiting photos.",
 "coffee and cardamom with jasmine over oud and vanilla.",["Gourmand","Spicy","Woody","Oriental"],["Spicy","Jasmine","Woody","Vanilla"])
SO("6298042001435","Mauritius Tease","43.99",[("Top","Strawberry, Raspberry, Cherry, Blackcurrant, Mandarin, Lemon"),("Heart","Coconut, Gardenia, Orange Blossom, Peony"),("Base","Sandalwood, Musk, Amber, Vanilla, Oakmoss")],
 "Fruity · Floral · Sweet","Juicy red berries and coconut over a creamy vanilla base.",
 "a juicy, fruity-floral fragrance. Strawberry, raspberry, cherry, blackcurrant, mandarin and lemon open brightly, a heart of coconut, gardenia, orange blossom and peony follows, and it settles into sandalwood, musk, amber, vanilla and oakmoss.",
 ["A juicy opening of red berries and citrus","A tropical heart of coconut and white flowers","A creamy base of sandalwood and vanilla","Bright and playful for every day"],
 "Notes confirmed by 2 sources (ScentVerdict, Zaoud). Zaoud lists it as women's; supplier's Unisex used. Awaiting photos.",
 "red berries and coconut over sandalwood and vanilla.",["Fruity","Floral"],["Fruity","Floral","Citrus","Sandalwood","Vanilla"])
SO("6298042001305","Mauritius Touch","43.99",[("Top","Mandarin, Lime, Apple"),("Base","Dark Chocolate, Sandalwood, Tonka Bean")],
 "Citrus · Gourmand · Woody","Zesty lime and mandarin over dark chocolate and sandalwood.",
 "a fresh-to-gourmand fragrance. Mandarin, lime and apple open with a zesty sparkle, and it dries down to a smooth base of dark chocolate, sandalwood and tonka bean.",
 ["A zesty opening of lime and mandarin","Crisp apple freshness","A smooth base of dark chocolate and sandalwood","Fresh yet cosy"],
 "Top and base notes confirmed by 2 sources (ScentVerdict, FilledWithBarakah); their heart notes differ (geranium, cinnamon, sage vs osmanthus, cedar, tobacco), so the heart is not shown. Notino markets it for men; supplier's Unisex used. Awaiting photos.",
 "lime and mandarin over dark chocolate and sandalwood.",["Citrus","Gourmand","Woody"],["Citrus","Fruity","Sandalwood"])
SO("6298042001312","Miami Magic","40.99",[("Top","Bergamot, Lemon, Lavender, Mint, Pepper"),("Heart","Cinnamon, Sage, Geranium"),("Base","Patchouli, Amber, Musk, Vanilla")],
 "Aromatic · Fresh · Spicy","Citrus, mint and lavender over a warm amber base.",
 "a fresh, aromatic fragrance. Bergamot, lemon, lavender, mint and pepper open crisply, a heart of cinnamon, sage and geranium follows, and it settles into patchouli, amber, musk and vanilla.",
 ["A crisp opening of citrus, mint and lavender","A spicy-aromatic heart of cinnamon and sage","A warm base of amber and vanilla","Fresh and energetic"],
 "Notes confirmed by 2 sources (ScentVerdict, FilledWithBarakah). ScentVerdict and Centrepoint market it for men; supplier's Unisex used. Awaiting photos.",
 "citrus, mint and lavender over amber and vanilla.",["Aromatic","Fresh","Spicy"],["Citrus","Lavender","Spicy","Vanilla"])
SO("6298042001442","Miami Mama","41.99",[("Top","Ylang-Ylang, Mimosa, Peach"),("Heart","Rose, Lily of the Valley, Vanilla"),("Base","Musk, Amber, Sandalwood, Benzoin")],
 "Floral · Fruity · Oriental","Peach and white flowers over warm amber and sandalwood.",
 "a soft, oriental-floral fragrance. Ylang-ylang, mimosa and peach open sweetly, a heart of rose, lily of the valley and vanilla follows, and it settles into musk, amber, sandalwood and benzoin.",
 ["A sweet opening of peach and mimosa","A floral heart of rose and lily of the valley","A warm base of amber, sandalwood and musk","Soft and easy to wear"],
 "Notes confirmed by 2 sources (ScentVerdict, Arabic Parfums). Awaiting photos.",
 "peach and rose over amber, sandalwood and musk.",["Floral","Fruity","Oriental"],["Floral","Fruity","Rose","Vanilla","Sandalwood"])
add(cat_name="Haircare",bc="0810912033672",title="Sol de Janeiro Brazilian Joia Strengthening + Smoothing Shampoo 90ml",handle="sol-de-janeiro-brazilian-joia-strengthening-smoothing-shampoo-90ml",vendor="Sol de Janeiro",type="Haircare",gender="Unisex",cat="hb-3-10-13-3",
 price="17.49",cmp="22.99",qty=5,form="Shampoo",size="90",unit="ml",status="done",
 tags=["Sol de Janeiro","Unisex","Haircare","Shampoo","Brazilian Joia","Sulfate-Free","Frizz Control","Travel Size"],
 seo=("Sol de Janeiro Brazilian Joia Shampoo 90ml","Sol de Janeiro Brazilian Joia Strengthening + Smoothing Shampoo 90ml: travel-size bonding care for frizz and split ends."+FREE),
 desc=body("Stronger, smoother hair, in a handy travel size.","Sol de Janeiro Brazilian Joia Strengthening + Smoothing Shampoo 90ml is a sulfate-free bonding shampoo for damaged hair. SOL Seal Technology, Brazil nut and buriti fruit oil help repair damage, smooth frizz and split ends and restore shine, while cleansing without stripping moisture.",
  [("Key ingredients",ul(["<strong>SOL Seal Technology:</strong> plant-based microcapsules that help bond split ends","<strong>Brazil nut</strong>","<strong>Buriti fruit oil:</strong> helps smooth and add shine"])),
   ("Suits",ul(["Fine to medium hair","Straight, wavy and curly hair","Damaged, frizzy hair"])),
   ("Scent",ul(["Cheirosa 62: pistachio, almond, vanilla and salted caramel"])),
   ("How to use",ul(["Wet hair thoroughly","Lather into the scalp for 1 to 2 minutes, adding water as needed","Rinse and follow with the Brazilian Joia Conditioner"])),
   ("Good to know",ul(["Sulfate-free and colour-safe","Contains nuts","Travel size"]))],
  [("Brand","Sol de Janeiro"),("Range","Brazilian Joia"),("Type","Strengthening + smoothing shampoo"),("Hair type","Fine to medium, damaged hair"),("Size","90ml")],
  ["Helps repair damage and split ends","Smooths frizz and adds shine","Sulfate-free and colour-safe","Handy travel size"],
  [("Which hair is it for?","Fine to medium hair, straight, wavy or curly, especially damaged or frizzy hair."),("Is it sulfate-free?","Yes, and it is colour-safe.")]),
 note="Facts confirmed by 2 sources (Sol de Janeiro, Beauty Bay; same formula as the 295ml, which Sol de Janeiro sells in 90ml too). Supplier lists the 90ml as Unisex (the 295ml as Women); Unisex used. Awaiting photos.")
add(cat_name="Bath & Body",bc="5030805002829",title="Molton Brown Mesmerising Oudh Accord & Gold Bath & Shower Gel 300ml",handle="molton-brown-mesmerising-oudh-accord-gold-bath-shower-gel-300ml",vendor="Molton Brown",type="Bath & Body",gender="Unisex",cat="hb-3-2-1-5",
 price="28.99",cmp="38.99",qty=5,form="Shower Gel",size="300",unit="ml",status="done",
 tags=["Molton Brown","Unisex","Bath & Body","Shower Gel","Oudh Accord & Gold","Woody","Vegan"],
 seo=("Molton Brown Oudh Accord & Gold Shower Gel 300ml","Molton Brown Mesmerising Oudh Accord & Gold Bath & Shower Gel 300ml: spiced oud and honey with gold flakes."+FREE),
 desc=body("Warm, spiced oud with a shimmer of gold.","Molton Brown Mesmerising Oudh Accord &amp; Gold Bath &amp; Shower Gel 300ml is a rich, woody body wash flecked with gold. Key notes of bergamot, spice, black tea, honey and an oudh accord leave skin cleansed and lingering with a warm, spiced scent.",
  [("Scent",ul(["Bergamot and spice","Black tea","Oudh accord and honey"])),
   ("How to use",ul(["Shower: apply to damp skin for a delicate lather","Bath: pour a generous amount under warm running water"])),
   ("Good to know",ul(["Contains gold flakes","Vegan formula","Made in England"]))],
  [("Brand","Molton Brown"),("Product","Mesmerising Oudh Accord & Gold Bath & Shower Gel"),("Scent profile","Woody · Spicy · Warm"),("Size","300ml")],
  ["Warm, spiced oud scent","Shimmering gold flakes","Use in the bath or shower","Vegan formula"],
  [("What does it smell like?","Warm and spiced: bergamot, black tea, honey and oud."),("Is it unisex?","Yes, it suits everyone.")]),
 note="Facts confirmed by 2 sources (Niche Beauty, Jarrold). They list different full pyramids, so only shared key notes shown; gold flake carat differs (23.5 vs 24), so carat left out. Awaiting photos.")
add(cat_name="Bath & Body",bc="5030805015027",title="Molton Brown Wild Mint & Lavandin Bath & Shower Gel 300ml",handle="molton-brown-wild-mint-lavandin-bath-shower-gel-300ml",vendor="Molton Brown",type="Bath & Body",gender="Unisex",cat="hb-3-2-1-5",
 price="28.99",cmp="38.99",qty=5,form="Bath & Shower Gel",size="300",unit="ml",status="done",
 tags=["Molton Brown","Unisex","Bath & Body","Shower Gel","Wild Mint & Lavandin","Aromatic","Vegan"],
 seo=("Molton Brown Wild Mint & Lavandin Shower Gel 300ml","Molton Brown Wild Mint & Lavandin Bath & Shower Gel 300ml: fresh mint and lavandin over warm tonka bean."+FREE),
 desc=body("Cool mint and soothing lavandin.","Molton Brown Wild Mint &amp; Lavandin Bath &amp; Shower Gel 300ml is a refreshing, aromatic body wash. Fresh wild mint and herbaceous lavandin meet warm orris root, nutmeg and tonka bean for a ritual that feels both stimulating and soothing.",
  [("Scent",kd([("Top","Wild Mint"),("Heart","Lavandin"),("Base","Tonka Bean, Orris Root, Nutmeg")])),
   ("How to use",ul(["Shower: apply to damp skin for a light lather","Bath: pour a generous amount under warm running water"])),
   ("Good to know",ul(["Vegan formula","Paraben-free","Made in England"]))],
  [("Brand","Molton Brown"),("Product","Wild Mint & Lavandin Bath & Shower Gel"),("Scent profile","Aromatic · Fresh"),("Size","300ml")],
  ["Fresh, aromatic scent","Stimulating yet soothing","Use in the bath or shower","Vegan formula"],
  [("What does it smell like?","Fresh wild mint and lavandin over orris root, nutmeg and tonka bean."),("Is it unisex?","Yes, it suits everyone.")]),
 note="Facts confirmed by 2 sources (Niche Beauty, Jarrold). Awaiting photos.")
inputs={}
for i,p in enumerate(P,1):
    assert len(p['seo'][0])<=60 and len(p['seo'][1])<=160,(p['title'],len(p['seo'][0]),len(p['seo'][1]))
    inputs[f"i{i}"]={"title":p['title'],"handle":p['handle'],"status":"DRAFT","vendor":p['vendor'],"productType":p['type'],
     "category":"gid://shopify/TaxonomyCategory/"+p['cat'],"tags":p['tags'],"descriptionHtml":p['desc'],"seo":{"title":p['seo'][0],"description":p['seo'][1]},
     "productOptions":[{"name":"Title","values":[{"name":"Default Title"}]}],
     "variants":[{"optionValues":[{"optionName":"Title","name":"Default Title"}],"price":p['price'],"compareAtPrice":p['cmp'],"barcodes":[{"value":p['bc']}],
       "inventoryItem":{"tracked":True},"inventoryQuantities":[{"locationId":LOC,"name":"available","quantity":p['qty']}]}]}
json.dump(inputs,open('vars.json','w'),ensure_ascii=False)
json.dump(P,open('P.json','w'),ensure_ascii=False)
for p in P: print(p['title'],len(p['seo'][0]),len(p['seo'][1]))
print(json.dumps(inputs,ensure_ascii=False))
