import json
P=json.load(open('P.json')); ids=json.load(open('ids.json')); sup=json.load(open('sup.json')); fid=json.load(open('fid.json'))
A=[];CY=[];WS=[];DS=[];DP=[]
for i,(p,(pid,vid,iid)) in enumerate(zip(P,ids)):
    row=452+i; n=lambda g:g.split('/')[-1]
    link="https://drive.google.com/drive/folders/"+fid[p['bc']]
    A.append([p['status']])
    CY.append([p['cat_name'],p['vendor'],p['title'],"",p['form'],p['size'],p['unit'],p['gender'],"'"+p['bc'],"","","£"+p['price'],"£"+p['cmp'],"",p['qty'],"","",link,"","","11/27/2026",
              "https://admin.shopify.com/store/f1d55c-f7/products/"+n(pid),p['note']])
    s=sup[p['bc']]
    WS.append([s[2],p['qty']])
    DS.append(["'"+p['bc'],s[2],p['title'],"Fragrance",n(pid),n(vid),n(iid),s[0],p['qty'],s[1],p['price'],p['cmp'],"DRAFT","No","","Created 27/11/2026 run 2",row])
    DP.append(["drafted",n(pid),row])
json.dump(dict(A=A,CY=CY,WS=WS,DS=DS,DP=DP),open('records.json','w'),ensure_ascii=False)
for k in "A CY WS DS DP".split(): print(k, json.dumps(locals()[k],ensure_ascii=False))
