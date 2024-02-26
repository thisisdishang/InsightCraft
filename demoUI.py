import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def on_button_click():
    label.config(text="Hello, " + entry.get())

# Create the main window
root = tk.Tk()
root.title("InsightCraft")

# Create a style object
style = ttk.Style()

# Configure the style to use a modern theme
style.theme_use('clam')

# Create a label
label = ttk.Label(root, text="Welcome to InsightCraft",font=("Times New Roman",20))
label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Add image
image = Image.open("1742.jpg")  # Replace "example_image.png" with your image file
image = image.resize((400, 400), Image.ADAPTIVE)
photo = ImageTk.PhotoImage(image)
image_label = ttk.Label(root, image=photo)
image_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Create a label
label = ttk.Label(root, text="Ask the question:")
label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Create an entry widget
entry = ttk.Entry(root,width=50)
entry.grid(row=3, column=0,columnspan=2, padx=10, pady=10)

# Create a button
button = ttk.Button(root, text="Let's go", command=on_button_click)
button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Start the main event loop
root.mainloop()
