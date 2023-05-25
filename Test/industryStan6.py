grade = 0

print("ISA - Quiz 6")

print("\n1. What do you call a command-line interpreter which lets you interact with your OS and execute Python commands and scripts?")
print(" ")
print("\ta. A console")
print("\tb. Jython")
print("\tc. A compiler")
print("\td. An editor")
print(" ")
choice = input("Enter choice: ")
if choice == "a":
  print("\nCorrect!")
  grade = grade + 20
else:
  print("\nIncorrect!")

print("\n2. What is true about compilation? (Select two answers)")
print(" ")
print("\ta. Both you and the end user must have the compiler to run your code")
print("\tb. It tends to be faster than interpretation")
print("\tc. It tends to be slower than interpretation")
print("\td. The code is converted directly into machine code executable by the processor")
print(" ")
choice = input("Enter choice: ")
if choice == "bd":
  print("\nCorrect!")
  grade = grade + 20
else:
  print("\nIncorrect!")

print("\n3. What are the four fundamental elements that make a language?")
print(" ")
print("\ta. An alphabet, a lexis, phonetics, and semantics")
print("\tb. An alphabet, morphology, phonetics, and semantics")
print("\tc. An alphabet, phonetics, phonology, and semantics")
print("\td. An alphabet, a lexis, a syntax, and semantics")
print(" ")
choice = input("Enter choice: ")
if choice == "d":
  print("\nCorrect!")
  grade = grade + 20
else:
  print("\nIncorrect!")

print("\n4. Select the true statements? (Select two answers)")
print(" ")
print("\ta. Python 3 is backwards compatible with Python 2")
print("\tb. Python is free, open-source, and multiplatform")
print("\tc. Python is a good choice for creating and executing tests for applications")
print("\td. Python is a good choice for low-level programming, e.g. when you want to implement an effective driver")
print(" ")
choice = input("Enter choice: ")
if choice == "bc":
  print("\nCorrect!")
  grade = grade + 20
else:
  print("\nIncorrect!")

print("\n5. What is CPython?")
print(" ")
print("\ta.	It's the default, reference implementation of Python, written in the C language")
print("\tb.	It's a programming language that is a superset of the C language, designed to produce Python-like performance with code written in C")
print("\tc.	It's the default, reference implementation of the C language, written in Python")
print("\td.	It's a programming language that is a superset of Python, designed to produce C-like performance with code written in Python")
print(" ")
choice = input("Enter choice: ")
if choice == "a":
  print("\nCorrect!")
  grade = grade + 20
else:
  print("\nIncorrect!")

print("\nGrade = " + str(grade))