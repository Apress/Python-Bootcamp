# Printing the details of a dictionary that has three key-value pairs

dictionary_sample = {1: "John", 2: 12, 3: "Sam"}
print(f"The dictionary contains: {dictionary_sample}")
print("-"*10)

# A dictionary can have keys and values of different types
dictionary_sample  = {1: "John", 2: 12, "third": "Sam", }
print(f"The dictionary contains: {dictionary_sample}")
print("-"*10)

# I want to print values for particular keys
dictionary_sample = {1: "John", 2: 12, "three": "Sam"}
print(f"The dictionary contains: {dictionary_sample}")
print("Value at key 1:", dictionary_sample[1])
print("Value at key 2:", dictionary_sample[2])
print("Value at key three:", dictionary_sample["three"])
print("-"*10)

# Finding the total number of elements in your dictionary.
dictionary_sample = {1: "John", 2: 12}
print(f"The dictionary contains: {dictionary_sample}")
print(f"Number of items: {len(dictionary_sample)}")
print("-"*10)

# Q&A:
# If you assign different values for the same key,
# the last assigned value will be kept
dictionary_sample = {1: "John", 2: 12, 1: "Bob"}
print(f"The dictionary contains: {dictionary_sample}")
print("Value at key 1:", dictionary_sample[1])

