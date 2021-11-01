prompt = "Why do you like programming?: "
prompt += "\nEnter 'quit' to end the program. \n"
reason = ""
while reason != 'quit':
    reason = input(prompt)

    if reason != 'quit':
        with open('responses.txt', 'a') as file_object:
            file_object.write(f"{reason}\n")

