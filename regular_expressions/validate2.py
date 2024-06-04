
# Operators/modifiers in re library are '.' '*' '+' '?' '{m}' '{m,n}'
# . any character except a newline
# * 0 or more repetitions
# + 1 or more repetitions
# ? 0 or 1 repetition
# {m} m repetitions
# {m,n} m-n repetitions



# The r before the string indicates "raw" string, which is a way of formatting the string so that 
# Python doesn't interperate \ as an escape sequence adding a new line, (it usually treats \ the
# same as \n) but in order to just escape one single character that is usually an operator
# /modifier - in this case we want a '.' treated as just a period with no function - we need to 
# add the r or raw string format to our string of conditions

import re 

email = input("What's your email? ")

if re.search(r".+@.+\.edu", email):
    print("Valid")
else:
    print("Invalid")




# More operators/modifiers '^' '$' '[]' '[^]'
# ^ on it's own means the opening/beginning condition must match(matches start of string) 
# $ means the ending conditions must match(matches end of string or before n/line at end of string)

# by adding both of the above we are saying the email must start with a username adn end with .edu
# this will stop the program from validating something like a sentence


email = input("What's your email? ")

if re.search(r"^.+@.+\.edu$", email):
    print("Valid")
else:
    print("Invalid")





# [] set of characters, means match every character put into brackets
# [^] complementing the set, means all possible character except anything entered in bracket to the
    # right of the carrot -as in[^@] or [^1234567890]- to exclude characters you don't consider valid




email = input("What's your email? ")

if re.search(r"^[^@]+@[^@]+\.edu$", email):
    print("Valid")
else:
    print("Invalid")


# Improved even further to get closer to industry standards see validate3.py









