import os
import pickle
import random


class Database:
    FILE = "students.data"

    def __init__(self):
        if not os.path.exists(self.FILE):
            try:
                with open(self.FILE, 'wb') as handler:
                    pickle.dump([], handler)
            except IOError as ex:
                print("Error: Could not create students.data.", ex)

    def load(self):
        students = []
        try:
            with open(self.FILE, 'rb') as handler:
                students = pickle.load(handler)
        except FileNotFoundError as ex:
            print("File Not Found:", ex)
        except IOError as ex:
            print("Reading Error:", ex)
        except EOFError as ex:
            print("End of File Error:", ex)
        return students

    def save(self, students):
        try:
            with open(self.FILE, 'wb') as handler:
                pickle.dump(students, handler)
        except FileNotFoundError as ex:
            print("File Not Found:", ex)
        except IOError as ex:
            print("Saving Error:", ex)

    def generate_student_id(self, students):
        existing = {s.id for s in students}
        while True:
            new_id = random.randint(1, 999999)
            if new_id not in existing:
                return new_id

    def clear(self):
        try:
            with open(self.FILE, 'wb') as handler:
                pickle.dump([], handler)
        except FileNotFoundError as ex:
            print("File Not Found:", ex)
        except IOError as ex:
            print("Clearing Error:", ex)
