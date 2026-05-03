from models.database import Database

class SubjectController:
    def __init__(self, student):
        self.db = Database()
        self.student = student

    def read_choice(self):
        return input("Student Course Menu (c/e/r/s/x): ").strip().lower()

    def subject_menu(self):
        choice = self.read_choice()
        while choice != 'x':
            try:
                match choice:
                    case 'c':
                        self.change_password()
                    case 'e':
                        self.enrol()
                    case 'r':
                        self.remove_subject()
                    case 's':
                        self.show_subjects()
                    case _:
                        self.help()
                choice = self.read_choice()
            except EOFError:
                break

    def change_password(self):
        pass

    def enrol(self):
        pass

    def remove_subject(self):
        pass

    def show_subjects(self):
        pass

    def help(self):
        print("Invalid option. Please try again.")
        print("c = change password")
        print("e = enrol in a subject")
        print("r = remove a subject")
        print("s = show subjects")
        print("x = exit")
