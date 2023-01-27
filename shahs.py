r1 = int(input("Ievadi r1 ==>"))
k1 = int(input("Ievadi r1 ==>"))
r2 = int(input("Ievadi r1 ==>"))
r2 = int(input("Ievadi r1 ==>"))

if r1 != r2 and k1 != k2:
    print("Nevar")
elif r1 < 1 or r1 > 8:
  print ("NEVAR")
elif k1 < 1 or k1 > 8:
  print ("NEVAR")
elif r2 < 1 or r2 > 8:
  print ("NEVAR")
elif k2 < 1 or k2 > 8:
  print ("NEVAR")
else:
  print ("VAR")