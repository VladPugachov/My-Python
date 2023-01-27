x1, y1, x2, y2 = input ("Ievadiet koord. x1,y1,x2,y2 => ").split()
x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
if (1<=x1<=8 and 1<=x2<=8 and 1<=y1<=8 and 1<=y2<=8):
    if x1-y1 == x2-y2: print("VAR")
    elif x1+y1 == x2+y2: print("VAR")
    else: print("NEVAR")
else: print("NEVAR")
