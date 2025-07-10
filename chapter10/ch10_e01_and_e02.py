class Employee:
   def __init__(self,id,name="Anonymous"):
        self.name=name
        self.id = id
   def describe(self):
        return f"{self.name} is an employee with ID: {self.id}"

# For exercise 10.1
mike= Employee(1,"Mike")
print(mike.describe())
# For exercise 10.2
mike=Employee(1)
print(mike.describe())


