import json
P=json.load(open('P.json')); ids=json.load(open('ids.json'))
FID={"8054754400618":"1gMhHvESyf4jcf9ZJBB5A_wjLdbUpl1DT","8054754400625":"1Y3DYI13KEM2kxkB9BGeFsUZyxFaKZMtO","7640233340561":"1mzUYAxtDKktZ0v1awZEWlzbKIbqho3ik","7640233340745":"1Q9T8NKmPfprpXQkp8sq6_qrg7cz-_gIx","0085805255824":"1hll_gc0hYsVWYGQSrt5IMF107PioB1RU","0887167697232":"1tvhhtBKRmw-V-ux_8mkOvySP4rafIyO8","6291106484434":"1R3ZIlNxwD0-1SnafkISzoWtg8yRoMO6e","7640164030616":"1DE-UsHoEJn87FnKFD5wITAdTiVXhGxe_","3346130010630":"11UEjB5UGubBrXDUoOIV3TvRIUirD37jQ","3616304198007":"1H0DC3WclVmqpX89KQwk_wP6dPtYizy7C"}
SUP={"8054754400618":("50","42.50","Dolce & Gabbana K Gift Set 100ml EDP + 50ml After Shave Balm + 50ml Shower Gel"),
"8054754400625":("50","38.92","Dolce & Gabbana K Intense Gift Set - EDP Intense 100ml Spray +10ml EDP"),
"7640233340561":("50","26.14","Elie Saab Girl of Now Gift Set 50ml EDP + 75ml Body Lotion"),
"7640233340745":("50","29.50","Elie Saab Le Parfum Lumière Gift Set 50ml EDP + 10ml EDP"),
"0085805255824":("22","10.66","Elizabeth Arden Sunflowers Gift Set 100ml EDT + 100ml Body Lotion"),
"0887167697232":("50","49.00","Estée Lauder Beautiful Gift Set 75ml Eau de Parfum + 10ml Eau de Parfum + 75ml Body Lotion"),
"6291106484434":("1","12.06","French Avenue Black Kabul Eau de Parfum 60ml Spray"),
"7640164030616":("23","38.17","Gisada Ambassador Women Gift Set 50ml EDP + 100ml Shower Gel"),
"3346130010630":("28","49.63","Hermès Terre d'Hermès Gift Set 100ml EDT + 80ml Shower Gel"),
"3616304198007":("50","33.26","Hugo Boss The Scent for Her Gift Set 50ml EDP + 75ml Body Lotion")}
json.dump(SUP,open('sup.json','w'),ensure_ascii=False)
prod=[];ws=[];dsc=[];dp=[]
for i,(p,(pid,vid,iid)) in enumerate(zip(P,ids)):
    row=228+i; bc=p["bc"]; st,sp,name=SUP[bc]
    prod.append([p["status"],None,p["cat_name"],p["vendor"],p["title"],"",p["form"],p["size"],p["unit"],p["gender"],"'"+bc,"","","£"+p["price"],"£"+p["cmp"],"",p["qty"],"","","https://drive.google.com/drive/folders/"+FID[bc],"","","11/20/2026","https://admin.shopify.com/store/f1d55c-f7/products/"+pid,p["note"]])
    ws.append([name,str(p["qty"])])
    dsc.append(["'"+bc,name,p["title"],p["cat_name"],pid,vid,iid,st,p["qty"],sp,p["price"],p["cmp"],"DRAFT","No","","Created 20/11/2026 run 3",row])
    dp.append(["drafted",pid,row])
json.dump({"prod":prod,"ws":ws,"dsc":dsc,"dp":dp},open('records.json','w'),ensure_ascii=False)
print(json.dumps(prod,ensure_ascii=False))
