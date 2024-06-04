# Going to refine this so if unexpected or incompatiable inputs are entered into the input the program renders some exit code 


x = int(input("What's x? "))
print(f"x is {x}")

# Catching ValueError(s) using try and except


try:
    x = int(input("What's x? "))
    print(f"x is {x}")

except ValueError:
    print("Please enter an integer")









