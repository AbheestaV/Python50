from tabulate import tabulate
import csv
import sys

def main():
    if len(sys.argv) != 2:
        sys.exit(1)
    elif not sys.argv[1].endswith(".csv"):
        sys.exit(1)
    else:
        tabler(sys.argv[1])

def tabler(f):
    table = []
    file = open(f, "r")
    data = list(csv.reader(file, delimiter=","))
    file.close()
    print(data)
    print(tabulate(data, headers="firstrow", tablefmt="grid"))

if __name__ == "__main__":
    main()