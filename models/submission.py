
from datetime import datetime


class Submission:
    def __init__(self, submission_id, student, assignment, file):
        if not submission_id or not student or not assignment or not file:
            raise ValueError("Submission information cannot be empty.")
        self.submission_id = submission_id
        self.submit_date = datetime.now()
        self.file = file
        self.student = student
        self.assignment = assignment
        self.grade = None

    def submit(self):
     for existing_submission in self.assignment.submissions:
        if existing_submission.student == self.student:
            raise ValueError("You have already submitted this assignment.")

     self.assignment.submissions.append(self)

     print(f"{self.student.name} submitted {self.file} successfully.")