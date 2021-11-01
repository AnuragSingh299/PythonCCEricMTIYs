person1 = {
	'first_name': 'jim',
	'last_name': 'beglin',
	'age': 56,
	'city': 'yorkshire',
}

person2 = {
	'first_name': 'tim',
	'last_name': 'fowler',
	'age': 64,
	'city': 'phoneix',
}

person3 = {
	'first_name': 'dave',
	'last_name': 'growhl',
	'age': 45,
	'city': 'new york',
}

people = [person1, person2, person3]

for person in people:
	print(f"{person['first_name'].title()} {person['last_name'].title()} lives in {person['city'].title()}. He is {person['age']} year old.")