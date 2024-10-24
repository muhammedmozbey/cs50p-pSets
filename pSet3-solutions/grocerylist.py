bag = {}
while True:
    try:
        userList = input("").upper()
        if userList in bag:
            bag[userList] += 1
        else:
            bag[userList] = 1
    except (EOFError, KeyboardInterrupt):
        print("")
        break
#.items() returns key and value pairs
for item, quantity in bag.items():
    print(f"{quantity} {item}")


