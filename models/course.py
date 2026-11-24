class Course:
    def __init__(self, course_id, course_name, description, instructor):
        if not course_id or not course_name or not description:
            raise ValueError("Course information cannot be empty.")
        self.course_id = course_id
        self.course_name = course_name
        self.description = description
        self.instructor = instructor

        self.students = []
        self.assignments = []
        self.materials = []
        self.announcements = []

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)

    def add_material(self, material):
     if material not in self.materials:
        self.materials.append(material)