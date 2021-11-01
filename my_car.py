from car import Car

my_new_car = Car('tarzan', 'a4', 2009)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 90
my_new_car.read_odometer()