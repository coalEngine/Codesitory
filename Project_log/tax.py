taxR = float(input("What is the tax rate?: ")) / 100
cost = float(input("What is the cost of your item?: "))
tax = cost * taxR
tpp = round(cost + tax, 2)


print("The Total Purchase Pricee of your item is:", tpp)