def main():
    name = input("camelCase: ")
    snake(name)

def snake(n):
    print("snake_case: ", end="")
    for i in n:
        if i.isupper():
            print(f"_{i.lower()}", end="")
        else:
            print(i, end="")
    print("")
main()

