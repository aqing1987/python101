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

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_new_car.update_odometer(25)
my_new_car.read_odometer()

my_new_car.update_odometer(20)

my_new_car.increase_odometer(20)
my_new_car.read_odometer()
