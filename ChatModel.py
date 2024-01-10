import google.generativeai as genai
from Util import apiKey

genai.configure(api_key=apiKey[::-1])
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[{"user":"Hello AI!","model":"Yes! ask for any assistance you need."}])
print(chat)

response = chat.send_message("In one sentence, explain how a computer works to a young child.")
print(response.text)

#print(response.candidates)