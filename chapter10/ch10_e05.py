class Employee:
   id=0
   def __init__(self, name="Anonymous"):
        self.name=name

   def update_id(self):
       self.id = 100

   def describe(self):
       self.update_id()
       return f"{self.name} is an employee with ID: {self.id}"

jack= Employee("Jack")
print(jack.describe())