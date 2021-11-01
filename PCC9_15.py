from random import choice
lottery = (23, 24, 45, 56, 67, 77, 86, 6, 34, 49, 'C', 'V', 'N', 'K', 'A')
# print(f"Any ticket matching these four numbers or letters wins a prize:")
# for i in range(0, 4):
#     i = choice(lottery)
#     print(i)
my_ticket = ('C')
count = 0
for i in range(0, len(my_ticket)):
    for j in range(0, len(lottery)):
        count = count + 1
        if my_ticket[i] == lottery[j]:
            print(f"The loop had to run {count} times.")

