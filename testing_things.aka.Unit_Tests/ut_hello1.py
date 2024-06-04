
def main():
    name = input("What is your name? ")
    print(hello(name))

def hello(to="world"):
    return f"hello, {to}"


if __name__ == "__main__":
    main()


#reformated to return the value and then print the return value, this is much better for testing/ more testable because it the pytest function is really formatted for inputs and returns, infact retun values. And in fact most tests are optimized for this, basically we have return values and side effects and in testing you generally want to avoid using/testing side effects, the print function is actually a side effect, this is why we changed the program to first supply a return value and then printed that return value so we can test that part of the code

# This can be further refined
