from models.database import Database

class SubjectController:
    INDENT = " " * 20

    def __init__(self, student):
        self.db = Database()
        self.student = student
    
    def iprint(self, text):
        print(f"{self.INDENT}{text}")

    def iinput(self, text):
        return input(f"{self.INDENT}{text}")

    def read_choice(self):
        return self.iinput("Student Course Menu (c/e/r/s/x): ").strip().lower()

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
        self.iprint("Invalid option. Please try again.")
        self.iprint("c = change password")
        self.iprint("e = enrol in a subject")
        self.iprint("r = remove a subject")
        self.iprint("s = show subjects")
        self.iprint("x = exit")
