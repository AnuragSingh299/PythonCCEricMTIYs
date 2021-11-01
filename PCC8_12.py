def make_sandwich(*items):
    print(f"Following sandwiches were ordered:")
    for item in items:
        print(f"- {item}")

make_sandwich('tomato', 'cucumber', 'lemon slice', 'onion', 'sauce')