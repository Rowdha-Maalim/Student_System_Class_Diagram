from models.user import User


class Student(User):
    def __init__(self, user_id, name, email, password, student_id):

        if not student_id:
            raise ValueError("Student ID cannot be empty.")

        super().__init__(user_id, name, email, password)

        self.student_id = student_id
        self.courses = []
        self.submissions = []
        self.grades = []

    def enroll_in_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            course.add_student(self)

    def submit_assignment(self, assignment):
        from models.submission import Submission

        for submission in self.submissions:
            if submission.assignment == assignment:
                raise ValueError("You have already submitted this assignment.")

        submission = Submission(
            submission_id=f"SUB{len(self.submissions) + 1:03}",
            student=self,
            assignment=assignment,
            file="assignment_file"
        )

        self.submissions.append(submission)
        return submission

    def view_grades(self):
        return self.grades
        