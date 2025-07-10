class Parent:
    def show(self):
        return "Parent.show"
    __show=show

class Child(Parent):
    def show(self):
        return "Child.show"

child=Child()
print(child.show())
print(child._Parent__show())


