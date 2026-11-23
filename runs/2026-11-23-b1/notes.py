import json,sys
Y=json.loads(sys.stdin.read())['values']
st=json.load(open('photo_mut.json'))['status']
rows=list(range(279,287))+list(range(302,312))
bcs=["6281085040011","6281085039657","6281085040059","6295124002236","6295124051456","6295124030581","6295124030253","6295124053269","3616304679483","0783320421211","0783320422393","3614273843195","3614274026511","3616303455309","8411061074855","8411061027981","5050456007387","5050456005680"]
allY={279+i:r[0] for i,r in enumerate(Y)}
out={};dpm={}
for row,bc in zip(rows,bcs):
    n,rej,miss=st[bc]
    miss=[("no main photo in folder" if "main" in m else "no box photo in folder") for m in miss]
    extra="; ".join(rej+miss)
    if n:
        txt="Photos attached 23/11"+(f" ({'box photo only' if all('main' in x for x in rej+miss if 'main' in x) and not any('box' in x for x in rej+miss) and (rej+miss) else ''}" if False else "")
        if extra: txt=f"Photos attached 23/11 ({extra})."; m=f"attached ({extra})"
        else: txt="Photos attached 23/11."; m="attached"
    else:
        txt=f"Photos rejected 23/11: {extra} – please replace them. Awaiting photos."; m=f"rejected – {extra}"
    assert "Awaiting photos." in allY[row], row
    out[row]=allY[row].replace("Awaiting photos.",txt,1); dpm[bc]=m
json.dump({"Y":out,"M":dpm},open('photo_notes.json','w'),ensure_ascii=False,indent=0)
for r,v in out.items(): print(r, v[-170:])
