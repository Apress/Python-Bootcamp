class Student:
    """ This is a simple class to model a student"""
    def __init__(self,name,roll_number):
       self.name=name
       self.roll_number=roll_number
       self.institution="St. Stephen's"

    def describe(self):
        """ A simple method to describe a student."""
        print(f"Name: {self.name}")
        print(f"Roll number: {self.roll_number}")
        print(f"Institution: {self.institution}")


class Department(Student):
    def __init__(self, name, roll_number, dept):
        """ Initializing the parent class attributes. """
        super().__init__(name, roll_number)
        #Student.__init__(self,name, roll_number)  # Bad practise
        self.dept=dept

    def describe(self):
        """ A specialized method to describe a student."""
        super().describe()
        print(f"Department: {self.dept}")

# Creating two objects from the Student class
sam= Department("Sam", 1,"Physics")
kate= Department("Kate", 2,"Computer Science")

# Displaying the student details
sam.describe()
print("*"*10)
kate.describe()



