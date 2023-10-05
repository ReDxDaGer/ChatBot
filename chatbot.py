import nltk
from nltk.chat.util import Chat, reflections


pairs = [
    ["Hello|hi|hey", ["Hello!", "Hi there!", "Hey!"]],
    ["sex krwado", ["mere sath he krloo uwu!!"]],
    ["How are you ?", ["I'm good, thanks. How can I assist you?", "I'm just a bot, but I'm here to help."]],
    ["What is your name", ["I'm a chatbot. You can call me ChatGPT.", "I don't have a name, but you can call me Chatbot."]],
    ["Bye|bye|goodbye", ["Goodbye!", "Have a great day!"]],
    ["(.*)(how|can)(.*)help", ["Sure, I can help you with that. What do you need assistance with?"]],
    ["(.*)", ["I'm sorry, I don't understand. Can you please rephrase your question?"]],
]

chatbot = Chat(pairs, reflections)
print("Hello! I'm your chatbot. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye!")
        break
    response = chatbot.respond(user_input)
    print("Chatbot:", response)