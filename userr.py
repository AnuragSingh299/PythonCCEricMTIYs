class User:
    
    def __init__(self, first_name, last_name, gender, age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
    
    def describe_user(self):
        print(f"Username: {self.first_name.title()} {self.last_name.title()}")
        print(f"Gender: {self.gender.title()}") 
        print(f"Age: {self.age}")

    def greet_user(self):
        print(f"Hello {self.first_name.title()}, Welcome to our service.")
