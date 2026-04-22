import re
from models.student import Student
from models.database import Database
from controllers.subject_controller import subject_menu

EMAIL_PATTERN = r'^[a-zA-Z]+\.[a-zA-Z]+@university\.com$'
PASSWORD_PATTERN = r'^[A-Z][a-zA-Z]{4,}\d{3,}$'

db = Database()


def validate(email, password):
    return bool(re.match(EMAIL_PATTERN, email) and re.match(PASSWORD_PATTERN, password))


def student_menu():
    while True:
        choice = input("Student System (l/r/x): ").strip().lower()
        if choice == 'l':
            login()
        elif choice == 'r':
            register()
        elif choice == 'x':
            break


def register():
    print("Student Sign Up")
    while True:
        email = input("Email: ")
        password = input("Password: ")
        if validate(email, password):
            print("email and password formats acceptable")
            break
        print("Incorrect email or password format")

    students = db.load()
    for student in students:
        if student.email == email:
            print(f"Student {student.name} already exists")
            return

    name = input("Name: ")
    print(f"Enrolling Student {name}")
    new_student = Student(name, email, password)
    new_student.id = db.generate_student_id(students)
    students.append(new_student)
    db.save(students)


def login():
    print("Student Sign In")
    while True:
        email = input("Email: ")
        password = input("Password: ")
        if validate(email, password):
            print("email and password formats acceptable")
            break
        print("Incorrect email or password format")

    students = db.load()
    for student in students:
        if student.email == email and student.password == password:
            subject_menu(student, students)
            return

    print("Student does not exist")
