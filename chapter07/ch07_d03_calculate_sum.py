# def calculate_sum(x, y):
#     return x + y
#
# total = calculate_sum(12, 15)
# #total = calculate_sum(12, 15, 25) # Error
# print(f"The sum of 12 and 15 is: {total}")

def repeat_sum(*args):
    current_total=0
    for num in args:
        current_total=current_total+num
    return current_total

total = repeat_sum(12, 15)
print(f"The sum of 12 and 15 is: {total}")

total = repeat_sum(20.5, 37,100)
print(f"The sum of 20.5, 37, and 100 is: {total}")

