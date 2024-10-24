randomInput = input("Expression: ")
x, y, z = randomInput.split(" ")
print(x, y, z)
floatx = float(x)
floatz = float(z)

if y == "+":
    print(round(floatx + floatz, 1))
elif y == "-":
    print(round(floatx - floatz, 1))
elif y == "/":
    print(round(floatx / floatz, 1))
else:
    print(round(floatx * floatz, 1))
