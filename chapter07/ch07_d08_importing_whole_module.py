import bootcamp_library
#from bootcamp_library import numbers, employees, double_the_total

# Using the list from the library.
#print(f"Available numbers are: {numbers}") # Error now
print(f"Available numbers are:{bootcamp_library.numbers}") # OK
print(f"The third number is: {bootcamp_library.numbers[2]}")

# Using the dictionary from the library.
print(f"The working employees are: {bootcamp_library.employees}")
print(f"The employee with ID 2 is: {bootcamp_library.employees[2]}")

# Using the double_the_total function from the library now.
result = bootcamp_library.double_the_total(20, 30.5)
print(f"Two times of 20 + 30.5 is: {result}")