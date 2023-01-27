skaits = 1
while skaits < 11:
    
    print("Ievadi 4 skaitļus no 1 līdz 8")
    sk1 = int(input("Ievadi 1. skaitli  ==> "))
    sk2 = int(input("Ievadi 2. skaitli  ==> "))
    sk3 = int(input("Ievadi 3. skaitli  ==> "))
    sk4 = int(input("Ievadi 4. skaitli  ==> "))
    if  ((sk1 > 8 or sk1 < 1) or (sk2 > 8 or sk2 < 1) or 
         (sk3 > 8 or sk3 < 1) or (sk4 > 8 or sk4 < 1)):
        print("NEVAR, koordinātes ārpus laukuma") 
    else:
        if abs(sk3 - sk1) == 2:
            if abs(sk4 - sk2) == 1:
                print("VAR")
        elif  abs(sk4 - sk2) == 2:
            if abs(sk3 - sk1) == 1:
                print("VAR")
        else:
           print("NEVAR")
    skaits += 1
