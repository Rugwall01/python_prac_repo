# Now what if we want all this to be sorted what can we do. we need to take a step back from this first

#with open("names5.txt", "r") as file:
#    for line in file:
#        print("hello,", line.rstrip())


# btw if you are opening up a file with open only to read it you dont actually have to specify "r" ans read mode is the default

names = []

with open("names5.txt") as file:
    for line in file:
        names.append(line.rstrip())


for name in sorted(names):
    print(f"hello, {name}")


# First I have to open the file and store all names in an appended format to a list that I assign/store in a variable called 'names', then I can sort the list(not the file) and print each line of the sorted list inside my f string 

# Here I will sort in reverse order


for name in sorted(names, reverse=True):
    print(f"hello, {name}")





































