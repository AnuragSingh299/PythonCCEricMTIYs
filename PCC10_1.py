with open('learning_python.txt') as file_object:
    contents = file_object.read()
    lines = file_object.readlines()
print("\nPrinting 1st time:\n")    
print(contents)

print("\nPrinting 2nd time:\n")
with open('learning_python.txt') as file_object:
    for line in file_object:
        print(line.strip())

print("\nPrinting 3rd time:\n")
with open('learning_python.txt') as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())