class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over")


my_dog = Dog('Willie', 6)
my_dog.sit()
my_dog.roll_over()



class Restaurant:
    def __init__(self, name, type, describe, open):
        self.name = name
        self.type = type
        self.describe = describe
        self.open = open

    def restaurant_name(self):
        print(f"Hello Names our restaurant {self.name}!")

    def cuisine_type(self):
        print(f"type kitchen {self.type}")

    def describe_restaurant(self):
        print(f"restaurant {self.describe}")

    def open_restaurant(self):
        print(f"Restaurant {self.open}")


restaurant = Restaurant('Antares', 'normal', 'Beautiful', 'Opem')
restaurant.restaurant_name()
restaurant.cuisine_type()
restaurant.describe_restaurant()
restaurant.open_restaurant()

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 23

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This has {self.odometer_reading} miles on it")

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

class Data:
    def __init__(self, name_user, salary):
        self.name_user = name_user
        self.salary = salary

    def name_salary_1(self):
        print(f"Hello {self.name_user} your salary: ${self.salary}")


name_salary = Data("Vova", 13000)
print(name_salary.name_salary_1())

class Car:
    def update_odometer(self, mileage):
        self.update_odometer = mileage

    def get_descriptive_name(self):
        pass

    def read_odometer(self):
        pass


my_new_car = Car()
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()
