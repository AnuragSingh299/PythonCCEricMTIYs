try:
    with open('cats.txt', 'r') as file_object:
        catnames = file_object.readlines()

    with open('dogs.txt', 'r') as file_object:
        dognames = file_object.readlines()

except FileNotFoundError:
    pass
    #print(f"Sorry we were unable to find one or more files.")

else:
    print("The cat names are:")
    for cat in catnames:
        print(cat.rstrip())
    print("The dog names are:")
    for dog in dognames:
        print(dog.rstrip())