# Defining the Student class
class Student:
    def __init__(self,name):
        self.name= name

# Creating two objects
jack = Student("Jack")
bob = Student("Bob")
jack2=Student("Jack")

# Verifying the object's identity
print(f"Are jack and bob the same object? {jack is bob}")
print(f"Is jack different from bob ? {jack is not bob}")
print(f"Are jack and jack2 the same object? {jack is jack2}")

# Verifying the IDs of jack and jack2
print(f"The ID of jack is {id(jack)}")
print(f"The ID of jack2 is {id(jack2)}")

# Checking the types of jack and bob
print(f"Is jack a Student object? {type(jack) is Student}")
print(f"Is jack an int type? {type(jack) is int}")
print(f"Is bob not an int type? {type(bob) is not int}")