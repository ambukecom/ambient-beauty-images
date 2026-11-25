import json
items=json.load(open('photo_items.json'))
r={x['barcode']:x for x in json.load(open('../../results/2026-11-25-b3-photos.json'))['items']}
T={"3423222118341":"Issey Miyake L'Eau d'Issey Eau de Parfum Intense 100ml","3423222048037":"Issey Miyake L'Eau d'Issey Pour Homme Eau & Cèdre Eau de Toilette Intense 50ml","3423470311358":"Issey Miyake L'Eau d'Issey Pour Homme Eau de Toilette 75ml","3423222106201":"Issey Miyake L'Eau d'Issey Pour Homme Solar Lavender Eau de Toilette Intense 50ml","3423474867059":"Issey Miyake L'Eau d'Issey Pour Homme Sport Eau de Toilette 50ml","3423478753754":"Issey Miyake L'Eau d'Issey Pure Pétale de Nectar Eau de Toilette 50ml","3423478515857":"Issey Miyake L'Eau d'Issey Rose & Rose Eau de Parfum Intense 50ml","3423222105860":"Issey Miyake L'Eau d'Issey Solar Violet Eau de Toilette Intense 50ml","3423222090715":"Issey Miyake L'Eau d'Issey Pour Homme Vétiver Eau de Toilette Intense 50ml","3423474889259":"Issey Miyake Nuit d'Issey Bleu Astral Eau de Toilette 125ml","7640171194455":"Jaguar Era Reloaded Eau de Parfum 100ml","7640171193069":"Jaguar Ultimate Power Eau de Toilette 100ml","5050456110018":"Jennifer Lopez Miami Glow Eau de Toilette 100ml","3386460073868":"Jimmy Choo L'Eau Eau de Toilette 90ml","3386460136549":"Jimmy Choo Rose Passion Eau de Parfum 100ml","3386460109369":"Jimmy Choo Urban Hero Eau de Parfum 100ml","3386460124867":"Karl Lagerfeld Bois d'Ambre Eau de Toilette 100ml","3386460133869":"Karl Lagerfeld Bois de Cyprès Eau de Toilette 100ml","3386460087261":"Karl Lagerfeld Bois de Vetiver Eau de Toilette 100ml","3386460094542":"Karl Lagerfeld Classic Aftershave Lotion 100ml","3386460161565":"Karl Lagerfeld Fleur d'Iris Eau de Parfum 100ml","3386460133814":"Karl Lagerfeld Fleur de Pivoine Eau de Parfum 100ml","3386460059183":"Karl Lagerfeld for Him Eau de Toilette 100ml","3386460160193":"Karl Lagerfeld Jeans Urban Pink Eau de Parfum 100ml","3386460149822":"Karl Lagerfeld Ikonik Pour Femme Eau de Parfum 100ml","3386460115551":"Karl Lagerfeld Karl New York Mercer Street Eau de Toilette 100ml","3386460130011":"Karl Lagerfeld Karl Rome Divino Amore Eau de Parfum 100ml","3274872472891":"Kenzo Flower Ikebana Sakura Eau de Parfum 75ml Gift Set with 10ml Travel Spray and 75ml Body Lotion","3274872423398":"Kenzo Homme Eau de Parfum 110ml","3274872421554":"Kenzo Homme Eau de Toilette Intense 110ml"}
REJ={"3423222118341":{"main":"cut-out washed out, bottle barely visible","box":"photo shows only the cap and part of the box"},
 "3423222048037":{"main":"main photo is the wooden cap only"},
 "3423222090715":{"main":"main photo is the wooden cap only"},
 "3386460073868":{"box":"box cut-out washed out with artefacts"},
 "3386460124867":{"box":"'box' photo shows the bottle only, no box"},
 "3386460133869":{"main":"main photo is a cropped close-up (top of bottle cut off)"},
 "3386460087261":{"main":"main photo is a cropped close-up (top of bottle cut off)"},
 "3386460161565":{"main":"main photo is a cropped close-up (top of bottle cut off)"},
 "3386460160193":{"box":"bottle in box photo partly washed out (unclean cut-out)"},
 "3386460115551":{"main":"cut-out washed out, bottle edges lost"},
 "3386460130011":{"main":"main photo is the cap only","box":"photo shows the cap and a cropped corner of the box only"}}
RAW="https://raw.githubusercontent.com/ambukecom/ambient-beauty-images/main/"
upd={};notes={};pid={i['barcode']:i['pid'] for i in items}
for it in items:
    bc=it['barcode'];media=[];why=[]
    for kind in ["main","box"]:
        info=r[bc]['images'].get(kind)
        if not info: why.append(f"no {kind} photo in folder"); continue
        if kind in REJ.get(bc,{}): why.append(f"{kind} rejected: {REJ[bc][kind]}"); continue
        media.append({"originalSource":RAW+info['path'],"alt":T[bc]+(" with box" if kind=="box" else ""),"mediaContentType":"IMAGE"})
    upd[bc]=media; notes[bc]=why
json.dump(upd,open('photo_upd.json','w'),ensure_ascii=False,indent=0); json.dump(notes,open('photo_notes.json','w'),ensure_ascii=False,indent=0)
att=[b for b in upd if upd[b]]; print(len(att),"with photos; none:",[b for b in upd if not upd[b]])
q=[];V={}
for i,b in enumerate(att):
    q.append(f'm{i}: productUpdate(product:{{id:"gid://shopify/Product/{pid[b]}"}}, media:$v{i}){{ userErrors{{ field message }} }}')
    V[f"v{i}"]=upd[b]
json.dump({"query":"mutation("+",".join(f"$v{i}:[CreateMediaInput!]" for i in range(len(att)))+"){"+" ".join(q)+"}","variables":V,"att":att},open('photo_mut.json','w'),ensure_ascii=False)
print(sum(len(upd[b]) for b in att),"images")
