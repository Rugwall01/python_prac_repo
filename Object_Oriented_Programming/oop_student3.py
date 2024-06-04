
# Here we use/go into the tuple to control for information we already know to be true.
# In the Harry Potter movies a character named "Padma" is in house Gryffindor, however in the books
# "Padma" the same character is in house "Ravenclaw"
# To "correct" this inconsitency we will apply boolean logic to our tuple base is below and edit is below that


def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)



if __name__ == "__main__":
    main()



# In the code below, if the user types Padma as the name and any other house than Ravenclaw for the house then 
# the output will still respond Padma from Ravenclaw


def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)



if __name__ == "__main__":
    main()


# But this above code is still invalid see oop_student4.py





























































