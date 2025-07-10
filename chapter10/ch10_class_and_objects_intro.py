class Student:
    """ This is a simple class to model a student"""
    def describe(self):
        """ A simple method to describe the behavior of a student."""
        print(f"A student must study before an examination.")

# Creating an object from Student class
sam = Student()
# Invoking the method
sam.describe()
# Invoking the method in a different way
Student.describe(sam)

# # Creating another object from Student class
# kate= Student()
# # Invoking the method
# kate.describe()


