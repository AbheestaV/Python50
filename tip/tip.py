def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    monies = float(d.strip("$"))
    return monies


def percent_to_float(p):
    # TODO
    perc = float(p.strip("%"))
    pe = perc/100
    return pe

main()
