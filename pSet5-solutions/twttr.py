#restructured for pset_5
def main():
    userInput = input("Input: ")
    shortened = shorten(userInput)
    print(f"Output: {shortened}")

def shorten(word):
    vowels = "aeiou"
    for vowel in vowels:
        word = word.replace(vowel, "")
    return word

if __name__ == "__main__":
    main()