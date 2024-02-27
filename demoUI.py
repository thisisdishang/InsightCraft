import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import Model

# Create the main window
root = tk.Tk()
root.title("InsightCraft")
root.minsize(600,600)

result = tk.StringVar()

def onSearchButtonClick():
    global result
    result = Model.getResponse(prompt=promptField.get())
    outputLabel.config(text = result)

# Create a style object
style = ttk.Style()

# Configure the style to use a modern theme
style.theme_use('clam')

# Create a label
headingLabel = ttk.Label(root, text="Welcome to InsightCraft",font=("Times New Roman",20))
headingLabel.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# A loading progress bar
# progressBar = ttk.Progressbar(root,orient='horizontal',mode='indeterminate',length=200)
# progressBar.grid(row=5, column =0, columnspan=2, padx=10, pady=20)

# Add image
image = Image.open("assets/1742.jpg")  # Replace "example_image.png" with your image file
image = image.resize((400, 400), Image.ADAPTIVE)
photo = ImageTk.PhotoImage(image)
image_label = ttk.Label(root, image=photo)
image_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Create a label
label = ttk.Label(root, text="Ask the question:")
label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Create an entry widget
promptField = tk.Entry(root,width=50,textvariable=result)
promptField.grid(row=3, column=0,columnspan=1, padx=10, pady=10)

# Create a button
searchButton = ttk.Button(root, text="Search", command=onSearchButtonClick)
searchButton.grid(row=3, column=1, columnspan=1, padx=10, pady=10)

outputLabel = ttk.Label(root, text=result.get(), anchor=tk.CENTER)
outputLabel.grid(row=1, column=2, columnspan=1, rowspan=5, padx=10, pady=10, sticky="nsew")

# Start the main event loop
root.mainloop()
