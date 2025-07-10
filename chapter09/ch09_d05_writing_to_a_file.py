# location="e:\\TestData\\NewFile.txt"
# with (open(location, "w") as file_object):
#     file_object.write("Python is a programming language. ")
#     file_object.write("It supports object-oriented programming.")
#
# print(f"Reading the content of {location} now.")
# with open(location, "r") as file_object:
#     content = file_object.read()
# print(content)

# Alternative implementation
location="e:\\TestData\\NewFile.txt"
with open(location, "w+") as file_object:
    # #  For Q&A
    # file_object.write("Python is a programming language. \n")
    # file_object.write("It supports object-oriented programming. \n")
    file_object.write("Python is a programming language. ")
    file_object.write("It supports object-oriented programming.")
    file_object.seek(0) # moving the pointer at the beginning
    print(f"Reading the content of {location} now.")
    content= file_object.read()
print(content)