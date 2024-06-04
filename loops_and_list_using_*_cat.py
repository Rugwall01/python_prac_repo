print("meow" * 3)

# This will print out 'meowmeowmeow'  with zero spaces


print("meow\n" * 3)

# Remember \n , this will 'return carriage' so to speak. Cursor is moved to the next line before the next input or output. But this returns an extra blank line below the last meow. How do we fic that? Look below.

print("meow\n" * 3, end="")

# Remember we can edit the underlying values of the 'print()' function and alter how it operates. Use end= or sep= after a comma andd then follow it with something or nothing inbetween 1 pair double quotes '""'
















