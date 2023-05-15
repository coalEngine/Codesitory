import nltk
from nltk.tokenize import word_tokenize

# Preprocessing
def preprocess(text):
    # Tokenize the text
    tokens = word_tokenize(text.lower())
    # Add any other preprocessing steps if needed
    return tokens

# Define predefined responses
responses = {
    "hello": "Hello!",
    "how are you": "I'm good, thank you!",
    "default": "Sorry, I didn't understand. Can you please rephrase?"

}

# Chatbot logic
def chatbot(user_input):
    # Preprocess user input
    tokens = preprocess(user_input)
    
    # Check for predefined responses
    for token in tokens:
        if token in responses:
            return responses[token]
    
    # If no predefined response matches, return default response
    return responses["default"]

# Main loop
while True:
    user_input = input("User: ")
    if user_input == "i want to leave":
        break
    response = chatbot(user_input)
    print("Chatbot: " + response)