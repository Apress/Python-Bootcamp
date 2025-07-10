# Using default values in a function
def print_details(name="Sam",age=35):
    """
    This function takes two parameters.
    You can supply the name and age of the user
    in this function.
    By default, the name is 'Sam' and the age is 35.
    """
    print(f"Hello {name}! How are you?")
    print(f"You are now {age}.")


print_details()  # Will take both the default values
print_details(name="Jack")  # Will take age=35 as default
print_details(age=45)  # Will take name="Sam" as default
# None of the default values are considered in the following line
print_details("Bob", 20)
