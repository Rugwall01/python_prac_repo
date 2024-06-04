#x = int(input("What's x? "))

#if x % 2 == 0:
  #  print("Even")
#else:
 #   print("Odd")



# Made this into a function below

def main():
    x = float(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0: 
        return True
    else:
        return False

# The most efficient and elligant way to define is_even below

def is_even(n):
    return True if n % 2 == 0 else False

# Actual most efficient while still readable below
def is_even(n):
    return n % 2 == 0 

# Because the above is naturally a true or false without explicitly wrapping it with if/else 
# statements, it can be used alone; and if the equation is rendered true by the number entered by 
# the user, then the value of is_even() will already equal true and apply to main().
# Think about it, you are essentially saying if n % 2 == 0 is true, return True, then apply the 
# returnTrue value to is_even() then allowing is_even true and to be in its place in main() because
# is_even() just has to be true to be in main(). But you can see how a value of true had to be 
# returned directly from the equation to the retun function in order for the return function to render
# True, so the implicit true or false value of the original equation alone already exists before the
# return value of True or False and thus can be applied as the mechanism by which is_even is itself 
# defined/rendered true

main()































