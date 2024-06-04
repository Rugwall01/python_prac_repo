# Now we change the code up here after altering def get_student() in oop_student4.py

def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")

def get_student():
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student

# Base code above needing change change below


# remember I created two key value pairs in my dict so I can index by them, I had to alter my quotation marks
# because I am nesting quotes inside quotes
# got rid of the padma condition for now just for simplicity


def main():
    student = get_student()
    print(f'{student["name"]} from {student["house"]}')

def get_student():
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student

if __name__ == "__main__":
    main()


# Now we can consolidate the get_student function by getting rid of some strictly speaking unneccesary things
# Below we create the dictionary and assign the keys to variables all at once inside the return statement
# you are essentially creating a dictionary and definining its keys on the fly all in one line

def main():
    student = get_student()
    print(f'{student["name"]} from {student["house"]}')

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}
    # see how the above dict was created at the end inside the return statement. It's saying return a dict with
    # a key called "name" equal to the varible called name and key "house" equal to variable house
if __name__ == "__main__":
    main()

# Now add back the Padma change, dictionaries like lists are mutable but the syntax is slightly different



def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
        # The above is saying if the variable student conatains a name key called Padma then change the value
        # of its house key to be equal to Ravenclaw
    print(f'{student["name"]} from {student["house"]}')

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}



if __name__ == "__main__":
    main()


# Nexts lets learn about classes so we can use them to collect more information see classes_tbd.py
