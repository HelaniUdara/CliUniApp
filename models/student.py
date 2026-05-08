class Student:
    def __init__(self, name, email, password):
        self.id = None
        self.name = name
        self.email = email
        self.password = password
        self.subjects = []
        self.avg = 0

    def match(self, email, password):
        return self.email == email and self.password == password

    def match_email(self, email):
        return self.email == email

    def __str__(self):
        return f"Student(id={self.id}, name='{self.name}', email='{self.email}')"