print("The following program can handle two different errors.")
a = input("Enter the dividend: ")
b = input("Enter the divisor: ")
try:
    result = int(a) / int(b)
except (ZeroDivisionError,ValueError) as e:
    print(f"Error details: {e}")
else:
    print(f"The result of the division is: {result}")
finally:
    print("The program completes successfully.")