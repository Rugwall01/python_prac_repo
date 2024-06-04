
name = input("What's your name? ")

file = open("names4.txt", "a")
file.write(f"{name}\n")
file.close()

# Adding new line at the end of each entry
