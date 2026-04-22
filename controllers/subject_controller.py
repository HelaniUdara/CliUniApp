from models.database import Database

db = Database()


def subject_menu(student, students):
    while True:
        choice = input("Student Course Menu (c/e/r/s/x): ").strip().lower()
        if choice == 'c':
            change_password(student, students)
        elif choice == 'e':
            enrol(student, students)
        elif choice == 'r':
            remove_subject(student, students)
        elif choice == 's':
            show_subjects(student)
        elif choice == 'x':
            break


def change_password(student, students):
    pass


def enrol(student, students):
    pass


def remove_subject(student, students):
    pass


def show_subjects(student):
    pass
