# 'sys.argv' sys is the module argv is the variable
# the '.argv' variable stands for argument vector, it means the list of all the words the user typed into the prompt before hitting enter
# The variable is a list and goes through each word similar to how loops go through each index


import sys

print("hello, my name is", sys.argv[1]) 

# The program needs to be executed with a command-line argument in order to display the name (it is the implied prompt)

# THE REASON we put the index of [1] for sys.argv is because when we pass in a command-line argument the program ile name itself is indexed at [0]. REMEMBER THAT pythons indexing starts from 0

# IF YOU DO NOT input an argument for the index value of [1] in your command-line after typing python3 and the file name, the the program will return an IndexError: list index out of range error


# In name1.py I am going to add try and except statements in order to prevent this error statement from occuring and making it basically loop back until the correct input is entered.













