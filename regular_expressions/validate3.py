# Specifying ranges and ranges of letters inside square brackets to specifify included/acceptable 
    # characters



import re


email = input("What's your email? ")

if re.search(r"^[a-zA-Z0-9_]+@[^@]+\.edu$", email):
    print("Valid")
else:
    print("Invalid")

# The above opening string included all lowercase 'a-z' letters all upper case 'A-Z' letters all digits
    # '0-9' and underscore '_'





email = input("What's your email? ")

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
    print("Valid")
else:
    print("Invalid")




# Built in shortcut below
# The \w in this instance means any word character and is a built in shortcut to include all the things 
# we specified above in the brackets to simplify the code, but no brackets this time though


email = input("What's your email? ")

if re.search(r"^\w+@\w+\.edu$", email):
    print("Valid")
else:
    print("Invalid")


# Here is a list of these shortcuts/patterns
# \d decimal digit
# \D not a decimal digit (anything thats not)
# \s whitespace characters
# \S not a whitespace character (anything thats not)
# \w word character as well as numbers and underscore
# \W not a word character (anything thats not)




# We can enter more "suffix"(my words) options using parenthesis' and the or pipe '|'



email = input("What's your email? ")

if re.search(r"^\w+@\w+\.(edu|com|gov|net|org)$", email):
    print("Valid")
else:
    print("Invalid")


# A|B either A or B
# (...) a group
# (?:...) non capturing version

# You can do the above with those shortcuts too
# Suppose we wanted to allow spaces in the username



email = input("What's your email? ")

if re.search(r"^(\w|\s)+@\w+\.(edu|com|gov|net|org)$", email):
    print("Valid")
else:
    print("Invalid")

# We also want to go back and strip any white space from aither side of the entry regardless of our setup (don't allow whitespace infront of \w in opening or after in end)



email = input("What's your email? ").strip()

if re.search(r"^\w+@\w+\.(edu|com|gov|net|org)$", email):
    print("Valid")
else:
    print("Invalid")

# Use the .strip() method to alter your input before its packaged into your variable



























