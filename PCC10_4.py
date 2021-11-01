prompt = "Please enter your name: "
prompt += "\nEnter 'quit' to end the program. "
name = ""
while name != 'quit':
    name = input(prompt)

    if name != 'quit':
        with open('guest_book.txt', 'a') as file_object:
            print(f"Welcome to the meeting {name}.\n")
            file_object.write(f"{name} has visited in the meeting.\n")

