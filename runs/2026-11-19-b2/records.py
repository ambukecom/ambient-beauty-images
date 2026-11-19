import json
P=json.load(open('P.json')); ids=json.load(open('ids.json'))
FID={"0085715166685":"1chfwHt8Oham6G35CNL1IxeKLLxhdaeWm","0085715167507":"18jn9vtKiIOlu0Y0VdPtxpg1a6xvOnbpL","0085715167316":"19qA94w4Ck8j6I2QHwQX2IsYjxtfayymD","0085715163394":"173TIglH0dj60WnwbdoiN3aTO2zITCakb","3616305447111":"1eHFvXmZ8e0GJYwmUkRQUw5rZpP3VuznR","3616305447043":"1R5h7oRbspYaWxZBcLCw6oWTeuQK1ASHa","3616305447098":"1VxqJJ8e8Sj3EnrMvAg9VTfSryAe-_k3z","3616305447241":"1rvwsX5UjMhtLP8WKfmJvx7FIMYEJWPqO","3616303322021":"1XRSQbS5XS2Dc6MDQxRlujODqvxBFluHB","3616305447203":"1My9chvHH9FZc96awdHHR6P8aHJLHz7rP"}
SUP={"0085715166685":("50","27.56","Abercrombie & Fitch Fierce Gift Set 100ml EDC + 10ml EDC"),
"0085715167507":("45","19.64","Abercrombie & Fitch First Extreme Instinct Eau de Parfum 100ml Spray"),
"0085715167316":("50","11.29","Abercrombie & Fitch First Instinct Blue for Her Gift Set 50ml EDP + 200ml Body Lotion"),
"0085715163394":("50","15.42","Abercrombie & Fitch First Instinct Gift Set 100ml EDT + 200ml Body Wash"),
"3616305447111":("50","5.76","Adidas Chill Zone Eau de Parfum 50ml Spray"),
"3616305447043":("50","5.76","Adidas Energy Drive Eau de Parfum 50ml Spray"),
"3616305447098":("50","5.76","Adidas Full Recharge Eau de Parfum 50ml Spray"),
"3616305447241":("50","5.76","Adidas Get Comfy Eau de Parfum 50ml Spray"),
"3616303322021":("50","3.92","Adidas Pure Game Eau de Toilette 100ml Spray"),
"3616305447203":("50","5.76","Adidas Spark Up Eau de Parfum 50ml Spray")}
json.dump(SUP,open('sup.json','w'),ensure_ascii=False)
# Daily Plan order (rows 72-81) by barcode
DP_ORDER=["0085715166685","0085715167507","0085715167316","0085715163394","3616305447111","3616305447043","3616305447098","3616305447241","3616303322021","3616305447203"]
prod=[];ws=[];dsc=[];row_of={}
for i,(p,(pid,vid,iid)) in enumerate(zip(P,ids)):
    row=188+i; bc=p["bc"]; st,sp,name=SUP[bc]; row_of[bc]=(pid,row)
    prod.append([p["status"],None,p["cat_name"],p["vendor"],p["title"],"",p["form"],p["size"],p["unit"],p["gender"],"'"+bc,"","","£"+p["price"],"£"+p["cmp"],"",p["qty"],"","","https://drive.google.com/drive/folders/"+FID[bc],"","","11/19/2026","https://admin.shopify.com/store/f1d55c-f7/products/"+pid,p["note"]])
    ws.append([name,str(p["qty"])])
    dsc.append(["'"+bc,name,p["title"],p["cat_name"],pid,vid,iid,st,p["qty"],sp,p["price"],p["cmp"],"DRAFT","No","","Created 19/11/2026 run 2",row])
dp=[["drafted",row_of[b][0],row_of[b][1]] for b in DP_ORDER]
json.dump({"prod":prod,"ws":ws,"dsc":dsc,"dp":dp},open('records.json','w'),ensure_ascii=False)
print(json.dumps(prod,ensure_ascii=False));print(json.dumps(ws,ensure_ascii=False));print(json.dumps(dsc,ensure_ascii=False));print(json.dumps(dp))
