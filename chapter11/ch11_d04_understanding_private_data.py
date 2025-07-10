class Person:
    def __init__(self,name):
        self.name = name
        self.designation = "Teacher"
        self.__salary = 10000.5  # acts like a private variable

    def display_salary(self):
        print(f"{self.name} earns ${self.__salary} per month.")

amit=Person("Amit")
print(amit.name) # OK
print(amit.designation) # OK
# print(amit.__salary) # Error

amit.display_salary() # OK
print(amit._Person__salary) # OK too