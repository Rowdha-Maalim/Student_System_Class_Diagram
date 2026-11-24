from models.user import User


class Instructor(User):
    def __init__(self, user_id, name, email, password, instructor_id):
       if not instructor_id:
        raise ValueError("Instructor ID cannot be empty.")
       super().__init__(user_id, name, email, password)
       self.instructor_id = instructor_id
       self.courses = []

    def create_course(self, course_id, course_name, description):
        from models.course import Course

        course = Course(course_id, course_name, description, self)
        self.courses.append(course)
        return course

    def create_assignment(self, course, assignment_id, title, deadline):
        from models.assignment import Assignment

        assignment = Assignment(assignment_id, title, deadline, course)
        course.assignments.append(assignment)
        return assignment

    def grade_submission(self, submission, grade_id, marks, feedback):
        from models.grade import Grade

        grade = Grade(grade_id, marks, feedback, submission)
        grade.record_grade()

        return grade
