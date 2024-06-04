# what if the user doesnt even type a twitter url? needs conditional logic


import re

url =  input("What's your twitter URL:").strip()

username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"username: {username}")

# Instead of using re.sub we are going to use re.search to solve the same issue but with a conditional


url =  input("What's your twitter URL:").strip()

matches = re.search(r"^(https?://)?(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
if matches:
    print(f"username:", matches.group(3))


# Tighten it up again with walrus operator := see twitter4.py

