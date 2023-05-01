grade = 0

print("Python - Quiz 4")

print("\n1. What operator performs multiplication in a Python program?")
print(" ")
print("\ta. /")
print("\tb. ×")
print("\tc. *")
print("\td. %")
print(" ")
choice = input("Enter choice: ")
if choice == "c":
  print("\nCorrect!")
  grade = grade + 20
else:
  print("\nIncorrect!")

print("\n2. Which of the following is the correct syntax of a conditional expression?")
print(" ")
print("\ta. c = a if (a < b) else c = b")
print("\tb. c = a if (a < b) else b")
print("\tc. a if (a < b) else b = c")
print("\td. a = c if (a < b) else b = c")
print(" ")
choice = input("Enter choice: ")
if choice == "b":
  print("\nCorrect!")
  grade = grade + 20
else:
  print("\nIncorrect!")

print("\n3. What function converts x to an integer whole number?")
print(" ")
print("\ta.	int(x)")
print("\tb.	float(x)")
print("\tc.	str(x)")
print("\td.	chr(x)")
print(" ")
choice = input("Enter choice: ")
if choice == "a":
  print("\nCorrect!")
  grade = grade + 20
else:
  print("\nIncorrect!")

print("\n4. What function converts x to a string representation?")
print(" ")
print("\ta.	int(x)")
print("\tb.	float(x)")
print("\tc.	str(x)")
print("\td.	chr(x)")
print(" ")
choice = input("Enter choice: ")
if choice == "c":
  print("\nCorrect!")
  grade = grade + 20
else:
  print("\nIncorrect!")

print("\n5. Which of the following is equivalent to a = a + b?")
print(" ")
print("\ta. a =+ b")
print("\tb. a += b")
print("\tc. b = a + a")
print("\td. a = a – b")
print(" ")
choice = input("Enter choice: ")
if choice == "b":
  print("\nCorrect!")
  grade = grade + 20
else:
  print("\nIncorrect!")

print("\nGrade = " + str(grade))