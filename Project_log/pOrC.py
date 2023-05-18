

num = int(input("Enter a number: "))
if num == 1:
    print("Number cannot be 1")
def prime_or_comp(num):
    if num % 2 == 0:
        print("Number is Composite")
    else:
        print("Number is Prime")
prime_or_comp(num)