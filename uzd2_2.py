# uzdevums 2.2
lietotaja_vards = "user"
parole = "par"
izvele = " "

lietotaja_vards_iev = input("Ievadiet vardu ==>")
parole_iev = input("Ievadiet paroli ==>")

while lietotaja_vards_iev != lietotaja_vards or parole_iev != parole:
    print("Lietotaja vards vai parole ievaditi nepareizi.")
    izvele = input("Vai atkartot ievadi (j/n)?")
    print(f"==> {izvele}")
    if izvele == "n":
        print("Programma beidz darbibu")
        break
    else:
        lietotaja_vards_iev = input("Ievadiet vardu ==>")
        parole_iev = input("Ievadiet paroli")
print("Ievade pareiza")
