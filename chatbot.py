
# Basic Rule-Based Chatbot

def chatbot_response(user_input):

    user_input = user_input.lower().strip()

    if user_input in ["hello", "hi", "hey"]:
        return "Hi! Welcome. How can I help you?"

    elif "how are you" in user_input:
        return "I'm fine, thanks! How are you?"

    elif "what is your name" in user_input:
        return "I'm Python Chatbot, your virtual assistant!"

    elif "what can you do" in user_input:
        return "I can answer simple questions and chat with you."

    elif "thank you" in user_input or "thanks" in user_input:
        return "You're welcome!"

    elif user_input in ["bye", "goodbye", "exit"]:
        return "Goodbye! Have a nice day!"

    else:
        return "Sorry, I don't understand that. Please try again."


# Main chatbot function
def start_chatbot():

    print("================================")
    print("       PYTHON CHATBOT")
    print("================================")
    print("Hello! I am your chatbot.")
    print("Type 'bye' to exit the chat.")

    while True:

        user_input = input("\nYou: ")

        response = chatbot_response(user_input)

        print("Bot:", response)

        if user_input.lower().strip() in ["bye", "goodbye", "exit"]:
            break


# Start the chatbot
start_chatbot()
