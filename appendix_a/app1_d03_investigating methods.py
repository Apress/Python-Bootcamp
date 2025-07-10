class Color:
    fav_color = "Green"

    def __init__(self, color):
        self.fav_color = color

    def instance_method(self):
        print("The instance method is called.")
        print(f"My favorite color is: {self.fav_color}")
        print("-"*15)

    @staticmethod
    def static_method():
        print("The static method is called.")
        print("You can call me without creating an instance.")
        print(f"My favorite color is: {Color.fav_color}")
        print("-"*15)

    @classmethod
    def class_method(cls):
        print("The class method is called.")
        print("You can call me without creating an instance.")
        print(f"My favorite color is: {cls.fav_color}")
        print("-" * 15)

# Creating an object from the Color class
favorite_color = Color("Blue")

# Calling the instance method
favorite_color.instance_method()
# Calling the static method
Color.static_method()
# Calling the class method
Color.class_method()

# print("*"*20)

# # Alternative code
# # Calling the instance method
# favorite_color.instance_method() # Also works
# # Calling the static method
# favorite_color.static_method() # Also works
# # Calling the class method
# favorite_color.class_method() # Also works

# print("*"*20)

# # Alternative code
# # Calling the instance method
# Color.instance_method(favorite_color) # Also works
# # Calling the static method
# Color.static_method() # Also works
# # Calling the class method
# Color.class_method() # Also works

