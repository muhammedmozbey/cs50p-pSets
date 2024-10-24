#og version
'''userInput = input("Fraction (e.g., 3/4): ")
numerator, denominator = userInput.split("/")


try:
    result = round((int(numerator) * 100) / int(denominator))
    if result == 100:
        print("Full")
    elif result > 100:
        print("Storage exceeded")
    elif result == 0:
        print("Empty")
    else:
        print(f"{result}%")
except ZeroDivisionError:
    print("cannot divide by zero")
except ValueError:
    print("not an integer")'''


#restructured and advanced for pset_5
def main():
    askUser = input("Fraction (e.g., 3/4): ")
    fraction(askUser)

def fraction(fuel):
    numerator, denominator = fuel.split("/")
    try:
        result = round((int(numerator) * 100) / int(denominator))
        if result == 100:
            return "Full"
        elif result > 100:
            return "Storage exceeded"
        elif result == 0:
            return "Empty"
        else:
            return f"{result}%"
    except ZeroDivisionError:
        return "cannot divide by zero"
    except ValueError:
        return "not an integer"

if __name__ == "__main__":
    main()