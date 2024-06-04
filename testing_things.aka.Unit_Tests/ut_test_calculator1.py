# Going off the below test code we are going to simplify it using some new concepts and test its functionality when broken. ut_calculator1.py will be an example of a broken code that will produce an error ut_calculator.py will be working and when it is tested we should see nothing.

#def main():
#    test_square()

#def test_square():
#    if square(2) != 4:
#        print("2 squared was not 4")
#    if square(3) != 9:
#        print("3 squared was not 9")
         


#if __name__ == "__main__":
#    main()

# This can be "simplified" by using the assert key word. If you assert something and it is true nothing will happen, if its false you will see an error on the screen

# look below


from ut_calculator1 import square

def main(): 
    test_square()

def test_square():
    assert square(2) == 4
    assert square(3) == 9


if __name__ == "__main__":
    main()

# In the next pile in the series I will apply the try an accept key words to this to add contingencies and or explanations for errors
