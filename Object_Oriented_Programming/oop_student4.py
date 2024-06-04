# IT TURNS OUT that you cannot change a tuplr THEY ARE IMMUTABLE, so in order for the below code to work we
# need to return a list instead of a tuple using []
# TypeError: 'tuple' object does not support item assignment

def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return [name, house]



if __name__ == "__main__":
    main()


# Now lets use dictionaries to solve this



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
# The above are keys'["name"]' and '["house"]' and their values we defined into existence inside 
# the dictionary we created with student = {}, then we have this function return the dictionary
# but now we have to change our def main() code, got to oop_student5.py

if __name__ == "__main__":
    main()





