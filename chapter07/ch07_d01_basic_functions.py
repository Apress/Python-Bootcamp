# The following function does not take any argument
def print_hello():
    print("Hello")


# The following function has two parameters.

def print_details(name, age):
    """
    This function takes two parameters.
    You can supply the name and age of the user
    in this function.
    """
    print(f"Hello {name}! How are you?")
    print(f"You are now {age}.")

print("Calling the function that has no parameter.")
print_hello()
print("Now, calling the function that has two parameters.")
print_details("Bob", 20)


# # Printing the documentation
# print(print_details.__doc__)

# # Testing keyword arguments
# print_details(age=20,name="Bob") # Expected outcome
# print_details(name="Bob", age=20) # Again expected outcome

# def main():
#     print("Calling the function that has no parameter.")
#     print_hello()
#     print("Now calling the function that has two parameters.")
#     print_details("Bob", 20)
#
#
# if __name__ == "__main__":
#    main()



