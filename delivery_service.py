# This program calculate delivery cost depending on weight and cost

print("Welcome to Delivery Service")
print("   ")
print("Standart Delivery:")
print("2 kg or less: 1.50 per kg ")
print("Over 2 kg but less than or equal to 6 kg: 3.00 per kg")
print("Over 6 kg but less than or equal to 10 kg: 4.00 per kg")
print("Over 10 kg: 4.75 per kg")
print("   ")
print("Fast Delivery:")
print("2 kg or less: 4.50 per kg ")
print("Over 2 kg but less than or equal to 6 kg: 9.00 per kg")
print("Over 6 kg but less than or equal to 10 kg: 12.00 per kg")
print("Over 10 kg: 14.25 per kg")
print("   ")

weight = float(input("Enter delivery weight: "))
while weight < 0:
    print("Incorrect weight!")
    weight = float(input("Enter delivery weight: "))
    

def standart_delivery(weight):
    standart_cost = 0
    if weight <= 2:
        standart_cost = weight * 1.50
        return standart_cost
    elif weight <= 6:
        standart_cost = weight * 3.00
        return standart_cost
    elif weight <= 10:
        standart_cost = weight * 4.00
        return standart_cost
    else:
        standart_cost = weight * 4.75
        return standart_cost

def fast_delivery(weight):
    fast_cost = 0
    if weight <= 2:
        fast_cost = weight * 4.5
        return fast_cost
    elif weight <= 6:
        fast_cost = weight * 9.00
        return fast_cost
    elif weight <= 10:
        fast_cost = weight * 12.00
        return fast_cost
    else:
        fast_cost = weight * 14.25
        return fast_cost

def main():
    choice = int(input("Your delivery choice: 1 = Standart Delivery, 2 = Fast Delivery "))
    while choice < 1 or choice > 2:
        print("Incorrect delivery choice!")
        choice = int(input("Your delivery choice: 1 = Standart Delivery, 2 = Fast Delivery "))
    if choice == 1:
        standart_cost = standart_delivery(weight)
        print(f"Your Standart Delivery {weight}kg cost: {round(standart_cost, 2)}")
    else:
        fast_cost = fast_delivery(weight)
        print(f"Your Fast Delivery {weight}kg cost: {round(fast_cost, 2)}")
      
main()
    
    