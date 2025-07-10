from ch10_student_module import * # Not a recommended practice

class Student:
    pass

# There will be a name collision after the addition
# of the Student class in the current file
# Creating a Student instance and displaying the info
sam= Student("Sam", 1)

sam.describe()
stream_sam= Stream(sam, "Science")
print(stream_sam.display())