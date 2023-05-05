import random
level = 0
while True:
    try:
        level = int(input("Level: "))
        num = random.randint(1,level)
    except:
        pass
    else:
        break


#print(num)
guess = 0
while True:
    try:
        guess = int(input("Guess: "))
    except:
        pass
    else:
        if guess > num:
            print("Too large!")
        elif num > guess:
            print("Too small!")
        elif num == guess:
            print("Just right!")
            break

