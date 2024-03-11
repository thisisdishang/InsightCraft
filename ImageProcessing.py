from Util import apiKey
import PIL.Image
import google.generativeai as genai

img = PIL.Image.open('D:\\Media\\profilePics\\164039.png')
# img.show()
genai.configure(api_key=apiKey[::-1])

model = genai.GenerativeModel('gemini-pro-vision')
response = model.generate_content(["Write a short, engaging blog post based on this picture.",img],stream=True)
print(response.text)