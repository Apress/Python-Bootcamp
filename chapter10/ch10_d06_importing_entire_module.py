import ch10_student_module

# Creating a Student instance and displaying the info
sam= ch10_student_module.Student("Sam", 1)
sam.describe()

stream_sam= ch10_student_module.Stream(sam, "Science")
print(stream_sam.display())