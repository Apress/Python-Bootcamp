# Creating a tuple and printing the elements inside it.
contents = ("John", 12, "Sam", True, 50.7)
print(f"The content of the tuple is: {contents}")
print("-"*10)

# Accessing the tuple elements (indexing is similar to the lists)
contents = ("John", 12, "Sam", True, 50.7)
print(f"The content of the tuple is: {contents}")
print(f"The first element is: {contents[0]}")
print(f"The last element is: {contents[-1]}")
print(f"Elements from index 1 to 3: {contents[1:4]}")
print(f"Elements from index 2 to end: {contents[2:]}")
print("-"*10)

# # You cannot reassign the value inside a tuple.
# my_tuple = ("John", 12, "Sam", True, 50.7)
# print("The content of my_tuple is:")
# print(my_tuple)
# print("Trying to replace 'Sam' with 'Bob':")
# my_tuple[2]= 'Bob' # Error
# print("-"*10)

# Converting a list to a tuple by using the built-in tuple() function
list_sample = ["John", 12, "Sam", True, 50.7]
print(f"The contents of the list are:{list_sample}")
# Converting the list to a tuple
tuple_sample=tuple(list_sample)
print(f"The contents of the tuple are:{tuple_sample}")
print("-"*10)

# Reversing the tuple elements
sample_tuple = (1, 2, 3, 4, 5)
print(f"The contents of the tuple are: {sample_tuple}")
print("Reversing the tuple now.")
rev_tuple = tuple(reversed(sample_tuple))
print(f"The contents of rev_tuple are: {rev_tuple}")
print("-"*10)

# Replacing one tuple with another
sample_tuple = (1, 2, 3, 4, 5)
print(f"The contents of sample_tuple are: {sample_tuple}")
sample_tuple=("a","b")+ sample_tuple[2:]
print(f"The contents of sample_tuple are: {sample_tuple}")
print("-"*10)

# Testing relational operators
tuple_sample1 = (1, 2, 3)
tuple_sample2 = (1,1,250)
tuple_sample3 = (0,50,500)
print(f"The contents of tuple_sample1 are: {tuple_sample1}")
print(f"The contents of tuple_sample2 are: {tuple_sample2}")
print(f"The contents of tuple_sample3 are: {tuple_sample3}")
print(f"tuple_sample1 < tuple_sample2 ? {tuple_sample1 < tuple_sample2}")
print(f"tuple_sample2 > tuple_sample3 ? {tuple_sample2 > tuple_sample3}")
print("-"*10)

# Q&A 6.3 and 6.4
content="a"
print(type(content))

content=("a")
print(type(content))

content="a",
print(type(content))

