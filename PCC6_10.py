favourite_numbers = {
	'josh': [17, 11, 56],
	'anish': [21, 90, 69, 96,],
	'anurag': [34, 49, 6, 0],
	'manish': [44, 88 , 99, 66],
	'danny': [9, 909, 101],
}

for name, numbers in favourite_numbers.items():
	print(f"{name.title()} favourite numbers are:")
	for number in numbers:
		print(f"{number}")