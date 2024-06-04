# Printing a large 3 by 3 square area, all this and all stuff in mario.py files can be applied to making graphics and games, et..




def main():
    print_square(3)


# Each step notated

def print_square(size):

    # For each row in square
    for i in range(size):

        # For each brick in row
        for j in range(size):

            # Print Brick
            print("#", end="")
        print()





main()







def main():
    print_square(3)


def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()


# Tighten it up further

def print_square(size):
    for i in range(size):
        print("#" * size)

# Taking this to mario4.py



















