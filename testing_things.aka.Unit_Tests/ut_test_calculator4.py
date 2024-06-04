
from ut_calculator1 import square
 
def test_pos():
    assert square(2) == 4
    assert square(3) == 9
    
def test_neg():
    assert square(-2) == 4
    assert square(-3) == 9
    
def test_zero():
    assert square(0) == 0


# Reference Harvard cs50 intro to programing with python https://www.youtube.com/watch?v=nLRL_NcnK-4 and got to near the end of the weeks class that includes this lesson arounf the 6hour and 50min mark. Hre is near the end of the lesson, the last 10min to 15min before this will explain up until here

# At this point we will switch todoing this same thing with strings and leear about using return f"string" {variable} instead of using print. got to ut_test_calculator5.py
