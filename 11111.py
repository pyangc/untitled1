class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number = 0

    def describe_restaurant(self):
        print(self.name)
        print(self.cuisine)

    def open_restaurant(self):
        print(self.name + " In operation")

    def people(self):
        print(self.number)

    def set_number_served(self):
        while True:
            print("Please enter the number of diners: ")
            self.number = input()
            if int(self.number) >= 1:
                print("There's a table for " + self.number + " today.")
                break
            else:
                print("Input Error")

    def increment_number_served(self, more):
        if more > 0:
            s = int(self.number)
            s += more
            print(s)
        else:
            print("Input Error")


data = Restaurant('柬埔寨', '汉菜')
data.set_number_served()
data.increment_number_served(more=1)