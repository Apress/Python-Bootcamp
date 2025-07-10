# String
message = "Welcome"
print(f"The string is: {message}")
print(f"Is 'com' present in the string? {'com' in message}")  # True
print(f"Is 'com' absent in the string? {'com' not in message}")  # False
print("-"*10)
# Tuple
numbers = (1, 2, 3)
print(f"The contents of the tuple are: {numbers}")
print(f"Is 1 present in the tuple? {1 in numbers}")  # True
print(f"Is 2 absent in the tuple? {2 not in numbers}")  # False
print("-"*10)
# Dictionary
sample_dict = {"key1": 10, "key2": 25}
print(f"The contents of the dictionary are: {sample_dict}")
print(f"Is key1 a key in the dictionary? {'key1' in sample_dict}")  # True
print(f"Is 20 a value in the dictionary? {20 in sample_dict.values()}")  # False
