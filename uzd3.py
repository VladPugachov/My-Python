import random

print("Programma uzminees lietotaaja izveeleetu skaitli no intervala [m; n]")
print("Iedomajies skaitli un ievadi intervala [m; n] galapunktus:")
m = int(input("m ==>"))
n = int(input("n ==>"))
sk = random.randint(m, n)
print(f"==> {sk}")
lielaks = 0
mazaks = 0
minejums = 0

while True:
    izvele = input('Ievadi: L-"Lielaaks", M-"Mazaaks" vai U-"Uzmineets"').upper()
    if izvele == "L":
        print("Lielaaks")
        lielaks = sk
        m = lielaks + 1
        sk = random.randint(m, n)
        print(f"==> {sk}")
        minejums += 1
    elif izvele == "M":
        print("Mazaaks")
        mazaks = sk
        n = mazaks - 1
        sk = random.randint(m, n)
        print(f"==> {sk}")
        minejums += 1
    else:
        print("Uzmineets")
        minejums += 1
        break
print(f"Mineejumu skait: {minejums}")
        