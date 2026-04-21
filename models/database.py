import os
import json
import random

from models.student import Student


class Database:
    FILE = "students.data"

    def __init__(self):
        if not os.path.exists(self.FILE):
            try:
                with open(self.FILE, 'w') as handler:
                    json.dump([], handler, indent=2)
            except IOError:
                print("Error: Could not create students.data.")

    def load(self):
        try:
            with open(self.FILE, 'r') as handler:
                data = json.load(handler)
                return [Student.from_dict(s) for s in data]
        except (json.JSONDecodeError, ValueError):
            return []

    def save(self, students):
        try:
            with open(self.FILE, 'w') as handler:
                json.dump([s.to_dict() for s in students], handler, indent=2)
        except IOError:
            print("Error: Could not save data.")

    def generate_student_id(self, students):
        existing = {s.id for s in students}
        while True:
            new_id = random.randint(1, 999999)
            if new_id not in existing:
                return new_id

    def clear(self):
        with open(self.FILE, 'w') as handler:
            json.dump([], handler, indent=2)
