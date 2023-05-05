import csv
import sys

def main():
    if len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    elif len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    try:
        scourgify(sys.argv[1], sys.argv[2])
    except:
        print(f"Could not read {sys.argv[1]}")
        sys.exit(1)

def scourgify(f,f2):
    students = []
    with open(f) as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({"name": row["name"], "house": row["house"]})

    with open(f2, "w") as file2:
        writer = csv.DictWriter(file2, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for student in students:
            last, first = student["name"].split(",")
            lastname = last.strip()
            firstname = first.strip()
            writer.writerow({"first": firstname, "last": lastname, "house": student["house"]})

if __name__ == "__main__":
    main()