
# keep all of the related code within the the same object
# if have a class i want to add functionality too,perhaps exclude things from, or validate the user entries
# I need to add all the code for that in the class definition, observe the base code below and then its changes 
# below that

class Student:
    def __init__(self, name, house):
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



#
# ok below we are going to try to handle unexpected entries and error.
# logically there are some ways to solve this using sys.exit or something similar but these things are 
# encombersome and cause other issues, you also cannot return a value of none in the __init__ funct
# because the the object for which it exists already has a retun value of the users input.
# So we come to a new key word(kw) 'raise' which allows us to raise/create our own exceptions for when things go
# wrong -in other words when things raise/cause an error according to our own standards
# and then it allows us to tell our program what to do when that error occurs

# Below we put in a conditional if statement to say if nothing was entered in for the name, now we have to raise 
# that as an error and decide what to do with it/ do next

class Student:
    def __init__(self, name, house):
        if not name: #<-- this means if the name entry is blank
            raise ValueError #<-- raising the error/exception
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




# we can treat ValueError and all exceptions in python like functions and pass to them explanitory messages etc.


class Student:
    def __init__(self, name, house):
        if not name: #<-- this means if the name entry is blank
            raise ValueError("Missing name!") #<-- raising the error/exception, and passing an explanation 
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    try: #<-- we can then place a try here and put our return for making the object in the first place inside it
        return Student(name, house)
    except Value: #<-- then we can put an except condition and outcome here to decide what the program does next
        ... #<-- placeholder


if __name__ == "__main__":
    main()

# ok lets no longer use try and except for a bit and just focus on the raise error portion of things below



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





































































