import json

filename = "favnumber.json"
fav = input("What is your favourite number?")

with open(filename, 'w') as f:
    json.dump(fav, f)