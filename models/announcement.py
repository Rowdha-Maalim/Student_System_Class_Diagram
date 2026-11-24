
class Announcement:
    def __init__(self, announcement_id, message, date, course):
        if not announcement_id or not message or not date:
            raise ValueError("Announcement information cannot be empty.")
        self.announcement_id = announcement_id
        self.message = message
        self.date = date
        self.course = course

    def publish(self):
     if self not in self.course.announcements:
        self.course.announcements.append(self)
        print(f"Announcement published: {self.message}")
     else:
        print("This announcement has already been published.")
