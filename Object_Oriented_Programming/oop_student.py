
name = input("Name: ")
house = input("House: ")
print(f"{name} from {house}")

# Evolved


def main():
    name = get_name()
    house = get_house()
    print(f"{name} from {house}")

def get_name():
    name = input("Name: ")
    return name


def get_house():
    house = input("House: ") 
    return house


# this can be tightened up by geting rid of the redundant variables in get_name() and get_house() and just
# directly retuning the input value



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
    # We do the above so we can use this as a library and the main() funct only triggeres if input in CLI
































