from models.subject import Subject


class Student:
    def __init__(self, name, email, password):
        self.id = None
        self.name = name
        self.email = email
        self.password = password
        self.subjects = []

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'subjects': [s.to_dict() for s in self.subjects]
        }

    @classmethod
    def from_dict(cls, data):
        student = cls(data['name'], data['email'], data['password'])
        student.id = data['id']
        student.subjects = [Subject.from_dict(s) for s in data['subjects']]
        return student
    
    def __str__(self):
        return f"Student(id={self.id}, name='{self.name}', email='{self.email}')"
