# we can refine/ simplify further if we want too in a couple ways


def main():
    name = get_name()
    house = get_house()
    print(f"{name} from {house}")

def get_name():
    return input("Name: ")

def get_house():
    return input("House: ") 


if __name__ == "__main__":
    main()

# See below for refinement in one way



def main():
    name, house = get_student()
    print(f"{name} from {house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house



if __name__ == "__main__":
    main()

# So it turns out the above is an example of using a tuple
# GO TO oop_student2.py where a tuple will be explained further

























