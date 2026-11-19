import json
P=json.load(open('P.json')); ids=json.load(open('ids.json'))
FID={"8411061081846":"1hLq9tMCIZOBo7RLzu-JDGZoVYYOPxUSv","6423080724118":"10VKNtoAg6VEHCxInkrBn2UXwd64WWHRp","0810101500060":"1XUgTSenYNQ6HnI4bsy1AaCB4ys-RoEso","6294015165036":"19D-O5bP6kSpyKi5oBPkbC56j8V2Fjdwc","6294015101379":"1Ipz_k-uOrBRm2wAOyIRNIOuaQS6eDyWH","3614274098440":"1zXqn4CJpT_O_tBNDxG0XXlPVYjUU1A46","3614273962391":"1icSF2ktumwqCROCnIJyQn6P_a0Kl93OG","7640171193403":"1YMzBTuST7w5VyYCRzKO3si62OSPJ6rsk","7640163970029":"1K10JI7VVmkHTAvUAellvTqhlGFA9DkaW","0719346567442":"1a_QbU3Nfg09si3-F0VdkUi4usNKwUq6c"}
SUP={"8411061081846":("50","10.09","Antonio Banderas Queen of Seduction Eau de Toilette 80ml Spray"),
"6423080724118":("31","14.34","Ard Al Zaafaran Turab Al Dhahab Gift Set 100ml EDP + 250ml Body Mist + 300ml Air Freshener"),
"0810101500060":("3","33.66","Ariana Grande Mod Blush Eau de Parfum 100ml Spray"),
"6294015165036":("2","18.26","Armaf L'Homme Parfum Intense Eau de Parfum 100ml Spray"),
"6294015101379":("47","11.17","Armaf Signature True Eau de Parfum 100ml Spray"),
"3614274098440":("50","22.24","Azzaro Chrome Azure Eau de Parfum 100ml"),
"3614273962391":("50","17.87","Azzaro Chrome Legend Eau de Toilette 100ml Spray"),
"7640171193403":("50","20.72","Bentley For Men Silverlake Eau de Parfum 100ml Spray"),
"7640163970029":("50","17.54","Bentley Infinite Intense Eau de Parfum 100ml Spray"),
"0719346567442":("50","11.28","Britney Spears Circus Fantasy Eau de Parfum 100ml Spray")}
json.dump(SUP,open('sup.json','w'),ensure_ascii=False)
prod=[];ws=[];dsc=[];dp=[]
for i,(p,(pid,vid,iid)) in enumerate(zip(P,ids)):
    row=208+i; bc=p["bc"]; st,sp,name=SUP[bc]
    prod.append([p["status"],None,p["cat_name"],p["vendor"],p["title"],"",p["form"],p["size"],p["unit"],p["gender"],"'"+bc,"","","£"+p["price"],"£"+p["cmp"],"",p["qty"],"","","https://drive.google.com/drive/folders/"+FID[bc],"","","11/19/2026","https://admin.shopify.com/store/f1d55c-f7/products/"+pid,p["note"]])
    ws.append([name,str(p["qty"])])
    dsc.append(["'"+bc,name,p["title"],p["cat_name"],pid,vid,iid,st,p["qty"],sp,p["price"],p["cmp"],"DRAFT","No","","Created 19/11/2026 run 4",row])
    dp.append(["drafted",pid,row])
json.dump({"prod":prod,"ws":ws,"dsc":dsc,"dp":dp},open('records.json','w'),ensure_ascii=False)
print(json.dumps(prod,ensure_ascii=False));print(json.dumps(ws,ensure_ascii=False));print(json.dumps(dsc,ensure_ascii=False));print(json.dumps(dp))
