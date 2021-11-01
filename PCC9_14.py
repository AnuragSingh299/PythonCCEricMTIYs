from random import choice
lottery = (23, 24, 45, 56, 67, 77, 86, 56, 34, 49, 'C', 'V', 'N', 'K', 'A')
print(f"Any ticket matching these four numbers or letters wins a prize:")
for i in range(0, 4):
    i = choice(lottery)
    print(i)
