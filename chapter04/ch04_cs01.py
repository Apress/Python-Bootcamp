user_input = input("Enter your age: ")
# Skipping the validation of the user's input
age = float(user_input)
if age < 10:
    print("Hi Dear. You can use the product for free.")
elif 10 <= age < 20:
    print("Please donate $1 for the product.")
elif 20 <= age < 30:
    print("Please donate $2 for the product.")
elif 30 <= age < 40:
    print("Please donate $3 for the product.")
else:
    print("Please donate $4 for the product.")
