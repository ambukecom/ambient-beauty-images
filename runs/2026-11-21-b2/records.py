import json,sys
P=json.load(open('P.json')); ids=json.load(open('ids.json')); FID=json.load(open('fid.json'))
SUP=json.load(open('sup_all.json'))
SUP.update({"0850050174301":["50","39.52","Michael Kors Gorgeous! Gift Set 100ml EDP + 100ml Body Lotion + 100ml Shower Gel + 10ml EDP"],
"0850050174349":["50","53.00","Michael Kors Pour Femme Gift Set 100ml EDP + 100ml Body Lotion + 100ml Shower Gel + 10ml EDP"],
"3386460130349":["50","33.26","Mont Blanc Legend Gift Set 100ml EDT + 100ml Shower Gel + 7.5ml EDT"],
"3386460133777":["50","19.75","Mont Blanc Legend Red Gift Set 50ml EDP + 100ml Shower Gel"],
"0849017007639":["50","9.73","Mustang Blue Gift Set 100ml EDT + 100ml Aftershave Balm + 100ml Hair & Body Wash"],
"3423222092726":["26","52.36","Narciso Rodriguez Bleu Noir Gift Set 100ml EDP + 10ml EDP + 50ml Shower Gel"]})
json.dump(SUP,open('sup.json','w'),ensure_ascii=False)
start=int(sys.argv[1])
prod=[];ws=[];dsc=[];dp=[]
for i,(p,(pid,vid,iid)) in enumerate(zip(P,ids)):
    row=start+i; bc=p["bc"]; st,sp,name=SUP[bc]
    prod.append([p["status"],None,p["cat_name"],p["vendor"],p["title"],"",p["form"],p["size"],p["unit"],p["gender"],"'"+bc,"","","£"+p["price"],"£"+p["cmp"],"",p["qty"],"","","https://drive.google.com/drive/folders/"+FID[bc],"","","11/21/2026","https://admin.shopify.com/store/f1d55c-f7/products/"+pid,p["note"]])
    ws.append([name,str(p["qty"])])
    dsc.append(["'"+bc,name,p["title"],p["cat_name"],pid,vid,iid,st,p["qty"],sp,p["price"],p["cmp"],"DRAFT","No","","Created 21/11/2026 run 2",row])
    dp.append(["drafted",pid,row])
json.dump({"prod":prod,"ws":ws,"dsc":dsc,"dp":dp},open('records.json','w'),ensure_ascii=False)
