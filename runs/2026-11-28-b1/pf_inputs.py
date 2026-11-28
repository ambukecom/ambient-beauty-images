import json
SH="https://admin.shopify.com/store/f1d55c-f7/products/"; DR="https://drive.google.com/drive/folders/"
cur=json.load(open('pf_cur.json'))
b4=json.load(open('../2026-11-27-b4/pf.json'))['rows'][2:]
U={r[4].lstrip("'"):[r[5],r[6],r[7]] for r in b4}
U["6298043160421"]=["Maison Alhambra Jean Lowe Fantasme Eau de Parfum 100ml",DR+"1K06Gts-GnPdiZgwrmM0SCye8A8Jx1QZg",SH+"15984668246356"]
U["0810876038119"]=["Lamborghini Millennials Dinamico Eau de Toilette 75ml",DR+"11NjhxnHOoN__9uG7-hbhzf0njs5RuGBB",SH+"16024141889876"]
FX={"0085715676726":"1L08U7lSOVAC_nwvZyuJjC1H09d3m76PF","0085715676733":"1SNUUaNnxGTJ503jrJ9DpEQGmC_9uP2dt","3386460169400":"1ATSW638qBxc8AJDhqfVhdcj1zbNgzY8M","3386460149969":"1OM8e3B3TeLnnQFKDknFyExzGNwMwxtgS","7640171199481":"19ESufnyv9vPVNHXz5usJDqCcEZQF5fNp","7640171199719":"1XihsfQ6vaQZ-cniN87Nn3Ona9LIWDIse","3614274380392":"1aOi1-TTYaeJWfWbRItzrNABSP1zDSHUO","3595471026897":"1_7r9OVEpUZ8gJm9s8lHRzq8auRMUvJcc","3595471091079":"1DfnkyhXmbkQpOVgAzB9x97w-oDFzG4Oy","3595471071156":"1bnH7GsH0sevZhJuiiQACzYlJXq-gYS83","3386460175609":"1eLB8NcnnYP_s8yI7FKkh2-CYcf1ZpXi6","3386460032780":"1yaFUM9dlWoQMq5sK6XU3VsqNy4yIpPlL","3423222133849":"1CdtrsntR-XeLsskdKgbkz4xmZa7VDtiG","6295124042799":"1e_70TqU7PJDN3fOFRalXswEE1DkxK_lh"}
F=json.load(open('fix_products.json'))
for b,f in FX.items(): U[b]=[F[b][2],DR+f,SH+F[b][0]]
UNL={"6293708007479","6298043160421","0008080151445","3386460149969","0679602793643","6298042001374","6290171074168","3474636976058","3516642044328"}
R0={  # reasons for rows with no photos (become Daily Plan M 'rejected – …')
"0085715169563":"Main shows only the cap; box cut-out eats into the bottle",
"0085715169570":"Main photo shows only the cap; box cut-out eats into the bottle",
"0085715167507":"Low-res source, stray cut-out fragments above the box; no box photo",
"6293708018901":"Low-res box photo with watermark, torn cut-out; no main photo",
"8411061081846":"Product tiny in source photos, only a sliver of box/bottle shows",
"6295156400215":"Main photo cropped at the bottom; box photo cut-out messy (white box on white background)",
"6290361912348":"The clear glass bottle disappears in the white-background cut-out (only cap left)",
"0812256028611":"Clear cloud top breaks up in the white-background cut-out",
"6294015102246":"Cut-outs show only fragments of the bottle/box (product tiny in source photos)",
"3614225358463":"Main photo shows only the eye banner; box photo cut-out messy",
"8411061074855":"Box rejected – bottle cut-out broken (only a sliver of the base shows); no main photo in folder",
"8054754400625":"Box: box cut-out is fragmented/messy",
"0085805255824":"Box: box cut-out is ragged with missing pieces",
"0085805557379":"The white bottle is washed out in the white-background cut-out",
"0719346158046":"No main photo in folder; box photo unusable (product tiny, cut-out is a thin line)",
"3516642127120":"No main photo in folder; box cut-out washed out, product barely visible",
"3516642044328":"No main photo in folder; box cut-out unclean, bottle edges lost",
"3516642117312":"No main photo in folder; box cut-out washed out, product barely visible",
"3423222118341":"Main rejected: cut-out washed out, bottle barely visible; box rejected: photo shows only the cap and part of the box",
"3386460160193":"No main photo in folder; box rejected: bottle in box photo partly washed out (unclean cut-out)",
"7640111499060":"Main rejected: cut-out washed out, bottle edges lost; box rejected: box cropped and bottle washed out",
"3454960024021":"Main rejected: cap only (product tiny in source); box rejected: cap only, box cut-out broken",
"0856857007194":"Box photo is unusable (fragments only)",
"3607342221208":"Cut-out lost the bottle (only daisy cap left)",
"3614227086227":"Cut-out lost the bottle (only cap charms left)",
"3616305181473":"Box: box cut-out is a thin sliver (product tiny in source)",
"3616303461881":"Cut-out lost the bottle (only cap charms left)",
"0008080151445":"Stray grey artefact in the cut-out",
"3386460028394":"Cut-out not clean (white bottle washed out)",
"0608940583562":"Box photo cut-out broken (only fragments of box and cap); no main photo in folder",
"0810912033672":"The cut-out damaged the white cap (jagged edges)",
"7640171199481":"Main and box photos still show the original Amethyst, not Exquise (no 'Exquise' on bottle or box)",
"3595471091079":"Box photo is still the 60ml box, not 20ml; no main photo in folder",
"3386460032780":"Photos still show the Legend Eau de Toilette bottle and EDT box, not the aftershave lotion",
"3423222133849":"New set photo still shows no 'Intense' on box or bottle (can't confirm edition); no box photo in folder",
"3423222107727":"Main and box photos show Bvlgari Pour Homme, not Narciso Rodriguez Vetiver Musc",
"6295124042799":"No main photo in folder; box photo cut-out broken (only fragments of a box and cap)",
"0085715167217":"Main and box photos cropped (bottle cut off at the bottom)",
"0085715167828":"Only a box photo, bottle and box cropped at the bottom",
"3614226905192":"Main bottle cropped at the bottom; 'box' photo shows a bottle only (looks like 100ml)",
"3666057157417":"Tiny source (90x322) with a perfume-click watermark",
"8435415082921":"The main photo is a close-up of the pump only, and the box photo is cropped and very small",
"3386460130011":"Main rejected: main photo is the cap only; box rejected: photo shows the cap and a cropped corner of the box only",
"3423222080952":"Main photo is a cropped close-up of the bottle top; no box photo in folder",
}
OA="Uploaded 27/11 (owner-approved) – rechecked 27/11: not right yet, see What's wrong"
K={b:OA for b in "0810101500060 3666057165580 3423473997658 3274872472891 3454960007468 0856857007101 3607349764289 3595471041012 3614274797220 3616304197420 3614274797213 3614274797244 3474636976058 6281085039978 3595471061096".split()}
K.update({"0738678000991":"Uploaded 27/11: main photo only – add box.jpg","0738678001042":"Uploaded 27/11: main photo only – add box.jpg",
"8411061044995":"Uploaded 27/11: box photo only – add main.jpg","4051395412110":"Uploaded 27/11: main photo only – add box.jpg","0679602793643":"Uploaded 27/11: box photo only – add main.jpg"})
RC="Rechecked 28/11: "
K.update({"0085715676726":RC+"main uploaded (no box photo in folder)","0085715676733":RC+"main uploaded (no box photo in folder)",
"3386460169400":RC+"main + box uploaded","3386460149969":RC+"main + box uploaded","7640171199719":RC+"main + box uploaded",
"3614274380392":RC+"main + box uploaded","3595471026897":RC+"main + box uploaded","3386460175609":RC+"main + box uploaded",
"3595471071156":RC+"1 photo uploaded (bottle with 20ml box) – add main.jpg",
"7640171199481":RC+"main + box still original Amethyst – not uploaded","3595471091079":RC+"box still 60ml, no main – not uploaded",
"3386460032780":RC+"still Legend EDT photos – not uploaded","3423222133849":RC+"no 'Intense' visible, no box photo – not uploaded",
"6295124042799":RC+"box cut-out broken, no main – not uploaded"})
checks=json.load(open('../../workflow/photo_checks.json'))
# new drafts of this run
P=json.load(open('P.json')); ids=json.load(open('ids.json')); fid=json.load(open('fid.json'))
prod=[];plan=[["h"]];ex=[["note"],["hdr"]];state={}
def add(bc,title,fold,pl,status,media,m):
    r=[""]*25; r[4]=title; r[10]="'"+bc; r[19]=fold; r[23]=pl; prod.append(r)
    d=[""]*14; d[6]=bc; d[12]=m; plan.append(d)
    state["gid://shopify/Product/"+pl.split('/')[-1]]=[status,len(media),media]
for b in cur:
    t,fo,pl=U[b]
    media=checks[b]['media'] if b in checks else []
    add(b,t,fo,pl,"UNLISTED" if b in UNL else "DRAFT",media,("rejected – "+R0[b]) if b in R0 else "")
    e=[""]*11; e[0]="FALSE"; e[4]="'"+b; e[10]=K.get(b,""); ex.append(e)
    if not media and b not in R0: print("!! no reason",b)
for p,i in zip(P,ids):
    add(p['bc'],p['title'],DR+fid[p['bc']],SH+i[0].split('/')[-1],"DRAFT",[],"")
json.dump({"values":prod},open('pf_prod.json','w'),ensure_ascii=False); json.dump({"values":plan},open('pf_plan.json','w'),ensure_ascii=False)
json.dump({"values":ex},open('pf_existing.json','w'),ensure_ascii=False); json.dump(state,open('pf_state.json','w'))
print(len(prod))
