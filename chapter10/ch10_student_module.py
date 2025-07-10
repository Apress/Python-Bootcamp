"""
This module is useful to create a student
and display the necessary information.
"""
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

class Stream:
    """ Initializes the student's stream """
    def __init__(self, student, stream):
        self.roll_number=student.roll_number
        self.stream=stream

    def display(self):
        """ Return the student details. """
        return f"Roll number {self.roll_number} belongs to the {self.stream} stream."
