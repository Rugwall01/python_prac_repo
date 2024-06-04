# If there are still more issues like user capitalizing the .suffix/.extension we can add
# more methods to the email variable when defined or when passed as an arg into re.search
# or more efficiently you can alter flags, def of re.search is "re.search(pattern, string, flags=0)"


import re

# Adding method to input
email = input("What's your email? ").strip().lower()

if re.search(r"^\w+@\w+\.(edu|com|gov|net|org)$", email):
    print("Valid")
else:
    print("Invalid")



# Adding method to re method/funct
email = input("What's your email? ").strip()

if re.search(r"^\w+@\w+\.(edu|com|gov|net|org)$", email.lower()):
    print("Valid")
else:
    print("Invalid")

    

# Altering flags

email = input("What's your email? ").strip()

if re.search(r"^\w+@\w+\.(edu|com|gov|net|org)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

# FLAGS ARE
# re.IGNORECASE - ignore case 
# re.MULTILINE - recognize multiple lines match by multiple line
# re.DOTALL - 




# Below allows us to use multiple periods in our domain name i.e. subdomains etc. 
# like atcasavant@ft.newyorklife.com or malan@cs50.harvard.edu


email = input("What's your email? ").strip()

if re.search(r"^\w+@\w+\.\w+\.(edu|com|gov|net|org)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")


# A|B either A or B - use to give optionality
# (...) a group - can actually group together things and apply operators to them
# (?:...) non capturing version - 

# Now the above unfortunately requires there to be a subdomain so let's fix tthat below
# we need to specify that it is optional, how do we do that. the or pipe | is not ideal, going back
# to our original operators remember there is a question mark '?' that signifies 0 or 1 repetion
# essentially saying you could put it here one time or not at all its up to you


# Add parenthesis to treat new part of pattern as one logical group
# then modify that group with the ? operator which will treat it as ooptional
email = input("What's your email? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.(edu|com|gov|net|org)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

# OPERATORS
# . any character except a newline
# * 0 or more repetitions
# + 1 or more repetitions
# ? 0 or 1 repetition
# {m} m repetitions
# {m, n} m-n repetitions


# THE OFFICIAL REGULAR EXPRESSION THAT BROWSERs USE NOW A DAYS, not all companies allow all of this but they might so browsers leave it open

# Simplified version below

#^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$

# re.match look these up
# re.fullmatch look these up











































