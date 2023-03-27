r = float(input("What is the rate?: ")) / 1200
prin = float(input("What is the Principal Amount?: "))
numMonth = int(input("What is the amount of months?: ")) * 12
mp = prin * (r + (r /(pow(1+r, numMonth) - 1)))
print("The Monthly Payment would be ${}".format(round(mp, 2)))