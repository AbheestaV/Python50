import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    return len(re.findall(r"[^a-zA-Z](u|U)m[^a-zA-Z]"," " + s +" "))

if __name__ == "__main__":
    main()
