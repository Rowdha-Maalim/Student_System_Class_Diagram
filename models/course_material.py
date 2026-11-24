class CourseMaterial:
    def __init__(self, material_id, file_name, file_type, course):
        if not material_id or not file_name or not file_type:
            raise ValueError("Course material information cannot be empty.")
        self.material_id = material_id
        self.file_name = file_name
        self.file_type = file_type
        self.course = course

    def upload_material(self):
     if self not in self.course.materials:
        self.course.add_material(self)
        print(f"{self.file_name} uploaded successfully.")
     else:
        print(f"{self.file_name} is already uploaded.")