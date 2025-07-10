import bootcamp_library as bl
#from bootcamp_library import numbers, employees, double_the_total

# Using the list from the library.
#print(f"Available numbers are: {numbers}") # Error now
print(f"Available numbers are:{bl.numbers}") # OK
print(f"The third number is: {bl.numbers[2]}")

# Using the dictionary from the library.
print(f"The working employees are: {bl.employees}")
print(f"The employee with ID 2 is: {bl.employees[2]}")

# Using the double_the_total function from the library now.
result = bl.double_the_total(20, 30.5)
print(f"Two times of 20 + 30.5 is: {result}")