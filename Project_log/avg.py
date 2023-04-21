avg = 0
rangee = 10
nums = []
for _ in range(rangee):
    ask = float(input("Number: "))
    avg += ask
    nums.append(ask)
trueAvg = avg / rangee
print("\nThe Average is", trueAvg)
print("\nYour lowest grade was:", min(nums))
print("\nYour highest grade was:", max(nums))

if trueAvg >= 65:
    print("\nYou passed the class")
else:
    print("\nYou failed the class")




    