# uzdevums 2.3
lietotaja_vards = "user"
parole = "par"
i = 0


while i < 5:
    lietotaja_vards_iev = input("Ievadiet vardu ==>")
    parole_iev = input("Ievadiet paroli ==>")
    if lietotaja_vards_iev != lietotaja_vards and parole_iev != parole and i == 4:
        print("Jus izmantojat visus meginajumus. Konts blokets, lugums sazinaties ar ....")
        break
    elif lietotaja_vards_iev == lietotaja_vards and parole_iev == parole:
        print("Ievade pareiza")
        break
    i += 1
    print("Ievade nepareiza")

   
