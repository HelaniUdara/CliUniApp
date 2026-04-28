from models.database import Database

class AdminController:
    def __init__(self):
        self.db = Database()

    def admin_menu(self):
        while True:
            choice = input("Admin System (c/g/p/r/s/x): ").strip().lower()
            if choice == 'c':
                pass
            elif choice == 'g':
                pass
            elif choice == 'p':
                pass
            elif choice == 'r':
                pass
            elif choice == 's':
                pass
            elif choice == 'x':
                break

