# import traceback
print("The following program can handle two different errors.")
a = input("Enter the dividend: ")
b = input("Enter the divisor: ")
try:
    result = int(a) / int(b)
    print(f"The result of the division is: {result}")
except ZeroDivisionError as e:
    print("Invalid input! Your divisor becomes zero!")
    print(f"Error details: {e}")
    # print(traceback.print_exc())
except ValueError as e:
    print("Invalid input! Provide a correct input next time!")
    print(f"Error details: {e}")
finally:
    print("The program completes successfully.")
