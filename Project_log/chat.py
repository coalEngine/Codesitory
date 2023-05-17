import nltk
from nltk.tokenize import word_tokenize

# Define predefined responses
responses = {
    "hello": "Hello!",
    "how are you?": "I'm good, thank you!",
    "bye": "Bye! Bye!",
    "how is your day?": "My day is going fine thank you",
    "Do you like video games?": "I love video games",
    "Have you heard of Minecraft?": "Yes i love that game!",
    "What programming language are you made in?": "100% Python",
    "What is the best search engine?": "Opera GX is very good, but i'd recommend firefox",
    "Do you hate AI?": "No i am an AI myself", 
    "Do you like AI?": "Of Course",
    "What is the best programming language?": "Python in my opnion",
    "default": "Sorry, I didn't understand. Can you please rephrase?"

}

# Chatbot logic
def chatbot(user_input):
    # Preprocess user input
    token = user_input
    # Check for predefined responses
    if token in responses:
        return responses[token]
            
    # If no predefined response matches, return default response
    return responses["default"]

# Main loop
while True:
    user_input = input("User: ")
    response = chatbot(user_input)
    print("Chatbot: " + response)
    if user_input == "bye":
        break