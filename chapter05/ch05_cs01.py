# Initially flag contains an empty string.
# We need a string other than quit to enter
# into the while loop to proceed further.
flag = ""
while flag != 'quit':
    user_input = input("Enter a valid number(type quit to end): ")
    # If the user does not type 'quit'
    # We can convert the valid user input to float
    if user_input != 'quit':
        user_input = float(user_input)
    else:
        flag = 'quit'
        break
    if user_input > 0:
        print("You have supplied a positive number.")
    elif user_input < 0:
        print("The supplied number is negative.")
    else:
        print("You've entered 0.")

print("Thank you. It is the end of the program.")
