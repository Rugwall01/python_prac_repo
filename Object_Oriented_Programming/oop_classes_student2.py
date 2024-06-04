# More learning about CLASSES and OBJECTS
# the ... is enough to create a CLASS, when I assign it to a variable I am creating an OBJECT of that class
# you create objects from classes to make the class do anything
# CLASSES are mutable but you can make them immutable
# the '.name' and '.house' are "attributes" but we will eventually call attributes more 
# technically "instance variables"


# Let's add more functionality to this

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


# See below

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

# so in the above I made two variables name and house and then I called my Student() function -see below- and
# passed those variables into my function and then put that funct with the passed variables into another 
# variable called student and then retunred that variable as the final step in the get_student variable
# A FUNCTION ALWAYS COMES ALONG WITH A CLASS AND CAN BE USED IN THE ABOVE WAY, the Student() funt is from the 
# class Student
# Go to oop_classes_student3.py


