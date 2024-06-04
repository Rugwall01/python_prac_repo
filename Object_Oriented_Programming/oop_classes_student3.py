
# The Student clas/funct doesnt know what to do with the arguments I passed into it yet, base code below

class Student:
    ...

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student


if __name__ == "__main__":
    main()


# CLASSES COME WITH METHODS, that you can define and that behave in a special way. you can determin behavior
# lets def a funct in our class to do this
#__init__ is used to initialize the contents of a an object in a class
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
    #adding instance variables to our object


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student


if __name__ == "__main__":
    main()

# parameter self (ADD MORE NOTES LATER
 # got to oop_classes_student4.py   
