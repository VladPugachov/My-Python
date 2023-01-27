import string

cipari = string.digits
simboli = string.punctuation
mazie_burti = string.ascii_lowercase
lielie_burti = string.ascii_uppercase
parole = input("Ievadi paroli ==>")

while True:
    drosiba = ""
    for c in cipari:
        if c in parole:
            drosiba += "c"
    for s in simboli:
        if s in parole:
            drosiba += "s"
    for m in mazie_burti:
        if m in parole:
            drosiba += "m"
    for l in lielie_burti:
        if l in parole:
            drosiba += "l"
    if len(parole) < 9:
        print("Parole nav drosa")
    elif (len(parole) >= 9 and "c" in drosiba and "s" in drosiba or
          len(parole) >= 9 and "s" in drosiba and "m" in drosiba or
          len(parole) >= 9 and "m" in drosiba and "l" in drosiba or
          len(parole) >= 9 and "l" in drosiba and "c" in drosiba or
          len(parole) >= 9 and "c" in drosiba and "m" in drosiba or
          len(parole) >= 9 and "s" in drosiba and "l" in drosiba):
        print("Parole ir drosa")
    else:
        print("Parole ir videji drosa")
    izvele = input("Vai atkartot? J/N ==>").upper()
    if izvele == "J":
        parole = input("Ievadi paroli ==>")
    else:
        break
