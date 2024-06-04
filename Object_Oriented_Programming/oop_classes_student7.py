# Base code


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



#  lets now modify this code with some things eventually the __str__ method inside the class
# similar to our __init__ method
# the __str__ method/funct will be called any time some other function wants to see our object as a string
# so in the above where we want to print our object, print wants to see our object as a string naturally
# lets incorporate our __str__ method/funct into our class

class Student:
    def __init__(self, name, house):
        if not name: 
            raise ValueError("Missing name!")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
    
    def __str__(self):    #<-- this is triggered any time the object is attempted to be called as a string
        return f"{self.name} from {self.house}" # whatever the current name of object or variable housing object is
                                                # (self) is entered in as the arg here and becomes synonamous
                                                # with the object every time, which is why returning self.name
                                                # returns the object.name <-- object with its attribute

def main():
    student = get_student()
    print(student)   

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)
    


if __name__ == "__main__":
    main()




















