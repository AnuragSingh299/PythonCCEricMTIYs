cities = {
	'mumbai': {
		'country': 'india',
		'population': 2507890098,
		'fact': "financial capital of india",
	},

	'tokyo': {
		'country': 'japan',
		'population': 1000809292,
		'fact':	"most populated city in japan",
	},

	'dubai': {
		'country': 'UAE',
		'population': 250909000,
		'fact': "best infrastructure",
	},
}

for city_name, city_info in cities.items():
	print(f"{city_name.title()} is in {city_info['country'].title()}. It's estimated population is {city_info['population']} and it is known for {city_info['fact'].title()}.")