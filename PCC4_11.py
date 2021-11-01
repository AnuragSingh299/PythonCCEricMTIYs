pizzas = ['cheese', 'veggie', 'pepperoni', 'margherita', 'huwaiean']
friend_pizzas = pizzas[:]
pizzas.append("chicken")
friend_pizzas.append("chilly")
print("My favourite pizzas are:")
for pizza in pizzas:
	print(pizza)
print("My friend's favourite pizzas are:")
for pizza in friend_pizzas:
	print(pizza)
