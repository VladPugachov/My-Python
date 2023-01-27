import string
import random

cipari = string.digits
simboli = string.punctuation
mazie_burti = string.ascii_lowercase
lielie_burti = string.ascii_uppercase
izvele = ""
print("Programma izveido drosu paroli")

while True:
    random_cipari = random.sample(cipari, 2)
    random_simboli = random.sample(simboli, 2)
    random_mazie_burti = random.sample(mazie_burti, 3)
    random_lielie_burti = random.sample(lielie_burti, 2)
    parole = random_cipari + random_simboli + random_mazie_burti + random_lielie_burti
    sample_parole = random.sample(parole, 9)
    gatava_parole ="".join(sample_parole)
    print(f"==> {gatava_parole}")
    izvele = input("Atkartot? J/N ==>").upper()
    if izvele == "N":
        break