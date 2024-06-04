

import re

url =  input("What's your twitter URL:").strip()

username = re.sub(r"https://twitter.com/", "", url)
print(f"username: {username}")


# more problems to chip away at
# what if the protocol is different http vs https 
# what if the subdomain is or needs to be there 'www.'

# first address the issue of matching from the beggining of the string so add a carrot '^' at beginning


url =  input("What's your twitter URL:").strip()

username = re.sub(r"^https://twitter.com/", "", url)
print(f"username: {username}")

# subtle bug with the period in the .com it needs to be escaped when using re


url =  input("What's your twitter URL:").strip()

username = re.sub(r"^https://twitter\.com/", "", url)
print(f"username: {username}")

# in order to allow http or https you can add an or pipe as below but there is a smarter way whichis below that



url =  input("What's your twitter URL:").strip()

username = re.sub(r"^(http|https)://twitter\.com/", "", url)
print(f"username: {username}")


# smarter way below anf much simpler is to use a '?' after the s in https as it will modify the s to optional zero or 1 of them


url =  input("What's your twitter URL:").strip()

username = re.sub(r"^https?://twitter\.com/", "", url)
print(f"username: {username}")


# Now tolerate 'www.' and make it optional


url =  input("What's your twitter URL:").strip()

username = re.sub(r"^https?://(www\.)?twitter\.com/", "", url)
print(f"username: {username}")

# Now make the protocol optional so people can just type starting with 'www.' if they want too


url =  input("What's your twitter URL:").strip()

username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"username: {username}")


# The theme throughout all my practice files of taking baby steps to construct these programs is extremely 
# important and applicable to the way in which you should approach coding and solving these issues in general
# rather than trying to created a complicated program that solves for all potential issues all in one go
# the first time, start with something small and simple and not fully functional, then keep adding
# to the code and refactoring the code to solve each new issue you want to solve for


# one more issue to solve with this one and we'll do it in twitter3.py





















