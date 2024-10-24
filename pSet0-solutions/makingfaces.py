randomInput = input()


sad = "🙁"
happy = "🙂"


if ":(" in randomInput:
    randomInput = randomInput.replace(":(", sad)
elif ":)" in randomInput:
    randomInput = randomInput.replace(":)", happy)

print(randomInput)