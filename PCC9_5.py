class User:
    
    def __init__(self, first_name, last_name, gender, age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"Username: {self.first_name.title()} {self.last_name.title()}")
        print(f"Gender: {self.gender.title()}") 
        print(f"Age: {self.age}")

    def greet_user(self):
        print(f"Hello {self.first_name.title()}, Welcome to our service.")

    def increment_login_attempts(self):
        self.login_attempts = self.login_attempts + 1

    def reset_login_attempts(self):
        self.login_attempts = 0

myuser = User('anurag', 'singh', 'male', 22)
# myuser2 = User('alan', 'johnson', 'male', 21)
# myuser3 = User('mohammad', 'suleman', 'male', 24)

# myuser.describe_user()
# myuser.greet_user()

# myuser2.describe_user()
# myuser2.greet_user()

# myuser3.describe_user()
# myuser3.greet_user()

myuser.increment_login_attempts()
myuser.increment_login_attempts()
myuser.increment_login_attempts()
myuser.increment_login_attempts()

print(f"Total login attempts by {myuser.first_name.title()}: {myuser.login_attempts}")

myuser.reset_login_attempts()
print(f"Total login attempts by {myuser.first_name.title()}: {myuser.login_attempts}")

