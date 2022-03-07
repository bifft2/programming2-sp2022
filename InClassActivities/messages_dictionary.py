text_messages = {}

def send_message(text_messages, name, message):
    if name in text_messages:
        text_messages[name].append(message)
    else:
        text_messages[name] = [message]

def get_messages(text_messages, name):
    return text_messages.get(name)


send_message(text_messages, "Jonah", "hello")
send_message(text_messages, "Beckett", "What time is dinner?")
send_message(text_messages, "Beckett", "Feed the dog.")
beckett_messages = get_messages(text_messages, "Beckett")
alberto_messages = get_messages(text_messages, "Alberto")

print(text_messages)
print(beckett_messages)
print(alberto_messages)