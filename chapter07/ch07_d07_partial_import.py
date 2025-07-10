from bootcamp_library import numbers, employees, double_the_total

# Using the list from the library.
print(f"Available numbers are: {numbers}")
print(f"The third number is: {numbers[2]}")

# Using the dictionary from the library.
print(f"The working employees are: {employees}")
print(f"The employee with ID 2 is: {employees[2]}")

# Using the double_the_total function from the library now.
result = double_the_total(20, 30.5)
print(f"Two times of 20 + 30.5 is: {result}")
