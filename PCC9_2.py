class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} offers {self.cuisine_type.title()} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open.")

restaurant1 = Restaurant('Iyer and sons', 'tamil')
restaurant1.describe_restaurant()

restaurant2 = Restaurant('Patel and sons', 'gujarati')
restaurant2.describe_restaurant()

restaurant3 = Restaurant('Sinde and sons', 'marathi')
restaurant3.describe_restaurant()