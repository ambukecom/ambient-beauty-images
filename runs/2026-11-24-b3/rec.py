import json
P=json.load(open('P.json')); ids=json.load(open('ids.json')); sup=json.load(open('sup.json'))
links=["1snT7Hk3Nph5zG7lX_LfKWb5JosZB5fq8","1Hqi_edw_268NVKlvstcES9kLDEIfebI-","1T6x1euJIpEoMkTZzeAIXAKSFEqHV1-b_","1anrivvVcTwns7CDdPB21rCaNFkMw2kxC","1YAxLj7h17G4bzhNBsi38_HVhdcDxkBfS","1vzyS9NX17cP7aGYKBSV852eElLQPHPI1","1TAW0b7U2-0d7LLYMmasawV3qD1WqgYvi","1wZh9_nWwps84YME5QhuDeViMa4ObTaby","1L08U7lSOVAC_nwvZyuJjC1H09d3m76PF","1SNUUaNnxGTJ503jrJ9DpEQGmC_9uP2dt"]
A=[];CY=[];WS=[];DS=[];DP=[]
for i,(p,(pid,vid,iid)) in enumerate(zip(P,ids)):
    row=352+i; n=lambda g:g.split('/')[-1]
    link="https://drive.google.com/drive/folders/"+links[i]
    A.append([p['status']])
    CY.append([p['cat_name'],p['vendor'],p['title'],"",p['form'],p['size'],p['unit'],p['gender'],p['bc'],"","","£"+p['price'],"£"+p['cmp'],"",p['qty'],"","",link,"","","11/24/2026",
              "https://admin.shopify.com/store/f1d55c-f7/products/"+n(pid),p['note']])
    s=sup[p['bc']]
    WS.append([s[2],p['qty']])
    DS.append([p['bc'],s[2],p['title'],"Fragrance",n(pid),n(vid),n(iid),s[0],p['qty'],s[1],p['price'],p['cmp'],"DRAFT","No","","Created 24/11/2026 run 3",row])
    DP.append(["drafted",n(pid),row])
json.dump(dict(A=A,CY=CY,WS=WS,DS=DS,DP=DP),open('records.json','w'),ensure_ascii=False)
print(json.dumps(A)); print(json.dumps(WS,ensure_ascii=False)); print(json.dumps(DS,ensure_ascii=False)); print(json.dumps(DP))
