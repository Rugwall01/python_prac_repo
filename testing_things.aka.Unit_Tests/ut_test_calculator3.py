

from ut_calculator1 import square
 
def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0
    assert square(4) == 16


# Did a little bit of overkill here but you get the idea, I simplty assert these things and instead of writing the test code in here I run this file in pytest instead of python3. pytest will apply all the test code to my assertions which pull from my library in-which I have introduced a flaw. The pytest program will pick this up itelf and present it to me doing all the extra work. I ust have to assert





























