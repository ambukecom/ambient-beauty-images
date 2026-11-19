from cands import BB, FR
L = BB + FR[:38]
B = {1: L[:10], 2: L[10:20], 3: L[20:30], 4: L[30:40]}
FID = """11J8_P1C_zYljg4EvRNq-TiezxcXw0fyU 1UmQo6_XMQqJQqt9TrvQ8XD2oKh71pTMC 1dsxzNI_h-ZJciTKu1cWZnu4zNy_Y6MQO 1Aq3_dnRoH3-LSKunNTajQc4GtK0GsKQC
1mhxWctbKL_3HG1BhTzZt2IoawBtoSoQK 1OPlLChC4pXvQVGkJ1NfO-qGhOZyUxoaa 1OyWlW-JFtNCoI6EF3t8QgEg-GKYVBrEL 1D_hFTKMLfhB2PANYInJsxge5BcabVLo9
1sD-YVcsIvxWzrimxIJXUznCU7V3UtYOu 19IjvRB_UvIlic0ZGG35zCDSpPcq0WdIr 1chfwHt8Oham6G35CNL1IxeKLLxhdaeWm 18jn9vtKiIOlu0Y0VdPtxpg1a6xvOnbpL
19qA94w4Ck8j6I2QHwQX2IsYjxtfayymD 173TIglH0dj60WnwbdoiN3aTO2zITCakb 1eHFvXmZ8e0GJYwmUkRQUw5rZpP3VuznR 1R5h7oRbspYaWxZBcLCw6oWTeuQK1ASHa
1VxqJJ8e8Sj3EnrMvAg9VTfSryAe-_k3z 1rvwsX5UjMhtLP8WKfmJvx7FIMYEJWPqO 1XRSQbS5XS2Dc6MDQxRlujODqvxBFluHB 1My9chvHH9FZc96awdHHR6P8aHJLHz7rP
1T4VXDtntlUyklbj5BLSevWJ1t37FZNJs 1SD6VwM1bfYVpbcb-czy6ueTtFS0u8zEo 1N64zxQH7nzSHPeDY9V9mBdPiTcFmYvJ4 1bbQqRLo3eM1QxJETNWISXfUpwQz_8aIF
1etdKZBEq-C2sp88_nX2nO6IDNayeaAVU 1M6lxSPBDjaigYurB1hHGQr28ZB5Xbacw 12cFIAKVSeA0R2jUOWB5Z6_PbMNHPLyiL 1t9u7ZIO0DqV7WPvJOMHq2MCTX7a2llQY
1RVtIbpksIkM_hzKfpssFcYowr-CU14EO 1suyWG4o0Rj6AI4EWkYU-EHJxuBp7Pr2R 1hLq9tMCIZOBo7RLzu-JDGZoVYYOPxUSv 10VKNtoAg6VEHCxInkrBn2UXwd64WWHRp
1XUgTSenYNQ6HnI4bsy1AaCB4ys-RoEso 19D-O5bP6kSpyKi5oBPkbC56j8V2Fjdwc 1Ipz_k-uOrBRm2wAOyIRNIOuaQS6eDyWH 1zXqn4CJpT_O_tBNDxG0XXlPVYjUU1A46
1icSF2ktumwqCROCnIJyQn6P_a0Kl93OG 1YMzBTuST7w5VyYCRzKO3si62OSPJ6rsk 1K10JI7VVmkHTAvUAellvTqhlGFA9DkaW 1a_QbU3Nfg09si3-F0VdkUi4usNKwUq6c""".split()
FID = {c[6]: f for c, f in zip(L, FID)}
RT = {1: "00:10", 2: "06:10", 3: "12:10", 4: "18:10"}
if __name__ == "__main__":
    import json
    rows = []
    for b, LL in B.items():
        for c in LL:
            rows.append(["19/11/2026", b, "'" + RT[b], c[0], c[1], c[2], "'" + c[6], f"{c[6]} - {c[2]}",
                         f"https://drive.google.com/drive/folders/{FID[c[6]]}", "planned", "", "", "", ""])
    json.dump(rows, open("plan_rows.json", "w"), ensure_ascii=False)
    print(json.dumps(rows, ensure_ascii=False))
