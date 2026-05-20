# CLIUniApp — University Enrolment System

**Assessment 1 – Part 2 | UTS FEIT | Group Submission**

A command-line university enrolment system built in Python. Students can register, log in, and manage subject enrolments through an interactive CLI. An admin subsystem allows database management without login. A standalone GUI application (GUIUniApp) is included and only registered students can use it.

All student data is persisted to `students.data` using Python's `pickle` module. Both CLIUniApp and GUIUniApp share the same data file.

---

## Setup and Installation

### Prerequisites

- **Python 3.10 or higher** — the `match` statement used for menu routing requires Python 3.10+
- No external libraries. Uses Python standard library only (`tkinter`, `pickle`, `os`, `re`, `random`)

Check your Python version:
```
python --version
```

---

### 1. Clone the repository

```
git clone https://github.com/HelaniUdara/CliUniApp.git
cd CLIUniApp
```

### 2. Run CLIUniApp (CLI)

Run from inside the project folder:
```
python cli_uni_app.py
```

`students.data` is created automatically on first run. You can safely delete it to reset all student records.

### 3. Run GUIUniApp (GUI)

Run from inside the same project folder:
```
python GUIUniApp.py
```

GUIUniApp reads registered students from `students.data`. Students must be registered via CLIUniApp before they can log in through the GUI.

---

## Project Structure

```
CLIUniApp/
├── cli_uni_app.py                  # Entry point — University System menu
├── GUIUniApp.py                    # Standalone GUI application
├── students.data                   # Auto-created on first run (pickle)
├── models/
│   ├── student.py                  # Student model class
│   ├── subject.py                  # Subject model class
│   └── database.py                 # File persistence — read/write/clear
└── controllers/
    ├── student_controller.py       # Student System — register, login, validation
    ├── subject_controller.py       # Subject Enrolment System — enrol, remove, show
    └── admin_controller.py         # Admin System — list, group, partition, remove, clear
```

---

## System Overview

### University Menu
```
University System: (A)dmin, (S)tudent, or X :
```
- `A` — Admin subsystem (no login required)
- `S` — Student subsystem
- `X` — Exit

### Student Menu
```
Student System (l/r/x):
```
- `l` — Login (redirects to Subject Enrolment on success)
- `r` — Register (validates email/password format; checks for duplicates, and register new students)
- `x` — Exit to University menu

### Subject Enrolment Menu
```
Student Course Menu (c/e/r/s/x):
```
- `c` — Change password (Allows changing the password)
- `e` — Enrol in a subject (max 4)
- `r` — Remove a subject by ID
- `s` — Show enrolled subjects with marks and grades
- `x` — Exit to Student menu

### Admin Menu
```
Admin System (c/g/p/r/s/x):
```
- `c` — Clear all student data (confirmation required)
- `g` — Group students by grade
- `p` — Partition students into PASS/FAIL categories
- `r` — Remove a student by ID
- `s` — Show all students
- `x` — Exit to University menu

---

## Validation Rules

| Field    | Rule                                                                 | Valid example                  |
|----------|----------------------------------------------------------------------|--------------------------------|
| Email    | `firstname.lastname@university.com` — letters only, dot separator   | `john.smith@university.com`    |
| Password | Starts with uppercase, at least 5 letters total, ends with 3+ digits | `Helloworld123`                |

---

## Grading Scale

| Mark range | Grade |
|------------|-------|
| < 50       | Z (Fail) |
| 50 – 64    | P (Pass) |
| 65 – 74    | C (Credit) |
| 75 – 84    | D (Distinction) |
| >= 85      | HD (High Distinction) |

A student passes overall if their average mark across all enrolled subjects is >= 50.

---

## Team Contributions

| Member | Contribution | Files |
|--------|-------------|-------|
| **Helani Seekkubadu** | University System, Student System, Database layer | `cli_uni_app.py`, `controllers/student_controller.py`, `models/student.py`, `models/database.py` |
| **Jayati Dave** | Subject Enrolment System | `controllers/subject_controller.py`, `models/subject.py` |
| **Ping-Chun Liao** | Admin System | `controllers/admin_controller.py` |
| **Satyam Das** | GUI Application | `GUIUniApp.py` |