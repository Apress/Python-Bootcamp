# Using the 'with' keyword, updating the previous approaches.
# Now Python closes the file when it is no longer needed.

location="e:\\TestData\\OriginalFile.txt"
# Approach-2: reading a file using a for loop
with open(location, "r") as file_object:
    for current_line in file_object:
        print(current_line, end="")
print("-"*10)
# Approach-3: reading a file using the read() function
with open(location, 'r') as file_object:
    content= file_object.read()
print(content)
