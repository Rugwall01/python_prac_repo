# Refining the basics of this code and not packaging it as functions but focusing on try and except and learning how they support other language like else

#import time

#def main():
#    execute_funct()


#def execute_funct():
#    try:
#        x = int(input("What's x? "))
#        print(f"x is {x}")
#    except ValueError:
#        print("Please enter and integer")
##       time.sleep(1)
#        execute_funct()



#execute_funct()

# Remember that the above is my modification, the "original" code is just the 'try:' and 'except ValueError:' without the defined functions and without "time.sleep()", a function I ultimately decided not to include in my application of the loop 



try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")

# The reason we separate the print(f"x is {x}") from try here is because it is best practice to only target what could potentially have the error with 'try'. If I put the print command alone outside of else it will work fine until the event of a ValueError because the 'except' function will handle the value error printing the "x is not an integer" and stopping the int(input"") from assigning to x. Then after all this python will continue to read the next line of code which would be print(f"x is {x}") and this would produce a ' NameError' because int(input"") was never assigned to x so python doesnt know what {x} is when you sate you want it printed. To solve this we add 'else:' and put print there. Essentially we are saying: "try to get 'this', if it doesnt work print 'it doesnt work', otherwise print what 'this' actually is." The otherwise portion of this is saying "if 'try' does work then do the thing that worked" essentially directly tying it back to 'try' and kinda double layering 'try' being True    

# In number3.py I am going to use this refined and best practice version and use a while loop and break to make it into a loop instead of the previous way I made the loop


















