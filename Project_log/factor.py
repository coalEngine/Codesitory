userNum = int(input("Number?: "))

n = 1
while (n <= userNum):
    if userNum % n == 0:
        print(n)
    n = n + 1

