import random
import string
n = 6
a = 1
b = 10
burti = string.ascii_uppercase

s1 = [random.randint(a, b) for i in range(n)]
s2 = random.sample(burti, n)
apvienots = list(zip(s1, s2))

print(s1)
print(s2)
print(apvienots)

