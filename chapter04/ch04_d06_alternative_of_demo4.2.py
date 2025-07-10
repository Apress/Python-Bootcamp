# Skipping the validation of the user's input
user_input=int(input("Enter an integer: "))
# The old codes from demo4.2
# if user_input < 5:
#     print(f"{user_input} is less than 5")
# else:
#     print(f"{user_input} is greater than or equal to 5")

msg1 = f"{user_input} is less than 5"
msg2 = f"{user_input} is greater than or equal to 5"
result= msg1 if user_input< 5 else msg2
# result= f"{user_input} is less than 5" if user_input< 5 else f"{user_input} is greater than or equal to 5"
print(result)