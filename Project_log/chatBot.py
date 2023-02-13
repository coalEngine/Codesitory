question_1 = input("What is your name? ")
print("Hello " + question_1)


question_2 = input("How is your day today?: ")
if question_2 == 'Bad':
    print("I'm sorry to hear that")
elif question_2 == 'Good':
    print("Great!")


question_3 = input("What is your favorite food?: ")
print("I like " + question_3 + " too!")


question_4 = input("What is your favorite drink?: ")
print("I haven't tried " + question_4 + " yet but it sounds nice")

question_5 = input("What programming language am i coded in?: ")
if question_5 == "Python":
    print("Correct!")
else:
    print("Not quite!")

question_6 = int(input("How old is Python? (Years): "))
if question_6 == 31:
    print("That's right!")
else: 
    print("Nope")
