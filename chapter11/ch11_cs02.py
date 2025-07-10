class Engineering:
    """ Engineering is the parent class. """
    def __init__(self,institution):
        # Initializes the common subjects
        self.institution = institution
        self.subject_1 = "Mathematics."
        self.subject_2 = "Artificial Intelligence."

class ComputerScience(Engineering):
    """
    The ComputerScience class inherits from
    the Engineering class.
    """

    def __init__(self,institution, elective):
        """ Initialize starts from parent class."""
        super().__init__(institution)
        self.subject_3 = elective

    def course_details(self):
        """ Prints the course details of an institution. """
        print("*"*10)
        print(f"Institution name: {self.institution}")
        print("Computer science course includes:")
        print(f"1:{self.subject_1}")
        print(f"2:{self.subject_2}")
        print(f"3:{self.subject_3}")
        print("*" * 10)

# Supply the institution name
institution_name = input("Enter the institution name: ")
# Enter the elective paper
elective_paper = input("Enter the elective paper: ")
cs_course= ComputerScience(institution_name,elective_paper)
cs_course.course_details()