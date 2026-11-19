from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, Vehicle_Name, Vehicle_no, Rent_price ):
        self.Vehicle_Name = Vehicle_Name
        self.Vehicle_no = Vehicle_no
        self.__Rental_Price = Rent_price

    @abstractmethod
    def calculate_rent(self):
        pass

    @property
    def Rental_price(self):
        return self.__Rental_Price

    @Rental_price.setter
    def Rental_price(self,update):
        if update <=0:
            raise 'The Rental price Cannot be Zero or Positive.'
        self.__Rental_Price = update

    def Display_details(self):
        print('\nVehicle Name       : ',self.Vehicle_Name,'\nVehichle No        : ', self.Vehicle_no,
              '\nRental Price       : ',self.__Rental_Price)

