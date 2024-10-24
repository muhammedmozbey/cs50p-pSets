def main():
    plate = input("Plate: ")
    is_valid(plate)

def is_valid(s):
    #CHECK -> first and second => CORRECT
    if s[0:2].isalpha() and 2 <= len(s) <= 6:
        pass
    else:
        return "Invalid"
    for i in range(2, len(s)):
        #CHECK -> punctuation and space => CORRECT
        if s[i].isspace() or s[i] in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~':
            return "Invalid"
        #CHECK -> number's position => CORRECT
        elif s[i].isalpha():
            if s[i - 1].isdigit():
                return "Invalid"
            else:
                pass
        elif s[i].isdigit() and s[i - 1].isalpha():
            if s[i] == "0":
                return "Invalid"
            else:
                pass

    return "Valid"

if __name__ == "__main__":
    main()
