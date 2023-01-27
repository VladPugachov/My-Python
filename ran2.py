import random
lielaka_summa = 0

for i in range(10):
    sk1 = random.randint(1, 6)
    sk2 = random.randint(1, 6)
    summa = sk1 + sk2
    print(f"{sk1} {sk2} | {max(sk1, sk2)} | {summa}")

    if summa > lielaka_summa:
        lielaka_summa = summa
print(lielaka_summa)
