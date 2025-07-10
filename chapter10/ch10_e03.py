class Employee:
   # def __init__(self,id,name="Anonymous"):     # Correct
   def __init__(self, name="Anonymous",id):     # Incorret
        self.name=name
        self.id = id
   def describe(self):
        return f"{self.name} is an employee with ID: {self.id}"

mike= Employee(1,"Mike")
print(mike.describe())