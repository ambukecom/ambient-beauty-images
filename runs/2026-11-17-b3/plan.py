import json
F={
"6290360617756":("1Pm-krzmq2YDc1PDIiGFzax2IRO5v5Df9","Fragrance","Ahmed Al Maghribi","Ahmed Al Maghribi Kaaf Noir Extrait de Parfum 100ml"),
"6293708007479":("1uNjTdOPpFTHgfUIl-4t9M9VsNr4Er6fW","Fragrance","Ajmal","Ajmal Cuir Musc Eau de Parfum 100ml"),
"6293708019458":("1Fe0GIhvnUlQremLdgnYaamL3oCh2wIZv","Fragrance","Ajmal","Ajmal Patchouli Wood Eau De Parfum 50ml"),
"6290361917183":("1hwi6SMF2NT_T9aQFI_quMRzOo-1oJM7P","Fragrance","Arabiyat Prestige","Arabiyat Prestige Aristo Eau de Parfum 100ml"),
"6295156400222":("1VQxIni-nzgGCxJxJ-8guhhqPyXXEtzgZ","Fragrance","Arabiyat Prestige","Arabiyat Prestige Marasi For Her Eau de Parfum 100ml"),
"6295156400215":("1Grsy6BRYLKeLAZtfh0y9Us6xSSfsAlFx","Fragrance","Arabiyat Prestige","Arabiyat Prestige Marasi For Him Eau de Parfum 100ml"),
"3474636976058":("16aZXrL9BmRDyOUhIcCnGC0q_zD8UPjZe","Haircare","L'Oréal","L'Oreal Serie Expert Vitamino Color Hair Mask 250ml"),
"3666057157417":("1_-g136qOMRn-bm19GyIxSIyEre-ThWZD","Makeup","Clarins","Clarins Wonder Perfect 4D Waterproof Mascara 8ml - 01 Perfect Black"),
"8005610477053":("1Dp4mWSpeXlkvqAD-iRF2o2UL0XKZdxNw","Bath & Body","Lacoste","Lacoste L.12.12 Pour Elle Sparkling Shower Gel 150ml"),
"0008080151445":("1pBlafBB9aSqBAPfM11jC6iucsCi_Q5ot","Bath & Body","Molton Brown","Molton Brown Heavenly Gingerlily Bath & Shower Gel 300ml"),
"5030805002942":("1KauhzxsshyGI96bxHQIGZG5H1GmWCOc_","Bath & Body","Molton Brown","Molton Brown Tobacco Absolute Bath and Shower Gel 300ml"),
"5060412678889":("1hxTlMCvHshBVJaYb-eqRMsXqgp4zJLRL","Bath & Body","Ted Baker","Ted Baker Cosmic Crush Body & Hair Mist 200ml"),
"6290361916964":("1pIhvrqTbFlenPU4Gos_FIyRWu36FMUVZ","Fragrance","Arabiyat Prestige","Arabiyat Prestige Sugar Coconot Chiffon Eau de Parfum 100ml"),
"6290361916933":("1hpJLQ77_2ee4BybsfFra-RjKNt034BH6","Fragrance","Arabiyat Prestige","Arabiyat Prestige Sugar Lemon Sorbet Eau de Parfum 100ml"),
"6290361916902":("11Db2XnWXBqCrCj17Zg43DuDA9i0BHwqh","Fragrance","Arabiyat Prestige","Arabiyat Prestige Sugar Matcha Latte Eau de Parfum 100ml"),
"6295199791189":("14GWoX_am44FRFhsFm3yLEYrH0X5t9QeB","Fragrance","Ard Al Zaafaran","Ard Al Zaafaran I Am The Queen Ana Al Malikah Eau de Parfum 100ml"),
"6438585524675":("1k23LYL5iKnSwIUN8Pt-gpWpHTue9MulO","Fragrance","Ard Al Zaafaran","Ard Al Zaafaran Layalina Eau De Parfum 100ml"),
"6295199790397":("161iAL5s20Bk1T4f6lIIEFUQr1ImKCIeu","Fragrance","Ard Al Zaafaran","Ard Al Zaafaran Mousuf Azure Eau de Parfum 100ml"),
"6295199790380":("1vXtmZ_avEi68jLi-p0S3YOslZNAEjboj","Fragrance","Ard Al Zaafaran","Ard Al Zaafaran Mousuf Eau de Parfum 100ml"),
"6294015131017":("1nrkpEExwj0tYTBWM5067VDWsoGQ0rr3E","Fragrance","Armaf","Armaf Club De Nuit Intense Eau de Parfum 150ml"),
}
rows=[]
for i,(bc,(fid,cat,br,nm)) in enumerate(F.items()):
    b=3 if i<10 else 4
    rows.append(["17/11/2026",b,"12:10" if b==3 else "18:10",cat,br,nm,"'"+bc,f"{bc} - {nm}",f"https://drive.google.com/drive/folders/{fid}","planned","","","",""])
json.dump(rows,open('plan_rows.json','w'),ensure_ascii=False)
print(json.dumps(rows,ensure_ascii=False))
