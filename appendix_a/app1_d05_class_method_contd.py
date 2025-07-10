class Parent:
    def instance_method(self):
        print(f"The instance method is called.{self}")
    @staticmethod
    def static_method():
        print("The static method is called.")
    @classmethod
    def class_method(cls):
        print(f"The class method is called.{cls}")

class Child(Parent):
    """ This is a Child class."""
    pass


# Creating an object from the Parent class
sample_object = Parent()
sample_object.instance_method()
# Parent.static_method()
sample_object.static_method() # Also ok
# Parent.class_method()
sample_object.class_method() # Also ok

print("*"*20)

# Using the Child class object now,
sample_object = Child()
sample_object.instance_method()

# Child.static_method()
sample_object.static_method()# Also ok

# Child.class_method()
sample_object.class_method()# Also ok












# class Parent:
#   @classmethod
#   def display(cls):
#      print(f"The display() method is called from {cls}")
#
# class Child(Parent):
#     pass
#
# sample_object=Parent()
# sample_object.display()
# sample_object=Child()
# sample_object.display()