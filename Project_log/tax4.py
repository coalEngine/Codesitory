print()
print()
print()
print()
cost = float(input("What is the cost of your item?: "))
quantity1 = int(input("Quantity?: "))
cost2 = float(input("What is the cost of your 2nd item?: "))
quantity2 = int(input("Quantity?: "))
cost3 = float(input("What is the cost of your 3rd  item?: "))
quantity3 = int(input("Quantity?: "))
cost4 = float(input("What is the cost of your 4th item?: "))
quantity4 = int(input("Quantity?: "))
cost5 = float(input("What is the cost of your 5th item?: "))
quantity5 = int(input("Quantity?: "))
cost6 = float(input("What is the cost of your 6th item?: "))
quantity6 = int(input("Quantity?: "))
cost7 = float(input("What is the cost of your 7th item?: "))
quantity7 = int(input("Quantity?: "))
cost8 = float(input("What is the cost of your 8th item?: "))
quantity8 = int(input("Quantity?: "))
cost9 = float(input("What is the cost of your 9th item?: "))
quantity9 = int(input("Quantity?: "))
cost10 = float(input("What is the cost of your 10th item?: "))
quantity10 = int(input("Quantity?: "))
Mdr = float(input("What is the Markdown Discount Rate?: ")) / 100
taxR = float(input("What is the tax rate?: ")) / 100

regularSaleP = (cost * quantity1) + (cost2 * quantity2) + (cost3 * quantity3) + (cost4 * quantity4) + (cost5 * quantity5) + (cost6 * quantity6) + (cost7 * quantity7) + (cost8 * quantity8) + (cost9 * quantity9) +  (cost10 * quantity10) 
md = round(regularSaleP * Mdr, 2)
sale = round(regularSaleP - md,2)
tax = sale * taxR
tax = round(tax)
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
