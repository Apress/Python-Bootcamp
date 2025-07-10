print("The following program can handle the non-system-exiting exceptions.")
a = input("Enter the dividend: ")
b = input("Enter the divisor: ")
try:
    result = int(a) / int(b)
# # The incorrect arrangement of the except blocks
# except Exception as e:
#     print(f"An unexpected error has occurred. Error details: {e}")
except ZeroDivisionError as e:
    print("Invalid input! Your divisor becomes zero!")
    print(f"Error details: {e}")
except ValueError as e:
    print("Invalid input! Provide a correct input next time!")
    print(f"Error details: {e}")
except Exception as e:
    print(f"An unexpected error has occurred. Error details: {e}")
else:
    print(f"The result of the division is: {result}")
finally:
    print("The program completes successfully.")