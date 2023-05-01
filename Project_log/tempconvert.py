
def convert(choice, choice2):
    if choice == 'F':
        F = float(input("Please input the Fahrenheit: "))
        if choice2 == 'R':
            print("Rankine: ", F + 459.7)
        elif choice2 == 'C':
            print("Celsius: ", (F - 32) / 1.8)
        else:
            print("Invalid")
    if choice == 'C':
         C = float(input("Please input the Celsius: "))
         if choice2 == 'F':
             print("Fahrenheit: ", (1.8 * C) + 32)
         if choice2 == 'K':
             print("Kelvin: ", C + 273.2)
    if choice == 'R':
        pass
def intro():
    choice = input("What do you want to convert?: ")
    choice2 = input("To?: ")
    convert(choice, choice2)

intro()