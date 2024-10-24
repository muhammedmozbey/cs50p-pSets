#og version
'''randomInput = input("Greeting: ")
if "hello" in randomInput:
    print("$0")
elif "h" in randomInput:
    print("$20")
else:
    print("$100")'''


#restructured and advanced for pset_5
def main():
    randomInput = input("Greeting: ").lower().strip()
    value(randomInput)


def value(greeting):
    greeting = greeting.lower().strip()
    if greeting.startswith("hello"):
        return "$0"
    elif greeting.startswith("h"):
        return "$20"
    else:
        return "$100"

if __name__ == "__main__":
    main()


