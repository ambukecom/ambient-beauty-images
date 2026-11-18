import json
P=json.load(open('P.json')); ids=json.load(open('ids.json')); SUP=json.load(open('sup.json'))
FID={"6290362348061":"1IHLo0-AsmW3VoRTpX05FBB65ruxyp_Jj","6291107459240":"1mKVWsjGCp65vbkbgfsbbIuOibmyIz28x","6290362340164":"1GwbtxdBrHeHWjVGKt_oDxMEz-POf09iu","6290362341123":"18BCoR3KjVoJmgZU6YGMHQimWzpExhnNi","6291108736319":"1fIqEuWxscZLtbDxnPGFqyvUICHAHpz1s","0614514178010":"1JUgzLfVN0WQgEvb339u6exh_g9jZGJh7","0614514178065":"1flyOjCp7QgCKt6PimLIHGpRgUUj_sdNz","0614514331262":"1nsUHC7viW8SzsQT8CxgHjKG5Z1qFAiP2","6290171010487":"1Ir3kD_MKVr6svU-5CJVEZep1kHvKrfKz","6290171010456":"1whR7UrW89_Dp3qTILHiB85TQdTPQD1Om"}
prod=[];ws=[];dsc=[];dp=[]
for i,(p,(pid,vid,iid)) in enumerate(zip(P,ids)):
    row=158+i; bc=p["bc"]; st,sp,_,name=SUP[bc]
    prod.append([p["status"],None,p["cat_name"],p["vendor"],p["title"],"",p["form"],p["size"],p["unit"],p["gender"],"'"+bc,"","","£"+p["price"],"£"+p["cmp"],"",p["qty"],"","","https://drive.google.com/drive/folders/"+FID[bc],"","","11/18/2026","https://admin.shopify.com/store/f1d55c-f7/products/"+pid,p["note"]])
    ws.append([name,str(p["qty"])])
    dsc.append(["'"+bc,name,p["title"],p["cat_name"],pid,vid,iid,st,p["qty"],sp,p["price"],p["cmp"],"DRAFT","No","","Created 18/11/2026 run 3",row])
    dp.append(["drafted",pid,row])
json.dump({"prod":prod,"ws":ws,"dsc":dsc,"dp":dp},open('records.json','w'),ensure_ascii=False)
print(json.dumps(prod,ensure_ascii=False))
