def main():
    months = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }
    #print(months[:-1])
    date = ''
    while True:
        try:
            date = input("Date: ").strip()
            if date[0].isalpha():
                mon, day, year = date.split(" ")
                mon = str(months[mon])
                if day[-1] == ",":
                    date = day[:-1]
                else:
                    continue
                if int(mon) > 12:
                    continue
                elif int(date) > 31:
                    continue
                if int(date) < 10:
                    date = "0" + date
                if int(mon) < 10:
                    mon = "0" + mon
                print(f"{year}-{mon}-{date}")
            else:
                mon, day, year = date.split("/")
                if int(mon) > 12:
                    continue
                elif int(day) > 31:
                    continue
                if int(day) < 10:
                    day = "0" + day
                if int(mon) < 10:
                    mon = "0" + mon
                print(f"{year}-{mon}-{day}")
        except ValueError:
            print("value error")
            continue
        except TypeError:
            print("type error")
            continue
        except KeyError:
            print("key error")
        else:
            break



main()
