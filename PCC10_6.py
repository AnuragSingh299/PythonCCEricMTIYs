while True:
    num1 = input("Enter 1st number: ");
    if num1 == 'q':
        break
    num2 = input("Enter 2nd number: ");
    if num2 == 'q':
        break
    print("Enter 'q' to quit")
    try:
        add = int(num1) + int(num2)
    except ValueError:
        print("Inputted value is not a number.")
    else:
        print(f"Sum: {add}")