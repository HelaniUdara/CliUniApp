import re
from models.student import Student
from models.database import Database
from controllers.subject_controller import SubjectController

EMAIL_PATTERN = r'^[a-zA-Z]+\.[a-zA-Z]+@university\.com$'
PASSWORD_PATTERN = r'^[A-Z][a-zA-Z]{4,}\d{3,}$'

def validate(email, password):
    try:
        return bool(re.match(EMAIL_PATTERN, email) and re.match(PASSWORD_PATTERN, password))
    except TypeError:
        return False


class StudentController:
    def __init__(self):
        self.db = Database()

    def student_menu(self):
        while True:
            try:
                choice = input("Student System (l/r/x): ").strip().lower()
            except EOFError:
                break
            if choice == 'l':
                self.login()
            elif choice == 'r':
                self.register()
            elif choice == 'x':
                break

    def register(self):
        print("Student Sign Up")
        try:
            while True:
                email = input("Email: ")
                password = input("Password: ")
                if validate(email, password):
                    print("email and password formats acceptable")
                    break
                print("Incorrect email or password format")

            students = self.db.load()
            for student in students:
                if student.email == email:
                    print(f"Student {student.name} already exists")
                    return

            name = input("Name: ")
            print(f"Enrolling Student {name}")
            new_student = Student(name, email, password)
            new_student.id = self.db.generate_student_id(students)
            students.append(new_student)
            self.db.save(students)

        except EOFError:
            print("Registration cancelled.")

    def login(self):
        print("Student Sign In")
        try:
            while True:
                email = input("Email: ")
                password = input("Password: ")
                if validate(email, password):
                    print("email and password formats acceptable")
                    break
                print("Incorrect email or password format")

            students = self.db.load()
            for student in students:
                if student.email == email and student.password == password:
                    SubjectController().subject_menu(student, students)
                    return

            print("Student does not exist")

        except EOFError:
            print("Login cancelled.")