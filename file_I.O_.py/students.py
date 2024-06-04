
students = []

with open("students.csv") as file:
    for line in file:
        name, home = line.rstrip().split(",")
        student = {"name": name, "home": home}
        students.append(student)

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")

#The issue with the above is that it will produce an errorr because the the line for Harry has too many commas. The value of the Harry key is supposed to be where he grew up but that value itself contains a comma. There are some quick ways to deal with this for small dataset such as changinging the diliniating character from a comma to something else. But it can quickly get complicated with larger datasets. So insteadd we use the csv library that coms with 
