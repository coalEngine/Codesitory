import math
a = float(input("Number: "))
b = float(input("Number: "))
c = float(input("Number: "))
x1 = (-b + math.sqrt(pow(b, 2) - (4 * a * c))) / (2 * a)
x2 = (-b - math.sqrt(pow(b, 2) - (4 * a * c))) / (2 * a)

print("x =", x1, "x =", x2)