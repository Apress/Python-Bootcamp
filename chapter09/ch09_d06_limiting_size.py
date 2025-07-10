location="e:\\TestData\\NewFile.txt"
with open(location, "r") as file_object:
    buffer=10
    content= file_object.read(buffer)
    while content:
        print(content)
        # print(content,end="")
        content = file_object.read(buffer)


