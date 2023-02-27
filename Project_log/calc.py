

num1 = 0
num2 = 0
num1 = input("Enter Number 1: ")
num2 = input("Enter Number 2: ")
operator = input("What operator do you want: ")


if operator == "+":
    answer = int(num1) + int(num2)
elif operator == "-":
    answer = int(num1) - int(num2)
elif operator == "*":
    answer = int(num1) * int(num2)
elif operator == "/":
    answer = int(num1) / int(num2)
else:
    print("Invalid Operator")


print("Answer:", answer)
