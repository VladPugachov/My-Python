n, m, k, c = input("Ievadi pirmā lauciņa rindu n un kolonnu m, otrā lauciņā rindu k un kolonnu c ==>").split()
n = int(n)
m = int(m)
k = int(k)
c = int(c)

if (1 <= n <= 8 and 1 <= m <= 8 and 1 <= k <= 8 and 1 <= c <= 8
    and abs(m - c) <= 1 and abs(n - k) <= 1):
    print("VAR")
else: print ("NEVAR")
