class Parent:
    def __init__(self):
        print("Invoking the display method...")
        # self.display()
        self.__display()
    def display(self):
        print("The parent.display is called.")
    __display=display # private copy of original display()

class Child(Parent):
    # def __init__(self):
    #     print("Invoking the display method...")
    #     self.display()

    def display(self):
        print("The child.display is called.")

# parent=Parent()
child=Child()

# child.__display()  # error
