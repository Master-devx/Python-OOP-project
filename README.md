# Python-OOP-project
Report card project 
Student Report Card System

A lightweight Python application demonstrating Object-Oriented Programming principles through a student grade management system. Built with clean architecture and modular design patterns.

Overview

This project implements a ReportCard class that encapsulates student data and behavior. It provides a complete CRUD interface for managing academic records, with automated grade calculation and dynamic subject handling.

Key Capabilities

- Student profile management (name, class, roll number)
- Subject-wise mark tracking via dictionary-based storage
- Automated average calculation
- Tiered grading system (A through F)
- Dynamic subject addition and removal
- Data integrity validation

Tech Stack

- Language: Python 3.x
- Paradigm: Object-Oriented Programming
- Development Environment: Pydroid 3

Installation

1. Clone the repository
2. Ensure Python 3.x is installed
3. Run the application:

python report_card.py

Usage Example

student = ReportCard("Alice", 12, 107, {
    "Maths": 89,
    "Science": 55,
    "Computer": 75
})

student.show_detail()
print(student.get_average())
print(student.get_grade())

student.add_subject("Art", 40)
student.remove_subject("Science")
student.show_detail()

Sample Output

Name: Alice
Class: 12
Roll number: 107
Subject and Marks
Maths: 89
Science: 55
Computer: 75

Average: 73.0
Grade: C

Art Subject added
Science removed

Name: Alice
Class: 12
Roll number: 107
Subject and Marks
Maths: 89
Computer: 75
Art: 40

Grade: D

Architecture

Class: ReportCard
- __init__(self, name, class, roll_number, marks)  → Initialize student record
- show_detail(self)                                  → Display full profile
- get_average(self)                                  → Calculate mean score
- get_grade(self)                                    → Return letter grade
- add_subject(self, subject, marks)                 → Append new subject
- remove_subject(self, subject)                     → Delete subject safely

Grade Scale

A  : 90 and above
B  : 80 - 89
C  : 70 - 79
D  : 60 - 69
E  : 50 - 59
F  : 40 - 49
Fail: Below 40

Design Principles Applied

- Encapsulation: Student data bundled with behavior
- Single Responsibility: Each method handles one task
- DRY: get_grade() reuses get_average() internally
- Safe Operations: Subject removal validated before execution

Roadmap

- [x] Core class structure
- [x] Grade calculation engine
- [x] Dynamic subject management
- [ ] Data persistence (JSON/CSV export)
- [ ] Multiple student batch processing
- [ ] GUI interface

License

Open source. Free to use and modify.

Contact

Built as part of a structured Python mastery curriculum.
Current milestone: OOP Fundamentals
Next milestone: Inheritance & Polymorphism
