import random

def lottery():
    bal = 1000
    while True:
        print(f"\033[1;37mCurrent Balance: {bal}\n")
        prompt = input("\n\n\033[1;37mCasino (Game) (Press N to Leave, Press C to continue): ")
        if prompt == 'C':
            bet = float(input("How much do you want to bet?: "))
            bal -= bet
            for _ in range(3):
                piece1 = random.randint(0, 9)
                piece2 = random.randint(0, 9)
                piece3 = random.randint(0, 9)
            print(f"\n{piece1} | {piece2} | {piece3}")
            if piece1 == piece2 or piece2 == piece3:
                bal += bet * (2.10)
                print("\033[1;94mDOUBLE BONUS!!!")
            elif piece1 == piece3:
                bal += bet * (2.10)
                print("\033[1;94mDOUBLE BONUS!!!")
            elif piece1 == piece2 == piece3:
                bal += bet * (3.10)
                print("\033[1;93mTRIPLE BONUS!!!")
            else:
                print("No winnnings...")
                if bal <= 0:
                    print("Out of Money...")
                    break
        else:
            break
lottery()