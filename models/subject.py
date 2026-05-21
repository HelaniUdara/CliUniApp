import random

class Subject:
    def __init__(self):
        self.id = f"{random.randint(1,999):03d}"
        self.mark = random.randint(25, 100)
        self.grade = self._get_grade()

    def _get_grade(self):
        if self.mark >= 85:
            return "HD"          
        elif self.mark >= 75 and self.mark < 85:
            return "D"         
        elif self.mark >= 65 and self.mark < 75:
            return "C"         
        elif self.mark >= 50 and self.mark < 65:
            return "P"          
        else:
            return "Z"         

    def __str__(self):
        return f"(Subject = {self.id}, mark = {self.mark}, grade = {self.grade})"
