import google.generativeai as genai
from Util import apiKey

genai.configure(api_key=apiKey[::-1])

textModel = genai.GenerativeModel("gemini-pro")
imageModel = genai.GenerativeModel('gemini-pro-vision')

def getPromptResponse(prompt):
    try:
        response = textModel.generate_content(prompt)
        return response.text
    except Exception as e:
        return e
