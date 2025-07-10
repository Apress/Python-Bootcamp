class Employee:
   id=0
   def __init__(self, name="Anonymous"):
        self.name=name
   def describe(self):
        return f"{self.name} is an employee with ID: {self.id}"

kate= Employee("Kate")
print(kate.describe())