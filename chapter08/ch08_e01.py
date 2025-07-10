try:
    result = 15/0
# except ArithmeticError:
#     print("Caught the ArithmeticError.Your divisor is zero.")
except ZeroDivisionError:
    print("Caught ZeroDivisionError.The divisor is zero.")
except ArithmeticError:
    print("Caught the ArithmeticError.Your divisor is zero.")
