# Trying to print what the student looks ike and more values

# Base codde
class Student:
    def __init__(self, name, house):
        if not name: 
            raise ValueError("Missing name!")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)
    


if __name__ == "__main__":
    main()


# Changes below


class Student:
    def __init__(self, name, house):
        if not name: 
            raise ValueError("Missing name!")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(student) #<-- the idea heree is to simplify and just print our student variable, but student isnt just
                       # a variable but an object, and this just prints out its physical location in memory  

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)
    


if __name__ == "__main__":
    main()


# We need to now modify this further see oop_classes_student.py




















