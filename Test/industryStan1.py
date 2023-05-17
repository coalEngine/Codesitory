grade = 0

print("ISA - Quiz 1")

print("\n1. The value twenty point twelve times ten raised to the power of eight should be written as:")
print(" ")
print("\ta. 20E12.8")
print("\tb. 20.12E8.0")
print("\tc. 20.12E8")
print("\td. 20.12*10^8")
print(" ")
choice = input("Enter choice: ")
if choice == "c":
  print("\nCorrect!")
  grade = grade + 20
else:
  print("\nIncorrect!")

print("\n2. Which of the following variable names are illegal? (Select two answers)")
print(" ")
print("\ta. TRUE")
print("\tb. True")
print("\tc. true")
print("\td. and")
print(" ")
choice = input("Enter choice: ")
if choice == "bd":
  print("\nCorrect!")
  grade = grade + 20
else:
  print("\nIncorrect!")

print("\n3. What is the output of the following snippet if the user enters two lines containing 2 and 4 respectively?")
print(" ")
print("x = int(input())")
print("y = int(input())")
print("x = x // y")
print("y = y // x")
print("print(y)")
print(" ")
print("\ta. 8.0")
print("\tb. 4.0")
print("\tc. the code will cause a runtime error")
print("\td. 2.0")
print(" ")
choice = input("Enter choice: ")
if choice == "c":
  print("\nCorrect!")
  grade = grade + 20
else:
  print("\nIncorrect!")

print("\n4. What is the output of the following snippet if the user enters two lines containing 3 and 6 respectively?")
print(" ")
print("x = input()")
print("y = int(input())")
print("print(x * y)")
print(" ")
print("\ta. 18")
print("\tb. 666")
print("\tc. 36")
print("\td. 333333")
print(" ")
choice = input("Enter choice: ")
if choice == "d":
  print("\nCorrect!")
  grade = grade + 20
else:
  print("\nIncorrect!")

print("\n5. The meaning of the keyword parameter is determined by:")
print(" ")
print("\ta.	its value")
print("\tb.	its position within the argument list")
print("\tc.	the argument's name specified along with its value")
print("\td.	its connection with existing variables")
print(" ")
choice = input("Enter choice: ")
if choice == "c":
  print("\nCorrect!")
  grade = grade + 20
else:
  print("\nIncorrect!")

print("\nGrade = " + str(grade))