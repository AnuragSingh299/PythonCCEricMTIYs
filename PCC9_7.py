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

class Admin(User):

    def __init__(self, first_name, last_name, gender, age):
        super().__init__(first_name, last_name, gender, age)
        self.privileges = Privileges()

    # def show_privileges(self):
    #     print("These are the following privileges given to the admin:")
    #     for privilege in self.privileges:
    #         print(privilege)

class Privileges:
    
    def __init__(self):
        self.privileges  = [
            "can add a post",
            "can delete a post",
            "can ban user",
            "can delete a user"
        ]

    def show_privileges(self):
        print("These are the following privileges given to the admin:")
        for privilege in self.privileges:
            print(privilege)

        



my_admin = Admin('Crowden', 'Marshall', 'Male', 55)
my_admin.privileges.show_privileges()