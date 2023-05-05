def main():
    s = input("Input: ").strip()
    print(f"Output: {shorten(s)}")


def shorten(word):
    new_word=""
    for c in word:
        if c == 'a' or c == 'e' or c == 'i' or c== 'o' or c== 'u' or c == 'A' or c == 'E' or c == 'I' or c== 'O' or c== 'U' :
            continue
        new_word += c
    return new_word


if __name__ == "__main__":
    main()
