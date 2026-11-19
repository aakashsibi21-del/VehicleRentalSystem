from Vehicle import Vehicle

class Bike(Vehicle):
    def __init__(self, Vehicle_Name, Vehicle_no, Rent_price, days):
        super().__init__(Vehicle_Name, Vehicle_no, Rent_price)
        self.days = days

    def calculate_rent(self):
        print('Total rental price : ',((self.Rental_price * self.days) + 100),'\n')
        
