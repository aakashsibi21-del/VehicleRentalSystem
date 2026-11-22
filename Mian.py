
# Importing Child classes.

from Car import Car
from Bike import Bike


# Creating Objects for Child Classes and Calling Abstract Methods.

car = Car('BMW', 'KL 38 A 7724', 5000, 3)
car.Display_details()
car.calculate_rent()

bike = Bike('Royal Enfield', 'KL 38 C 6645', 2000, 3)
bike.Display_details()
bike.calculate_rent()

