from configure import textModel

chat = textModel.start_chat()

try:
    while True:
        print()

        userPrompt = input("User: ")
        response = chat.send_message(userPrompt)

        print(response.text)
        print("-"*80)

except KeyboardInterrupt:
    print(chat.history)

'''
for chunk in response:
    print(chunk.text)
    print("-"*80)
'''