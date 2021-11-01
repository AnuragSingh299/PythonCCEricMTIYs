sandwich_orders = ['cheese', 'pastrami', 'fruit', 'salad','pastrami', 'egg', 'chicken', 'pastrami']
finished_sandwiches = []
print("Deli has run out of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    print(f"I made your {finished_sandwich} sandwich.")
    
    finished_sandwiches.append(finished_sandwich)

print("\nList of sandwiches made:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)