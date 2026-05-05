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
                        self.clear_database()
                    case 'g':
                        self.group_students()
                    case 'p':
                        self.partition_students()
                    case 'r':
                        self.remove_student()
                    case 's':
                        self.show_students()
                    case _:
                        self.help()
                choice = self.read_choice()
            except EOFError:
                break

    def show_students(self):
        students = self.db.load()
        if not students:
            print("No students found.")
            return

        print("Student List")
        for student in students:
            print(student)

    def get_average_mark(self, student):
        if not student.subjects:
            return 0
        return sum(subject.mark for subject in student.subjects) / len(student.subjects)

    def get_grade(self, mark):
        if mark >= 85:
            return "HD"
        elif mark >= 75:
            return "D"
        elif mark >= 65:
            return "C"
        elif mark >= 50:
            return "P"
        else:
            return "Z"

    def group_students(self):
        students = self.db.load()
        groups = {"HD": [], "D": [], "C": [], "P": [], "Z": []}

        for student in students:
            avg = self.get_average_mark(student)
            grade = self.get_grade(avg)
            groups[grade].append(student)

        for grade, group in groups.items():
            print(f"{grade}:")
            if not group:
                print("  No students")
            else:
                for student in group:
                    print(f"  {student.name} :: {student.id}")

    def partition_students(self):
        students = self.db.load()
        passed = []
        failed = []

        for student in students:
            avg = self.get_average_mark(student)
            if avg >= 50:
                passed.append(student)
            else:
                failed.append(student)

        print("PASS:")
        for student in passed:
            print(f"  {student.name} :: {student.id}")

        print("FAIL:")
        for student in failed:
            print(f"  {student.name} :: {student.id}")

    def remove_student(self):
        student_id = input("Remove student by ID: ").strip()
        students = self.db.load()

        updated_students = [student for student in students if str(student.id) != student_id]

        if len(updated_students) == len(students):
            print(f"Student {student_id} does not exist.")
            return

        self.db.save(updated_students)
        print(f"Removing Student {student_id} Account")

    def clear_database(self):
        confirm = input("Are you sure you want to clear the database? (Y/N): ").strip().upper()

        if confirm == "Y":
            self.db.clear()
            print("Students data cleared.")
        else:
            print("Clear database cancelled.")
    
    def help(self):
        print("Invalid option. Please try again.")
        print("c = clear database")
        print("g = group students")
        print("p = partition students")
        print("r = remove student")
        print("s = show students")
        print("x = exit")

