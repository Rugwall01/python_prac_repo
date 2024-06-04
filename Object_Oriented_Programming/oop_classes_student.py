# We are going to make a class and then use it inside out get_student funct
# '.''s are usesd to denot atttributes with classes, so we can define attributes with a period followed by 
# the name of the attribut affter the name of the variable that we have our class inside
# this is akin to using brackets '[]' when doing this same thing on dictionaries

class Student:
    ...

def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f'{student["name"]} from {student["house"]}')

def get_student():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student


if __name__ == "__main__":
    main()

# Now below we go in and remove the padma code to focus on one thing at a time and then change the print syntax
# that was previously for dictionary indexing and change it ti=o attribute indexing for a class


class Student:
    ...

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student


if __name__ == "__main__":
    main()

# Working version in oop_classes_student1.py for demonstration of this step working
# GO TO either that or too oop_classes_student2.py





























