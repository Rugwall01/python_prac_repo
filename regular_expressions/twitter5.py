import re


url =  input("What's your twitter URL:").strip()

if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE)
    print(f"username:", matches.group(1))

# allows only the twitter username specific characters nothing need to be upercase, and also we need to tolerate# 1 or more of these symbols with the '+' and allow for an ending slash or period or other character by getting
# rid of the '$'


url =  input("What's your twitter URL:").strip()

if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE)
    print(f"username:", matches.group(1))



# other functions/methods in re
# re.split(pattern, string, maxsplit=0, flags=0)
# re.findall(pattern, string, flags=0)
# look up all re documentation

















