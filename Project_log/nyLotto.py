import random
for _ in range(3):
    piece1 = random.randint(0, 9)
    piece2 = random.randint(0, 9)
    piece3 = random.randint(0, 9)
print(f"{piece1} | {piece2} | {piece3}")
for _ in range(1):
    userPiece = int(input("\nGuess the first number: "))
    userPiece1 = int(input("Guess the second number: "))
    userPiece2 = int(input("Guess the third number: "))


if piece3 == userPiece2:
    print("Piece 3 is correct")
if piece2 == userPiece1:
    print("Piece 2 is correct")
if piece1 == userPiece:
    print("Piece 1 is correct")
elif piece1 == userPiece and piece2 == userPiece1 and piece3 == userPiece2:
    print("You won!")
else:
    print("You lose!")