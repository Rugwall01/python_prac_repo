
from ut_calculator import square


def main():
    test_square()

def test_square():
    if square(2) != 4:
        print("error: incorrect result. 2 squared was not 4!")
    if square(3) != 9:
        print("error: incorrect result. 3 squared was not 9!")


if __name__ == "__main__":
    main()
