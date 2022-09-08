# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sklearn.model_selection


class Vehicle:

    tyre = 'tubeless'

    def __init__(self, brand, model, type):
        self.brand = brand
        self.model = model
        self.type = type
        self.gas_tank_size = 16
        self.fuel_level = 0

    def fuel_up(self):
        self.fuel_level = self.gas_tank_size
        print('Gas tank is now full.')

    def drive(self):
        print(f'The {self.model} is now driving.')


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print(Vehicle.tyre)

    vehicle_obj = Vehicle('BMW', 'C Series', 'Truck')

    print(vehicle_obj.brand)
    print(vehicle_obj)
    print(vehicle_obj.type)

    vehicle_obj.fuel_up()
    vehicle_obj.drive()


###
from sklearn.linear_model import LinearRegression()

from sklearn.metrics import classification_report()
