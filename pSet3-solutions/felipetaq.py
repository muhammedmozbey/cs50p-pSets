#program that's wanted
'''menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.0,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}
total = 0
while True:
    try:
        userFood = input("Item (e.g. burrito, or ctrl-c to quit): ").title()
        for food in menu:
            if userFood == food:
                total += menu[food]
                print(f"Current Total: ${total}")
    except (EOFError, KeyboardInterrupt):
        print("")
        break
print(f"Total: ${total}")'''

#advanced version
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.0,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}
total = 0
while True:
    try:
        userFood = input("Item (e.g. burrito, or ctrl-c to quit): ").title()
        if userFood in menu:
            total += menu[userFood]
            print(f"Current Total: ${total:.2f}")
        else:
            print("Not on the menu!")
    except (EOFError, KeyboardInterrupt):
        print("")
        break
print(f"Total: ${total:.2f}")
