import json
P=json.load(open('P.json')); ids=json.load(open('ids.json'))
fid={"8436581946246":"1gdtBTonSlAp6nf_ZHPpFvf-zYpfjcuvS","8436581946253":"1T3yFh304Z_vakT2YngtUnktyMmmX1cDW",
"3616302038909":"1UY2_eY3UGl3Hxvo15qwtAyoP_j2hZuGY","3616303470654":"1s9F1LuClNjfvCUKh98XDn3IfpjLNu-Su",
"8052464899104":"13cguwcNUDOFv352uPN1BgoG4zOsIGZNH","3616302038961":"1oaVyPomPowC4JX9P6FrT_hPmuA6b6JIS",
"3616303445232":"1-PuJKwGT7088Xtrk0tXrkpoowKkx602i","8052464896868":"1V1uveHqSoSpHEF5EYQReaT_6sf8reO2e",
"3616304668722":"16KV6YuCBDL4469P5KvWbDX1OAfNzeDBN","8056860214660":"1xhcHoBaeWzCE7QXPp4W0vsGiDMmtHACk"}
sup={"8436581946246":["50","7.13","Reebok Cool Your Body Women Gift Set 100ml EDT + 150ml Body Spray"],
"8436581946253":["50","8.25","Reebok Inspire Your Mind Woman Gift Set 100ml EDT + 150ml Body Spray"],
"3616302038909":["50","53.21","Roberto Cavalli Bloodiris Eau de Parfum 100ml Spray"],
"3616303470654":["50","53.21","Roberto Cavalli Divine Oud Eau de Parfum Intense 100ml Spray"],
"8052464899104":["50","15.31","Roberto Cavalli Just Cavalli Eau de Toilette 90ml Spray"],
"3616302038961":["50","53.21","Roberto Cavalli Magnetic Guaiac Eau de Parfum 100ml Spray"],
"3616303445232":["40","22.89","Roberto Cavalli Paradiso Assoluto Eau de Parfum 100ml Spray"],
"8052464896868":["47","20.80","Roberto Cavalli Paradiso Assoluto Eau de Parfum 75ml Spray"],
"3616304668722":["50","53.21","Roberto Cavalli Royal Soul Eau de Parfum 100ml Spray"],
"8056860214660":["49","20.72","Roberto Cavalli Signature Verde Assoluto Eau de Parfum 75ml"]}
json.dump(sup,open('sup.json','w'),indent=0); json.dump(fid,open('fid.json','w'))
A=[];CY=[];WS=[];DS=[];DP=[]
for i,(p,(pid,vid,iid)) in enumerate(zip(P,ids)):
    row=490+i; n=lambda g:g.split('/')[-1]
    link="https://drive.google.com/drive/folders/"+fid[p['bc']]
    A.append([p['status']])
    CY.append([p['cat_name'],p['vendor'],p['title'],"",p['form'],p['size'],p['unit'],p['gender'],"'"+p['bc'],"","","£"+p['price'],"£"+p['cmp'],"",p['qty'],"","",link,"","","11/28/2026",
              "https://admin.shopify.com/store/f1d55c-f7/products/"+n(pid),p['note']])
    s=sup[p['bc']]
    WS.append([s[2],p['qty']])
    DS.append(["'"+p['bc'],s[2],p['title'],"Fragrance",n(pid),n(vid),n(iid),s[0],p['qty'],s[1],p['price'],p['cmp'],"DRAFT","No","","Created 28/11/2026 run 2",row])
    DP.append(["drafted",n(pid),row])
json.dump(dict(A=A,CY=CY,WS=WS,DS=DS,DP=DP),open('records.json','w'),ensure_ascii=False)
for k in "A CY WS DS DP".split(): print(k, json.dumps(locals()[k],ensure_ascii=False))
