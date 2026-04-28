from models.database import Database

class SubjectController:
    def __init__(self):
        self.db = Database()

    def subject_menu(self, student, students):
        while True:
            try:
                choice = input("Student Course Menu (c/e/r/s/x): ").strip().lower()
            except EOFError:
                break
            if choice == 'c':
                self.change_password(student, students)
            elif choice == 'e':
                self.enrol(student, students)
            elif choice == 'r':
                self.remove_subject(student, students)
            elif choice == 's':
                self.show_subjects(student)
            elif choice == 'x':
                break

    def change_password(self, student, students):
        pass

    def enrol(self, student, students):
        pass

    def remove_subject(self, student, students):
        pass

    def show_subjects(self, student):
        pass