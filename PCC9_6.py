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

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = ['straweberry', 'chocolate', 'vanilla', 'mango', 'butterscotch']

    def display_flavours(self):
        flavours_list = self.flavours
        print(f"These are the available flavours:")
        for flavour in flavours_list:
            print(flavour)
            

icecream = IceCreamStand('Iyer and sons', 'tamil')
icecream.display_flavours()