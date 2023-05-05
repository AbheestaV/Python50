def main():
    amt = 50
    coin = diff = 0
    while True:
        print(f"Amount Due: {amt}")
        coin = int(input("Insert Coin: "))
        match coin:
            case 25 | 10 | 5:
                amt -= coin
            case _:
                amt = amt
        if amt <= 0:
            break
    amt = amt*(-1)
    print(f"Change Owed: {amt}")

main()
