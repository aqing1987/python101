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
