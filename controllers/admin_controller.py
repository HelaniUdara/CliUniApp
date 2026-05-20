from models.database import Database

class AdminController:
    INDENT = " " * 10

    def __init__(self):
        self.db = Database()
    
    def iprint(self, text):
        print(f"{self.INDENT}{text}")

    def iinput(self, text):
        return input(f"{self.INDENT}{text}")

    def read_choice(self):
        return self.iinput("Admin System (c/g/p/r/s/x): ").strip().lower()
    
    def show_menu(self):
        self.iprint("Admin System")
        self.iprint("  c = Clear Database")
        self.iprint("  g = Group Students")
        self.iprint("  p = Partition Students")
        self.iprint("  r = Remove Student")
        self.iprint("  s = Show Students")
        self.iprint("  x = Exit")

    def admin_menu(self):
        self.show_menu()
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
                self.iprint("Error occurred. Returning to University Menu.")
                break

    def show_students(self):
        students = self.db.load()
        if not students:
            self.iprint("< Nothing to Display >")
            return

        self.iprint("Student List")
        for student in students:
            self.iprint(f"{student.name} :: {student.id} --> Email: {student.email}")

    def get_average_mark(self, student):
        return student.avg

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
            self.iprint("Grade Grouping")
            self.iprint("< Nothing to Display >")
            return

        groups = {"HD": [], "D": [], "C": [], "P": [], "Z": []}

        for student in students:
            avg = self.get_average_mark(student)
            grade = self.get_grade(avg)
            groups[grade].append((student, avg))

        self.iprint("Grade Grouping")

        for grade in ["HD", "D", "C", "P", "Z"]:
            group = groups[grade]

            if group:
                entries = []
                for student, avg in group:
                    entries.append(
                        f"{student.name} :: {student.id} --> GRADE: {grade} - MARK: {avg:.2f}"
                    )

                self.iprint(f"{grade} --> [{', '.join(entries)}]")

    def partition_students(self):
        students = self.db.load()

        if not students:
            self.iprint("PASS/FAIL Partition")
            self.iprint("< Nothing to Display >")
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

        self.iprint("PASS/FAIL Partition")
        self.iprint(f"FAIL --> [{', '.join(failed)}]")
        self.iprint(f"PASS --> [{', '.join(passed)}]")

    def remove_student(self):
        student_id = self.iinput("Remove student by ID: ").strip()
        students = self.db.load()

        updated_students = [student for student in students if str(student.id) != student_id]

        if len(updated_students) == len(students):
            self.iprint(f"Student {student_id} does not exist.")
            return

        self.db.save(updated_students)
        self.iprint(f"Removing Student {student_id} Account")

    def clear_database(self):
        confirm = self.iinput("Are you sure you want to clear the database? (Y/N): ").strip().upper()

        if confirm == "Y":
            self.db.clear()
            self.iprint("Students data cleared.")
        else:
            self.iprint("Clear database cancelled.")
    
    def help(self):
        self.iprint("Invalid option. Please try again.")
        self.show_menu()


