class Student:
    """ This is a simple class to model a student"""
    institution="St.Stephen's"  # class variable
    def __init__(self,name,roll_number):
       self.name=name # instance variable
       self.roll_number=roll_number # instance variable
       # self.institution="St. Stephen's" # instance variable

    def describe(self):
        """ A simple method to describe a student."""
        print(f"Name: {self.name}")
        print(f"Roll number: {self.roll_number}")
        print(f"Institution: {self.institution}")

# Creating two objects from the Student class
sam= Student("Sam", 1)
kate= Student("Kate", 2)

# Displaying the student details
sam.describe()
print("*"*10)
kate.describe()

