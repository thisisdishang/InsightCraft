import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import configure

# Create the main window
root = tk.Tk()
root.title("Insight Craft")
root.minsize(600,600)

result = tk.StringVar()

def onSearchButtonClick():
    global result
    result = configure.getPromptResponse(prompt=promptField.get())
    outputLabel.config(text = result)

# Create a style object
style = ttk.Style()

# Configure the style to use a modern theme
style.theme_use('clam')

# Create a label
headingLabel = ttk.Label(root, text="Welcome to InsightCraft",font=("Times New Roman",20))
headingLabel.pack(side="top", padx=20, pady=8)

# A loading progress bar
# progressBar = ttk.Progressbar(root,orient='horizontal',mode='indeterminate',length=200)
# progressBar.pack(side="top")

# Add image
image = Image.open("assets/1742.jpg")  # Replace "example_image.png" with your image file
image = image.resize((300, 300), Image.ADAPTIVE)
photo = ImageTk.PhotoImage(image)
image_label = ttk.Label(root, image=photo)
image_label.pack(side="top", padx=10, pady=10)

# Create a label
label = ttk.Label(root, text="Ask the question:")
label.pack(side="top", padx=20, pady=8)

# Create an entry widget
promptField = tk.Entry(root,width=50,textvariable=result)
promptField.pack(side="top", padx=20, pady=8)

# Create a button
searchButton = ttk.Button(root, text="Search", command=onSearchButtonClick)
searchButton.pack(side="top", padx=20, pady=8)

outputLabel = ttk.Label(root, text=result.get(), anchor=tk.CENTER)
outputLabel.pack(side="top",padx=20, pady=8)

# Create a Vertical Scrollbar
vertical_scrollbar = ttk.Scrollbar(root, orient="vertical", style="Output.Vertical.TScrollbar")
vertical_scrollbar.pack(side="right",padx=20, pady=8)

# Start the main event loop
root.mainloop()
