import random
a = 1
b = 15
m = 5
n = 7

s1 = [random.randint(a, b) for x in range(m)]
s2 = [random.randint(a, b) for x in range(n)]
s3 = [x for x in s1 if x in s2]

print(s1)
print(s2)
print(s3)