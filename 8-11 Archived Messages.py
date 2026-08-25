ef send_messages(short_text_messages):
    while short_text_messages:
        old_part = short_text_messages.pop()
        print(f"The following messages are being sent: {old_part}")
        sent_messages.append(old_part)




def show_messages(sent_messages):
    print("\nThe following messages have been sent")
    for messages in sent_messages:
        print(messages)




short_text_messages = ['Hi Babe!', 'Oh Wait, I dont have a gf:(']
sent_messages = []


send_messages(short_text_messages[:])
show_messages(sent_messages)


print("                                                            ")
print(short_text_messages)
print(sent_messages)
