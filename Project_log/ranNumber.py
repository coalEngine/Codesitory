import random

amount_guess = 0
rand = round(random.random() * 100, 0)

while amount_guess < 7:
    print()
    guess = float(input("Guess the number: "))
    amount_guess+=1
    if guess > rand:
        print()
        print("Integer is Lower")
    elif guess < rand:
        print()
        print("Integer is Higher")
    elif guess == rand:
        print()
        print("Correct")
        break
    if amount_guess == 7:
        print()
        print("Out of guesses")
        break