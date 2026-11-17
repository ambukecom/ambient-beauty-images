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
    return f"A heart of {a[0]}, settling into {a[1]}."
def F(bc,vendor,title,gender,size,price,cmp,qty,pyr,profile,hook,intro,love,note,seo_d,of,fr,conc="Eau De Parfum",concl="Eau de Parfum",name=None,status="done"):
    h=title.lower().replace(" & ","-").replace(".","").replace(" ","-")
    q2=("Is it unisex?","Yes, it is made for everyone.") if gender=="Unisex" else (("Is it for men?","Yes, it is a men's fragrance.") if gender=="Men" else ("Is it for women?","Yes, it is a women's fragrance."))
    frag(bc,vendor,title,h,gender,size,price,cmp,qty,pyr,profile,hook,intro,love,[(f"What does {name} smell like?",faq(name,pyr)),q2] if pyr else [q2],note,seo_d,conc=conc,concl=concl,of=of,fr=fr,status=status)
F("6281085040417","Surrati","Surrati Lateefa Eau de Parfum 100ml","Unisex","100","28.49","37.99",3,[("Heart","Rose, White Flowers"),("Base","Musk, Amber")],
 "Floral · Musky · Soft","Soft rose and white flowers over warm musk and amber.",
 "Surrati Lateefa Eau de Parfum 100ml is a soft, elegant floral fragrance. A delicate floral opening leads to a heart of rose and white flowers, settling into a warm, comforting base of musk and amber.",
 ["A soft, delicate floral opening","A heart of rose and white flowers","A warm base of musk and amber","Easy to wear every day"],
 "Heart and base notes confirmed by 2 sources (Just My Look, Perfume Trading); their top notes differ slightly, so only shared notes shown. Just My Look lists it as women's; supplier's Unisex used. Awaiting photos.",
 "rose and white flowers over musk and amber.",["Floral","Musky"],["Rose","Floral"],name="Lateefa")
F("6281085019758","Surrati","Surrati Ameer Al Oud Eau de Parfum 100ml","Unisex","100","19.99","26.99",1,[("Top","Pepper, Nutmeg"),("Heart","Rose, Oud"),("Base","Sandalwood, Patchouli, Vetiver")],
 "Woody · Spicy · Oud","Spiced oud and rose over sandalwood and vetiver.",
 "Surrati Ameer Al Oud Eau de Parfum 100ml is a rich, spicy oud fragrance for everyone. Pepper and nutmeg open warmly, a heart of rose and smoky oud follows, and it settles into a woody base of sandalwood, patchouli and vetiver.",
 ["A warm, spicy opening of pepper and nutmeg","A heart of rose and smoky oud","A woody base of sandalwood and vetiver","Great value 100ml bottle"],
 "Notes confirmed by 2 sources (Superdrug, EAN matches 6281085019758; FilledWithBarakah). Awaiting photos.",
 "pepper and rose with smoky oud over sandalwood.",["Woody","Spicy","Oriental"],["Woody","Spicy","Rose","Sandalwood"],name="Ameer Al Oud")
F("6295124048494","Swiss Arabian","Swiss Arabian Soul of Bali Extrait de Parfum 100ml","Unisex","100","52.49","68.99",1,[("Top","Bergamot, Rhubarb, Pink Pepper, Pineapple, Ginger, Mango"),("Heart","Aquatic Notes, Saffron, Cardamom, Nutmeg, Rosewood, Olibanum"),("Base","Ambergris, Sandalwood, Cypriol, Musk")],
 "Fruity · Aquatic · Spicy","Tropical fruits and sea air over warm spices and woods.",
 "Swiss Arabian Soul of Bali Extrait de Parfum 100ml is a vibrant, tropical fragrance for everyone. Bergamot, rhubarb, pineapple, mango, ginger and pink pepper open brightly, a heart of aquatic notes, saffron, cardamom, nutmeg, rosewood and olibanum follows, and it settles into ambergris, sandalwood, cypriol and musk.",
 ["A juicy tropical opening of pineapple and mango","An aquatic, spicy heart","A warm base of ambergris and sandalwood","Long-lasting extrait concentration"],
 "Notes confirmed by 2 sources (Just My Look, Arabic Parfums). Awaiting photos.",
 "pineapple and mango with sea air, saffron and sandalwood.",["Fruity","Aquatic","Spicy","Woody"],["Fruity","Aquatic","Spicy","Sandalwood"],conc="Extrait De Parfum",concl="Extrait de Parfum",name="Soul of Bali")
F("0022548055373","Tommy Hilfiger","Tommy Hilfiger Tommy Eau de Toilette 30ml","Men","30","24.49","33.99",3,[],
 "Fresh · Aromatic · Fruity","The classic all-American fresh scent for men.",
 "Tommy Hilfiger Tommy Eau de Toilette 30ml is a fresh, aromatic classic for men. Key notes include grapefruit, lavender, cranberry, bluegrass, yellow rose and a warm apple pie accord, finishing with woody maple.",
 ["A fresh, aromatic classic","Crisp grapefruit and lavender","Fruity cranberry and apple pie","Handy 30ml size"],
 "Key notes confirmed by 2 sources (Escentual, Just My Look); they place notes in different tiers, so key notes listed instead of a pyramid. Store has the 100ml and 200ml (not duplicates). Awaiting photos.",
 "grapefruit, lavender and cranberry with apple pie and maple.",["Fresh","Aromatic","Fruity"],["Citrus","Lavender","Fruity","Rose","Woody"],conc="Eau De Toilette",concl="Eau de Toilette")
F("6290360379791","Street Origins","Street Origins Hot Drip Dubai Extrait de Parfum 75ml","Unisex","75","43.49","57.99",1,[("Top","Passion Fruit, Saffron, Rose"),("Heart","Oud, Patchouli, Benzoin"),("Base","Leather, Vanilla, Amber, Cistus")],
 "Oriental · Woody · Spicy","Passion fruit and saffron over oud, leather and vanilla.",
 "Street Origins Hot Drip Dubai Extrait de Parfum 75ml is a rich, oriental fragrance. Passion fruit, saffron and rose open warmly, a heart of oud, patchouli and benzoin follows, and it settles into leather, vanilla, amber and cistus.",
 ["A fruity, spicy opening of passion fruit and saffron","A rich heart of oud and patchouli","A warm base of leather, vanilla and amber","Long-lasting extrait concentration"],
 "Notes confirmed by 2 sources (FilledWithBarakah, Perfume Oriental); Superdrug confirms EAN 6290360379791. Perfume Oriental markets it for men; supplier's Unisex used. Awaiting photos.",
 "passion fruit and saffron over oud, leather and vanilla.",["Oriental","Woody","Spicy"],["Fruity","Spicy","Rose","Woody","Vanilla"],conc="Extrait De Parfum",concl="Extrait de Parfum",name="Hot Drip Dubai")
F("6298042001275","Street Origins","Street Origins Hawaii Beau Eau de Parfum 75ml","Unisex","75","32.49","44.99",1,[("Top","Bergamot, Grapefruit"),("Heart","Oak, Sandalwood"),("Base","Ambroxan, Tonka Bean")],
 "Citrus · Woody · Fresh","Bright citrus over smooth woods and ambroxan.",
 "Street Origins Hawaii Beau Eau de Parfum 75ml is a fresh, woody fragrance for everyone. Bergamot and grapefruit open brightly, a heart of oak and sandalwood follows, and it settles into a smooth base of ambroxan and tonka bean.",
 ["A bright citrus opening","A smooth heart of oak and sandalwood","A warm ambroxan and tonka finish","Fresh and easy to wear every day"],
 "Notes confirmed by 2 sources (ScentVerdict, FilledWithBarakah). Awaiting photos.",
 "bergamot and grapefruit over sandalwood and ambroxan.",["Citrus","Woody","Fresh"],["Citrus","Woody","Sandalwood"],name="Hawaii Beau")
def sdj(bc,size,price,cmp):
    add(cat_name="Haircare",bc=bc,title=f"Sol de Janeiro Brazilian Joia Strengthening + Smoothing Conditioner {size}ml",handle=f"sol-de-janeiro-brazilian-joia-strengthening-smoothing-conditioner-{size}ml",vendor="Sol de Janeiro",type="Haircare",gender="Women",cat="hb-3-10-13-1",
     price=price,cmp=cmp,qty=5,form="Conditioner",size=size,unit="ml",status="done",
     tags=["Sol de Janeiro","Women","Haircare","Conditioner","Brazilian Joia","Frizz Control","Damaged Hair","Vegan"],
     seo=(f"Sol de Janeiro Brazilian Joia Conditioner {size}ml",f"Sol de Janeiro Brazilian Joia Strengthening + Smoothing Conditioner {size}ml: smooths frizz and helps repair split ends."+FREE),
     desc=body("Smoother, stronger hair with the Cheirosa 62 scent.",f"Sol de Janeiro Brazilian Joia Strengthening + Smoothing Conditioner {size}ml is a rich yet weightless bond-repairing conditioner. SOL Seal Technology, Brazil nut oil and buriti fruit help repair split ends, smooth frizz and boost shine, scented with the brand's Cheirosa 62 fragrance.",
      [("Key ingredients",ul(["<strong>SOL Seal Technology:</strong> plant-based microcapsules that help repair damage","<strong>Brazil nut oil:</strong> for shine","<strong>Buriti fruit:</strong> helps fight frizz"])),
       ("Suits",ul(["Fine to medium hair","Straight, wavy and curly hair","Damaged, frizzy hair"])),
       ("How to use",ul(["After shampooing, apply to the mid-lengths and ends","Leave for 2 to 3 minutes, then rinse thoroughly","For a mask, leave on for 10 to 20 minutes"])),
       ("Good to know",ul(["Vegan and colour-safe","Contains nuts"]))],
      [("Brand","Sol de Janeiro"),("Range","Brazilian Joia"),("Type","Strengthening + smoothing conditioner"),("Hair type","Fine to medium, damaged hair"),("Size",f"{size}ml")],
      ["Smooths frizz and boosts shine","Helps repair split ends","Weightless, rich conditioning","The much-loved Cheirosa 62 scent"],
      [("How long do I leave it on?","2 to 3 minutes, or 10 to 20 minutes as a mask."),("What should I use with it?","The Brazilian Joia Strengthening + Smoothing Shampoo.")]),
     note="Facts confirmed by 2 sources (Sephora UK, Ulta). Clinical percentage claims left out. Awaiting photos.")
sdj("0810912033696","295","30.49","40.99"); sdj("0810912033689","90","17.49","22.99")
add(cat_name="Bath & Body",bc="5030805002683",title="Molton Brown Re-Charge Black Pepper Bath & Shower Gel 300ml",handle="molton-brown-re-charge-black-pepper-bath-shower-gel-300ml",vendor="Molton Brown",type="Bath & Body",gender="Men",cat="hb-3-2-1-5",
 price="27.49",cmp="36.99",qty=5,form="Shower Gel",size="300",unit="ml",status="done",
 tags=["Molton Brown","Men","Bath & Body","Shower Gel","Re-Charge Black Pepper","Spicy","Vegan"],
 seo=("Molton Brown Re-Charge Black Pepper Shower Gel 300ml","Molton Brown Re-Charge Black Pepper Bath & Shower Gel 300ml: an energising spicy wash with black pepper and vetiver."+FREE),
 desc=body("An energising, spicy start to the day.","Molton Brown Re-Charge Black Pepper Bath &amp; Shower Gel 300ml is an invigorating, spicy body wash. Heated notes of black pepper, aromatic coriander and vetiver leave skin feeling deeply cleansed and energised, perfect for a morning shower or after a workout.",
  [("Scent",kd([("Top","Cardamom, Bergamot"),("Heart","Black Pepper, Pink Pepper, Lavandin"),("Base","Cedarwood, Vetiver, Musk")])),
   ("How to use",ul(["Shower: lather onto damp skin, then rinse","Bath: pour a generous amount under warm running water"])),
   ("Good to know",ul(["Vegan formula","Paraben-free","Made in England"]))],
  [("Brand","Molton Brown"),("Product","Re-Charge Black Pepper Bath & Shower Gel"),("Scent profile","Spicy · Woody"),("Size","300ml")],
  ["Energising spicy scent","Leaves skin feeling deeply cleansed","Use in the bath or shower","Vegan formula"],
  [("What does it smell like?","Black pepper with cardamom, bergamot and lavandin over cedarwood and vetiver."),("Can I use it in the bath?","Yes, pour it under warm running water.")]),
 note="Facts confirmed by 2 sources (John Lewis, Niche Beauty). Scent pyramid from Niche Beauty; John Lewis confirms black pepper and vetiver. Awaiting photos.")
add(cat_name="Bath & Body",bc="5030805003321",title="Molton Brown Rose Dunes Bath & Shower Gel 300ml",handle="molton-brown-rose-dunes-bath-shower-gel-300ml",vendor="Molton Brown",type="Bath & Body",gender="Unisex",cat="hb-3-2-1-5",
 price="28.99",cmp="38.99",qty=5,form="Shower Gel",size="300",unit="ml",status="done",
 tags=["Molton Brown","Unisex","Bath & Body","Shower Gel","Rose Dunes","Floral","Vegan"],
 seo=("Molton Brown Rose Dunes Bath & Shower Gel 300ml","Molton Brown Rose Dunes Bath & Shower Gel 300ml: rose, saffron and patchouli in a shimmering, vegan gel."+FREE),
 desc=body("Desert rose and spice in a shimmering gel.","Molton Brown Rose Dunes Bath &amp; Shower Gel 300ml is a rich, floral-amber body wash. Cassis, saffron, violet leaf and pepper open onto a heart of rose and geranium over Sulawesi patchouli. The shimmering gel cleanses gently and leaves skin soft and subtly scented.",
  [("Scent",kd([("Top","Cassis, Saffron, Violet Leaf, Pepper"),("Heart","Rose, Geranium"),("Base","Sulawesi Patchouli")])),
   ("How to use",ul(["Shower: apply to damp skin for a delicate lather","Bath: pour a generous amount under warm running water"])),
   ("Good to know",ul(["Vegan formula","Made in England"]))],
  [("Brand","Molton Brown"),("Product","Rose Dunes Bath & Shower Gel"),("Scent profile","Floral · Amber · Spicy"),("Size","300ml")],
  ["Rich rose and saffron scent","Leaves skin soft and subtly scented","Use in the bath or shower","Vegan formula"],
  [("What does it smell like?","Cassis, saffron and pepper, then rose and geranium, over Sulawesi patchouli."),("Is it unisex?","Yes, it suits everyone.")]),
 note="Facts confirmed by 2 sources (Niche Beauty, Lyko); only notes listed by both are shown. Awaiting photos.")
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
