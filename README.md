# CLIUniApp — University Enrolment System

A command-line university enrolment system built in Python. Students can register, log in, and manage subject enrolments. Admins can manage the student database. All data is persisted to a shared `students.data` file in JSON format.

---

## Project Structure

```
CLIUniApp/
├── models/
│   ├── student.py            # Student class — fields, grade logic, JSON serialisation
│   ├── subject.py            # Subject class — random mark/grade, JSON serialisation
│   └── database.py           # File read/write using json.load() and json.dump()
├── controllers/
│   ├── student_controller.py # University menu, Student menu, Register, Login
│   ├── subject_controller.py # Subject enrolment menu — TO BE IMPLEMENTED
│   └── admin_controller.py   # Admin menu — TO BE IMPLEMENTED
├── cli_uni_app.py            # Entry point — University menu
├── students.data             # Auto-created on first run (JSON)
```
---

## What Is Already Implemented

| Area | File | Status |
|---|---|---|
| University menu | `cli_uni_app.py` | Done |
| Student menu | `controllers/student_controller.py` | Done |
| Register | `controllers/student_controller.py` | Done |
| Login | `controllers/student_controller.py` | Done |
| Email/password validation | `controllers/student_controller.py` | Done |
| Student model | `models/student.py` | Done |
| Subject model | `models/subject.py` | Done |
| File read/write | `models/database.py` | Done |

---

## Data File

`students.data` is created automatically on first run. It is a JSON file shared by all parts of the system. Sample structure:

```json
[
  {
    "id": 123456,
    "name": "John Smith",
    "email": "john.smith@university.com",
    "password": "Hello123",
    "subjects": [
      { "id": 541, "mark": 55, "grade": "P" },
      { "id": 455, "mark": 72, "grade": "C" }
    ]
  }
]
```

To read and write this file, use the existing `Database` methods — do **not** modify `database.py`:

```python
from models.database import Database

db = Database()
students = db.load()    # read all students
db.save(students)       # write all students back
db.clear()              # reset the file to empty
```

---

## Validation Rules

| Field | Rule | Example |
|---|---|---|
| Email | `firstname.lastname@university.com` | `john.smith@university.com` |
| Password | Starts uppercase, at least 5 letters, ends with 3+ digits | `Hello123` |

Use the shared `validate()` function — do not rewrite it:

```python
from controllers.student_controller import validate

validate(email, password)   # returns True or False
```

---
## Setup and Installation

### Prerequisites

- Python 3.8 or higher
- No external libraries required — uses Python standard library only (`json`, `os`, `re`, `random`)

Check your Python version:

```
python --version
```

### 1. Clone the repository

```
git clone <repository-url>
cd CLIUniApp
```

### 2. Run the application

```
python cli_uni_app.py
```

If you want you can delete the existing `students.data` file as it will be created automatically in the same directory on first run.

When you are implementing your parts in the controllers, you need to import the database like below:

```python
from models.database import Database

db = Database()
```

Do not modify `models/database.py`, or `controllers/student_controller.py`.

