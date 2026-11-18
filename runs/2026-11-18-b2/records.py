import json
P=json.load(open('P.json')); ids=json.load(open('ids.json'))
SUP={"6291107015750":("50","7.53","Gulf Orchid Diwan Eau de Parfum 85ml Spray"),
"6290362160588":("49","8.67","Gulf Orchid Flame Eau de Parfum 110ml Spray"),
"6290362164425":("15","12.11","Gulf Orchid Mawj Eau de Parfum 110ml Spray"),
"6290362162476":("31","10.09","Gulf Orchid Perfection Eau de Perfume 105ml Spray"),
"6290362348108":("32","19.75","Lattafa Pride Gift Set Collection No.1 - 5 x 20ml"),
"6290362348078":("35","16.51","Lattafa Pride Gift Set Collection No.2 - 5 x 20ml"),
"6290362348092":("13","19.75","Lattafa Pride Gift Set Collection No.3 - 5 x 20ml"),
"6290362348085":("27","25.17","Lattafa Pride Gift Set Collection No.4 - 5 x 20ml (This set contains: \nArt of Arabia III \nAjwaa\nAl Qiam Gold\nMasa\nBrioche Vanille)"),
"5060412678872":("24","6.96","Ted Baker Midnight Petal Body & Hair Mist 200ml"),
"5060412678865":("5","6.96","Ted Baker Pink Bloom Body & Hair Mist 200ml")}
FID={"5060412678872":"19-9rPSue-f4m8L1UAEDdcV9oB5uYt_nJ","5060412678865":"10oiPYs9OoSCqh3z262-Pu73M2DcoXZfe","6291107015750":"1SQ-2i-mJBJP9ghX118YI4g1CIYbKVQoY","6290362160588":"1a5wwco8zvqksMM6t0MP3R-jU3Bc84zfZ","6290362164425":"1wxAYlkvONmoKZsndGP0zM_YccDJLGIMA","6290362162476":"1pqKMd8_X_rtshY0V5hlHrdohGVIHbund","6290362348108":"11_CvpNb-YbSKwHbEB-kuxOz6Ua8iKr7w","6290362348078":"12zjPXy-rfGz2Jbh0GRkxJrFrYTVghRNu","6290362348092":"1DNys1XU2btG8YV38C5cACbNh6-gBQke0","6290362348085":"1ezlKy-ksH5eJylIg3zHSlwTtd7Gtw-ss"}
# Daily plan row order (rows 32-41) by barcode
DP=["5060412678872","5060412678865","6291107015750","6290362160588","6290362164425","6290362162476","6290362348108","6290362348078","6290362348092","6290362348085"]
prod=[];ws=[];dsc=[];dp={}
for i,(p,(pid,vid,iid)) in enumerate(zip(P,ids)):
    row=148+i; bc=p["bc"]; st,sp,name=SUP[bc]
    prod.append([p["status"],None,p["cat_name"],p["vendor"],p["title"],"",p["form"],p["size"],p["unit"],p["gender"],"'"+bc,"","","£"+p["price"],"£"+p["cmp"],"",p["qty"],"","","https://drive.google.com/drive/folders/"+FID[bc],"","","11/18/2026","https://admin.shopify.com/store/f1d55c-f7/products/"+pid,p["note"]])
    ws.append([name,str(p["qty"])])
    dsc.append(["'"+bc,name,p["title"],p["cat_name"],pid,vid,iid,st,p["qty"],sp,p["price"],p["cmp"],"DRAFT","No","","Created 18/11/2026 run 2",row])
    dp[bc]=["drafted",pid,row]
json.dump({"prod":prod,"ws":ws,"dsc":dsc,"dp":[dp[b] for b in DP]},open('records.json','w'),ensure_ascii=False)
print(json.dumps([dp[b] for b in DP]))
