import json
P=json.load(open('P.json')); ids=json.load(open('ids.json'))
FID={"6293708018901":"1T4VXDtntlUyklbj5BLSevWJ1t37FZNJs","6293708005352":"1SD6VwM1bfYVpbcb-czy6ueTtFS0u8zEo","0085715064752":"1N64zxQH7nzSHPeDY9V9mBdPiTcFmYvJ4","0085715081872":"1bbQqRLo3eM1QxJETNWISXfUpwQz_8aIF","8411061081587":"1etdKZBEq-C2sp88_nX2nO6IDNayeaAVU","8411061982105":"1M6lxSPBDjaigYurB1hHGQr28ZB5Xbacw","8411061044995":"12cFIAKVSeA0R2jUOWB5Z6_PbMNHPLyiL","8411061117071":"1t9u7ZIO0DqV7WPvJOMHq2MCTX7a2llQY","8411061088593":"1RVtIbpksIkM_hzKfpssFcYowr-CU14EO","8411061081341":"1suyWG4o0Rj6AI4EWkYU-EHJxuBp7Pr2R"}
SUP={"6293708018901":("1","13.99","Ajmal My Stellar Eau de Parfum 100ml Spray"),
"6293708005352":("3","8.24","Ajmal Silver Shade Eau De Parfum 100ml Spray"),
"0085715064752":("50","11.17","Anna Sui Sky Eau de Toilette 75ml Spray"),
"0085715081872":("50","9.61","Anna Sui Sui Dreams Eau de Toilette 50ml Spray"),
"8411061081587":("50","11.02","Antonio Banderas Blue Seduction for Women Eau de Toilette 200ml Spray"),
"8411061982105":("50","9.61","Antonio Banderas Blue Seduction for Women Eau de Toilette 80ml Spray"),
"8411061044995":("50","11.04","Antonio Banderas Diavolo For Men Gift Set 50ml EDT + 75ml Aftershave Balm"),
"8411061117071":("18","9.94","Antonio Banderas Essence of Success Eau de Toilette 100ml Spray"),
"8411061088593":("50","10.09","Antonio Banderas Her Secret Absolu Eau de Parfum 80ml Spray"),
"8411061081341":("50","10.09","Antonio Banderas King of Seduction Absolute Eau de Toilette 100ml Spray")}
json.dump(SUP,open('sup.json','w'),ensure_ascii=False)
NOTE_FIX={"0085715064752":"Photos attached 19/11.","8411061044995":"Photo rejected 19/11: source image (445x275) has a retailer 'perfume…' watermark and no box photo – please add a clean main.* (and box.*) photo."}
prod=[];ws=[];dsc=[];dp=[]
for i,(p,(pid,vid,iid)) in enumerate(zip(P,ids)):
    row=198+i; bc=p["bc"]; st,sp,name=SUP[bc]
    note=p["note"]
    if bc in NOTE_FIX: note=note.replace("Awaiting photos.",NOTE_FIX[bc])
    prod.append([p["status"],None,p["cat_name"],p["vendor"],p["title"],"",p["form"],p["size"],p["unit"],p["gender"],"'"+bc,"","","£"+p["price"],"£"+p["cmp"],"",p["qty"],"","","https://drive.google.com/drive/folders/"+FID[bc],"","","11/19/2026","https://admin.shopify.com/store/f1d55c-f7/products/"+pid,note])
    ws.append([name,str(p["qty"])])
    dsc.append(["'"+bc,name,p["title"],p["cat_name"],pid,vid,iid,st,p["qty"],sp,p["price"],p["cmp"],"DRAFT","Yes" if bc=="0085715064752" else "No","","Created 19/11/2026 run 3",row])
    dp.append(["drafted",pid,row,"attached" if bc=="0085715064752" else ("rejected – watermark on source photo, low resolution, no box photo" if bc=="8411061044995" else None)])
json.dump({"prod":prod,"ws":ws,"dsc":dsc,"dp":dp},open('records.json','w'),ensure_ascii=False)
print(json.dumps(prod,ensure_ascii=False));print(json.dumps(ws,ensure_ascii=False));print(json.dumps(dsc,ensure_ascii=False));print(json.dumps(dp,ensure_ascii=False))
