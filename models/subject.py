import random

class Subject:
    def __init__(self):
        self.id = random.randint(1, 999)
        self.mark = random.randint(25, 100)
        self.grade = self._get_grade()

    def _get_grade(self):
        pass

    def __str__(self):
        return f"(Subject = {self.id:03d}, mark = {self.mark}, grade = {self.grade:>3})"
