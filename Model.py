import google.generativeai as genai
import textwrap
from Util import apiKey
from IPython.display import Markdown

def toMarkdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

genai.configure(api_key=apiKey[::-1])
model = genai.GenerativeModel("gemini-pro")

response = model.generate_content("Tell me a joke.")
#toMarkdown(response.text)
responseMessage = ""
try:
    responseMessage = response.text
except Exception as e:
    print(f'{type(e).__name__}:{e}')

print(responseMessage)
