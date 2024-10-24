import inflect

p = inflect.engine()

names = []

while True:
    try:
        userInput = input("Name: ").capitalize()
        if userInput not in names:
            names.append(userInput)
    except (EOFError, KeyboardInterrupt):
        print("")
        break

output = p.join(names)

print(f"Adieu, adieu, to {output}")
