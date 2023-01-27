a, b = input("Ievadi a un b ==>").split()
a = int(a)
b = int(b)

def devides_evenly(a, b):
    if a % b == 0:
        return True
    else:
        return False

print(devides_evenly(a, b))



