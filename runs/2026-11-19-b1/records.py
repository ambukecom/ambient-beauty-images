import json
from plan import FID
P=json.load(open('P.json')); ids=json.load(open('ids.json'))
SUP={"3616305181381":("50","44.15","Marc Jacobs Daisy Gift Set 100ml EDT + 75ml Body Lotion"),
"0679602793643":("34","9.73","Police To Be Camouflage Gift Set 75ml EDT + 100ml Shower Gel"),
"0085715166708":("50","20.85","Abercrombie & Fitch 100% Passion Man Eau de Toilette 100ml Spray"),
"0085715166494":("50","20.85","Abercrombie & Fitch 100% Passion Woman Eau de Parfum 100ml Spray"),
"0085715166425":("50","16.51","Abercrombie & Fitch Authentic Night Gift Set 100ml EDT + 15ml EDT"),
"0085715166517":("50","18.41","Abercrombie & Fitch Authentic Woman Eau de Parfum 100ml Spray"),
"0085715164179":("50","16.51","Abercrombie & Fitch Away Man Gift Set 50ml EDT + 200ml Hair & Body Wash"),
"0085715169303":("50","13.55","Abercrombie & Fitch Away Tonight Man Eau de Toilette 100ml Spray"),
"0085715169563":("50","8.84","Abercrombie & Fitch Fierce Eau de Cologne 30ml Spray"),
"0085715169570":("50","12.92","Abercrombie & Fitch Fierce Eau de Cologne 50ml Spray")}
json.dump(SUP,open('sup.json','w'),ensure_ascii=False)
prod=[];ws=[];dsc=[];dp=[]
for i,(p,(pid,vid,iid)) in enumerate(zip(P,ids)):
    row=178+i; bc=p["bc"]; st,sp,name=SUP[bc]
    prod.append([p["status"],None,p["cat_name"],p["vendor"],p["title"],"",p["form"],p["size"],p["unit"],p["gender"],"'"+bc,"","","£"+p["price"],"£"+p["cmp"],"",p["qty"],"","","https://drive.google.com/drive/folders/"+FID[bc],"","","11/19/2026","https://admin.shopify.com/store/f1d55c-f7/products/"+pid,p["note"]])
    ws.append([name,str(p["qty"])])
    dsc.append(["'"+bc,name,p["title"],p["cat_name"],pid,vid,iid,st,p["qty"],sp,p["price"],p["cmp"],"DRAFT","No","","Created 19/11/2026 run 1",row])
    dp.append(["drafted",pid,row])
json.dump({"prod":prod,"ws":ws,"dsc":dsc,"dp":dp},open('records.json','w'),ensure_ascii=False)
print(json.dumps(prod,ensure_ascii=False))
