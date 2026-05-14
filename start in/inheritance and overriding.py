class Car:
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles  on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cant rol back")
    
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()
    
    def discribe_bettery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size = 400):
        self.battery_size = battery_size

    def discribe_battery(self):
        print(f"This car has a {self.battery_size} -kWh battery.")

    def get_range(self):
        
        if self.battery_size == 400:
            range = 150
        elif self.battery_size == 500:
            range = 200

        print(f"This car can go about {range} miles on a full charge.")





my_leaf = ElectricCar('nissan', 'leaf', 2024)

print(my_leaf.get_descriptive_name())

my_leaf.battery.discribe_battery()
my_leaf.battery.get_range()
my_leaf.battery.battery_size = 500
my_leaf.battery.discribe_battery()
my_leaf.battery.get_range()
