# figuring out
'''print("Amount Due: 50")
insertion = int(input("Insert Coin: "))
amountdue = 50
result = amountdue - insertion

print(f"Amount Due: {result}")
insertionnd = int(input("Insert Coin: "))
resultnd = result - insertionnd

print(resultnd)
'''

# without 25-10-5 only rule
'''amountdue = 50
print("Amount Due: 50")
insertion = int(input("Insert Coin: "))

change = amountdue - insertion

while change != 0:
    amountdue = change
    print(f"Amount Due: {change}")
    continuous_insertion = int(input("Insert Coin: "))
    change = amountdue - continuous_insertion
    if change == 0:
        print("Change Owed: 0")
        break
    else:
        print(f"Change Owed: {abs(change)}")
        break'''

# with 25-10-5 only rule and cleaner
amountdue = 50

while amountdue > 0:
    print(f"Amount Due: {amountdue}")
    insertion = int(input("Insert Coin: "))
    if insertion in [25, 10, 5]:
        amountdue = amountdue - insertion
    else:
        print("25, 10, 5 only!")

changeowed = abs(amountdue)
print(f"Change Owed: {changeowed}")

