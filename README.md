Student Record Management System

A command-line Python project that retrieves student and lecturer records by checking both an ID and a name. The application demonstrates dictionaries, functions, loops, input validation, typed data structures, modular design, and unit testing.

Project status

Version: 1.0.0Environment: Python 3.10+Runtime dependencies: None

Main features

Student record lookup using a student ID and student name.

Display of student name, parent phone number, and email address.

Optional lecturer panel.

Lecturer record lookup using lecturer ID and lecturer name.

Validation for numeric IDs, empty names, and yes/no answers.

Case-insensitive name comparison.

Reusable functions separated from the interactive interface.

Automated unit tests using Python's built-in unittest framework.

Project structure

student_record_management_project/
├── README.md
├── CHANGELOG.md
├── requirements.txt
├── .gitignore
├── assets/
│   └── system_architecture.png
├── docs/
│   ├── Student_Record_Management_System_Technical_Documentation.docx
│   ├── DEVELOPER_GUIDE.md
│   ├── USER_GUIDE.md
│   └── TEST_PLAN.md
├── src/
│   └── student_record_management.py
└── tests/
    └── test_student_record_management.py

Installation

Install Python 3.10 or later.

Extract or clone the project.

Open a terminal in the project folder.

An optional virtual environment can be created:

python -m venv .venv
.venv\Scripts\activate

On Linux or macOS:

python3 -m venv .venv
source .venv/bin/activate

There are no third-party runtime packages to install. The following command is safe but optional:

python -m pip install -r requirements.txt

Running the application

From the project root, run:

python src/student_record_management.py

Example interaction

**********************************************************************
STUDENT RECORD MANAGEMENT SYSTEM
**********************************************************************
Enter your student ID: 111
Enter your name: Christian Effiong
Student ID: 111
Student name: Christian Effiong
Parent phone number: 075900747
Email: chriseffi@gmail.com
######################################################################
LECTURER LOGIN PANEL
######################################################################
Are you a lecturer? Enter yes or no: no
Lecturer panel skipped.

Running the tests

python -m unittest discover -s tests -v

Expected result:

Ran 8 tests
OK

Core functions

Function

Responsibility

normalize_name()

Removes extra spaces and normalizes letter case.

find_student()

Matches a student ID and student name.

find_lecturer()

Matches a lecturer ID and lecturer name.

format_student()

Produces readable student output.

format_lecturer()

Produces readable lecturer output.

prompt_integer()

Repeats until an integer is entered.

prompt_name()

Repeats until a usable name is entered.

prompt_yes_no()

Accepts yes/y or no/n.

main()

Starts the student panel and lecturer panel.

Data storage

The current version uses in-memory Python dictionaries. Records disappear when the program closes and must be edited in the source file. This design is suitable for a learning project but not yet for a real school deployment.

Recommended production upgrade:

Store records in SQLite or MySQL.

Hash passwords instead of relying only on matching IDs and names.

Add administrator authentication and role-based access control.

Avoid displaying personal contact information without authorization.

Add create, update, delete, search, attendance, grades, and reporting features.

Documentation

docs/Student_Record_Management_System_Technical_Documentation.docx: formal project and technical report.

docs/DEVELOPER_GUIDE.md: implementation, extension, coding, and maintenance notes.

docs/USER_GUIDE.md: instructions for users.

docs/TEST_PLAN.md: test strategy, cases, expected results, and acceptance criteria.

CHANGELOG.md: version history.

Original prototype issues corrected

The submitted prototype had several control-flow problems. A return statement occurred inside a loop and therefore ended the function during the first iteration. Lecturer variables could be referenced before assignment when the user answered "no." Name validation attempted an unnecessary integer conversion, and the same dictionaries were recreated each time a function ran. The revised source corrects these issues while retaining the original project idea.

Privacy notice

The included records are sample data. For a real institution, obtain authorization before storing or displaying names, phone numbers, email addresses, attendance, grades, or other personal records. Use proper access control and comply with applicable privacy requirements.

Author and maintenance

This project is prepared as a programmer-oriented academic package. Update the version number and CHANGELOG.md whenever behaviour changes.
