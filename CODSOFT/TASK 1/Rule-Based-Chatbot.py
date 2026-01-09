def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user = input("You: ").lower()

        if user == "bye":
            print("Chatbot: Goodbye! Have a nice day.")
            break

        elif "hello" in user or "hi" in user:
            print("Chatbot: Hello! How can I help you?")

        elif "how are you" in user:
            print("Chatbot: I'm doing great! Thanks for asking.")

        elif "name" in user:
            print("Chatbot: I am a rule-based chatbot.")

        elif "help" in user:
            print("Chatbot: I can answer simple questions.")

        else:
            print("Chatbot: Sorry, I don't understand that.")

chatbot()