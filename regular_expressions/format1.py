import re


name = input("What's your name? ")
matches = re.search(r"^(.+), *(.+)$", name)

if matches:
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")


# tightened up below

name = input("What's your name? ")
 
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")


# This is the walrus operator ':=' and it allows you to assign and ask an if or elif question at the same time, (allows to assign a value and ask boolean question about it)






