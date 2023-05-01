grade = 0

print("Python - Quiz 5")

print("\n1. What is the logical AND operator?")
print(" ")
print("\ta. and")
print("\tb. &&")
print("\tc. &")
print("\td. +")
print(" ")
choice = input("Enter choice: ")
if choice == "a":
  print("\nCorrect!")
  grade = grade + 20
else:
  print("\nIncorrect!")

print("\n2. What is the logical OR operator?")
print(" ")
print("\ta. ||")
print("\tb. or")
print("\tc. –")
print("\td. ++")
print(" ")
choice = input("Enter choice: ")
if choice == "b":
  print("\nCorrect!")
  grade = grade + 20
else:
  print("\nIncorrect!")

print("\n3. Who developed Python?")
print(" ")
print("\ta. Dennis Ritchie")
print("\tb. Guido van Rossum")
print("\tc. Ada Lovelace")
print("\td. Steve Wozniak")
print(" ")
choice = input("Enter choice: ")
if choice == "b":
  print("\nCorrect!")
  grade = grade + 20
else:
  print("\nIncorrect!")

print("\n4. What does Python use to group together statements into code “blocks”?")
print(" ")
print("\ta. Keywords")
print("\tb. Punctuation")
print("\tc. Indentation")
print("\td. None of the above")
print(" ")
choice = input("Enter choice: ")
if choice == "c":
  print("\nCorrect!")
  grade = grade + 20
else:
  print("\nIncorrect!")

print("\n5. What must a string of characters in Python always be enclosed between?")
print(" ")
print("\ta.	square brackets")
print("\tb.	curly brackets")
print("\tc.	double quote marks or single quote marks")
print("\td.	angled brackets")
print(" ")
choice = input("Enter choice: ")
if choice == "c":
  print("\nCorrect!")
  grade = grade + 20
else:
  print("\nIncorrect!")

print("\nGrade = " + str(grade))