import random


while True:
    try:
        userLevel = int(input("Level(level > 0): "))
        if userLevel.is_integer() and userLevel > 0:
            r = random.randint(1, userLevel)
            break
        else:
            print("Please enter a valid integer")
    except ValueError:
        print("Please enter an integer")


while True:
    try:
        userGuess = int(input("Guess(guess > 0): "))
        if  userGuess < 1:
            print("Please enter a valid integer")
        else:
            if userGuess == r:
                print("Just right!")
                break
            elif userGuess < r:
                print("Too small!")
            else:
                print("Too large!")
    except ValueError:
        print("Please enter an integer")


