grade = 0

print("Python - Quiz 3")

print("\n1. Which of the following assigns a Boolean value to the variable?")
print(" ")
print("\ta.	var = 8")
print("\tb.	var = 3.142")
print("\tc.	var = ‘Python in easy steps’")
print("\td.	var = True")
print(" ")
choice = input("Enter choice: ")
if choice == "d":
  print("\nCorrect!")
  grade = grade + 20
else:
  print("\nIncorrect!")

print("\n2. What starts and ends a multiple-line comment?")
print(" ")
print("\ta.	“““ and ”””")
print("\tb.	### and ###")
print("\tc.	??? and ???")
print("\td.	!!! and !!!")
print(" ")
choice = input("Enter choice: ")
if choice == "a":
  print("\nCorrect!")
  grade = grade + 20
else:
  print("\nIncorrect!")

print("\n3. What function accepts a string within its parentheses that will prompt the user for input by displaying that string then wait to read a line of input?")
print(" ")
print("\ta.	read()")
print("\tb.	in()")
print("\tc.	prompt()")
print("\td.	input()")
print(" ")
choice = input("Enter choice: ")
if choice == "d":
  print("\nCorrect!")
  grade = grade + 20
else:
  print("\nIncorrect!")

print("\n4. What is the logical NOT operator?")
print(" ")
print("\ta.	*")
print("\tb.	!")
print("\tc.	not")
print("\td.	< >")
print(" ")
choice = input("Enter choice: ")
if choice == "c":
  print("\nCorrect!")
  grade = grade + 20
else:
  print("\nIncorrect!")

print("\n5. What function converts integer x to a hexadecimal string?")
print(" ")
print("\ta.	hx(x)")
print("\tb.	h(x)")
print("\tc.	hexadecimal(x)")
print("\td.	hex(x)")
print(" ")
choice = input("Enter choice: ")
if choice == "d":
  print("\nCorrect!")
  grade = grade + 20
else:
  print("\nIncorrect!")

print("\nGrade = " + str(grade))