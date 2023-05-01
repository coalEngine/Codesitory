grade = 0

print("Python - Quiz 1")

print("\n1. What file extension are Python programs saved as?")
print(" ")
print("\ta.	.py")
print("\tb.	.python")
print("\tc.	.pyt")
print("\td.	.pyth")
print(" ")
choice = input("Enter choice: ")
if choice == "a":
  print("\nCorrect!")
  grade = grade + 20
else:
  print("\nIncorrect!")

print("\n2. What function is used to specify the message within its parentheses?")
print(" ")
print("\ta.	print()")
print("\tb.	out()")
print("\tc.	write()")
print("\td.	output()")
print(" ")
choice = input("Enter choice: ")
if choice == "a":
  print("\nCorrect!")
  grade = grade + 20
else:
  print("\nIncorrect!")

print("\n3. Which of the following assigns an integer value to the variable?")
print(" ")
print("\ta.	var = 8")
print("\tb.	var = 3.142")
print("\tc.	var = ‘Python in easy steps’")
print("\td.	var = True")
print(" ")
choice = input("Enter choice: ")
if choice == "a":
  print("\nCorrect!")
  grade = grade + 20
else:
  print("\nIncorrect!")

print("\n4. Which of the following assigns a float value to the variable?")
print(" ")
print("\ta.	var = 8")
print("\tb.	var = 3.142")
print("\tc.	var = ‘Python in easy steps’")
print("\td.	var = True")
print(" ")
choice = input("Enter choice: ")
if choice == "b":
  print("\nCorrect!")
  grade = grade + 20
else:
  print("\nIncorrect!")

print("\n5. Which of the following is the correct way to initialize variables named “a”, “b”, and “c” each with a numeric value of eight?")
print(" ")
print("\ta.	a = b = c = 8")
print("\tb.	8 = = a = = b = = c")
print("\tc.	8 = a = b = c")
print("\td.	a = = b = = c = = 8")
print(" ")
choice = input("Enter choice: ")
if choice == "a":
  print("\nCorrect!")
  grade = grade + 20
else:
  print("\nIncorrect!")

print("\nGrade = " + str(grade))