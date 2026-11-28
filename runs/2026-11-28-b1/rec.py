import json
P=json.load(open('P.json')); ids=json.load(open('ids.json')); fid=json.load(open('fid.json'))
sup={"0679602549646":["50","7.56","Police Amber Gold for Women Gift Set 100ml EDT + 125ml Body Lotion"],
"0679602221108":["48","9.61","Police Contemporary Deep Blue Eau de Toilette 100ml"],
"0679602201018":["50","8.53","Police Contemporary Extreme Eau De Toilette 100ml"],
"0679602001472":["50","7.71","Police Contemporary Love Cherry Eau de Toilette 100ml Spray"],
"0679602161107":["50","6.84","Police Dark Women Eau de Toilette 100ml Spray"],
"0679602591010":["50","8.25","Police Silver Allure Man Eau de Toilette 100ml Spray"],
"0679602001458":["50","9.01","Police Wild Night Eau de Toilette 100ml Spray"],
"5050456101207":["50","14.93","Porche Design Porche Titan Eau de Toilette 50ml Spray"],
"3360377032767":["50","33.83","Ralph Lauren Polo Black Eau de Toilette 125ml Spray"],
"6297001571330":["50","16.73","Rayhaan Aquatica Eau de Parfum 100ml Spray"]}
json.dump(sup,open('sup.json','w'),indent=0)
A=[];CY=[];WS=[];DS=[];DP=[]
for i,(p,(pid,vid,iid)) in enumerate(zip(P,ids)):
    row=480+i; n=lambda g:g.split('/')[-1]
    link="https://drive.google.com/drive/folders/"+fid[p['bc']]
    A.append([p['status']])
    CY.append([p['cat_name'],p['vendor'],p['title'],"",p['form'],p['size'],p['unit'],p['gender'],"'"+p['bc'],"","","£"+p['price'],"£"+p['cmp'],"",p['qty'],"","",link,"","","11/28/2026",
              "https://admin.shopify.com/store/f1d55c-f7/products/"+n(pid),p['note']])
    s=sup[p['bc']]
    WS.append([s[2],p['qty']])
    DS.append(["'"+p['bc'],s[2],p['title'],"Fragrance",n(pid),n(vid),n(iid),s[0],p['qty'],s[1],p['price'],p['cmp'],"DRAFT","No","","Created 28/11/2026 run 1",row])
    DP.append(["drafted",n(pid),row])
json.dump(dict(A=A,CY=CY,WS=WS,DS=DS,DP=DP),open('records.json','w'),ensure_ascii=False)
for k in "A CY WS DS DP".split(): print(k, json.dumps(locals()[k],ensure_ascii=False))
