from models.student import Student
from models.course import Course
from models.instructor import Instructor


try:
    student = Student(
        "U004", "", "test@example.com", "pass123", "ST003"
    )
except ValueError as error:
    print("Student validation works:", error)



try:
    course = Course(
        "C002", "", "Introduction to programming", None
    )
except ValueError as error:
    print("Course validation works:", error)
    
try:
    instructor = Instructor(
        "U005", "Sarah", "", "pass123", "INS002"
    )
except ValueError as error:
    print("Instructor validation works:", error)
    
from models.student import Student
from models.course import Course

student = Student(
    "U006", "Alex", "alex2@example.com", "pass123", "ST006"
)

course = Course(
    "C003", "Python", "Python programming", None
)

assignment = None

from models.assignment import Assignment

assignment = Assignment(
    "A003", "Python Basics", "2026-12-10", course
)


submission = student.submit_assignment(assignment)
print("First submission successful.")


try:
    student.submit_assignment(assignment)
except ValueError as error:
    print("Duplicate submission prevented:", error)