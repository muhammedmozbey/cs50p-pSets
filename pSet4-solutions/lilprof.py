import random

correctCount = 0
attempts = 0

#userLevel = int(input("Level(1 <= level <= 3): "))

while attempts < 10:
    r = random.randint(1, 9)
    p = random.randint(1, 9)
    wrongCount = 0
    while wrongCount < 3:
        try:
            sum = int(input(f"{r} + {p} = "))
            if sum == r + p:
                correctCount += 1
                attempts += 1
                break
            else:
                print("EEE")
                wrongCount += 1
                attempts += 1
        except ValueError:
            print("EEE")
            wrongCount += 1
            attempts += 1
    if wrongCount == 3:
        print(f"{r} + {p} = {r + p}")
        attempts += 1
print(f"Score: {correctCount}")