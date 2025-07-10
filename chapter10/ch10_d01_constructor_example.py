class Student:
    """ This is a simple class to model a student"""
    def __init__(self,name,roll_number):
       self.name=name
       self.roll_number=roll_number

    def describe(self):
        """ A simple method to describe a student."""
        print(f"{self.name} has been assigned roll number {self.roll_number}")

# Creating two objects from the Student class
sam= Student("Sam", 1)
kate= Student("Kate", 2)

# Describing the students
sam.describe()
kate.describe()
