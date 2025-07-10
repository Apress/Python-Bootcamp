initial_numbers= [100, 200, 300, 400, 500]
print(f"The original numbers are {initial_numbers}")
# Incrementing each item in the list by 5% 
new_numbers = list(map(lambda x: x * 1.05, initial_numbers))
print(f"The updated numbers are {new_numbers}")

