import re
from models.student import Student
from models.database import Database
from controllers.subject_controller import SubjectController

EMAIL_PATTERN = r'^[a-zA-Z]+\.[a-zA-Z]+@university\.com$'
PASSWORD_PATTERN = r'^[A-Z][a-zA-Z]{4,}\d{3,}$'


class StudentController:
    INDENT = " " * 10

    def __init__(self):
        self.db = Database()
    
    def iprint(self, text):
        print(f"{self.INDENT}{text}")

    def iinput(self, text):
        return input(f"{self.INDENT}{text}")

    def validate(self, email, password):
        try:
            return bool(re.match(EMAIL_PATTERN, email) and re.match(PASSWORD_PATTERN, password))
        except TypeError:
            return False
    
    def read_choice(self):
        return self.iinput("Student System (l/r/x): ").strip().lower()
    
    def show_menu(self):
        self.iprint("Student System")
        self.iprint("  l = Login")
        self.iprint("  r = Register")
        self.iprint("  x = Exit")

    def sign_up_instructions(self):
        self.iprint("Enter your email and password.")
        self.iprint("Email must be in format firstname.lastname@university.com")
        self.iprint("Password must start with uppercase, have 5+ letters and 3+ digits (e.g. Password123)")

    def student_menu(self):
        self.show_menu()
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
                self.iprint("Error occurred. Returning to Main Menu.")
                break

    def register(self):
        self.iprint("Student Sign Up:")
        try:
            self.sign_up_instructions()
            while True:
                email = self.iinput("Email: ")
                password = self.iinput("Password: ")
                if self.validate(email, password):
                    self.iprint("email and password formats acceptable")
                    break
                self.iprint("Incorrect email or password format. Email must be in format firstname.lastname@university.com and password must be in format Password123")

            existing = self.db.get_student_by_email(email)
            if existing:
                self.iprint(f"Student {existing.name} already exists")
                return

            name = self.iinput("Name: ")
            self.iprint(f"Enrolling Student {name}")
            new_student = Student(name, email, password)
            students = self.db.load()
            new_student.id = self.db.generate_student_id(students)
            students.append(new_student)
            self.db.save(students)

        except EOFError:
            self.iprint("Error occurred. Registration cancelled.")

    def login(self):
        self.iprint("Student Sign In")
        try:
            while True:
                email = self.iinput("Email: ")
                password = self.iinput("Password: ")
                if self.validate(email, password):
                    self.iprint("email and password formats acceptable")
                    break
                self.iprint("Incorrect email or password format")

            student = self.db.match(email, password)
            if student:
                SubjectController(student).subject_menu()
            else:
                self.iprint("Student does not exist")

        except EOFError:
            self.iprint("Error occurred. Login cancelled.")

    def help(self):
        self.iprint("Invalid option. Please try again.")
        self.show_menu()

    