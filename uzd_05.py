import random
a = 1
b = 10
m = 5
n = 7
s1 = [random.randint(a, b) for x in range(m)]
s2 = [random.randint(a, b) for x in range(n)]
s3 = [(x, y) for x in s1 for y in s2 if x in s2 and y in s1 and x == y]

print(s1)
print(s2)
print(s3)
