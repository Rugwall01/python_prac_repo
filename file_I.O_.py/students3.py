import csv

students = []

with open("students3.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")



# Lets break this down

#create variable and assign empy list to be filled
students = []

#with-kw open-fnct "file lctn" as file:
with open("students3.csv") as file:
#create variable reader, assign to it csv-fnct w/DictReader-method applied to the file '(file)'
    reader = csv.DictReader(file)
#for each row-giving name row to each line- in the variable reader    
    for row in reader:
#append to variable students(crtd dict's "name" and "home" made of each row[column1] row[column2]    
        students.append({"name": row["name"], "home": row["home"]})

#for each student-giving name student to each dict in list students- in sorted(list students, specs of sort lambda on created loop variable student which is a dict, easch dictionary at this point containes each seperate row/line, inside each dict/row/line student, it has columns which are specifcied as '["name"]'and '["home"]') then comes a colon to say what to do in this for loop as specified
for student in sorted(students, key=lambda student: student["name"]):

    #print format string "dict student, column1 is from dict student column2"    
    print(f"{student['name']} is from {student['home']}")

    #so all the rows were read by the csv.DictReader which specilizes in reading and interpreting
    #csv files, then we converted each of the rows into dictionararies that each had 2 columns,
    #then we fed these dictionaries into a list
    #then we used a for loop to iterate over each dictionary in the list after the list was
    #sorted within the for loop definition
    #with each iteration we print the specific format string that contains the information in each
    #column of each dictionary in our list and put "is from" in between
