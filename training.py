"""class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
            print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
            self.odometer_reading += miles

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print(self.year)

class Battery:
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()"""
# 9-4 就餐人数：在为完成练习 9-1 而编写的程序中，添加一个名为 number_served
# 的属性，并将其默认值设置为 0。根据这个类创建一个名为 restaurant 的实例；打印有
# 多少人在这家餐馆就餐过，然后修改这个值并再次打印它。
# 添加一个名为 set_number_served()的方法，它让你能够设置就餐人数。调用这个
# 方法并向它传递一个值，然后再次打印这个值。
# 调用这个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待的就餐人数。
# 添加一个名为 increment_number_served()的方法，它让你能够将就餐人数递增。
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)
    def open_restaurant(self):
        print(self.restaurant_name + " In operation")
    def people(self):
        print(self.number_served)
    def set_number_served(self):
        while True:
            print("Please enter the number of diners: ")
            self.number_served = input()
            if int(self.number_served) >= 1:
                print("There's a table for " + self.number_served + " today.")
                break
            else:
                print("Input Error")
    def increment_number_served(self, more):
        if int(more) > 0:
            s = int(self.number_served)
            s += more
            print(s)
        else:
            print("Input Error")

data = Restaurant('1', '2',)
data.number_served = 23
data.set_number_served()
data.increment_number_served(3)