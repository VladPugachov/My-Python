a = int(input("Ievadiet pirmo skaitli ==>"))
b = int(input("Ievadiet otro skaitli ==>"))
c = int(input("Ievadiet treso skaitli ==>"))

if a > b and a > c:
    print(f"Lielakais ir : {a}")
elif b > a and b > c:
    print(f"Lielakais ir : {b}")
elif c > a and c > b:
    print(f"Lielakais ir : {c}")
else:
    print("Skaitli ir vienadi")
