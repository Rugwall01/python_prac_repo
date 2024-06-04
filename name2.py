import sys


#if len(sys.argv) < 2:
#    print("Too few arguments")
#elif len(sys.argv) > 2:
#    print("Too many arguments")

#print("hello, my name is", sys.argv[1])

# The above creates a problem we have seen before. When is the argument is not entered the program will display the correct message but then seperately afterward it will still try to print sys.argv[1] which is not defined because the argument was not entered. This will cause a name error

# The below uses a function of the sys module to solve that issue


if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1])










