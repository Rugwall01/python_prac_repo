# 


import random

coin = random.choice(["heads", "tails"])
print(coin)



# OK so if we want to take the above and instead of importing the entire random library we only want to import 1 module for the whole page we can do the below


from random import choice

# Now we can just say choice as the call for the module in that library

coin = choice(["heads", "tails"])
print(coin)

# This is advantagous because we may create our own variables and functions that share the same name as ones in the library and we dont want them conflicting. So we dont import the whole library just the module 

# Cont in generate1.py


















