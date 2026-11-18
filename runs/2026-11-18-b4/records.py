import json
P=json.load(open('P.json')); ids=json.load(open('ids.json')); SUP=json.load(open('sup.json'))
FID={"6298042001251":"1O2rHFI_CcAZIWBMV1eli7aQfQBiWB14h","6290360379869":"18M-KRvpkxh_Y7INgax3fdJtvzIViqLFW","6290360379845":"1Wd6K62y2T3Q8g_O54WfyeV75G93bLxj6","6298042001459":"1YvtBf_kLw2LH29DCBkjf3wxJMXvJPm6T","6298042001329":"1WCSP_2VPzUaN-0S1SqyqSjtH8EqoycWB","6290360379746":"1nV5Ali8fKdlATzwRXPAilhb-zwijLEKb","6290360379760":"1BTlRrICoRunzVfeq_6rZNEK0yDCs1j4z","6290360379838":"1q69xjbwwSPrhn08GXM3-FuQHAXc6G0PI","6298042001466":"1FmGtV8iZK4NKMBkbHLJf5FENKVpQ3oC4","6298042001336":"1tibyT3Zns-3iedpm1gDYwuCG32SindDJ"}
prod=[];ws=[];dsc=[];dp=[]
for i,(p,(pid,vid,iid)) in enumerate(zip(P,ids)):
    row=168+i; bc=p["bc"]; st,sp,name=SUP[bc]
    prod.append([p["status"],None,p["cat_name"],p["vendor"],p["title"],"",p["form"],p["size"],p["unit"],p["gender"],"'"+bc,"","","£"+p["price"],"£"+p["cmp"],"",p["qty"],"","","https://drive.google.com/drive/folders/"+FID[bc],"","","11/18/2026","https://admin.shopify.com/store/f1d55c-f7/products/"+pid,p["note"]])
    ws.append([name,str(p["qty"])])
    dsc.append(["'"+bc,name,p["title"],p["cat_name"],pid,vid,iid,st,p["qty"],sp,p["price"],p["cmp"],"DRAFT","No","","Created 18/11/2026 run 4",row])
    dp.append(["drafted",pid,row])
json.dump({"prod":prod,"ws":ws,"dsc":dsc,"dp":dp},open('records.json','w'),ensure_ascii=False)
print(json.dumps(prod,ensure_ascii=False))
