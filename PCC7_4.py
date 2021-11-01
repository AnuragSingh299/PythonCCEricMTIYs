prompt = "Please enter the toppings you want\n"
prompt += "Enter 'quit' to stop\n"

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f"{topping} is added.") 