# Student System Class Diagram

## About the Project

This is a Python project that demonstrates how students and instructors interact with courses.

An instructor can create a course, create assignments, upload course materials, publish announcements and grade submissions. Students can enrol in a course, submit an assignment and view their grades.

## Features

- Create student and instructor objects
- Create courses and enrol students in them
- Create assignments and submit work
- Record grades and feedback
- Add course materials
- Post course announcements
- Check that required information is not empty
- Prevent duplicate student enrollments and assignment submission.


## Technologies Used

- Python 3.12
- Visual Studio Code
- diagrams.net (for the UML class diagram)

No additional python libraries are required.

## Project Structure

- `models/` contains the class files (User, Student, Instructor, Course, Assignment, CourseMaterial, Announcement, Submission and Grade)
- `design/` contains the UML class diagram
- `main.py` creates objects from the classes and runs the system
- `test_validation.py` contains tests for empty information and duplicate submissions
- `README.md` provides information about the project

## How to Run

1. Install Python 3.12.
2. Open the project folder in Visual Studio Code.
3. Open the terminal in the project folder.
4. Run the following command:

```
python main.py
```

## OOP Concepts Used

- **Classes and objects:** each part of the system is a class, and objects are made from those classes.
- **Inheritance:** Student and Instructor inherit from User, so they share its attributes and its login and logout methods.
- **Encapsulation:** each class keeps its own data and the methods that work on that data. The constructors also check for empty values.
- **Methods:** actions like enrolling, submitting and grading are written as methods.
- **Relationships:** the classes link to each other, for example a course holds its students and assignments, and a submission belongs to a student and an assignment.

## Testing

I tested the program by running it with different inputs. I checked that empty information raises an error and that a student cannot enrol in the same course twice.

## Purpose

I made this project to turn a UML class diagram into working Python code and to practise what I learned about software implementation.
