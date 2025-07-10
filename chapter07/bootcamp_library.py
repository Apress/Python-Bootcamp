
# A private field
__flag = 5

# A simple list
numbers = [1, 2.2, 3.3, 4, 5.5]

# A simple dictionary
employees = {1: "Jack", 2: "Kate", 3: "Bob"}


def double_the_total(first, second):
    """
    This function takes two numbers, adds them
    and doubles the result
    """
    total = first + second
    return total * 2


def make_average(first, second, third=0):
    """
    This function takes three numbers and returns
    the average. The third number is optional.
    """
    total = first + second + third
    return total / 3
