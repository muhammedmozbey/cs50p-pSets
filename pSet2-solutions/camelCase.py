camelCase = input("camelCase:  ")

print("snake_case: ", end="")

'''for i in range(len(camelCase)):
    if camelCase[i].isupper():
        snake_case = camelCase.replace(camelCase[i], "_")
'''

for i in camelCase:
    if i.isupper():
        print("_" + i.lower(), end="")
    else:
        print(i, end="")

print()
