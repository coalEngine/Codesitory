from fraction import *
from math import *

def reduceFraction(x, y) :
     
    d = gcd(x, y);
 
    x = x // d;
    y = y // d;
    count = 0
    if x > y:
       count+=1
       print(count)
    else:
        print(f"{x}/{y}")

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
    final = fraction1_piece1 * fraction2_piece1 
    final2 = fraction1_piece2 * fraction2_piece2

    
    print(f"{fraction1_piece1}/{fraction1_piece2} * {fraction2_piece1}/{fraction2_piece2} = ", end="")
    reduceFraction(final, final2)