# Using number variables
from math import *

# Using numeric types
number_of_pens=15
print(number_of_pens) # Prints 15
weight=65.3
print(weight) # Prints 65.3
print("-"*10)

# Performing some basic arithmetic operations
print(1+2) # Prints 3
print(100-79) # Prints 21
print(25* 3) # Prints 75
print(12.88/4) # Prints 3.22
print("-"*10)

# Performing some complex arithmetic operations
print(1+2*3) # Prints 7
print((1+2)*3) # Prints 9
print(4/2**3)  # Prints 0.5
print((4/2)**3)  # Prints 8
print("-"*10)

# Showing the difference between the numbers and strings
string1="10"
string2 = "22"
number1=10
number2=22
print(string1+string2) # Prints 1022
print(number1+number2) # Prints 32
print("-"*10)

# Improving the readability of big numbers (using underscores)
annual_income=12_000_000
print(annual_income)
print("-"*10)

# I want to concatenate a string and a number following different
# approaches.
text1= "Python version:"
version=13.0
print("I'm using",text1, version) # Using comma to concatenate
print("I'm using "+text1+" "+ str(version)) # Using + to concatenate
print("I'm using {} {}".format(text1, version)) # Using built-in format method
print(f"I'm using {text1} {version}") # Using f-strings
print("-"*10)

# print("My favorite number is:" +99) # Error
# print(99+ " is my favorite number")  # Error
print("-"*10)

# I want to convert strings to integers
# Here I test decimal, binary, and hexadecimal numbers

decimal_number_string="8"
binary_number_string="101"
hexadecimal_number_string="B"
print(int(decimal_number_string)) # Prints 8
print(int(decimal_number_string,10)) # Prints 8
print(int(binary_number_string,2)) # Prints 5
print(int(hexadecimal_number_string,16)) # Prints 11
print("-"*10)

# All strings are not convertible to a number
invalid_number="abc"
#print(int(invalid_number, 10)) # Error
print("-"*10)

# Testing whether a given string is a digit string
print(f"Is 25 a valid number? {"25".isdigit()}")
print(f"Is 'abc' a valid number? {"abc".isdigit()}")
print("-"*10)
# Rounding the numbers
print(round(2.51))  # Prints 3
print(round(5.32))  # Prints 5

print("-"*10)

# Finding the maximum
print(f"Maximum of 1,2,3,4 and 5 is: {max(1,2,3,4,5)}")

# Finding the minimum
print(f"Minimum of 1,2,3,4 and 5 is: {min(1,2,3,4,5)}")
print("-"*10)

# Printing the square root of 25
print(f"The square root of 25 is: {sqrt(25)}")
# Printing the square root of 6.24
print(f"The square root of 6.24 is: {sqrt(6.24)}")
print("-"*10)

# Finding the ceiling value
# This is the smallest integer that is greater than
# or equal to the given number.

print(f"The ceiling value of 39.3 is: {ceil(39.3)}")

# Finding the floor value
# This is the largest integer that is less than
# or equal to the given number.
print(f"The floor value of 39.3 is: {floor(39.3)}")
print("-"*10)

# Finding the greatest common divisor (gcd) of 4 and 14
print(f"The gcd of 4 and 14 is: {gcd(4,14)}")
# Finding the gcd of 14 and 63
print(f"The gcd of 63 and 14 is: {gcd(63,14)}")
print("-"*10)

# Finding the factorial of 5
print(f"The factorial of 5 is: {factorial(5)}")
# Finding the factorial of 7
print(f"The factorial of 7 is: {factorial(7)}")
print("-"*10)
