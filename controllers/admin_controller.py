from models.database import Database

db = Database()


def admin_menu():
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
