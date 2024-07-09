import nltk
import re
from nltk.chat.util import Chat, reflections

# Define chatbot responses using pattern-response pairs
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"hi|hello|vanakkam",
        ["itho vanthuttanla en chellam vanthuttanla",]
    ],
    [
        r"what is your name?",
        ["My name is ChatBot and I'm here to help you.",]
    ],
    [
        r"how are you?",
        ["I'm doing good\nHow about You ?",]
    ],
    [
        r"who is your friend?",
        ["Gopalu irukkanla gopalu",]
    ],
    [
        r"do you earn?",
        ["Beta engamma tharanga pongalum puliyotharaiyum potu samalichuranga",]
    ],
    [
        r"today's weather report",
        ["intha pakkam paatha soonu mazhai...seri nu intha pakkam patha soo nu mazhai",]
    ],
    [
        r"sorry (.*)",
        ["It's alright","It's OK, never mind",]
    ],
    [
        r"(.*) (good|well|fine)",
        ["That's good to hear", "Nice to hear that",]
    ],
    [
        r"varataaahhh....",
        ["poda dei poda.. posa ketta paya"]
    ],
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

def chatbot_response(input_text):
    return chatbot.respond(input_text)

# Main function to run the chatbot
if __name__ == "__main__":
    print("Welcome to ChatBot! Start chatting with the bot (type quit to exit).")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("ChatBot:", response)
        if user_input.lower() == "quit":
            break