location="e:\\TestData\\OriginalFile.txt"
file_object = open(location, "r")
# Approach-1: reading a file line by line
# first_line = file_object.readline()
# print(first_line)
# second_line = file_object.readline()
# print(second_line)
# third_line = file_object.readline()
# print(third_line)
# file_object.close()

# Approach-2: reading a file using a for loop
for current_line in file_object:
    print(current_line, end="")
file_object.close()
#
# Approach-3: using the read() function
# content = file_object.read()
# print(content)
