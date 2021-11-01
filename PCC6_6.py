favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

people = ['dave', 'karim', 'sarah', 'bochan', 'jen']

for person in people:
	if person in favorite_languages.keys():
		print(f"Thanks {person.title()} for taking the poll.")
	else:
		print(f"{person.title()} please taking the poll.")