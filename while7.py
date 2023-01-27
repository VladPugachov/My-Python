# 8 uzdevums
skaits = 0
lielakais = None
mazakais = None
while skaits < 10:
    skaitlis = int(input("Ievadi skaitli ==> "))
    print(skaitlis)
    skaits += 1
    if lielakais == None or lielakais < skaitlis:
        lielakais = skaitlis
        print(f"Lielakais skaitlis ir {lielakais}")
    if mazakais == None or mazakais > skaitlis:
        mazakais = skaitlis
        print(f"Mazakais skaitlis ir {mazakais}")
    if skaitlis == 0:
        print("Skaitlis ir 0, darbiba partraukta")
        break
print(f"Lielakais skaitlis ir {lielakais}")
print(f"Mazakais skaitlis ir {mazakais}")

