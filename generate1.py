# Here we import the random library

import random

# Here I use the random.randint()  which generates a psuedo random integer between the numbers I specify in () seperated by a comma

number = random.randint(1,1000)
print(number)

# Now I use random.shuffle() to shuffle a list and then output the current order after the shuffle

cards = ["Jack", "Queen", "King"]
random.shuffle(cards)
for card in cards:
    print(card)


# Go to average.py where we are going to import the statistics library and use some of the functions in its modules to get statistical variables of sets of numbers/lists/etc., like mean/avg, median, and mode, etc..












