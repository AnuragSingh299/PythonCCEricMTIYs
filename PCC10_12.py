import json

def get_favnumber():
    filename = "favnumber.json"

    try:
        with open(filename) as f:
            num = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return num

def get_new_favnum():
    favnum = input("What is your fav num?")
    filename = 'favnum.json'
    with open(filename, 'w') as f:
        json.dump(favnum, f)
    return favnum

def display_num():
    favnum = get_favnumber()
    if favnum:
        print(f"Favourite number: {favnum}")
    else:
        get_new_favnum()

display_num()