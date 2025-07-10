# Skipping the validation of the user's input
user_input=int(input("Enter an integer: "))
if user_input < 5:
    print(f"{user_input} is less than 5")
elif user_input== 5:
    print(f"The user-provided value is equal to 5")
else:
    print(f"{user_input} is greater than 5")