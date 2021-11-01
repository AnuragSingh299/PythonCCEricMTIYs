class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} offers {self.cuisine_type.title()} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open.")

restaurant = Restaurant('Iyer and sons', 'tamil')
print(f"Restauarnt name is {restaurant.restaurant_name.title()}")
print(f"Cuisine is {restaurant.cuisine_type.title()}")
restaurant.describe_restaurant()
restaurant.open_restaurant()