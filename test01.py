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
        print(str(self.number_served))

    def set_number_served(self, virtual):
        self.number_served = virtual

    def increment_number_served(self, more):
        if more > 0:
            self.number_served += more
            print(self.number_served)
        else:
            print("Input Error")

data = Restaurant('柬埔寨', '汉菜',)
data.number_served = 23
data.set_number_served(2)
data.increment_number_served(3)
# 9-5 尝试登录次数：在为完成练习 9-3 而编写的 User 类中，添加一个名为
# login_attempts 的属性。编写一个名为 increment_login_attempts()的方法，它将属性
# login_attempts 的值加 1。再编写一个名为 reset_login_attempts()的方法，它将属性
# login_attempts 的值重置为 0。
"""class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print("User first_name: " + self.first_name)
        print("User last_name: " + self.last_name)
        print("User age: " + str(self.age))

    def greet_user(self):
        print("Hello,I'm " + self.first_name + " " + self.last_name)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

# 根据 User 类创建一个实例，再调用方法 increment_login_attempts()多次。打印属
# 性 login_attempts 的值，确认它被正确地递增；然后，调用方法 reset_login_attempt"""