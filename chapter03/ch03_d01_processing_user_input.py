# Supply a name
user_name = input("Enter your name: ")
# Enter the age
user_age = input("Enter your age: ")
# Displaying the intended message
print(f"Welcome, {user_name}! You are now {user_age}")
# Trying to increment the age by 1 as follows:
# user_age=user_age + 1 # Error
user_age=int(user_age)
user_age=user_age + 1 # OK now
print(f"In the next birthday, you'll be {user_age}")


