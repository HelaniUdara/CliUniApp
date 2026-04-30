import tkinter as tk
from tkinter import messagebox
import re

from models.student import Student
from models.subject import Subject
from models.database import Database


# ============================================================
# EXCEPTION WINDOW
# A small popup window that shows an error or warning message
# Contributed by: Satyam Das
# ============================================================
class ExceptionWindow(tk.Toplevel):

    def __init__(self, parent, message):
        super().__init__(parent)
        self.title("Notice")
        self.geometry("320x150")
        self.resizable(False, False)

        # Warning icon label
        tk.Label(self, text="⚠", font=("Arial", 28), fg="#e74c3c").pack(pady=(15, 5))

        # The actual error message text
        tk.Label(
            self,
            text=message,
            font=("Arial", 10),
            wraplength=280,
            justify="center"
        ).pack(pady=5)

        # OK button to close the window
        tk.Button(
            self,
            text="OK",
            command=self.destroy,
            width=10,
            bg="#e74c3c",
            fg="white",
            font=("Arial", 10)
        ).pack(pady=(5, 15))

        # Make this window modal (blocks interaction with the parent)
        self.grab_set()
        self.focus()

        # Center on screen
        self.update_idletasks()
        x = (self.winfo_screenwidth() // 2) - (320 // 2)
        y = (self.winfo_screenheight() // 2) - (150 // 2)
        self.geometry(f"320x150+{x}+{y}")


# ============================================================
# SUBJECT WINDOW
# Shows the full list of subjects a student is enrolled in,
# including each subject's mark and grade
# Contributed by: Satyam Das
# ============================================================
class SubjectWindow(tk.Toplevel):

    def __init__(self, parent, student):
        super().__init__(parent)
        self.title("My Subjects")
        self.geometry("480x360")
        self.resizable(False, False)

        # Title label
        tk.Label(
            self,
            text=f"Enrolled Subjects — {student.name}",
            font=("Arial", 13, "bold"),
            pady=12
        ).pack()

        # Divider line
        tk.Frame(self, height=1, bg="#cccccc").pack(fill=tk.X, padx=20)

        # Frame that holds the listbox and scrollbar side by side
        list_frame = tk.Frame(self)
        list_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Scrollbar on the right side
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Listbox that shows each subject as a formatted string
        self.listbox = tk.Listbox(
            list_frame,
            yscrollcommand=scrollbar.set,
            font=("Courier New", 11),
            height=10,
            selectmode=tk.SINGLE,
            bd=0,
            highlightthickness=1
        )
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.listbox.yview)

        # Fill the listbox with subject data
        if student.subjects:
            for sub in student.subjects:
                grade_str = sub.grade if sub.grade is not None else "N/A"
                display = f"  [ Subject::{sub.id:03d} -- mark = {sub.mark} -- grade = {grade_str:>3} ]"
                self.listbox.insert(tk.END, display)
        else:
            self.listbox.insert(tk.END, "  < No subjects enrolled yet >")

        # Close button at the bottom
        tk.Button(
            self,
            text="Close",
            command=self.destroy,
            width=12,
            bg="#7f8c8d",
            fg="white",
            font=("Arial", 10)
        ).pack(pady=10)

        self.grab_set()

        # Center on screen
        self.update_idletasks()
        x = (self.winfo_screenwidth() // 2) - (480 // 2)
        y = (self.winfo_screenheight() // 2) - (360 // 2)
        self.geometry(f"480x360+{x}+{y}")


# ============================================================
# ENROLMENT WINDOW
# Opens after a successful login.
# Students can enrol in subjects (max 4), view their subjects,
# or log out from this window.
# Contributed by: Satyam Das
# ============================================================
class EnrolmentWindow(tk.Toplevel):

    def __init__(self, parent, student):
        super().__init__(parent)
        self.title("Enrolment")
        self.geometry("400x320")
        self.resizable(False, False)

        self.student = student
        self.db = Database()

        # Welcome header
        tk.Label(
            self,
            text=f"Welcome, {student.name}",
            font=("Arial", 15, "bold"),
            pady=15
        ).pack()

        # Divider
        tk.Frame(self, height=1, bg="#cccccc").pack(fill=tk.X, padx=30)

        # Subject count display (this label is updated dynamically)
        self.count_label = tk.Label(
            self,
            text=self._count_text(),
            font=("Arial", 11),
            pady=10
        )
        self.count_label.pack()

        # Enrol button - adds a new random subject
        tk.Button(
            self,
            text="Enrol in a Subject",
            command=self.enrol_subject,
            width=22,
            bg="#27ae60",
            fg="white",
            font=("Arial", 11),
            pady=5
        ).pack(pady=6)

        # View Subjects button - opens the subject list window
        tk.Button(
            self,
            text="View My Subjects",
            command=self.view_subjects,
            width=22,
            bg="#2980b9",
            fg="white",
            font=("Arial", 11),
            pady=5
        ).pack(pady=6)

        # Logout button
        tk.Button(
            self,
            text="Logout",
            command=self.logout,
            width=22,
            bg="#c0392b",
            fg="white",
            font=("Arial", 11),
            pady=5
        ).pack(pady=6)

        # When the user closes the window with the X button, treat it as logout
        self.protocol("WM_DELETE_WINDOW", self.logout)

        # Make modal so user must interact here before returning to login
        self.grab_set()

        # Center on screen
        self.update_idletasks()
        x = (self.winfo_screenwidth() // 2) - (400 // 2)
        y = (self.winfo_screenheight() // 2) - (320 // 2)
        self.geometry(f"400x320+{x}+{y}")

    def _count_text(self):
        # Helper to build the "Enrolled: X / 4 subjects" label text
        return f"Enrolled: {len(self.student.subjects)} / 4 subjects"

    def enrol_subject(self):
        # Block if the student is already at the 4-subject limit
        if len(self.student.subjects) >= 4:
            ExceptionWindow(
                self,
                "You are already enrolled in 4 subjects.\nStudents cannot enrol in more than 4 subjects."
            )
            return

        # Create a new random subject and add it to the student
        new_subject = Subject()
        self.student.subjects.append(new_subject)

        # Save the updated student data back to the file
        all_students = self.db.load()
        for i, s in enumerate(all_students):
            if s.id == self.student.id:
                all_students[i] = self.student
                break
        self.db.save(all_students)

        # Refresh the counter label so the user sees the updated count
        self.count_label.config(text=self._count_text())

        # Show a success message
        grade_str = new_subject.grade if new_subject.grade is not None else "N/A"
        messagebox.showinfo(
            "Enrolled",
            f"Successfully enrolled in Subject-{new_subject.id}!\n"
            f"Mark: {new_subject.mark}  |  Grade: {grade_str}"
        )

    def view_subjects(self):
        # Open the Subject window to show the full list
        SubjectWindow(self, self.student)

    def logout(self):
        # Release the modal lock and close this window
        self.grab_release()
        self.destroy()


# ============================================================
# LOGIN WINDOW
# The main window of GUIUniApp.
# Students enter their email and password to log in.
# Registered students are loaded from students.data.
# Contributed by: Satyam Das
# ============================================================
class LoginWindow:

    # Same validation patterns as CLIUniApp
    EMAIL_PATTERN = re.compile(r'^[a-zA-Z]+\.[a-zA-Z]+@university\.com$')
    PASSWORD_PATTERN = re.compile(r'^[A-Z][a-zA-Z]{4,}\d{3,}$')

    def __init__(self):
        # Create the main application window
        self.root = tk.Tk()
        self.root.title("GUIUniApp")
        self.root.geometry("380x280")
        self.root.resizable(False, False)

        self.db = Database()

        self._build_ui()

        # Center the window on the screen
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (380 // 2)
        y = (self.root.winfo_screenheight() // 2) - (280 // 2)
        self.root.geometry(f"380x280+{x}+{y}")

    def _build_ui(self):
        # ---- Title ----
        tk.Label(
            self.root,
            text="University Login",
            font=("Arial", 17, "bold"),
            pady=18
        ).pack()

        # ---- Email row ----
        email_row = tk.Frame(self.root)
        email_row.pack(pady=6)

        tk.Label(email_row, text="Email:", font=("Arial", 11), width=10, anchor="e").pack(side=tk.LEFT)
        self.email_entry = tk.Entry(email_row, font=("Arial", 11), width=24)
        self.email_entry.pack(side=tk.LEFT, padx=6)

        # ---- Password row ----
        pass_row = tk.Frame(self.root)
        pass_row.pack(pady=6)

        tk.Label(pass_row, text="Password:", font=("Arial", 11), width=10, anchor="e").pack(side=tk.LEFT)
        # show="*" hides the typed characters for privacy
        self.pass_entry = tk.Entry(pass_row, font=("Arial", 11), width=24, show="*")
        self.pass_entry.pack(side=tk.LEFT, padx=6)

        # ---- Login button ----
        tk.Button(
            self.root,
            text="Login",
            command=self.attempt_login,
            font=("Arial", 11),
            width=16,
            bg="#2980b9",
            fg="white",
            pady=5
        ).pack(pady=18)

        # Allow pressing Enter key to trigger login
        self.root.bind("<Return>", lambda event: self.attempt_login())

    def attempt_login(self):
        email = self.email_entry.get().strip()
        password = self.pass_entry.get().strip()

        # 1. Check for empty fields
        if not email or not password:
            ExceptionWindow(self.root, "Email and password fields cannot be empty.")
            return

        # 2. Validate format using regex
        if not self.EMAIL_PATTERN.match(email) or not self.PASSWORD_PATTERN.match(password):
            ExceptionWindow(self.root, "Incorrect email or password format.\n\nEmail: firstname.lastname@university.com\nPassword: Starts uppercase, 5+ letters, 3+ digits.")
            return

        # 3. Check credentials against the saved students file
        students = self.db.load()
        for student in students:
            if student.email == email and student.password == password:
                # Login successful - hide login window, open enrolment window
                self.root.withdraw()
                enrolment = EnrolmentWindow(self.root, student)
                enrolment.wait_window()   # Wait here until the student logs out

                # After logout, show the login window again
                self.root.deiconify()
                self.email_entry.delete(0, tk.END)
                self.pass_entry.delete(0, tk.END)
                return

        # 4. No matching student found in the database
        ExceptionWindow(
            self.root,
            "Student does not exist.\n\nPlease register first using CLIUniApp."
        )

    def run(self):
        # Start the tkinter event loop (keeps the window open)
        self.root.mainloop()


# ============================================================
# START THE GUI APPLICATION
# ============================================================
if __name__ == "__main__":
    app = LoginWindow()
    app.run()
