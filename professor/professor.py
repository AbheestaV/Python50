import random


def main():
    a = get_level()
    score = 0
    for i in range(10):
        EEE = 0
        x = generate_integer(a)
        y = generate_integer(a)
        ans = x + y
        while True:
            sum = int(input(f"{x} + {y} = "))
            if EEE >= 2 :
                print(f"{x} + {y} = {ans}")
                break
            elif sum == ans:
                score += 1
                break
            else:
                print("EEE")
                EEE += 1
    print(f"Score: {score}")



def get_level():
    while True:
        try:
            lvl = int(input("Level: "))
            if lvl > 3 or lvl < 1:
                raise ValueError
        except ValueError:
            pass
        else:
            break
    return lvl


def generate_integer(level):
    if level == 1:
        num = random.randint(0, pow(10,level) - 1)
    else:
        num = random.randint(pow(10,(level-1)), pow(10,level) - 1)
    #print(pow(10,level) - 1)
    return num


if __name__ == "__main__":
    main()
