
import re


url =  input("What's your twitter URL:").strip()

if matches := re.search(r"^(https?://)?(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print(f"username:", matches.group(3))




# even one more refinement to this: make the first two groups in re.search and make them non capture groups
# then change matches.group(3) inside print funct and make it matches.group(1)

url =  input("What's your twitter URL:").strip()

if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
    print(f"username:", matches.group(1))

# another refinement that pertains specifically to twitter is that it doesnt allow anything for the username but
# our program does, go see twitter5.py


