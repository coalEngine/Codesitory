R = float(input("\n\n\n\nAmount of regular withdrawal: "))
i = float(input("Nominal interest rate: ")) / 100
N = int(input("Number of withdrawals per year: "))
Y = int(input("Number of years: "))
P = ((R * N) / i) * (1 - (1 / (pow((1 + (i/N)),(N* Y) ))))
print("\n\n\n\nMinimum Investment: {}\n\n\n".format(round(P, 2)))