import json
F={"3616304197420":"1n3bosWWFP897t7AagXF7OGzZPQ6BPUpa","0085715169952":"1hFssC44nQOIHyNwO4C3W6GLT5PDB9w3O","0085715169402":"1UdvPLQ7hJ5mmxwu81loqt2upJ2SHQqkH","0085715167217":"1KCNsz0qyfWIyDd3GrD-FkalESaz42Pt4","0085715167620":"1-6MBHF2eimbX9YmIIkyKVjDrxcCO2LM4","0085715167828":"1NZCjzfkyEoxwlCUckKP_EZmLEox5eUfS","0085715167804":"1kAytOV3iAdokXTktQXGe54q3KsKNfV_E","8411061084922":"1vuM_KKdLVJIlyzKjTd9ADfbM3SxWov0n","8411061080641":"1zGExiLe2Nm56gyVYykOIF1zyYzMz5NJV","0812256024194":"1MO1JLfN7XpEV6y5D1JgeV5Z6WUcVO_0H","0719346565868":"1i2fZcaPS2yXYPusGT7RK-F_yoIw2BGcX","9362014000010":"1PSKozKhohMIfKGGbqyuISBOVS1QaMwIK","9362014011610":"1oePk2lQgP6qrfannnNQ2uMYwc_vBL_he","3614226905192":"1yWV2S1XjrBOltZCZ-Bxn_NI_pZ5U0dJ_","3614226904997":"1CH7nsI-RH4h3ofHbTkP1rGesqci4s48w","0088300107407":"1Auu3j0uUrR5EknM8Z7IJaoxrVdl5f3KE","3614221537763":"1HWxYCPHnCaFFv_zoJfMm8zvhKAOzFq6M","0088300178278":"1yuPL6ndvy3mmZN6OQFyd_0yXUGuYFWEi","0088300073627":"1FwJnGZsYaZnpoFVJOqgLZdsZfuHoLmky","3614225358463":"1-pOVIpnwAKHpi9FfqvDXH__-0VQn47sp"}
exec(open('cand.py').read())
R={r[0]:r for r in ROWS}
R["3616304197420"]=["3616304197420","Davidoff","Davidoff Cool Water Gift Set 75ml EDT + 70g Deodorant Stick","Men","32.49","42.99","5"]
order=list(F)
rows=[]
for i,bc in enumerate(order):
    b=3 if i<10 else 4; r=R[bc]
    cat="Bath & Body" if bc=="3616304197420" else "Fragrance"
    rows.append(["23/11/2026",str(b),"12:10" if b==3 else "18:10",cat,r[1],r[2],"'"+bc,f"{bc} - {r[2]}","https://drive.google.com/drive/folders/"+F[bc],"planned","","","",""])
json.dump(F,open('fid.json','w')); json.dump(rows,open('dp_rows.json','w'),ensure_ascii=False)
print(json.dumps(rows,ensure_ascii=False))
