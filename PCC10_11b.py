import json

filename = 'favnumber.json'

with open(filename) as f:
    num = json.load(f)

print(f"Your favourite number is {num}")