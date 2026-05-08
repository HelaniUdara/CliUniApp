from models.database import Database
from models.subject import Subject
import re

class SubjectController:
    INDENT = " " * 20

    def __init__(self, student):
        self.db = Database()
        self.student = student
    
    def iprint(self, text):
        print(f"{self.INDENT}{text}")

    def iinput(self, text):
        return input(f"{self.INDENT}{text}")

    def read_choice(self):
        return self.iinput("Student Course Menu (c/e/r/s/x): ").strip().lower()

    def subject_menu(self):
        choice = self.read_choice()
        while choice != 'x':
            try:
                match choice:
                    case 'c':
                        self.change_password()
                    case 'e':
                        self.enrol()
                    case 'r':
                        self.remove_subject()
                    case 's':
                        self.show_subjects()
                    case _:
                        self.help()
                choice = self.read_choice()
            except EOFError:
                break

    def save_student(self):
        students = self.db.load()
        for i, s in enumerate(students):
            if s.id == self.student.id:
                students[i] = self.student
                break
        self.db.save(students)

    def change_password(self):
        pattern = r'^[A-Z][A-Za-z]{4,}\d{3,}$'
        try:
            while True:
                password = self.iinput("New Password: ")
                if re.match(pattern, password):
                    break
                self.iprint("Invalid password. Must start with uppercase, have 5+ letters and 3+ digits")
            confirm_password = self.iinput("Confirm Password: ")
            if password == confirm_password:
                self.student.password = password
                self.save_student()
                self.iprint("Password updated successfully")
            else:
                self.iprint("Passwords don't match, please try again")
        except EOFError:
            pass

    def enrol(self):
        if len(self.student.subjects) >= 4:
            self.iprint("You are already enrolled in the maximum of 4 subjects.") 
            return    
        else:   
            subject = Subject()    
            self.student.subjects.append(subject)    
            self.iprint(f"Enrolled in: {subject}")        
            self.iprint(f"You are now enrolled in {len(self.student.subjects)} out of 4 subjects")           
            if len(self.student.subjects) > 0: 
                self.student.avg = sum(s.mark for s in self.student.subjects)/len(self.student.subjects)
            else: 
                self.student.avg = 0
            self.save_student() 

    def remove_subject(self):
        if len(self.student.subjects) == 0: 
            self.iprint("You are not enrolled in any subjects.")
            return 
        self.show_subjects()          
        remove_this = self.iinput("Which subject do you want to remove? ").zfill(3)      
        for subject in self.student.subjects:
            if subject.id == remove_this:         
                self.student.subjects.remove(subject)           
                self.iprint(f"Removed Subject: {remove_this}") 
                if len(self.student.subjects) > 0:
                    self.student.avg = sum(s.mark for s in self.student.subjects)/len(self.student.subjects)
                else:
                    self.student.avg = 0
                self.save_student()
                return        
        self.iprint("No subject with that ID found.")         

    def show_subjects(self):
        if len(self.student.subjects) == 0:        
            self.iprint("You are not enrolled in any subjects.") 
            return          
        self.iprint(f"Enrolment List:")           
        for subject in self.student.subjects:           
            self.iprint(subject)        

    def help(self):
        self.iprint("Invalid option. Please try again.")
        self.iprint("c = change password")
        self.iprint("e = enrol in a subject")
        self.iprint("r = remove a subject")
        self.iprint("s = show subjects")
        self.iprint("x = exit")