print("🤖 Hello! I am your simple chatbot. Type 'bye' to exit.\n ")

responses = {
    "hello": "Hi there!",
    "how are you": "I'm just a program, but I'm doing fine!",
    "what is your name": "I'm PyBot, your friendly assistant.",
    "bye": "Goodbye! Have a nice day!"
}

while True:
    user_input = input("You: ").lower()

    if user_input == "bye":
        print("Bot:", responses["bye"])
        break

    response = responses.get(user_input, "I don't understand that. Try something else.")
    print("Bot:", response)
