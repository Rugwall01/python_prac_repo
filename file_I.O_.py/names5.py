# Its too easy to forget to close files in code you dont need to strictly call close on a file as below, we will see even further down how to do things more pythonically so you won't have to call file.close() explicitly (asnd I guess the idea here is we won't have to remember to do it so we won't forget to close? not sure yet)

# We will use the keyword 'with' to do this

#name = input("What's your name? ")

#file = open("names5.txt", "a")
#file.write(f"{name}\n")        



name = input("What's your name? ")

with open("names5.txt", "a") as file:
    file.write(f"{name}\n")

# This automates the closing of a file since file.write is indented within the with keyword command

# in names6.py we will read the information in names5.txt in the fashion we specify they be read















