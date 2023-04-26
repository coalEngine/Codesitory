import math

E0 = 10 ** 4.40
j = float(input("Joules?: ")) * pow(10, 16)

M = (2/3) * math.log(j / E0, 10)
print(round(M, 2))
if M < 4.5:
    print("Destructive Power: Small")
if M >= 4.5 and M < 5.5:
    print("Destructive Power: Moderate")
if M >= 5.5 and M < 6.5:
    print("Destructive Power: Large")
if M >= 6.5 and M < 7.5:
    print("Destructive Power: Major")
if M >= 7.5:
    print("Destructive Power: Greatest")
 
