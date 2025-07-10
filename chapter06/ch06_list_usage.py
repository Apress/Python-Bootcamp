numbers = [1,2.5,3,5.7,9.1]
print(f"The contents of the list are: {numbers}")
print("-"*10)

# Printing the elements of a list using an index. The indexing starts
# with 0 from the extreme left.(The usage is similar to strings.)
names = ["John", "Sam", "Kate"]
print(names[0])
print(names[1])
print(names[2])
# Error: List index out of range
# print(names[3])
print("-"*10)

# Printing the elements of a list from the extreme right.
# In this case, it starts from -1
names = ["John", "Sam", "Kate"]
print(names[-1])
print(names[-2])
print(names[-3])
print("-"*10)

# Let me show you some ways to reverse a list
contents = ["John", 12, "Sam", True, 50.7]
print(f"The original list:{contents}")
print("Reversing the list.")
contents.reverse()
print(f"The modified list is:{contents}")
print("Reversing the list again using the reversed function")
rev_contents=list(reversed(contents))
print(f"Now the list is:{rev_contents}")
print("-"*10)

# I'd like to show you the slicing of a list
contents = ["John", 12, "Sam", True, 50.7]
print(f"The original list is: {contents}")
print("Printing the elements from index position 2 to end:")
print(contents[2:])
print("Printing the elements from index position 1 to 3(i.e.4-1):")
print(contents[1:4])
print("-"*10)

# Showing some more slicing examples
contents = ["John", 12, "Sam", True, 50.7]
print("Omitting the first index to start slicing at the beginning.")
print(contents[:4])
print("Omitting both indexes is allowed as well.")
print(contents[:])
print("Printing the first element while skipping every second one.")
print(contents[0::2])
print("The reverse list is as follows:")
print(contents[::-1])
print("-"*10)

# You can reassign a new value inside the list
list_contents = ["John", 12, "Sam", True, 50.7]
print(f"The original list: {list_contents}")
print("Changing the element at index 2.")
list_contents [2] = "Bob"
print(f"Now the list is: {list_contents}")
print("-"*10)

# Concatenation example
contents1 = ["John", 12, 50.7]
contents2 = ["Sam", 25, "John", False, 100.2]
print("Original lists are:")
print(contents1)
print(contents2)
print("After concatenating the lists, you get the following list:")
print(contents1 + contents2)
print("-"*10)

# Printing a specific number of elements of a list from the end.
sample_list = ["John", 12, "Sam", True, 50.7]
print(f"The original list is: {sample_list}")
print(f"The last 3 elements of the list are: {sample_list[-3:]}")
print(f"The last 2 elements of the list are: {sample_list[-2:]}")
print(f"The last element of the list is: {sample_list[-1]}")
print("-"*10)

# Removing list elements using three different approaches
contents = ["John", 12, "Sam", True, 50.7,12]
print(f"The original list is: {contents}")
print("Removing the element at index 2 using the del function.")
del(contents[2])
print(f"Now the list is: {contents}")
print("Removing the element at index 3 using the pop function.")
contents.pop(3)
print(f"Now the list is: {contents}")
print("Removing the first occurrence of 12 using the remove function.")
contents.remove(12)
print(f"Now the list is: {contents}")
print("-"*10)

# Checking whether an element is present inside a list
names = ["John", "Sam","Bob", "Ester"]
print(f"Is 'Sam' present on the list? {'Sam' in names} ")
print(f"Is 'sam' present on the list? {'sam' in names} ")
# Checking whether an element is absent inside a list
print(f"Is 'Jeniffer' missing from the list? {'Jennifer' not in names}")

print("-"*10)

# Finding the maximum and minimum from a number list
numbers = [1, 23, 56.2, -3.7, 999]
print("The original list is:")
print(numbers)
print(f"The largest number is: {max(numbers)}")
print(f"The smallest number is: {min(numbers)}")
print("-"*10)

# # The max function cannot work on the following list
# contents = [1, 23, -3.7, 999, "abc", "bob"] 
# # contents = [1, 23, -3.7, 999] # max can work here
# # contents = ["def", "abc", "bob"] # max can work here
# print("The original list is:")
# print(contents)
# print(f"The largest number is: {max(contents)}")
# print("-"*10)

# Testing booleans with max() and min()
contents = [0.75, True, False, 0.5, 0.6,1,0]
#contents = [0.75, 1, 0, 0.5, 0.6, True, False]
print(f"The original list: {contents}")
print(f"The largest number: {max(contents)}")
print(f"The smallest number: {min(contents)}")
print("-"*10)

# You can add an element or a list of elements at the end of a list
contents = ["John", 12, "Sam"]
print(f"The original list is:{contents}")
print("Appending 25 at the end of the list.")
contents.append(25)
print(f"After adding 25, the list is: {contents}")
print("Appending a list of elements ['Kate', 20] at the end of the list.")
contents.append(['Kate',20])
print(f"Now the list is: {contents}")
# contents.append(10,20) # error
print("-"*10)

# Using the insert function, you can add an element to a particular position
contents = ["John", 12, "Sam", True, 50.7]
print("The original list is:")
print(contents)
print("Inserting the element 'Jack' at index 3.")
contents.insert(3, "Jack")
print(f"Now the list is:{contents}")
print("-"*10)

# Sorting a list
numbers = [33, 11, 555, 77, 111, 333]
print(f"The original list is: {numbers}")
numbers.sort()
print(f"The sorted list in ascending order: {numbers}")
print("Now sorting the list in descending order.")
numbers.sort(reverse = True)
print(f"Now the list is: {numbers}")
print("-"*10)

# If you have mixed data types in your list and you apply sort() on that,
# you’ll encounter errors.

# contents = ["John", 12, "Sam", True, 50.7]
# contents.sort() # Error now

# The following segment is OK:
# tags = ["abc","jkl","mno","def","ghi"]
# print(f"The list of tags is:{tags}")
# print(f"The sorted list:{sorted(tags)}")
# print(f"The list of tags now:{tags}")
print("-"*10)

# Q&A 6.1
# If you want to prevent modification of the original list, you can use
# the sorted() function.
numbers = [33, 11, 555, 77, 111, 333]
print(f"The list of numbers are: {numbers}")
print(f"The sorted list: {sorted(numbers)}")
print(f"The current list of numbers is: {numbers}")
print("-"*10)

# Q&A 6.2
# You can add multiple elements to a list using the extend function.
contents = ["John", 12, "Sam"]
print(f"The original list is:{contents}")
print("Adding 25,'Bob', and 100.2 at the list end.")
contents.extend([25, 'Kate', 20])
print(f"Now the list is:{contents}")
print("-"*10)