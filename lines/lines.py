import sys

def main():
    #print(sys.argv[1][-3:])
    if len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif not sys.argv[1].endswith(".py"):
        print("Not a Python file")
        sys.exit(1)
    else:
        count(sys.argv[1])

def count(f):
    c = 0
    try:
        with open(f, "r") as file:
            for line in file:
                if line.lstrip().startswith("#"):
                    continue
                elif (line.rstrip()):
                    c += 1

    except:
        print("File does not exist")
        sys.exit(1)
    print(c, end="")

if __name__ == "__main__":
    main()