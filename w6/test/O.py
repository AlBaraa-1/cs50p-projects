"""
names = []

with open("text.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f"Hello, {name.upper()}!")
"""
import csv

"""
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.split(",")
        students.append({"name": name, "house": house.rstrip()})

for student in sorted(students):
    print(f"{student['name']} is in {student['house']}")
"""
"""
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.split(",")
        student = {"name": name, "house": house.rstrip()}
        students.append(student)

def get_name(student):
    return student["name"]

for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}")
"""

"""
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.split(",")
        student = {"name": name, "house": house.rstrip()}
        students.append(student)

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")
"""
"""
students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    for name, house in reader:
        students.append({"name": name, "house": house})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")
    """
students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row['name'], "house": row['house']})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")