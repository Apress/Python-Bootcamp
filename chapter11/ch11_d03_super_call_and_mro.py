class Grandfathers:
    def describe(self):
        print("Both grandfathers are artists.")

class Father(Grandfathers):
    def describe(self):
        print("The father is an employee.")
        super().describe()

class Mother(Grandfathers):
    def describe(self):
        print("The mother is a housewife.")
        # super().describe()

class Child(Father,Mother):
    pass

child=Child()
child.describe()
print(Child.mro())

