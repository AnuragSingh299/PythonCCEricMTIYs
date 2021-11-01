favourite_places = {
		'jim': ['tokyo', 'sydney', 'istanbul'],
		'tom': ['varanasi', 'barcelona'],
		'mike': ['wellington', 'new york'],
	}

for name, places in favourite_places.items():
	print(f"\n{name.title()} favourite places are:")
	for place in places:
		print(f"\n{place.title()}")