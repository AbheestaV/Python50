def main():
    fuel = 0
    while True:
        try:
            f = input ("Fraction: ")
            fuel = convert(f)
            if fuel > 100:
                continue
        except ValueError:
            print("", end = "")
        except ZeroDivisionError:
            print("", end = "")
        else:
            break
    print(gauge(fuel))


def convert(fraction):
    a, b = fraction.split("/")
    return round((int(a)/int(b))*100)

def gauge(percentage):
    if percentage > 1 and percentage < 99:
        return f"{int(percentage)}%"
    elif percentage <= 1:
        return f"E"
    elif percentage >= 99:
        return f"F"


if __name__ == "__main__":
    main()
