# Improves on (hello, 'name') with functions

# Below is how you make your own function by def (defining) it as the indented lines below the line 
# ending in a colon. Notice the : and then the indented line below, indentation matters


def hello():
    print("hello,")



name = input("What's your name? ").strip().title()
hello()
print(name)




# Evolution of code
# Designing the function we defined to take parameter/arg 'to'


def hello(to):
    print("hello,", to)



name = input("What's your name? ").strip().title()
hello(name)


# making the default output hello world if no input recieved



def hello(to="world"):
    print("hello,", to)


name = input("What's your name? ").strip().title()
hello(name)

hello()









