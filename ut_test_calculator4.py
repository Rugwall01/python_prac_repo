
from ut_calculator1 import square
 
def test_pos():
    assert square(2) == 4
    assert square(3) == 9
    
def test_neg():
    assert square(-2) == 4
    assert square(-3) == 9
    
def test_zero():
    assert square(0) == 0
