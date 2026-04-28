from models.subject import Subject

class Student:
    def __init__(self, name, email, password):
        self.id = None
        self.name = name
        self.email = email
        self.password = password
        self.subjects = []
    
    def __str__(self):
        return f"Student(id={self.id}, name='{self.name}', email='{self.email}')"
