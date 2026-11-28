import json
P=json.load(open('P.json')); ids=json.load(open('ids.json'))
fid={"3614228890137":"152XnZs0JQAXwIJk4iY6UK-I5tSoJpBxn","3616302038916":"14qTNaS4F11simyc6Jt6pM73nkCKP_wwJ",
"3386460137386":"1KR3h-giG0HN42vc0Qcn4sa-jBkXO6h1U","3386460136754":"1k1dVKQvrIGtnw1GhNoLUFLDefkuFVTOd",
"8052086376496":"1rSrHtjRCVzFNtLHWEokO3_lbnJPbWJDp","8052086376533":"1n1Pz0Vo2-rMEOJkdNu3u8WEJWnOjseg-",
"8052464892174":"1FDNqHc1OWM-IHZh8XuLK80RuYtgamYxb","8034097950025":"1S087H8EXKTZBauJTCFXK3uHxM4bhgcIi",
"8056860210853":"1mj9k-yPoxeYga69pZubmGwA9axsrBkpf","8034097956027":"150gEFHGv81pFSdb5BNXhI-SRUtwk_uwG"}
sup={"3614228890137":["50","53.21","Roberto Cavalli Sublime Tonka Eau de Parfum 100ml Spray"],
"3616302038916":["50","53.21","Roberto Cavalli Woodiris Eau de Parfum 100ml Spray"],
"3386460137386":["50","29.78","Rochas Girl Life Eau de Parfum 150ml Refill"],
"3386460136754":["50","22.89","Rochas Man Intense Eau de Parfum 100ml Spray"],
"8052086376496":["21","23.97","Salvatore Ferragamo Amo Ferragamo Flowerful Eau de Toilette 100ml Spray"],
"8052086376533":["50","16.51","Salvatore Ferragamo Amo Ferragamo Flowerful Gift Set 50ml EDT Spray + 100ml Body Lotion"],
"8052464892174":["43","23.97","Salvatore Ferragamo Amo Ferragamo Oriental Wood Eau de Parfum 100ml Spray"],
"8034097950025":["24","17.47","Salvatore Ferragamo F by Ferragamo Free Time Eau de Toilette 100ml Spray"],
"8056860210853":["46","30.47","Salvatore Ferragamo Ferragamo Intense Leather Eau de Parfum 100ml Spray"],
"8034097956027":["30","14.22","Salvatore Ferragamo Incanto Bloom (2014) Eau de Toilette 100ml Spray"]}
json.dump(sup,open('sup.json','w'),indent=0); json.dump(fid,open('fid.json','w'))
A=[];CY=[];WS=[];DS=[];DP=[]
for i,(p,(pid,vid,iid)) in enumerate(zip(P,ids)):
    row=500+i; n=lambda g:g.split('/')[-1]
    link="https://drive.google.com/drive/folders/"+fid[p['bc']]
    A.append([p['status']])
    CY.append([p['cat_name'],p['vendor'],p['title'],"",p['form'],p['size'],p['unit'],p['gender'],"'"+p['bc'],"","","£"+p['price'],"£"+p['cmp'],"",p['qty'],"","",link,"","","11/28/2026",
              "https://admin.shopify.com/store/f1d55c-f7/products/"+n(pid),p['note']])
    s=sup[p['bc']]
    WS.append([s[2],p['qty']])
    DS.append(["'"+p['bc'],s[2],p['title'],"Fragrance",n(pid),n(vid),n(iid),s[0],p['qty'],s[1],p['price'],p['cmp'],"DRAFT","No","","Created 28/11/2026 run 3",row])
    DP.append(["drafted",n(pid),row])
json.dump(dict(A=A,CY=CY,WS=WS,DS=DS,DP=DP),open('records.json','w'),ensure_ascii=False)
for k in "A CY WS DS DP".split(): print(k, json.dumps(locals()[k],ensure_ascii=False))
