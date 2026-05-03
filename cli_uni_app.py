from controllers.student_controller import StudentController
from controllers.admin_controller import AdminController


def help():
    print("Invalid option. Please try again.")
    print("A = Admin")
    print("S = Student")
    print("X = Exit")

def read_choice():
    return input("University System: (A)dmin, (S)tudent, or X : ").strip().upper()

def main():
    try:
        choice = read_choice()
        while choice != 'X':
            match choice:
                case 'A':
                    AdminController().admin_menu()
                case 'S':
                    StudentController().student_menu()
                case _:
                    help()
            choice = read_choice()
        print("Thank You")
    except EOFError:
        print("\nThank You")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nThank You")
    except Exception as e:        
        print(f"An error occurred: {e}")