grade = 0

print("ISA - Quiz 3")

print("\n1. The 0o prefix means that the number after it is denoted as:")
print(" ")
print("\ta. decimal")
print("\tb. hexadecimal")
print("\tc. octal")
print("\td. binary")
print(" ")
choice = input("Enter choice: ")
if choice == "c":
  print("\nCorrect!")
  grade = grade + 20
else:
  print("\nIncorrect!")

print("\n2. What is the output of the following snippet?")
print(" ")
print("y = 2 + 3 * 5")
print("print(Y)")
print(" ")
print("\ta. 17")
print("\tb. 17.0")
print("\tc. the snippet will cause an execution error")
print("\td. 25")
print(" ")
choice = input("Enter choice: ")
if choice == "c":
  print("\nCorrect!")
  grade = grade + 20
else:
  print("\nIncorrect!")

print("\n3. The \\n digraph forces the print() function to:")
print(" ")
print("\ta. stop its execution")
print("\tb. break the output line")
print("\tc. output exactly two characters: \ and n")
print("\td. duplicate the character next to the digraph")
print(" ")
choice = input("Enter choice: ")
if choice == "b":
  print("\nCorrect!")
  grade = grade + 20
else:
  print("\nIncorrect!")

print("\n4. The result of the following division:")
print(" ")
print("1 / 1")
print(" ")
print("\ta. is equal to 1")
print("\tb. cannot be evaluated")
print("\tc. cannot be predicted")
print("\td. is equal to 1.0")
print(" ")
choice = input("Enter choice: ")
if choice == "d":
  print("\nCorrect!")
  grade = grade + 20
else:
  print("\nIncorrect!")

print("\n5. The print() function can output values of:")
print(" ")
print("\ta.	any number of arguments (including zero)")
print("\tb.	just one argument")
print("\tc.	not more than five arguments")
print("\td.	any number of arguments (excluding zero")
print(" ")
choice = input("Enter choice: ")
if choice == "a":
  print("\nCorrect!")
  grade = grade + 20
else:
  print("\nIncorrect!")

print("\nGrade = " + str(grade))