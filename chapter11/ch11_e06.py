class Parent:
    pass
class Child(Parent):
    def display(self):
        print("Child.display")

parent=Parent()
# parent.display() # Error