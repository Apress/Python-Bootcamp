print("This program prints the sum of two valid numbers.")
first_input = input("Enter a valid number: ")
second_input = input("Enter another valid number: ")
total = 0  #default value
try:
    a = float(first_input)
    b = float(second_input)
except ValueError as e:
    pass
else:
    total = a + b
    print(f"The sum of numbers: {total}")
finally:
    print("The program completes successfully.")


