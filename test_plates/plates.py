def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    for c in s:
        if not (c.isalpha() or c.isdigit()):
            return False
    if s[:2].isalpha():
        if len(s) >= 2 and len(s) <= 6:
            if cond3(s):
                return True
    return False

def cond3(s):
    flag = 0
    for c in s:
        if flag == 0:
            if c.isalpha():
                continue
            else:
                if c == '0':
                    return 0
                flag = 1
                continue
        else:
            if c.isalpha():
                return 0
    return 1

if __name__ == "__main__":
    main()

