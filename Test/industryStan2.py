grade = 0

print("ISA - Quiz 2")

print("\n1. What is the output of the following snippet?")
print(" ")
print("z = y = x = 1")
print("print(x, y, z, sep='*')")
print(" ")
print("\ta. x*y*z")
print("\tb. x y z")
print("\tc. 1*1*1")
print("\td. 1 1 1")
print(" ")
choice = input("Enter choice: ")
if choice == "c":
  print("\nCorrect!")
  grade = grade + 20
else:
  print("\nIncorrect!")

print("\n2. What is the output of the following snippet?")
print(" ")
print("x = 1")
print("y = 2")
print("z = x")
print("x = y")
print("y = z")
print("print(x, y)")
print(" ")
print("\ta. 1 1")
print("\tb. 2 2")
print("\tc. 2 1")
print("\td. 1 2")
print(" ")
choice = input("Enter choice: ")
if choice == "c":
  print("\nCorrect!")
  grade = grade + 20
else:
  print("\nIncorrect!")

print("\n3. Left-sided binding determines that the result of the following expression:")
print(" ")
print("1 // 2 * 3")
print("is equal to:")
print(" ")
print("\ta. 4.5")
print("\tb. 0.16666666666666666")
print("\tc. 0")
print("\td. 0.0")
print(" ")
choice = input("Enter choice: ")
if choice == "c":
  print("\nCorrect!")
  grade = grade + 20
else:
  print("\nIncorrect!")

print("\n4. What is the output of the following snippet?")
print(" ")
print("x = 1 / 2 + 3 // 3 + 4 ** 2")
print("print(x)")
print(" ")
print("\ta. 17")
print("\tb. 17.5")
print("\tc. 8.5")
print("\td. 8")
print(" ")
choice = input("Enter choice: ")
if choice == "b":
  print("\nCorrect!")
  grade = grade + 20
else:
  print("\nIncorrect!")

print("\n5. What is the output of the following snippet if the user enters two lines containing 11 and 4 respectively?")
print(" ")
print("x = int(input())")
print("y = int(input())")
print("x = x % y")
print("x = x % y")
print("y = y % x")
print("print(y)")
print(" ")
print("\ta.	1")
print("\tb.	4")
print("\tc.	3")
print("\td.	2")
print(" ")
choice = input("Enter choice: ")
if choice == "a":
  print("\nCorrect!")
  grade = grade + 20
else:
  print("\nIncorrect!")

print("\nGrade = " + str(grade))