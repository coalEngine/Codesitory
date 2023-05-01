grade = 0

print("Python - Quiz 2")

print("\n1. Which of the following is the correct way to initialize variables named “a”, “b”, and “c” with numeric values of one, two, and three respectively?")
print(" ")
print("\ta.	a , b , c = = 1 , 2 , 3")
print("\tb.	a , b , c = 1 , 2 , 3")
print("\tc.	1 , 2 , 3 = a , b , c")
print("\td.	1 , 2 , 3 = = a , b , c")
print(" ")
choice = input("Enter choice: ")
if choice == "b":
  print("\nCorrect!")
  grade = grade + 20
else:
  print("\nIncorrect!")

print("\n2. What starts a comment in Python?")
print(" ")
print("\ta.	//")
print("\tb.	?")
print("\tc.	!")
print("\td.	#")
print(" ")
choice = input("Enter choice: ")
if choice == "d":
  print("\nCorrect!")
  grade = grade + 20
else:
  print("\nIncorrect!")

print("\n3. What operator performs floor division in a Python program?")
print(" ")
print("\ta. //")
print("\tb. ÷")
print("\tc. *")
print("\td. /")
print(" ")
choice = input("Enter choice: ")
if choice == "a":
  print("\nCorrect!")
  grade = grade + 20
else:
  print("\nIncorrect!")

print("\n4. What operator returns the remainder of division?")
print(" ")
print("\ta.	%")
print("\tb.	/")
print("\tc.	÷")
print("\td.	remainder")
print(" ")
choice = input("Enter choice: ")
if choice == "a":
  print("\nCorrect!")
  grade = grade + 20
else:
  print("\nIncorrect!")

print("\n5. Which of the following assigns a string value to the variable?")
print(" ")
print("\ta.	var = 8")
print("\tb.	var = 3.142")
print("\tc.	var = ‘Python in easy steps’")
print("\td.	var = True")
print(" ")
choice = input("Enter choice: ")
if choice == "c":
  print("\nCorrect!")
  grade = grade + 20
else:
  print("\nIncorrect!")

print("\nGrade = " + str(grade))