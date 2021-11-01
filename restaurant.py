class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0        

    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} offers {self.cuisine_type.title()} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open.")

    def set_number_served(self, num_served):
        self.number_served = num_served

    def increment_number_served(self, serves):
        self.number_served += serves
