from ai import initialize, pred_class, get_response

if __name__ == '__main__':
	print("Please wait as the AI is being initialized...")
	model, words, classes, data = initialize()
	
    # Interacting with the mangobot
    print("Press 0 if you don't want to chat with the Mango.")
    while True:
        message = input("")
        if message == "0":
            break
        intents = pred_class(message, words, classes)
        result = get_response(intents, data)
        print(result)
