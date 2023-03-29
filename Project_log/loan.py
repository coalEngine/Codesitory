B1, B2, B3, B4 = 0, 0, 0, 0
A = int(input("Amount Borrowed:"))
n = int(input("Number of payments per year: "))
P =  int(input("Amount paid per payment: "))
r = float(input("Annual percentage rate (APR): ")) / 100

B1 = (A * pow(1 + (r/n), n * 1)) - (P * ((pow(1 + (r/n), n * 1) - 1)) / ((1 + (r/n)) - 1))
B5 = (A * pow(1 + (r/n), n * 5)) - (P * ((pow(1 + (r/n), n * 5) - 1)) / ((1 + (r/n)) - 1))
B10 = (A * pow(1 + (r/n), n * 10)) - (P * ((pow(1 + (r/n), n * 10) - 1)) / ((1 + (r/n)) - 1))
B20 = (A * pow(1 + (r/n), n * 20)) - (P * ((pow(1 + (r/n), n * 20) - 1)) / ((1 + (r/n)) - 1))
B30 = (A * pow(1 + (r/n), n * 30)) - (P * ((pow(1 + (r/n), n * 30) - 1)) / ((1 + (r/n)) - 1))
print("\n\n\n\nAmount After 1 year: {}\nAmount After 5 years: {}\nAmount After 10 years: {}\nAmount After 20 years: {}\nAmount after 30 years: {}\n\n\n\n".format(round(B1, 2), round(B5, 2), round(B10, 2), round(B20, 2), round(B30, 2)))
