
with open("names5.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello,",line.rstrip())

# Added.rstrip() to line to strip off the extra \n we put on there when we created an entry into the txt file, the reason is because print supplies its own \n, doubling up the spacing check what the output looks like with and without .rstrip()


# We can simplify this even further by not even assigning the read results of the file to a variable


with open("names5.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())


