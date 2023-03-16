print()
print()
print()
print()
cost = float(input("What is the cost of your item?: "))
Mdr = float(input("What is the Markdown Discount Rate?: ")) / 100
taxR = float(input("What is the tax rate?: ")) / 100


md = round(cost * Mdr, 2)
sale = round(cost - md,2)
tax = sale * taxR
tpp = round(sale + tax, 2)

print()
print()
print()
print("The Markdown Discount is:", md)
print("The Sale Price is:", sale)
print("The Total Purchase Price of your item is:", tpp)
print("The Tax is:", tax)
print()
print()
print()
