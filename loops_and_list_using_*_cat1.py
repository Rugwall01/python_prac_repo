# How to make the number the cat meows derived from the user input and contrain that input to a positive integer

while True:
    n = int(input("What's n? "))
    if n < 0:
        continue
    else:
        break


# While True immediately creates an infinite loop, inside it we aske our question and if n < 0 or in other words if the user inputs a negative number the the loop continues and it just re -asks for the input. If the user enters the desired input which is any positive integer then the loop will break. Noteuse of continue and break pythons key-words to augment loops

# OK below we tighten it up further

while True:
    n = int(input("What's n? "))
    if n > 0:
        break

   
# See how this negates the need for an if and an else. the else is implied. Start the loop if we get the input we want break the loop. Otherwise the loop is just still running.


# Now we pair this up and tell this loop why its really here



while True:
    n = int(input("What's n? "))
    if n > 0:
        break



for _ in range(n):
    print("meow")



















