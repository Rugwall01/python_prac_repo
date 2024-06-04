# What is a 'tuple'? 
# by retunng multiple valuse we are using a tuple
# a tuple is an immutable collection of values meaning you can not change the values
# this is unlike a list whch is mutable meaning you can change  the values in a list




def main():
    name, house = get_student()
    print(f"{name} from {house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house



if __name__ == "__main__":
    main()


# you can put parenthesis around the tuple if you like to make it more clear to the reader that this is one 
# tuple value and not two seperate values
# through assignment to two variables we break it up again in out main() funct



def main():
    name, house = get_student()
    print(f"{name} from {house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)



if __name__ == "__main__":
    main()


# if you want to consolidate the tuple into one single variable you can still index into the tuple using
# basic indexing, see below where I get rid of name, house variables and replace with student





def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house



if __name__ == "__main__":
    main()

# See how I indexed into student to print the correct pieces of the tuple

# GO TO oop_student3.py to test immutability of tuples and learn more 



















































