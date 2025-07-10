class Calculator:
    def sum(self,a,b):
        return a+b

class AdvancedCalculator(Calculator):
    # def sum(self, a, b,c):
    # def sum(self, a, b, c=0):
    #     return a+b+c
    def sum(self, *numbers):
        total=0
        for number in numbers:
            total += number
        return total

calc=AdvancedCalculator()
print(f"2 + 3.5 + 7 = {calc.sum(2,3.5,7)}") # Ok
print(f"2 + 3.5 = {calc.sum(2,3.5)}") # Error
