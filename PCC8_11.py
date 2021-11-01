def send_messages(msg, sent_messages):
    sent_messages = []
    while msg:
        poppedmsg = msg.pop()
        print(f"{poppedmsg}")
        sent_messages.append(poppedmsg)
    return sent_messages

messages = ['hello world', 'good morning', 'good evening', 'hello', 'good night']
sent_messages = []
sent_messages = send_messages(messages, sent_messages)
print(messages)
print(sent_messages)

messages = send_messages(sent_messages, messages)
print(messages)
print(sent_messages)
