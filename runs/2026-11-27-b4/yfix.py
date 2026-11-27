import json
SID=526927699
R=json.load(open('fix_rows.json'))
res={i['barcode']:sorted(i['images']) for i in json.load(open('../../results/2026-11-27-b4-fixes.json'))['items']}
def rng(r): return {"sheetId":SID,"startRowIndex":r-1,"endRowIndex":r,"startColumnIndex":24,"endColumnIndex":25}
reqs=[]
for b,r in R.items():
    imgs=res[b]
    s="Photos attached 27/11 (owner-approved fix)." if len(imgs)==2 else f"Photo attached 27/11 (owner-approved fix; {imgs[0]} photo only)."
    if r==306:
        reqs.append({"findReplace":{"find":"Photos rejected 23/11: box rejected – perfume-click watermark; no main photo in folder – please replace them. Awaiting photos.","replacement":s,"range":rng(r)}})
    elif r in (14,):
        reqs.append({"findReplace":{"find":"^.*$","replacement":"Superdrug lists this barcode as Classic Daily Shampoo 450ml. "+s,"searchByRegex":True,"range":rng(r)}})
    elif r==24 and False: pass
    else:
        reqs.append({"findReplace":{"find":r"\s*(Photos? (NOT )?attached|Photos? rejected|Main photo attached|Box photo attached|Photo label reads|Awaiting second).*$","replacement":" "+s,"searchByRegex":True,"range":rng(r)}})
B4={472:"Photo rejected 27/11: main photo is a cropped close-up of the bottle top (bottle cut off at the bottom); no box photo in folder.",
473:"Photos attached 27/11 (box photo only – no main photo in folder).",474:"Photos attached 27/11 (box photo only – no main photo in folder).",
475:"Photos attached 27/11.",476:"Photos attached 27/11 (main photo only – no box photo in folder).",
477:"Photos rejected 27/11: main and box photos show Bvlgari Pour Homme, not Narciso Rodriguez Vetiver Musc.",
478:"Photo rejected 27/11: box photo cut-out broken (only fragments of box and cap); no main photo in folder.",
479:"Photos attached 27/11 (box photo only – no main photo in folder)."}
for r,s in B4.items():
    reqs.append({"findReplace":{"find":"Awaiting photos.","replacement":s,"range":rng(r)}})
json.dump(reqs,open('yfix_reqs.json','w'),ensure_ascii=False)
print(json.dumps(reqs,ensure_ascii=False))
