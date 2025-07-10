class Student:
    """ This is a simple class to model a student"""
    def __init__(self,name,roll_number):
       self.name=name
       self.roll_number=roll_number

    def describe(self):
        """ A simple method to describe a student."""
        print(f"{self.name}'s current roll number is {self.roll_number}")

    def update_roll_number(self, roll_number):
        """ Updating the roll number of a student."""
        self.roll_number=roll_number
        print(f"{self.name}'s roll number has been updated to {self.roll_number}")

# Creating an object and showing the details
sam= Student("Sam", 1)
sam.describe()
print("-"*10)

print("Updating the roll number and showing the details:")
sam.roll_number=11
sam.describe()
print("-"*10)

print("Updating the roll number again and showing the details:")
sam.update_roll_number(21)
sam.describe()
print("-"*10)