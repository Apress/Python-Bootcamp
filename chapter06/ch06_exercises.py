# Exercise 6.1
contents = ["John", 12, 25, "Sam", True, 50.7]
print(f"The original list is: {contents}")
# Removing the last two elements from the list
del(contents[-2:])
print(f"Now the list is: {contents}")
print("-"*10)

# Exercise 6.2
sample_tuple = (1, 2, 3, "Sam", 5)
# print(sample_tuple[5]) # Error
print(sample_tuple[2:6])
print("-"*10)

# Exercise 6.3
sample_tuple = (1, 2, 3, 4, 5)
first=sample_tuple[0]
print(f"Got first: {first}")
last=sample_tuple[-1]
print(f"Got last: {last}")
print(f"first+last: {first+last}")
print("-"*10)

# Exercise 6.4
sample_tuple = (1, 2, 3, 4, 5)
first=sample_tuple[:1]
print(f"Got first: {first}")
last=sample_tuple[-1:]
print(f"Got last: {last}")
print(f"first+last: {first+last}")
print("-"*10)

# Exercise 6.5
sample_dictionary={1:"One", 5:"Five", 3:"Three", 2:"Two"}
print(f"The given dictionary is: {sample_dictionary}")
keys_sorted=sorted(sample_dictionary)
print(f"Traversing the keys in the sorted order.")
for key in keys_sorted:
    print(key,sample_dictionary[key])
print("-"*10)

# Exercise 6.6
dictionary_sample = {1: "John", 2: 12, 1:"Bob"}
print(f"The dictionary contains: {dictionary_sample}")
print(f"Number of items: {len(dictionary_sample)}")
print("-"*10)