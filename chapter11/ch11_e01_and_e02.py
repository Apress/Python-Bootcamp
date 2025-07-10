class Vehicle:
    def __init__(self):
        print("A vehicle is created.")
class Bus(Vehicle):
    def __init__(self):
        #super().__init__()  # For Exercise 11.1
        print("A bus is created.")

vehicle=Bus()