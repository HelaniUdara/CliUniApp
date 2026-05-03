import re
from models.student import Student
from models.database import Database
from controllers.subject_controller import SubjectController

EMAIL_PATTERN = r'^[a-zA-Z]+\.[a-zA-Z]+@university\.com$'
PASSWORD_PATTERN = r'^[A-Z][a-zA-Z]{4,}\d{3,}$'


class StudentController:
    def __init__(self):
        self.db = Database()

    def validate(self, email, password):
        try:
            return bool(re.match(EMAIL_PATTERN, email) and re.match(PASSWORD_PATTERN, password))
        except TypeError:
            return False
    
    def read_choice(self):
        return input("Student System (l/r/x): ").strip().lower()

    def student_menu(self):
        choice = self.read_choice()
        while choice != 'x':
            try:
                match choice:
                    case 'l':
                        self.login()
                    case 'r':
                        self.register()
                    case _:
                        self.help()
                choice = self.read_choice()
            except EOFError:
                break

    def register(self):
        print("Student Sign Up")
        try:
            while True:
                email = input("Email: ")
                password = input("Password: ")
                if self.validate(email, password):
                    print("email and password formats acceptable")
                    break
                print("Incorrect email or password format")

            existing = self.db.get_student_by_email(email)
            if existing:
                print(f"Student {existing.name} already exists")
                return

            name = input("Name: ")
            print(f"Enrolling Student {name}")
            new_student = Student(name, email, password)
            students = self.db.load()
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
                if self.validate(email, password):
                    print("email and password formats acceptable")
                    break
                print("Incorrect email or password format")

            student = self.db.match(email, password)
            if student:
                SubjectController(student).subject_menu()
            else:
                print("Student does not exist")

        except EOFError:
            print("Login cancelled.")

    def help(self):
        print("Invalid option. Please try again.")
        print("l = login")
        print("r = register")
        print("x = exit")
