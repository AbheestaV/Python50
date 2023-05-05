while True:
    try:
        f = input ("Fraction: ")
        a, b = f.split("/")
        fuel = round((int(a)/int(b))*100)
        if fuel > 100:
            continue
    except ValueError:
        print("", end = "")
    except ZeroDivisionError:
        print("", end = "")
    else:
        break
if fuel > 1 and fuel < 99:
    print(f"{int(fuel)}%")
elif fuel <= 1:
    print("E")
elif fuel >= 99:
    print("F")