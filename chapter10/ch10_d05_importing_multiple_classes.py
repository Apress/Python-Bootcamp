from ch10_student_module import Student,Stream

# Creating a Student instance and displaying the info
sam= Student("Sam", 1)
sam.describe()

stream_sam=Stream(sam,"Science")
print(stream_sam.display())