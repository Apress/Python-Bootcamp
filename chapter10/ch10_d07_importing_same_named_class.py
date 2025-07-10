import ch10_student_module

class Student:
    def __init__(self):
        print("Using the new Student class of the current file now.")

# Creating a Student instance and displaying the info
sam= ch10_student_module.Student("Sam", 1)
sam.describe()

stream_sam= ch10_student_module.Stream(sam, "Science")
print(stream_sam.display())

# Using the Student class of the current file
jack=Student()