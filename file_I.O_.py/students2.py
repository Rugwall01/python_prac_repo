import csv


students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name": name, "home": home})


for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")

# name, home in the first for loop could be written as just row and is more versatile. Predefining just 2 variables only works in this senario if you know you only have 2 columns, to define this all as each row and bake name,home int the file we have to add the name,home line on our first line in our csv file to define the columns this way
# see student3.csv
