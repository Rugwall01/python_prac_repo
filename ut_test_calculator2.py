
from ut_calculator1 import square

def main(): 
    test_square()

def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared was not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared was not 9")

    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 squared was not 4")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 squared was not 9")

    try:
        assert square(0) == 0
    except AssertionError:
        print("0 squared was not 0")
    try:
        assert square(4) == 16
    except AssertionError:
        print("4 squared was not 16")
if __name__ == "__main__":
    main()




# Who wants to write tons of test code like this for a smaller amount of original code, to solve this we make it simpler by downloading pytest and using that tool to help us test our code, go to ut_test_calculator3.py
