#must start with at least two letters
#may contain 2 <= char <= 6
#numbers cannot be used in the middle of plate, first number can't be 0
#no periods, spaces, punctuation allowed


#og version
'''def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    #CHECK -> first and second => CORRECT
    if s[0:2].isalpha() and 2 <= len(s) <= 6:
        pass
    else:
        return False
    for i in range(2, len(s)):
        #CHECK -> punctuation and space => CORRECT
        if s[i].isspace() or s[i] in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~':
            return False
        #CHECK -> number's position => CORRECT
        elif s[i].isalpha():
            if s[i - 1].isdigit():
                return False
            else:
                pass
        elif s[i].isdigit() and s[i - 1].isalpha():
            if s[i] == "0":
                return False
            else:
                pass

    return True

main()'''


#restructured and advanced for pset_5
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





