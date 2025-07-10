def make_double(input_list):
    """
    It is a function that can return multiple values.
    Each element in the list will be doubled
    by this function.
    """
    for element in input_list:
        resultant_list.append(2 * element)

initial_list=[1,2,3,4,5]
resultant_list=[]
print(f"The initial_list is: {initial_list}")
print("Calling the function make_double now.")
make_double(initial_list)
print(f"The resultant list is: {resultant_list}")
print(f"The initial_list is: {initial_list}")  # unchanged initial list

