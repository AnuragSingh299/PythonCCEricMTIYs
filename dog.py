class Dog:
    """We are trying to model a general dog as a class."""

    def __init__(self, name, age):
        """Initializing name and age attributes"""
        self.name = name
        self.age = age      

    def sit(self):
        print(f"{self.name} is sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over.")

my_dogg = Dog('Hammer', 10)
my_dog = Dog('Kevin', 9)

print(f"My dog's name is {my_dogg.name}.")
print(f"My dog's age is {my_dogg.age}")

my_dogg.sit()
my_dogg.roll_over()

print(f"My dog's name is {my_dog.name}.")
print(f"My dog's age is {my_dog.age}")

my_dog.sit()
my_dog.roll_over()