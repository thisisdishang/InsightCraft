from util import apiKey
import PIL.Image
import google.generativeai as genai
from tkinter import filedialog
from configure import imageModel

genai.configure(api_key=apiKey)

def open_file_dialog():
    file_path = filedialog.askopenfilenames(filetypes=[("Image File",'.jpg, .png ,jpeg')])
    return PIL.Image.open(file_path)

def reasoning_image(img):

    response = imageModel.generate_content(["What are your thoughts on this picture.", img], stream=True)
    response.resolve()
    print(response.text)

imageFile = open_file_dialog()
reasoning_image(imageFile)
