fruits = [
    {"name": "apple", "calories": 95},
    {"name": "banana", "calories": 105},
    {"name": "orange", "calories": 62},
    {"name": "strawberries", "calories": 50},
    {"name": "grapes", "calories": 104},
    {"name": "pineapple", "calories": 82},
    {"name": "peach", "calories": 59},
    {"name": "pear", "calories": 101},
    {"name": "cherries", "calories": 95},
    {"name": "kiwifruit", "calories": 64,}
]

askUser = input("Item: ").lower()

for fruit in fruits:
    if askUser == fruit["name"]:
        print(f"Calories: {fruit["calories"]}")
        break
else:
    print("Fruit calorie not found!")
