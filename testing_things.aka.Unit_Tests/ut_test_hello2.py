# Corresponds to ut_hello1.py

from ut_hello1 import hello


def test_default():
    assert hello() == "hello, world"

def test_argument():
    assert hello("Austin") == "hello, Austin"

