sandwich_orders = ['cheese', 'fruit', 'salad', 'egg', 'chicken']
finished_sandwiches = []

while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    print(f"I made your {finished_sandwich} sandwich.")
    
    finished_sandwiches.append(finished_sandwich)

print("\nList of sandwiches made:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)