import random
a = 1
b = 10
datora_sk = random.randint(a, b)
lietotaja_sk = a - 1
minejumu_sk = 0
print(f"Jums jauzmin datora izvelets skaits no intervala [{a} : {10}]")
print("Ievadi skaitli")

while lietotaja_sk != datora_sk:
    lietotaja_sk = int(input("==>"))
    if datora_sk > lietotaja_sk:
        print("Lielaks")
    elif datora_sk < lietotaja_sk:
        print("Mazaks")
    else:
        print("Uzminets")
    minejumu_sk += 1

print(f"Minejumu skaits {minejumu_sk}")

