# This below will allow you to enter multiple names and the program will say hi to each name as a different person

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

    for arg in sys.argv:
        print("hello, my name is", arg)



# The above is going to include all indexed arguments (args) including the {0} index which is out file name and say hello to the file name
# TO FIX this we will take a 'SLICE' from the list
# 'slice' is a technical term in python 'slices' are substes of data structures such as lists, to take a 'slice' is to take a subset of one of these data structures again such as taking a slice from a list

# In name4.py I will explore slices





















