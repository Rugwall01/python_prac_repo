# re.match(pattern, string, falgs=0)
# re.fullmatch "   "

import re

name = input("What's your name? ").strip()
if "," in name:
    last, first = name.split(", ")
    name = f"{first} {last}"


print(f"hello, {name}")

# This is one way of formatting user input but look at a more succinct version

name = input("What's your name? ")
re.search(r"^.+, .+$", name)

# re.search is even more powerful than this
# you can capture things in pRENTHESIS in re.search
# you can also use non capture grouping

name = input("What's your name? ")
matches = re.search(r"^(.+), (.+)$", name)

# Above we group the first and last name (.+). remember .+ is saying "any character '.', one or more times '+'"
# Then we can do this with the groups

if matches:
    last, first = matches.groups()
    names = f"{first} {last}"
print(f"hello, {name}")


# Now we can be a little more explicit

name = input("What's your name? ")
matches = re.search(r"^(.+), (.+)$", name)


if matches:
    last = matches.group(1)
    first = matches.group(2)
    names = f"{first} {last}"
print(f"hello, {name}")


# Then to tighten it up even further



name = input("What's your name? ")
matches = re.search(r"^(.+), (.+)$", name)


if matches:
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")

# When using re.search something else always occupies index (0) so the parenthesis the target always start indexing at (1)

# Adding ? to tolerate optional of whitespace or no whitespace inbetween the names


name = input("What's your name? ")
matches = re.search(r"^(.+), ?(.+)$", name)


if matches:
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")

# This would allow to many spaces/keep to many spaces so instead lets use star '*'



name = input("What's your name? ")
matches = re.search(r"^(.+), *(.+)$", name)


if matches:
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")


# Go to format1.py to see a feature that tightens this up even further





































