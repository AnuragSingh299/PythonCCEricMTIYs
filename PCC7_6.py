prompt = "\nWhat is your age?"
prompt += "\nEnter 'quit' to stop.\n"
active = True
while active == True:
    age = input(prompt)
    if age == 'quit':
        break
        active = false
    else:
        #age = input("\nWhat is your age?\n Enter 'quit' to stop.")
        if int(age) < 3:
            print("Your ticket is free.")
        elif int(age) >= 3 and int(age) <= 12:
            print("Your ticket is 10$.")
        elif int(age) > 12:
            print("Your ticker is 15$.")