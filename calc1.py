def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n

main()


# Another way of defining powers, use **, whatever is on the left -in this case 'n'- to the power of 
# whatever is on the right -in this case '2'

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n ** 2

main()



# ANother way is to use the predefined pow function that exists in python, see below

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return pow(n, 2)


main()























