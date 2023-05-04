num = int(input("How many do you want to display?: "))
def cubed(numDisplay):
    num = 1
    count = 0
    while count < numDisplay:
        print(num * num * num, " ", end="")
        num += 1
        count += 1
cubed(num)