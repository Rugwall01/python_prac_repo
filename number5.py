

def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer. Please enter an integer.")
        else:
            break
    return x

main()


# Refined below



def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer. Please enter an integer.")
        else:
            return x
main()

# Shortened again below but remember sometimes it makes sense to keep shortening and tightening and sometimes it doesn't make sure you have a good reason for your decisions regardless of what they are




def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            print("x is not an integer. Please enter an integer.")
main()


# Refined to just re-prompt without telling the user that they were wrong just re-looping to the entry


def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass
main()

# 'Pass' within the 'except ValueError:' statement still catches the error but "passes" on doing anything specific with it and then "passes" nothing back up to the loop so the loop can start again. It essentially just helps tell the loop where to go when the "try:' argument is false helping the while loop to know that it is infact false but not doing anything else but allowing the loop to restart again













