import tkinter as tk
from tkinter import filedialog
from configure import imageModel
from util import apiKey
import PIL.Image
import google.generativeai as genai

genai.configure(api_key=apiKey)

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(filetypes=[("Image File",'.jpg, .png ,jpeg')])
img = PIL.Image.open(file_path)

query = input("Enter your query here: ")

response = imageModel.generate_content([query, img],stream=True)
response.resolve()
print(response.text)