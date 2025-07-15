import threading
from models.student import Student
from datetime import datetime

class StudentService:
    def __init__(self):
        self.students = {}           # Stores student objects keyed by student ID
        self.student_counter = 1     # Auto-incrementing ID for new students
        self.students_lock = threading.Lock()  # Ensures thread-safe access

    def create_student(self, name, age, email, interests=None, achievements=None, courses=None):
        # Create and add a new student to the store
        with self.students_lock:
            student = Student(
                id=self.student_counter,
                name=name.strip(),
                age=age,
                email=email.strip(),
                interests=interests or [],
                achievements=achievements or [],
                courses=courses or []
            )
            self.students[self.student_counter] = student
            self.student_counter += 1
            return student

    def get_all_students(self):
        # Return a list of all students
        with self.students_lock:
            return list(self.students.values())

    def get_student_by_id(self, student_id):
        # Fetch a student by their ID
        with self.students_lock:
            return self.students.get(student_id)

    def update_student(self, student_id, **kwargs):
        # Update fields of an existing student
        with self.students_lock:
            student = self.students.get(student_id)
            if not student:
                return None

            allowed_fields = {"name", "age", "email", "interests", "achievements", "courses"}

            # Update only allowed fields if value is not None
            for field, value in kwargs.items():
                if field in allowed_fields and value is not None:
                    if field in {"name", "email"} and isinstance(value, str):
                        setattr(student, field, value.strip())
                    else:
                        setattr(student, field, value)

            # Update the last-modified timestamp
            student.updated_at = datetime.now().isoformat()
            return student

    def delete_student(self, student_id):
        # Remove a student by ID
        with self.students_lock:
            return self.students.pop(student_id, None)

    def get_student_count(self):
        # Get total number of students
        with self.students_lock:
            return len(self.students)

# Global service instance to be used by API
student_service = StudentService()
