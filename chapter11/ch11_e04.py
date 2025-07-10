class Car:
    def __init__(self):
        print("It is a car.")

class ElectricCar(Car):
    def __init__(self):
        super().__init__()
        print("It uses an electric motor. ")

class DieselCar(Car):
    def __init__(self):
        super().__init__()
        print("It uses a diesel engine. ")

first_car= ElectricCar()
print("-"*10)
second_car= DieselCar()

