import textwrap
from IPython.display import Markdown

def toMarkdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# response = model.generate_content("Tell me a joke.")
# toMarkdown(response.text)
