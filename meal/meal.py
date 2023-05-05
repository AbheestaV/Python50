def main():
    t = input("What is the time?: ")
    time = convert(t)
    if time >=7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")

def convert(time):
    ht, mt = time.split(":")
    hour = float(ht)
    min = float(mt)
    if min >=15 and min < 30:
        hour += 0.25
    elif min >= 30 and min < 45:
        hour += 0.5
    elif min >=45 and min <= 59:
        hour += 0.45
    return hour



if __name__ == "__main__":
    main()
