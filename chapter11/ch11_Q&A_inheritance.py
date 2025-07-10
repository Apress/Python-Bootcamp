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
        """Initializing the parent class attributes."""
        super().__init__(name, roll_number)
        #Student.__init__(self,name, roll_number)  # Bad practise
        self.dept=dept

    def describe(self):
        """ A specialized method to describe a student."""
        super().describe()
        print(f"Department: {self.dept}")

    def show_elective_paper(self,subject):
        """ A specialized method to mention the elective papers."""
        print(f"{self.name} has taken {subject} as an elective subject. ")

# For Q&A
print("*"*15)
sam= Student("Sam", 1)
sam.describe()
# sam.show_elective_paper("Nuclear Physics") # Error
print("-"*10)
sam= Department("Sam", 1,"Physics")
sam.describe()
sam.show_elective_paper("Nuclear Physics")
