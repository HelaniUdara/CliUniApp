import tkinter as tk
from tkinter import messagebox
import re

from models.student import Student
from models.subject import Subject
from models.database import Database


class ExceptionWindow(tk.Toplevel):
    def __init__(self, parent, message):
        super().__init__(parent)
        self.title("Notice")
        self.geometry("320x150")
        self.resizable(False, False)

        tk.Label(self, text="⚠", font=("Arial", 28), fg="#e74c3c").pack(pady=(15, 5))
        tk.Label(self, text=message, font=("Arial", 10), wraplength=280, justify="center").pack(pady=5)
        tk.Button(self, text="OK", command=self.destroy, width=10, bg="#e74c3c", fg="white", font=("Arial", 10)).pack(pady=(5, 15))

        self.grab_set()
        self.focus()
        self.update_idletasks()
        x = (self.winfo_screenwidth() // 2) - 160
        y = (self.winfo_screenheight() // 2) - 75
        self.geometry(f"320x150+{x}+{y}")


class SubjectWindow(tk.Toplevel):
    def __init__(self, parent, student):
        super().__init__(parent)
        self.title("My Subjects")
        self.geometry("480x360")
        self.resizable(False, False)

        tk.Label(self, text=f"Enrolled Subjects — {student.name}", font=("Arial", 13, "bold"), pady=12).pack()
        tk.Frame(self, height=1, bg="#cccccc").pack(fill=tk.X, padx=20)

        list_frame = tk.Frame(self)
        list_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox = tk.Listbox(list_frame, yscrollcommand=scrollbar.set, font=("Courier New", 11), height=10, selectmode=tk.SINGLE, bd=0, highlightthickness=1)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.listbox.yview)

        if student.subjects:
            for sub in student.subjects:
                grade_str = sub.grade if sub.grade is not None else "N/A"
                line = f"  [ Subject::{sub.id:03d} -- mark = {sub.mark} -- grade = {grade_str:>3} ]"
                self.listbox.insert(tk.END, line)
        else:
            self.listbox.insert(tk.END, "  < No subjects enrolled yet >")

        tk.Button(self, text="Close", command=self.destroy, width=12, bg="#7f8c8d", fg="white", font=("Arial", 10)).pack(pady=10)

        self.grab_set()
        self.update_idletasks()
        x = (self.winfo_screenwidth() // 2) - 240
        y = (self.winfo_screenheight() // 2) - 180
        self.geometry(f"480x360+{x}+{y}")


class EnrolmentWindow(tk.Toplevel):
    def __init__(self, parent, student):
        super().__init__(parent)
        self.title("Enrolment")
        self.geometry("400x320")
        self.resizable(False, False)

        self.student = student
        self.db = Database()

        tk.Label(self, text=f"Welcome, {student.name}", font=("Arial", 15, "bold"), pady=15).pack()
        tk.Frame(self, height=1, bg="#cccccc").pack(fill=tk.X, padx=30)

        self.count_label = tk.Label(self, text=f"Enrolled: {len(student.subjects)} / 4 subjects", font=("Arial", 11), pady=10)
        self.count_label.pack()

        tk.Button(self, text="Enrol in a Subject", command=self.enrol_subject, width=22, bg="#27ae60", fg="white", font=("Arial", 11), pady=5).pack(pady=6)
        tk.Button(self, text="View My Subjects", command=self.view_subjects, width=22, bg="#2980b9", fg="white", font=("Arial", 11), pady=5).pack(pady=6)
        tk.Button(self, text="Logout", command=self.logout, width=22, bg="#c0392b", fg="white", font=("Arial", 11), pady=5).pack(pady=6)

        self.protocol("WM_DELETE_WINDOW", self.logout)
        self.grab_set()

        self.update_idletasks()
        x = (self.winfo_screenwidth() // 2) - 200
        y = (self.winfo_screenheight() // 2) - 160
        self.geometry(f"400x320+{x}+{y}")

    def enrol_subject(self):
        if len(self.student.subjects) >= 4:
            ExceptionWindow(self, "You are already enrolled in 4 subjects.\nStudents cannot enrol in more than 4 subjects.")
            return

        new_subject = Subject()
        self.student.subjects.append(new_subject)

        # save changes to file
        all_students = self.db.load()
        for i, s in enumerate(all_students):
            if s.id == self.student.id:
                all_students[i] = self.student
                break
        self.db.save(all_students)

        self.count_label.config(text=f"Enrolled: {len(self.student.subjects)} / 4 subjects")

        grade_str = new_subject.grade if new_subject.grade is not None else "N/A"
        messagebox.showinfo("Enrolled", f"Successfully enrolled in Subject-{new_subject.id}!\nMark: {new_subject.mark}  |  Grade: {grade_str}")

    def view_subjects(self):
        SubjectWindow(self, self.student)

    def logout(self):
        self.grab_release()
        self.destroy()


class LoginWindow:
    EMAIL_PATTERN = re.compile(r'^[a-zA-Z]+\.[a-zA-Z]+@university\.com$')
    PASSWORD_PATTERN = re.compile(r'^[A-Z][a-zA-Z]{4,}\d{3,}$')

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("GUIUniApp")
        self.root.geometry("380x280")
        self.root.resizable(False, False)

        self.db = Database()
        self._build_ui()

        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - 190
        y = (self.root.winfo_screenheight() // 2) - 140
        self.root.geometry(f"380x280+{x}+{y}")

    def _build_ui(self):
        tk.Label(self.root, text="University Login", font=("Arial", 17, "bold"), pady=18).pack()

        # email
        email_row = tk.Frame(self.root)
        email_row.pack(pady=6)
        tk.Label(email_row, text="Email:", font=("Arial", 11), width=10, anchor="e").pack(side=tk.LEFT)
        self.email_entry = tk.Entry(email_row, font=("Arial", 11), width=24)
        self.email_entry.pack(side=tk.LEFT, padx=6)

        # password
        pass_row = tk.Frame(self.root)
        pass_row.pack(pady=6)
        tk.Label(pass_row, text="Password:", font=("Arial", 11), width=10, anchor="e").pack(side=tk.LEFT)
        self.pass_entry = tk.Entry(pass_row, font=("Arial", 11), width=24, show="*")
        self.pass_entry.pack(side=tk.LEFT, padx=6)

        tk.Button(self.root, text="Login", command=self.attempt_login, font=("Arial", 11), width=16, bg="#2980b9", fg="white", pady=5).pack(pady=18)

        self.root.bind("<Return>", lambda event: self.attempt_login())

    def attempt_login(self):
        email = self.email_entry.get().strip()
        password = self.pass_entry.get().strip()

        if not email or not password:
            ExceptionWindow(self.root, "Email and password fields cannot be empty.")
            return

        if not self.EMAIL_PATTERN.match(email) or not self.PASSWORD_PATTERN.match(password):
            ExceptionWindow(self.root, "Incorrect email or password format.\n\nEmail: firstname.lastname@university.com\nPassword: Starts uppercase, 5+ letters, 3+ digits.")
            return

        students = self.db.load()
        for student in students:
            if student.email == email and student.password == password:
                self.root.withdraw()
                enrolment = EnrolmentWindow(self.root, student)
                enrolment.wait_window()
                # show login again after logout
                self.root.deiconify()
                self.email_entry.delete(0, tk.END)
                self.pass_entry.delete(0, tk.END)
                return

        ExceptionWindow(self.root, "Student does not exist.\n\nPlease register first using CLIUniApp.")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = LoginWindow()
    app.run()