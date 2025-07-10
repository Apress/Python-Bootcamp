class Car:
    def __init__(self,company,model):
        self.company=company
        self.model=model
    def display_car(self):
        print(f"Company:{self.company}, Model: {self.model}")

def cars_info():
    # Making Toyota cars
    glanza= Car("Toyota","Glanza")
    rumion = Car("Toyota", "Rumion")
    # Listing Toyota models
    toyota_models = [glanza.model, rumion.model]

    # Making Ford cars
    mustang= Car("Ford", "Shelby Mustang")
    gt40=Car("Ford","Ford GT40")
    fiesta=Car("Ford","Ford Fiesta")
    # Listing Ford models
    ford_models=[mustang.model,gt40.model,fiesta.model]

    # Storing the models along with the company names
    cars = {"Toyota": toyota_models,"Ford": ford_models}
    # Traversing the dictionary and displaying the details
    for key,value in cars.items():
        print(f"{key} models: {value}")

if __name__== "__main__":
    cars_info()