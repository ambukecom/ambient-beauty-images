import json
F=json.load(open('fix_products.json'))
M={"3454960007468":"75594695147860","0856857007101":"75594695115092","6290360591551":"75594694623572","6290360599243":"75594695999828","6290362343196":"75594694295892","3607349764289":"75594696687956","3616302025930":"75594696491348","3595471041012":"75594696950100","3595471061096":"75594694787412","3595471023001":"75594694754644","0850050174691":"75594696982868","3386460167048":"75594696458580","3386460139373":"75594696720724","0679602793643":"75316369195348","3360377022928":"75594696589652","5060412678872":"75316380631380","5060523017997":"75440285417812","3474636976058":"75253471936852","5030805002829":"75229824483668","6298042001244":"75229161914708","3274872472891":"75533762199892"}
json.dump(M,open('fix_old_media.json','w'))
det=",".join(f'{{id:"gid://shopify/MediaImage/{m}",referencesToRemove:["gid://shopify/Product/{F[b][0]}"]}}' for b,m in M.items())
open('detach_mut.txt','w').write(f'mutation{{ fileUpdate(files:[{det}]){{ files{{id}} userErrors{{field message}} }} }}')
def media(res, title, keep=None):
    out=[]
    for k in ["main","box"]:
        if k in res['images'] and (keep is None or k in keep):
            out.append({"originalSource":res['images'][k]['url'],"alt":title+(" with box" if k=="box" else ""),"mediaContentType":"IMAGE"})
    return out
jobs=[]
R={i['barcode']:i for i in json.load(open('../../results/2026-11-27-b4-fixes.json'))['items']}
for b,v in F.items(): jobs.append((b,v[0],media(R[b],v[2])))
P={p['bc']:p for p in json.load(open('P.json'))}; ids={p['bc']:i[0].split('/')[-1] for p,i in zip(json.load(open('P.json')),json.load(open('ids.json')))}
R2={i['barcode']:i for i in json.load(open('../../results/2026-11-27-b4-photos.json'))['items']}
KEEP={"3423222108373":["box"],"3423222092528":["box"],"3423478925557":["main","box"],"3423222107611":["main"],"0608940575307":["box"]}
for b,k in KEEP.items(): jobs.append((b,ids[b],media(R2[b],P[b]['title'],k)))
json.dump(jobs,open('attach_jobs.json','w'),ensure_ascii=False)
V={f"m{i}":j[2] for i,j in enumerate(jobs)}
q="mutation("+",".join(f"$m{i}:[CreateMediaInput!]" for i in range(len(jobs)))+"){"+" ".join(f'a{i}: productUpdate(product:{{id:"gid://shopify/Product/{j[1]}"}}, media:$m{i}){{ userErrors{{field message}} }}' for i,j in enumerate(jobs))+"}"
open('attach_mut.txt','w').write(q); json.dump(V,open('attach_vars.json','w'),ensure_ascii=False)
print(len(jobs), len(q), len(json.dumps(V)))
