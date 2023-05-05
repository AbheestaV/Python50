import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    i=1
    if matches := re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip):
        while i<5:
            if int(matches.group(i)) > 255:
                return False
            elif int(matches.group(i)) < 0:
                return False
            i += 1
        return True
    else:
        return False




if __name__ == "__main__":
    main()
