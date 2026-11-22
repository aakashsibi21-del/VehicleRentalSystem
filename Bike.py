from Vehicle import Vehicle       # Importing Parent Classes.

class Bike(Vehicle):      # Child Class.
    def __init__(self, Vehicle_Name, Vehicle_no, Rent_price, days):
        super().__init__(Vehicle_Name, Vehicle_no, Rent_price)
        self.days = days

    def calculate_rent(self):      # Defining Abstract Method from Parent Class.
        print('Total rental price : ',((self.Rental_price * self.days) + 100),'\n')
        
