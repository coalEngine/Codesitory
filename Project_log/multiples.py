number = int(input("What is the number?: "))
number_of_multiple = 1
multiple = 0
num_time = int(input("How many times do you want to multiple?: "))
while (number_of_multiple <= num_time):
    multiple = number * number_of_multiple
    print(multiple)
    number_of_multiple = number_of_multiple + 1
print(".\n.\n.")