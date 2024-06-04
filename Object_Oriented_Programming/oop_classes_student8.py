# Lets create our own methods base code is endcode from oop_classes_student7.py


class Student:
    def __init__(self, name, house, patronus): #<-- adding patronus arg to __init__ method
        if not name: 
            raise ValueError("Missing name!")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus #<-- create empty attribute & "blindly" assign to variable 
                                    # this variable later to be filled with user input so lets go down and prompt
    
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
    patronus = input("Patronus: ") #<-- create variable patronus assign to user input
    return Student(name, house, patronus) #<-- pass variable into object
    


if __name__ == "__main__":
    main()


# Now you can enter the patronus but nothing is printed differently
# lets add that fnctionality and make it even better, 
# function inside a class is called method but its still a function


# lets add a function called charm


class Student:
    def __init__(self, name, house, patronus): #<-- adding patronus arg to __init__ method
        if not name: 
            raise ValueError("Missing name!")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus 
    
    def __str__(self):    
        return f"{self.name} from {self.house}"
    def charm(self): #<-- making our own method in class (self) is convention
        match self.patronus:
            case "Stag":
                return "\U &#x1F984;"
            case "otter":
                return "\U &#x1F407;"
            case "Jack Russell terrier":
                return "\U &#x1F407;"
            case _:
                return "\U &#x1F42E;"

def main(): 
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())   

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ") 
    return Student(name, house, patronus) 
    


if __name__ == "__main__":
    main()



















 
