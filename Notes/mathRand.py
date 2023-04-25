import math, random

print("Rounded up 9.5:", math.ceil(9.5))
print("Rounded down 9.5:", math.floor(9.5))
num = 4
print(num, 'Squared:', pow(num, 2))
print(num, 'Square Root:', math.sqrt(4))

num = random.sample(range(1, 59), 6)
print("Your Lucky Lotto Numbers are:", num)