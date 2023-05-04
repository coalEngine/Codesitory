amount = int(input("How long should this go on for?: "))
def sequence(amount):
    num = 1
    added = 2
    count = 0
    print(str(num) + ", ", end="")
    while count < amount:
        num = num + added
        print(str(num) + ", ", end="")
        added += 1
        count += 1
sequence(amount)