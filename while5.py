# 6 uzdevums
summa = 0

while True:
    skaitlis = int(input("ievadi skaitli ==> "))
    summa += skaitlis
    print(f"Summa ir {summa}")
    if skaitlis == 0:
        print("Skaitlis ir 0, darbiba partraukta")
        break
print(f"Pilna summa ir {summa}")
