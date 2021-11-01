pet_0 = {
	'type': 'dog',
	'owner_name': 'Henderson',
}

pet_1 = {
	'type': 'cat',
	'owner_name': 'katherine',
}

pet_2 = {
	'type': 'fish',
	'owner_name': 'Krishnan',
}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
	print(f"{pet['owner_name'].title()} owns a {pet['type']}.")
