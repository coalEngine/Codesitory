from fraction import *

while True:
    print("Type Q to Quit")
    fraction1_piece1 = int(input("Fraction 1 (Numerator): "))
    fraction1_piece2 = int(input("Fraction 1 (Demominator): "))
    fraction2_piece1 = int(input("Fraction 2 (Numerator): "))
    fraction2_piece2 = int(input("Fraction 2 (Demominator): "))
    if fraction1_piece2 == 0:
        print("fraction1.piece2 is undefined") 
        break
    elif fraction2_piece2 == 0:
        print("fraction2.piece2 is undefined")
        break
    final = Fraction(fraction1_piece1, fraction2_piece2) * Fraction(fraction2_piece1, fraction2_piece2)
    print(f"{fraction1_piece1}/{fraction1_piece2} * {fraction2_piece1}/{fraction2_piece2} = {final}")