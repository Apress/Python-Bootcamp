def transform_lists():
    """
    It is a function that can return multiple values.
    Each element in the initial_list will be doubled
    by this function.
    """
    global initial_list
    global resultant_list
    # First, reversing the list before calling pop()
    initial_list.reverse()
    #print(f"The list becomes:{input_list}")
    while initial_list:
     for element in initial_list:
        element = initial_list.pop()
        # print(element)
        resultant_list.append(2 * element)

initial_list = [1,2,3,4,5]
resultant_list=[]
print(f"The initial_list is: {initial_list}")
print("Calling the function transform_lists now.")
transform_lists()
print(f"The initial_list is: {initial_list}")
print(f"The resultant list is: {resultant_list}")



