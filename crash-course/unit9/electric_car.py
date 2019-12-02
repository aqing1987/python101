class Car():
    """emulate car"""

    def __init__(self, make, model, year):
        """init car attribute"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """return tidy descriptive info"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """print info about odometer"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """set odometer value to pointed value,
        disable roll back"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")

    def increase_odometer(self, mileage):
        """increase current odometer"""
        self.odometer_reading += mileage

    def fill_gas_tank(self):
        """fill gas tank"""
        print("Fill gas tank now")


class ElectricCar(Car):
    """electric car has some special feature"""

    def __init__(self, make, model, year):
        """
        init father's attribute
        then init electric car's special attribute"""
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        """info about battery"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def fill_gas_tank(self):
        """electric special fill overplace father's"""
        print("This car doesn't need a gas tank")


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()
