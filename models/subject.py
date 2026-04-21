import random


class Subject:
    def __init__(self):
        self.id = random.randint(1, 999)
        self.mark = random.randint(25, 100)
        self.grade = self._get_grade()

    def _get_grade(self):
        pass

    def to_dict(self):
        return {
            'id': self.id,
            'mark': self.mark,
            'grade': self.grade
        }

    @classmethod
    def from_dict(cls, data):
        subject = cls.__new__(cls)
        subject.id = data['id']
        subject.mark = data['mark']
        subject.grade = data['grade']
        return subject

    def __str__(self):
        return f"(Subject = {self.id:03d}, mark = {self.mark}, grade = {self.grade:>3})"
