from datetime import date
import inflect
import sys

p = inflect.engine()

def main():
    s = input("Date of Birth: ")

    print(convert(s))


def convert(s):
    try:
        if not "-" in s:
            raise ValueError
        timesince = date.today() - date.fromisoformat(s)
        dayssince = timesince.days
        minutessince = dayssince*1440
        res = p.number_to_words(minutessince)
    except ValueError:
        sys.exit("Invalid date")
    min = res.replace(' and ',' ').capitalize()
    min2 = min + " minutes"
    return min2

if __name__ == "__main__":
    main()
