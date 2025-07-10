class Car:
    def __init__(self,company,model):
        self.company=company
        self.model=model
    def display_car(self):
        print(f"Company: {self.company}, Model: {self.model}")

def main():
    glanza= Car("Toyota","Glanza")
    glanza.display_car()
    mustang= Car("Ford", "Shelby Mustang")
    mustang.display_car()

if __name__== "__main__":
    main()
