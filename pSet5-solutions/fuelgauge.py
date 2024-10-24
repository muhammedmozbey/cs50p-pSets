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
