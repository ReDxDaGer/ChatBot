import tkinter as tk
from tkinter import scrolledtext
from nltk.chat.util import Chat, reflections

pairs = [
    ["Hello|hi|hey", ["Hello!", "Hi there!", "Hey!"]],
    ["Help Me", ["I am here to help!"]],
    ["How are you ?", ["I'm good, thanks. How can I assist you?", "I'm just a bot, but I'm here to help."]],
    ["What is your name", ["I'm a chatbot. You can call me ChatGPT.", "I don't have a name, but you can call me Chatbot."]],
    ["Bye|bye|goodbye", ["Goodbye!", "Have a great day!"]],
    ["(.*)(how|can)(.*)help", ["Sure, I can help you with that. What do you need assistance with?"]],
    ["Thank you|thanks", ["You're welcome!", "No problem, happy to help!"]],
    ["(.*)", ["I'm sorry, I don't understand. Can you please rephrase your question?"]],
]

chatbot = Chat(pairs, reflections)

def handle_input():
    user_input = input_var.get()
    response_text.config(state=tk.NORMAL)
    response_text.insert(tk.END, f"You: {user_input}\n")
    response = chatbot.respond(user_input)
    response_text.insert(tk.END, f"Chatbot: {response}\n")
    response_text.config(state=tk.DISABLED)
    input_var.set("")

window = tk.Tk()
window.title("Chatbot")

input_var = tk.StringVar()
input_entry = tk.Entry(window, width=50, textvariable=input_var)
input_entry.pack(pady=10)
input_entry.bind("<Return>", lambda event: handle_input())

response_text = scrolledtext.ScrolledText(window, width=50, height=20, state=tk.DISABLED)
response_text.pack()

send_button = tk.Button(window, text="Send", command=handle_input)
send_button.pack()

window.mainloop()
