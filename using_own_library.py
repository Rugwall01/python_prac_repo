import sys
from making_libraries import hello

if len (sys.argv) == 2:
    hello(sys.argv[1])


# Unfortunately this library making_libraries is written in such a way that every function() inside it executes because they are tied to main() and main executes in the library
# Go to using_own_library1.py and reference the new library that is updated correctly at making_libraries1


