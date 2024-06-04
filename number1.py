# Taking the try and except from number.py I will now try to make it into a loop when the except value is true



#try:
#    x = int(input("What's x? "))
#    print(f"x is {x}")
#except ValueError:
#    print("please enter an integer")


# Attempt to put into loop below

import time

def main():
    execute_funct()


def execute_funct():
    try:
        x = int(input("What's x? "))
        print(f"x is {x}")
    except ValueError:
        print("Please enter and integer")
#       time.sleep(1)
        execute_funct()



execute_funct()

# Took me a while to get this right, I defined everything as functions instead of leaving them "raw"
# Then as the last line of code for for the event of a ValueError under 'except ValueError:' I entered the command to execute the function again. This creates an infinite loop if and only if the user prompts a value error and continues to do so. The lop is broken by inputing the expected value type in this case an integer. 
# Additionally I added the time.sleep tool but opted to not actually include it this time. Notice how I had to import time first at the top of the code


# Refined more in number2.py









