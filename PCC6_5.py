rivers = {
	'ganga': 'india',
	'nile': 'egypt',
	'thames': 'united Kingdom',
}

for river,country in rivers.items():
	print(f"{river.title()} runs through {country.title()}.")

print(f"The rivers included are:")
for river in rivers.keys():
	print(f"{river.title()}")

print(f"The countries included are:")
for country in rivers.values():
	print(f"{country.title()}")