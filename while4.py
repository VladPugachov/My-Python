# 1.5
n = int(input("Ievadi n ==> "))
i = 1
reizinajums = 1
while i <= n:
    reizinajums *= i
    print(i, end=' ')
    i += 1
print(f"Reizinajums ir {reizinajums}")

