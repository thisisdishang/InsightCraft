from configure import textModel


def get_response(prompt):
    try:
        chat = textModel.start_chat()
        while True:
            #userPrompt = input("User: ")

            #if(prompt == "exit"):
                #raise KeyboardInterrupt()

            response = chat.send_message(prompt)

            return response.text

    except KeyboardInterrupt:
        print(chat.history)


'''
for chunk in response:
    print(chunk.text)
    print("-"*80)
'''