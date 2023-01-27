n = int(input("Ievadi n ==>"))

summa = n
summa_ievadita = 0

for i in range(1, n):
    s = int(input("Ievadi skaitli ==>"))
    summa_ievadita += s
    summa += i

pazaudeta_karts = summa - summa_ievadita
print(pazaudeta_karts)
