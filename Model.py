import google.generativeai as genai
import textwrap

from IPython.display import Markdown

def toMarkdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

key = "API_KEY"
genai.configure(key)
model = genai.GenerativeModel("gemini-pro")

response = model.generate_content("What is meaning of life?")
toMarkdown(response.text)
print(response.text)
