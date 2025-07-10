class Car:
    def __init__(self,company,model):
        self.company=company
        self.model=model
    def display_car(self):
        print(f"Company:{self.company}, Model: {self.model}")

def cars_info():
    # making Toyota cars
    glanza= Car("Toyota","Glanza")
    rumion = Car("Toyota", "Rumion")
    toyota_cars= [glanza, rumion]
    for car in toyota_cars:
        car.display_car()

    mustang= Car("Ford", "Shelby Mustang")
    gt40=Car("Ford","Ford GT40")
    fiesta=Car("Ford","Ford Fiesta")
    ford_cars=[mustang,gt40,fiesta]
    for car in ford_cars:
        car.display_car()
cars_info()