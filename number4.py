
def main():
    x = get_int()
    print(f"x is {x}")



def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer. Please enter an integer.")
        else:
            break

    return x



main()

# 'return x' just shoves the end value of x into the value of get_int() overall allowing our main function to seperately define x again in its own function by assigning get_int() to x 



# Refined again in number5.py










