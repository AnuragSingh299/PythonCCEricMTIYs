from userr import User
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
