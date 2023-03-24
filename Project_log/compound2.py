p = float(input("Principal Amount: "))
n = int(input("Number of Times compounded: "))
r = 0.01
onePer = "  ${}\t      ${}\t      ${}\t      ${}".format(round(p * (1 + (r/n)) ** (n * 1), 2), round(p * (1 + (r/n)) ** (n * 5), 2), round(p * (1 + (r/n)) ** (n * 10), 2), round(p * (1 + (r/n)) ** (n * 20), 2))
r = 0.05
fivePer = "  ${}\t      ${}\t      ${}\t      ${}".format(round(p * (1 + (r/n)) ** (n * 1), 2), round(p * (1 + (r/n)) ** (n * 5), 2), round(p * (1 + (r/n)) ** (n * 10), 2), round(p * (1 + (r/n)) ** (n * 20), 2))
r = 0.07
sevenPer = "  ${}\t      ${}\t      ${}\t      ${}".format(round(p * (1 + (r/n)) ** (n * 1), 2), round(p * (1 + (r/n)) ** (n * 5), 2), round(p * (1 + (r/n)) ** (n * 10), 2), round(p * (1 + (r/n)) ** (n * 20), 2))
r = 0.10
tenPer = "  ${}\t      ${}\t      ${}\t      ${}".format(round(p * (1 + (r/n)) ** (n * 1), 2), round(p * (1 + (r/n)) ** (n * 5), 2), round(p * (1 + (r/n)) ** (n * 10), 2), round(p * (1 + (r/n)) ** (n * 20), 2))
print("\t1\t\t5\t\t10\t\t20") 
print("1% {}\n\n5% {}\n\n7% {}\n\n10%{}".format(onePer, fivePer, sevenPer, tenPer))

