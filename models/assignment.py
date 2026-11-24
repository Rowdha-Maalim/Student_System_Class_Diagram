class Assignment:
    def __init__(self, assignment_id, title, deadline, course):
        if not assignment_id or not title or not deadline:
            raise ValueError("Assignment information cannot be empty.")
        self.assignment_id = assignment_id
        self.title = title
        self.deadline = deadline
        self.course = course
        self.submissions = []

    def set_details(self, title, deadline):
        if not title or not deadline:
            raise ValueError("Assignment title and deadline cannot be empty.")
        self.title = title
        self.deadline = deadline