
from models.instructor import Instructor
from models.student import Student
from models.course_material import CourseMaterial
from models.announcement import Announcement


# 1. Create an instructor
instructor = Instructor(
    "U001",
    "Sarah",
    "sarah@example.com",
    "example123",
    "INS001"
)

# 2. Create students
student1 = Student(
    "U002", "Alex", "alex@example.com", "example123", "ST001"
)

student2 = Student(
    "U003", "John", "john@example.com", "example123", "ST002"
)

# 3. Instructor creates a course
course = instructor.create_course(
    "C001",
    "Python Programming",
    "Introduction to Python programming"
)

# 4. Students enroll in the course
student1.enroll_in_course(course)
student2.enroll_in_course(course)

# 5. Instructor creates an assignment
assignment = instructor.create_assignment(
    course,
    "A001",
    "Python Basics",
    "2026-12-10"
)

# 6. Students submit their assignments
submission1 = student1.submit_assignment(assignment)
submission1.file = "Alex_Assignment.pdf"
submission1.submit()

submission2 = student2.submit_assignment(assignment)
submission2.file = "John_Assignment.pdf"
submission2.submit()

# 7. Instructor uploads course material
material = CourseMaterial(
    "M001",
    "Python_Notes.pdf",
    "PDF",
    course
)

material.upload_material()

# 8. Instructor publishes an announcement
announcement = Announcement(
    "ANN001",
    "Remember to complete your Python assignment.",
    "2026-11-22",
    course
)

announcement.publish()

# 9. Instructor grades the submissions
grade1 = instructor.grade_submission(
    submission1, "G001", 85.5, "Good work!"
)

grade2 = instructor.grade_submission(
    submission2, "G002", 90.0, "Excellent work!"
)

# 10. Display the system information
print("\n===== STUDENT COURSE MANAGEMENT SYSTEM =====")

print("\nCourse:", course.course_name)
print("Instructor:", course.instructor.name)

print("\nEnrolled Students:")
for student in course.students:
    print("-", student.name, "|", student.student_id)

print("\nAssignments:")
for item in course.assignments:
    print("-", item.title, "| Deadline:", item.deadline)

print("\nSubmissions:")
for submission in assignment.submissions:
    print("-", submission.student.name, "|", submission.file)

print("\nStudent Grades:")
for student in course.students:
    print("\nStudent:", student.name)

    for grade in student.view_grades():
        print("Marks:", grade.marks)
        print("Feedback:", grade.feedback)

print("\nTotal Course Materials:", len(course.materials))
print("Total Announcements:", len(course.announcements))

print("\n===== END OF SYSTEM =====")




