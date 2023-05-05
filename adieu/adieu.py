import sys

names = []
while True:
    try:
        n = input("Name: ")
        names.append(n)
    except EOFError:
        break

print("Adieu, adieu, to ", end = "")
print(names[0], end = "")
for a in names[1:-1]:
    print(", ", end = "")
    print(a, end="")
if len(names) > 2:
    print(f", and {names[-1]}")
elif len(names) == 2:
    print(f" and {names[-1]}")
else:
    print("")
