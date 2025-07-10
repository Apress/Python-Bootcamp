numbers = [1, 2, 3, 4, 5]
# Adds 100 to each item in the list
new_numbers= list(map(lambda x: x + 100, numbers))
print(f"The original list: {numbers}")
print(f"The updated list: {new_numbers}")

