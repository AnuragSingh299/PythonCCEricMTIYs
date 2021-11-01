my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print(friend_foods)
my_foods.append('cannoli')
friend_foods.append('ice cream')

print(friend_foods)
print(my_foods)

for food in my_foods:
	print(food)
for food in friend_foods:
	print(food)