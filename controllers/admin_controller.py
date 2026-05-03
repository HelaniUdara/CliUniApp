from models.database import Database

class AdminController:
    def __init__(self):
        self.db = Database()

    def read_choice(self):
        return input("Admin System (c/g/p/r/s/x): ").strip().lower()
    
    def admin_menu(self):
        choice = self.read_choice()
        while choice != 'x':
            try:
                match choice:
                    case 'c':
                        pass
                    case 'g':
                        pass
                    case 'p':
                        pass
                    case 'r':
                        pass
                    case 's':
                        pass
                    case _:
                        self.help()
                choice = self.read_choice()
            except EOFError:
                break

    def help(self):
        print("Invalid option. Please try again.")
        print("c = clear database")
        print("g = group students")
        print("p = partition students")
        print("r = remove student")
        print("s = show students")
        print("x = exit")

