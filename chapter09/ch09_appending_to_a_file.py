location="e:\\TestData\\OriginalFile.txt"
# Opening the file in 'a' mode and adding the content
with open(location, "a") as file_object:
    file_object.write("Python supports object-oriented programming.")    

# Verifying the file contents now
with open(location, "r") as file_object:
    print(f"Reading the content of {location} now.")
    content= file_object.read()
    print(content)
