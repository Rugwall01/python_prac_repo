# Defining your functions first without calling them will allow you to list them in any order
# and then call them in the order you want them below
# If you simultaniously call and define youf function as in creating_funtions.py then you must always
# define your function above its use case. Avoid this by first only defining things (by using 
# indentation properly) then calling them after

def main():
    name = input("What's your name? ")
    hello(name)



def hello(to="world"):
    print("hello,", to)



main()


# See how above I defined my main function before the underlying function that it relies on
# However since niether was being called the order doesnt matter (note that this is because the call
# is under all definitions 






















