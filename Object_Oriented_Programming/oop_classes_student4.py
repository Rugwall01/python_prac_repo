# Technically we can get rid of the variable in our get_student funct and just return the value of that variable
# directly to the get_student funt, the value of that variable being the Student(name, home) funct/object/class
# that is initialized as an object when it is cnstructed and then references its class and the funct
# __init__ defined within it. It ha to be populated with name and house and then designed to call them as 
# attributes. Then that is how the object is defined, the object is returned into the get_student() funct
# then in the main() funct the get_student() funct is pkged up into a variable and the attributes of that
# variable are printed


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


# Now lets solve for some issues like unexpected entries, such as just pressing enter, and also constrict the 
# available valid entries to what is consistent in the harry potter world










