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
            print("< Nothing to Display >")
            return

        print("Student List")
        for student in students:
            print(f"{student.name} :: {student.id} --> Email: {student.email}")

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

        if not students:
            print("Grade Grouping")
            print("< Nothing to Display >")
            return

        groups = {"HD": [], "D": [], "C": [], "P": [], "Z": []}

        for student in students:
            avg = self.get_average_mark(student)
            grade = self.get_grade(avg)
            groups[grade].append((student, avg))

        print("Grade Grouping")

        for grade in ["HD", "D", "C", "P", "Z"]:
            group = groups[grade]

            if group:
                entries = []
                for student, avg in group:
                    entries.append(
                        f"{student.name} :: {student.id} --> GRADE: {grade} - MARK: {avg:.2f}"
                    )

                print(f"{grade} --> [{', '.join(entries)}]")

    def partition_students(self):
        students = self.db.load()

        if not students:
            print("PASS/FAIL Partition")
            print("< Nothing to Display >")
            return

        passed = []
        failed = []

        for student in students:
            avg = self.get_average_mark(student)
            grade = self.get_grade(avg)

            entry = f"{student.name} :: {student.id} --> GRADE: {grade} - MARK: {avg:.2f}"

            if avg >= 50:
                passed.append(entry)
            else:
                failed.append(entry)

        print("PASS/FAIL Partition")
        print(f"FAIL --> [{', '.join(failed)}]")
        print(f"PASS --> [{', '.join(passed)}]")

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

