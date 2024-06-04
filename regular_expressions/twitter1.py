

url =  input("What's your twitter URL:").strip()

username = url.removeprefix("https://twitter.com/")
print(f"username: {username}")

# You can see if you test this it doesnt yet work but it is a step in the right direction, see below
# We are going to use re.sub(pattern, repl, string, count=0, flags=0)

import re

url =  input("What's your twitter URL:").strip()

username = re.sub(r"https://twitter.com/", "", url)
print(f"username: {username}")


# more problems to chip away at
# what if the protocol is different http vs https 
# what if the subdomain is or needs to be there 'www.'
# got to twitter2.py 









































