from configure import textModel

chat = textModel.start_chat()

response = chat.send_message("In one sentence, explain how a computer works to a young child.")
print(response.text)
# print(chat.history)

response = chat.send_message("Okay, how about a more detailed explanation to a high schooler?", stream=True)

for chunk in response:
    print(chunk.text)
    print("-"*80)