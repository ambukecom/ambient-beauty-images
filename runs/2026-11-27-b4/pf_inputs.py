import json
SH="https://admin.shopify.com/store/f1d55c-f7/products/"; DR="https://drive.google.com/drive/folders/"
F=json.load(open('fix_products.json'))
res={i['barcode']:sorted(i['images']) for i in json.load(open('../../results/2026-11-27-b4-fixes.json'))['items']}
FOLD={"0085715163394":"173TIglH0dj60WnwbdoiN3aTO2zITCakb","0738678000991":"1d5YjF8HgyQ4B0GyhWnyv_z0o-YM5jlh4","0738678001042":"1es_fDYyBk5cpYtVE_f3Yn8gl_rEgsSd1","6290361915912":"1YS1mLt_2e2H6sTBuoFiHjS2sWP_LBoa5","6294015176100":"1mgveBIc8lQhQXAtEfNmUOXcOYwi7hco2","4051395412110":"1ZfYahWwGP8C_X0GR_IualbICfC1aUcm5","9362014000140":"1bLMblRSi0U2VlU_hwsz8cs7fCWud-BFQ","3616304197420":"1n3bosWWFP897t7AagXF7OGzZPQ6BPUpa","3423473997658":"1T6x1euJIpEoMkTZzeAIXAKSFEqHV1-b_","3454960007468":"1WHd_3nC1Z43zNfnbwpSKaOtDE5wIkl56","0856857007101":"1ZnVkCw_WvUXA-HC0Txk4EYmQp1jXHpe5","6290360591551":"1jmyhReRfFVD-EFls7AHQdCoaOc0gOPVO","6290360599243":"1HXLQGugxNjhYXYEklA9JS1fI1u3kx07D","6290362343196":"1oKhJYOYEl3BzljDrjwjcpJFr3j6tAe24","3607349764289":"14CsQKwEVTOiMe7GlCXauC_RQIx5ai60J","3616302025930":"18ypoeaFmRVlGaxeFHbHWTkW0Fq1z2Sp0","3595471041012":"1-Qd3XFLJfLyMXrkdJhbstAWzCEp7kOJI","3595471061096":"1fyERhq3Uggr1YvKbfSqFlvQ53nvon-hb","3595471023001":"1jEhd6ZtRB8JQoXUsBxVk-rbtL1r0RHQX","0850050174691":"1-d_QjcMJAY_csZ6gcXpGFDkwE1Stip2O","3386460167048":"1CAP48U5tJDrznbngHbPEomwwWNI1kEid","3386460139373":"12MPNq2yGIbPWep2bX6H-cc3PTCLJn1V9","0679602793643":"1UmQo6_XMQqJQqt9TrvQ8XD2oKh71pTMC","3360377022928":"16h13CLkGc5miJTiMHb8FTRyYpmCm1iaS","5060412678872":"19-9rPSue-f4m8L1UAEDdcV9oB5uYt_nJ","5060523017997":"1TfPBNEj9D76VXvGOiqIx_rFA_hbd_RWz","0810101500060":"1XUgTSenYNQ6HnI4bsy1AaCB4ys-RoEso","3474636976058":"16aZXrL9BmRDyOUhIcCnGC0q_zD8UPjZe","5030805002829":"1tO4jGNYHgvrX1WXMBAnBt7G-aYBMF37W","6298042001244":"1i0xy1_spNo66BQYaKH4eV3eAjmN3Umnz","6281085039978":"1QoLohapXcOw3I8C0-ll0vaOHXcfItmDT","6290362348078":"12zjPXy-rfGz2Jbh0GRkxJrFrYTVghRNu","3614274797213":"1zuX1HjAkc3UTTru5j04w4ZVBVPS2AZ5h","3614274797244":"1M60w_RtnEUQLNGC6vPwBUvZfYOXqiW3C","3614274797220":"11rWzMhJbnUncAGqb9vzjru5-aTVlLkAi","8411061044995":"12cFIAKVSeA0R2jUOWB5Z6_PbMNHPLyiL","3614274026511":"1DURuH33mnSGq-kQkU2UW8aA54SMpFTK-","3666057165580":"1tBf4lTvMa2lPXhNzfCDhyJSzFLOhucek","3274872472891":"1KaovcX-nEzFlM5nPJZBGqJHcZsj79WyV"}
json.dump(FOLD,open('fix_folders.json','w'))
prod=[];plan=[["h"]];ex=[["note"],["hdr"]]
def P(bc,title,fold,pid): r=[""]*25; r[4]=title; r[10]="'"+bc; r[19]=DR+fold; r[23]=SH+pid; prod.append(r)
def D(bc,m): r=[""]*14; r[6]=bc; r[12]=m; plan.append(r)
def E(bc,tick,k=""): r=[""]*11; r[0]="TRUE" if tick else "FALSE"; r[4]="'"+bc; r[10]=k; ex.append(r)
for l in open('pf_keep.tsv'):
    t,c,bc,title,fold,pid=l.rstrip('\n').split('\t'); P(bc,title,fold,pid); D(bc,"rejected – "+c); E(bc,t=="T")
done=[]
for bc,v in F.items():
    im=res[bc]
    if len(im)==1:
        miss="box" if im[0]=="main" else "main"
        P(bc,v[2],FOLD[bc],v[0]); D(bc,f"rejected – no {miss} photo in folder ({im[0]} photo uploaded 27/11, owner-approved)")
        E(bc,False,f"Uploaded 27/11: {im[0]} photo only – add {miss}.jpg")
    det={2:"Main + box uploaded",1:("Main" if im==["main"] else "Box")+" photo uploaded (only one in folder)"}[len(im)]
    done.append({"date":"27/11/2026","barcode":bc,"title":v[2],"folder":DR+FOLD[bc],"shopify":SH+v[0],
                 "status":{"DRAFT":"Draft","UNLISTED":"Unlisted","ACTIVE":"Active"}[v[3]],"photos":len(im),"detail":det})
B4=json.load(open('P.json')); ids=json.load(open('ids.json')); fid=json.load(open('fid.json'))
M={"3423222080952":"rejected – main photo is a cropped close-up of the bottle top; no box photo in folder",
   "3423222108373":"attached (box only)","3423222092528":"attached (box only)","3423478925557":"attached","3423222107611":"attached (main only)",
   "3423222107727":"rejected – main and box photos show Bvlgari Pour Homme, not Narciso Rodriguez Vetiver Musc",
   "0608940583562":"rejected – box photo cut-out broken (only fragments of box and cap); no main photo in folder","0608940575307":"attached (box only)"}
for p,i in zip(B4,ids):
    P(p['bc'],p['title'],fid[p['bc']],i[0].split('/')[-1]); D(p['bc'],M[p['bc']])
json.dump({"values":prod},open('pf_prod.json','w'),ensure_ascii=False); json.dump({"values":plan},open('pf_plan.json','w'),ensure_ascii=False)
json.dump({"values":ex},open('pf_existing.json','w'),ensure_ascii=False); json.dump(done,open('pf_done_new.json','w'),ensure_ascii=False,indent=0)
print(len(prod),len(done))
