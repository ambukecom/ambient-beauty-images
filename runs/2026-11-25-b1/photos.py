import json
T={"0085715801555":"Dunhill Desire Blue Eau de Toilette 100ml","0719346010115":"Elizabeth Taylor Passion Eau de Toilette 74ml","3760060761880":"Dumont Nitro Red Eau de Parfum 100ml","3605520386442":"Diesel Fuel For Life Homme Eau de Toilette 50ml","3614273924443":"Diesel D Red Eau de Parfum 50ml","3607347462583":"Davidoff Cool Water Woman Sea Rose Eau de Toilette 100ml","3616302038794":"Davidoff Cool Water Reborn Eau de Toilette 75ml","3616306130777":"Davidoff Cool Elixir Parfum Intense 50ml Gift Set with 75ml Hair & Body Wash","0020714156893":"Clinique Happy Eau de Parfum 100ml","0020714170479":"Clinique Happy Heart Eau de Parfum 50ml","3616303806101":"Davidoff Cool Water Woman Eau de Toilette 30ml Gift Set with 75ml Body Lotion","3414202000664":"Davidoff Cool Water Aftershave Lotion 125ml","0020714080310":"Clinique Happy for Men Cologne Spray 100ml","0020714711740":"Clinique Aromatics in White Eau de Parfum 100ml","0020714769987":"Clinique Aromatics In Black Eau de Parfum 100ml","3614223379897":"Davidoff Cool Water Wave Eau de Toilette 40ml","7640233340097":"Elie Saab Le Parfum Royal Eau de Parfum 90ml","0085715807595":"Dunhill Mongolian Cashmere Eau de Parfum 100ml","0719346450409":"Elizabeth Taylor Diamonds & Sapphires Eau de Toilette 100ml","7640233342466":"Elie Saab Girl of Now Rose Petal Eau de Parfum 90ml","0719346022705":"Elizabeth Taylor White Diamonds Eau de Toilette 100ml","3423473997658":"Elie Saab Le Parfum in White Eau de Parfum 90ml","0085715676733":"FCUK Him Eau de Toilette 3 x 25ml Gift Set – Original, Friction & Connect","7640233342565":"Elie Saab L'Homme Eau de Parfum 100ml","0719346158046":"Elizabeth Taylor Violet Eyes Eau de Parfum 100ml","0020714052959":"Clinique Happy Eau de Parfum 50ml","0085715807748":"Dunhill Driven Eau de Toilette 60ml","0085715676726":"FCUK Her Eau de Toilette 3 x 25ml Gift Set – Original, Friction & Connect","7640233341070":"Elie Saab Girl of Now Lovely Eau de Parfum 90ml","5050456522781":"Cerruti 1881 Eau de Toilette 200ml","3516641842321":"Franck Olivier Bella In Paris Eau de Parfum 75ml","3516642127120":"Franck Olivier Eau de Passion Men Eau de Toilette 75ml","3516642044328":"Franck Olivier Giorgia Eau de Parfum 75ml","3516641926328":"Franck Olivier One Kiss Eau de Parfum 75ml","3516642117312":"Franck Olivier White Touch Eau de Parfum 100ml","6291107015941":"Gulf Orchid Silver Absolute Eau de Parfum 100ml","6290362163091":"Gulf Orchid Smoky Vanilla Eau de Parfum 100ml","3423222092924":"Issey Miyake A Drop d'Issey Eau de Parfum 50ml Gift Set with 50ml Hand Cream","3423222010492":"Issey Miyake Fusion d'Issey IGO Eau de Toilette 80ml with 20ml Travel Spray","3423222048013":"Issey Miyake L'Eau d'Issey Eau & Magnolia Eau de Toilette Intense 50ml"}
# rejections: barcode -> {kind: reason}
REJ={"0020714170479":{"main":"main photo is a close-up of the cap only"},
 "7640233342466":{"main":"main photo is a close-up of the cap only"},
 "3423473997658":{"main":"photos show the 50ml size (box reads 50ml), product is 90ml","box":"box reads 50ml, product is 90ml"},
 "0085715676733":{"box":"photo shows a 4 x 18ml fcuk Discovery Set for Her, not the 3 x 25ml Him set"},
 "0085715676726":{"box":"photo shows a 4 x 18ml fcuk Discovery Set for Her, not the 3 x 25ml set"},
 "0719346158046":{"box":"product tiny/unusable in source photo (cut-out is a thin line)"},
 "7640233341070":{"main":"main photo is a close-up of the cap only"},
 "5050456522781":{"main":"main photo is a close-up of the cap only"},
 "3516641842321":{"main":"main cut-out unclean (wrapping/artefacts around bottle)"},
 "3516642127120":{"box":"cut-out washed out, product barely visible"},
 "3516642044328":{"box":"cut-out unclean, bottle edges lost"},
 "3516642117312":{"box":"cut-out washed out, product barely visible"},
 "6291107015941":{"main":"main photo is a close-up of the cap only"},
 "3423222048013":{"main":"main photo is the wooden cap only"}}
r=json.load(open('../../results/2026-11-25-b1-photos.json'))['items']
pid={x['barcode']:x['pid'] for x in json.load(open('photo_items.json'))}
RAW="https://raw.githubusercontent.com/ambukecom/ambient-beauty-images/main/"
upd={};notes={}
for it in r:
    bc=it['barcode'];media=[];why=[]
    for kind in ["main","box"]:
        info=it['images'].get(kind)
        if not info: why.append(f"no {kind} photo in folder"); continue
        if kind in REJ.get(bc,{}): why.append(f"{kind} rejected: {REJ[bc][kind]}"); continue
        media.append({"originalSource":RAW+info['path'],"alt":T[bc]+(" with box" if kind=="box" else ""),"mediaContentType":"IMAGE"})
    upd[bc]=media; notes[bc]=why
json.dump(upd,open('photo_upd.json','w'),ensure_ascii=False,indent=0); json.dump(notes,open('photo_notes.json','w'),ensure_ascii=False,indent=0)
att=[b for b in upd if upd[b]]; none=[b for b in upd if not upd[b]]
print(len(att),"with photos;",none)
q=[];V={}
for i,b in enumerate(att):
    q.append(f'm{i}: productUpdate(product:{{id:"gid://shopify/Product/{pid[b]}"}}, media:$v{i}){{ userErrors{{ field message }} }}')
    V[f"v{i}"]=upd[b]
mut="mutation("+",".join(f"$v{i}:[CreateMediaInput!]" for i in range(len(att)))+"){"+" ".join(q)+"}"
json.dump({"query":mut,"variables":V},open('photo_mut.json','w'),ensure_ascii=False)
print(len(mut))
