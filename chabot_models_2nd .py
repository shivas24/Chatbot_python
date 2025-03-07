

# Simple Customer Support Chatbot
import pprint
from Chatbot_python.data import smartwatch as d  # Importing the class

# Create an instance of the Smartwatch class and call the method

responses = d.smartwatch_datafile()


def get_bot_response(user_input):
    user_input = user_input.lower()
    
    for keyword, response in responses.items():
        if user_input in keyword:
            return response
        elif user_input in response:
            return response

    return "I'm not sure how to respond to that. Can you try asking something else?"

while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit", "bye", "goodbye", " ", "close", "end"]:
        print("Bot: Goodbye! If you have any more questions, we're here to help.")
        break

    response = get_bot_response(user_input)
    pprint.pprint(f"Bot: {response}")  # Use pprint.pprint correctly
    print()
