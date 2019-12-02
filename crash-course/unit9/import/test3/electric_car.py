"""class for describe electric car"""

from car import Car


class Battery():
    """emulate electric battery"""

    def __init__(self, battery_size=70):
        """init battery attribute"""
        self.battery_size = battery_size

    def describe_battery(self):
        """info about battery"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """info about range"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)


class ElectricCar(Car):
    """electric car has some special feature"""

    def __init__(self, make, model, year):
        """
        init father's attribute
        then init electric car's special attribute"""
        super().__init__(make, model, year)
        self.battery = Battery()
