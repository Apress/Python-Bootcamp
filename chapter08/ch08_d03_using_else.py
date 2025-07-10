print("The following program can handle two different errors.")
a = input("Enter the dividend: ")
b = input("Enter the divisor: ")
try:
    result = int(a) / int(b)
except ZeroDivisionError as e:
    print("Invalid input! Your divisor becomes zero!")
    print(f"Error details: {e}")
except ValueError as e:
    print("Invalid input! Provide a correct input next time!")
    print(f"Error details: {e}")
else:
    print(f"The result of the division is: {result}")
finally:
    print("The program completes successfully.")