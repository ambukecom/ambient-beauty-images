import json
P=json.load(open('P.json')); ids=json.load(open('ids.json')); sup=json.load(open('sup.json'))
links=["1ot-Q6LlSE6vaHkgVubU16byrq_n6BUzh","1YxpLbByTvmjNhVrLYdVyXSARpTLMiA2c","17qTjt9slikFVVtyNODBqDaqM_sP7tUBR","11Dur4RGNBJFT_-aLctgfKBKzmh3718Nq","1QSz3fWh-ba5NkyUvOa3Vvqln1FiYqF78","1xS0yiRXv_Y6jsQiVf5ZNT2-sLT_Pi712","14lBjLc-ndaxIjPo4wEGGPeZeOidzbHpa","1b76xR4H3fXMLuGMY8JLQUkOtGbcphznD","1uLiUO767NToueqXp_gCu1nEKGrJGr1Oc","1jxfAEB8l-w89pXJaG31yMJ1XaWraRtj6"]
A=[];CY=[];WS=[];DS=[];DP=[]
for i,(p,(pid,vid,iid)) in enumerate(zip(P,ids)):
    row=362+i; n=lambda g:g.split('/')[-1]
    link="https://drive.google.com/drive/folders/"+links[i]
    A.append([p['status']])
    CY.append([p['cat_name'],p['vendor'],p['title'],"",p['form'],p['size'],p['unit'],p['gender'],p['bc'],"","","£"+p['price'],"£"+p['cmp'],"",p['qty'],"","",link,"","","11/24/2026",
              "https://admin.shopify.com/store/f1d55c-f7/products/"+n(pid),p['note']])
    s=sup[p['bc']]
    WS.append([s[2],p['qty']])
    DS.append([p['bc'],s[2],p['title'],"Fragrance",n(pid),n(vid),n(iid),s[0],p['qty'],s[1],p['price'],p['cmp'],"DRAFT","No","","Created 24/11/2026 run 4",row])
    DP.append(["drafted",n(pid),row])
json.dump(dict(A=A,CY=CY,WS=WS,DS=DS,DP=DP),open('records.json','w'),ensure_ascii=False)
print(json.dumps(A)); print(json.dumps(CY,ensure_ascii=False)); print(json.dumps(WS,ensure_ascii=False)); print(json.dumps(DS,ensure_ascii=False)); print(json.dumps(DP))
