
def convert(choice, choice2):
    if choice == 'F':
        F = float(input("Please input the Fahrenheit: "))
        if choice2 == 'R':
            print("Rankine: ", F + 459.7)
        elif choice2 == 'C':
            print("Celsius: ", (F - 32) / 1.8)
        elif choice2 == "K":
            print("Kelvin: ", (F- 459.67) / (5/9))
        else:
            print("Invalid")
    if choice == 'C':
         C = float(input("Please input the Celsius: "))
         if choice2 == 'F':
             print("Fahrenheit: ", (1.8 * C) + 32)
         if choice2 == 'K':
             print("Kelvin: ", C + 273.2)
         if choice2 == "R":
            print("Rankine: ", (C + 273.15) * 1.8)
    if choice == 'R':
        R = float(input("Please input the Rankine: "))
        if choice2 == 'F':
            print("Fahreheit: ",  R - 459.67)
        if choice2 == 'K':
            print("Kelvin: ", R / 1.8)
        if choice2 == 'C':
            print("Celsius: ", (R / (9/5)) - 491.67)
    if choice == 'K':
         K = float(input("Please input the Kelvin: "))
         if choice2 == 'C':
             print("Celsius: ", K - 273.15)
         if choice2 == 'R':
             print("Rankine: ", K * (9/5))
         if choice2 == 'F':
             print("Fahrenheit: ", (K * (9/5)) - 459.67)
         
def intro():
    choice = input("What do you want to convert?: ")
    choice2 = input("To?: ")
    convert(choice, choice2)

intro()