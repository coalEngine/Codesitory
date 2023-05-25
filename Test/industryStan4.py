grade = 0

print("ISA - Quiz 4")

print("\n1. Which of the following statements are true? (Select two answers)")
print(" ")
print("\ta. Addition precedes multiplication")
print("\tb. The ** operator uses right-sided binding")
print("\tc. The right argument of the % operator cannot be zero")
print("\td. The result of the / operator is always an integer value")
print(" ")
choice = input("Enter choice: ")
if choice == "bc":
  print("\nCorrect!")
  grade = grade + 20
else:
  print("\nIncorrect!")

print("\n2. The ** operator:")
print(" ")
print("\ta. performs floating-point multiplication")
print("\tb. performs duplicated multiplication")
print("\tc. performs exponentiation")
print("\td. does not exist")
print(" ")
choice = input("Enter choice: ")
if choice == "c":
  print("\nCorrect!")
  grade = grade + 20
else:
  print("\nIncorrect!")

print("\n3. What is the output of the following snippet if the user enters two lines containing 2 and 4 respectively?")
print(" ")
print("x = input())")
print("y = input())")
print("print(x + y)")
print(" ")
print("\ta. 4")
print("\tb. 2")
print("\tc. 6")
print("\td. 24")
print(" ")
choice = input("Enter choice: ")
if choice == "d":
  print("\nCorrect!")
  grade = grade + 20
else:
  print("\nIncorrect!")

print("\n4. What is the output of the following snippet if the user enters two lines containing 2 and 4 respectively?")
print(" ")
print("x = int(input())")
print("y = int(input())")
print("print(x + y)")
print(" ")
print("\ta. 24")
print("\tb. 6")
print("\tc. 2")
print("\td. 4")
print(" ")
choice = input("Enter choice: ")
if choice == "b":
  print("\nCorrect!")
  grade = grade + 20
else:
  print("\nIncorrect!")

print("\n5. What is the output of the following snippet if the user enters two lines containing 2 and 4 respectively?")
print(" ")
print("x = int(input())")
print("y = int(input())")
print("x = x / y")
print("y = y / x")
print("print(y)")
print(" ")
print("\ta.	8.0")
print("\tb.	2.0")
print("\tc.	the code will cause a runtime error")
print("\td.	4.0")
print(" ")
choice = input("Enter choice: ")
if choice == "a":
  print("\nCorrect!")
  grade = grade + 20
else:
  print("\nIncorrect!")

print("\nGrade = " + str(grade))