import random
burti = "ASP"
lietotaja_uzvara = 0
datora_uzvara = 0
spele = 0
print("Spele: Akmens, skeeres, papiritis")

while spele <= 10:
    datora_izvele = random.choice(burti)
    lietotaja_izvele = input('Ievadi: A-"Akmens", S-"Skeeres", P-"Papiritis" ==>').upper()
    print(f"Tava izvele ==> {lietotaja_izvele}")
    print(f"Datora izvele ==> {datora_izvele}")
    if lietotaja_izvele == datora_izvele:
        print("Neizskirts")
    elif (lietotaja_izvele == "A" and datora_izvele == "P" or
          lietotaja_izvele == "S" and datora_izvele == "A" or
          lietotaja_izvele == "P" and datora_izvele == "S" or
          lietotaja_izvele != "A" and lietotaja_izvele != "S" and
          lietotaja_izvele != "P"):
        print("Uzvar dators")
        datora_uzvara += 1
    else:
        print("Uzvar lietotajs")
        lietotaja_uzvara += 1
    print("Vai atkaartot (y/n)?")
    izvele = input("==>")
    if izvele == "n":
        break
    spele += 1
print(f"Lietotajs uzvareja: {lietotaja_uzvara}")
print(f"Dators uzvareeja: {datora_uzvara}")
print("Paldies par Speeli!")

