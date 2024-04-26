import tkinter as tk
import ChatModel as model

root = tk.Tk()
root.grid_anchor(anchor="center")
root.title(string="Insight Craft")
root.minsize(width=600,height=600)

bot_response = tk.StringVar()
question = tk.StringVar()
messages = tk.StringVar()
prompts = ["User: Hello", "Bot: Hi"]
messages.set(value=prompts)

def add_answer():
    bot_response = model.get_response(prompt=question.get())
    global prompts
    prompts.append("User: " + question.get())
    prompts.append("Bot: " + bot_response)
    messages.set(prompts)

listbox = tk.Listbox(root, listvariable=messages, height = 20, width = 150)
listbox.grid(row = 0, column = 0,padx=10,pady=10)

# Create an entry widget
prompt_field = tk.Entry(root, width=50, textvariable=question).grid()

send_button = tk.Button(root, text="Send", command=add_answer).grid()

root.mainloop()
