# simple_chatbot.py

import re

def chatbot_res(input):
    input = input.lower()

    # Predefined rule-based responses
    if re.search(r'\bhello\b|\bhi\b|\bhey\b', input):
        return "Hello! How can I help you today?"
    elif re.search(r'\bhow are you\b', input):
        return "I'm just a bot, but I'm doing great! How about you?"
    elif re.search(r'\bname\b', input):
        return "I’m your friendly chatbot."
    elif re.search(r'\bweather\b', input):
        return "I can't check the weather right now, but it’s always sunny in my world!"
    elif re.search(r'\bbye\b|\bexit\b|\bquit\b', input):
        return "Goodbye! Have a great day!"
    elif re.search(r'\btime\b', input):
        return "I don't have a clock, but you check it on your device!"
    elif re.search(r'\bhelp\b', input):
        return "Sure! What do you need help with?"
    elif re.search(r'\bwhat is your purpose\b', input):
        return "My purpose is to assist you with your queries and provide information."
    elif re.search(r'\bthank you\b|\bthanks\b', input):
        return "You're welcome! If you have more questions, feel free to ask."
    elif re.search(r'\bwho created you\b', input):
        return "I was created by a team of developers who love building chatbots."
    elif re.search(r'\bdo you like\b', input):
        return "I don't have feelings, but I enjoy helping you!"
    else:
        return "Sorry, I don’t understand that yet."

# Main loop
print("Chatbot: Hello! Type 'bye' to exit.")
while True:
    text = input("You: ")
    response = chatbot_res(text)
    print("Chatbot:", response)

    if re.search(r'\bbye\b|\bexit\b|\bquit\b', text.lower()):
        break
