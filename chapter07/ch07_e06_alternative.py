def make_double(input_list, new_list):
# def make_double():
    """
    It is a function that can return multiple values.
    Each element in the input_list will be doubled
    by this function.
    """
    # First, reversing the list before calling pop()
    input_list.reverse()
    #print(f"The list becomes:{input_list}")
    while input_list:
     for element in input_list:
        element = input_list.pop()
        # print(element)
        resultant_list.append(2 * element)

global initial_list
initial_list = [1,2,3,4,5]

global resultant_list
resultant_list=[]
print(f"The initial_list is: {initial_list}")
print("Calling the function make_double now.")
make_double(initial_list,resultant_list)
print(f"The initial_list is: {initial_list}")
print(f"The resultant list is: {resultant_list}")
