p = float(input("Principal Amount: "))
r = float(input("Annual Interest Rate: ")) / 100
n = int(input("Number of times compunded (Per Year): "))
t = int(input("Years: "))
A = round(p * (1 + (r/n)) ** (n * t), 2)
print("\n\nBalanced after {} years:".format(t), ":", A)
interst = round(A - p, 2)
print("Interest:", interst, "\n\n") 