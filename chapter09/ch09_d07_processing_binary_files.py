# Using two files-one for reading and one for writing
input_file="e:\\TestData\\flower.png"
output_file="e:\\TestData\\new_flower.png"

with open(input_file, "rb") as input_object:
    content=input_object.read()
    # print(content)
    with open(output_file, "wb") as output_object:
        output_object.write(content)
        #  The following block will also work
        # for content in input_object:
        #     output_object.write(content)





