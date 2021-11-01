from random import randint
class Dice:
    def __init__(self):
        self.sides = 6

    def make_dice(self, no_of_sides):
        self.sides = no_of_sides

    def roll_die(self):
        result = randint(1, self.sides)
        print(result)
        print(f"The dice has {self.sides} no of sides.")

myDice = Dice()
# for i in range(1,11):
#     myDice.roll_die()

# myDice.make_dice(10)
# for i in range(1,11):
#     myDice.roll_die()

myDice.make_dice(20)
for i in range(1,11):
    myDice.roll_die()