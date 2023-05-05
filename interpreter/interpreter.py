x, y, z = input("Expression: ").split(" ")
if y == "+":
    a = float(x) + float(z)
elif y == "-":
    a = float(x) - float(z)
elif y == "*":
    a = float(x) * float(z)
elif y == "/":
    a = float(x) / float(z)
print(a)