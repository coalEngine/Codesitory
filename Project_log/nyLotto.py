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

gotOnePiece = False
if piece1 == userPiece:
    print("Piece 1 is correct")
    gotOnePiece = True
elif piece1 == userPiece1:
    print("Piece 1 is correct")
    gotOnePiece = True
elif piece1 == userPiece2:
    print("Piece 1 is correct")
    gotOnePiece = True
else:
    print("Piece 1 is wrong")

if piece2 == userPiece:
    print("Piece 2 is correct")
    gotOnePiece = True
elif piece2 == userPiece1:
    print("Piece 2 is correct")
    gotOnePiece = True
elif piece2 == userPiece2:
    print("Piece 2 is correct")
    gotOnePiece = True
else: 
    print("Piece 2 is wrong")

if piece3 == userPiece:
    print("Piece 3 is correct")
    gotOnePiece = True
elif piece3 == userPiece1:
    print("Piece 3 is correct")
    gotOnePiece = True
elif piece3 == userPiece2:
    print("Piece 3 is correct")
    gotOnePiece = True
else:
    print("Piece 3 is wrong")

if gotOnePiece == True:
    print("You Won!")
else:
    print("You lose!")
