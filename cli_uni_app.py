from controllers.student_controller import student_menu
from controllers.admin_controller import admin_menu


def main():
    while True:
        choice = input("University System: (A)dmin, (S)tudent, or X : ").strip().upper()
        if choice == 'A':
            admin_menu()
        elif choice == 'S':
            student_menu()
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