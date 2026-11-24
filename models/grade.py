

class Grade:
    def __init__(self, grade_id, marks, feedback, submission):

        if not 0 <= marks <= 100:
            raise ValueError("Marks must be between 0 and 100.")

        self.grade_id = grade_id
        self.marks = marks
        self.feedback = feedback
        self.submission = submission

    def record_grade(self):

        if self.submission.grade is not None:
            raise ValueError("This submission has already been graded.")

        self.submission.grade = self

        student = self.submission.student

        if self not in student.grades:
            student.grades.append(self)

        print(f"Grade recorded for {student.name}.")

