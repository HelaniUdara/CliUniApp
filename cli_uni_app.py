from controllers.student_controller import StudentController
from controllers.admin_controller import AdminController


def main():
    while True:
        choice = input("University System: (A)dmin, (S)tudent, or X : ").strip().upper()
        if choice == 'A':
            AdminController().admin_menu()
        elif choice == 'S':
            StudentController().student_menu()
        elif choice == 'X':
            print("Thank You")
            break


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nThank You")
    except Exception as e:        
        print(f"An error occurred: {e}")
