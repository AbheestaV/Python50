d = {}
while True:
    try:
        item = input().upper()
        if item in d:
            d[item] += 1
        else:
            d[item] = 1
    except EOFError:
        break
a = sorted(d)
for i in a:
    print(f"{d[i]} {i}")