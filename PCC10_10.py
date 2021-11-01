filename = 'test.txt'
with open(filename, 'r') as file_object:
    contents = file_object.read()
    print(contents.lower().count('the'))


