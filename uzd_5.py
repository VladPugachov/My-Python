import string

teksts = input("Ievadiet rakstziimju virkni kas satur tikai vardus un atstarpes ==>")
cipari = string.digits
simboli = string.punctuation

while True:
    for c in cipari:
        if c in teksts:
            print("Ievade nepareiza")
            teksts = input("Ievadiet rakstziimju virkni kas satur tikai vardus un atstarpes ==>")
    for s in simboli:
        if s in teksts:
            print("Ievade nepareiza")
            teksts = input("Ievadiet rakstziimju virkni kas satur tikai vardus un atstarpes ==>")
    else:
        split_teksts = teksts.split()
        title_teksts = " ".join(split_teksts).title()
        print(title_teksts)
        break