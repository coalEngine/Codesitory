print()
print()
print()
print()
cost = float(input("What is the cost of your item?: "))
cost2 = float(input("What is the cost of your 2nd item?: "))
cost3 = float(input("What is the cost of your 3rd  item?: "))
cost4 = float(input("What is the cost of your 4th item?: "))
cost5 = float(input("What is the cost of your 5th item?: "))
cost6 = float(input("What is the cost of your 6th item?: "))
cost7 = float(input("What is the cost of your 7th item?: "))
cost8 = float(input("What is the cost of your 8th item?: "))
cost9 = float(input("What is the cost of your 9th item?: "))
cost10 = float(input("What is the cost of your 10th item?: "))
Mdr = float(input("What is the Markdown Discount Rate?: ")) / 100
taxR = float(input("What is the tax rate?: ")) / 100

regularSaleP = cost + cost2 + cost3 + cost4 + cost5 + cost6 + cost7 + cost8 + cost9 + cost10
md = round(regularSaleP * Mdr, 2)
sale = round(regularSaleP - md,2)
tax = sale * taxR
tpp = round(sale + tax, 2)

print()
print()
print()
print("The Regular Selling Price is:", regularSaleP)
print("The Markdown Discount is:", md)
print("The Sale Price is:", sale)
print("The Total Purchase Price of your item is:", tpp)
print("The Tax is:", tax)
print()
print()
print()
