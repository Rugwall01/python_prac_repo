with open("names_houses.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")


# Each line in the file will contain woth the name and the house seperated by a comma, in order to have our programs recognize the seperation we have to use the .split method on the lines and specify that the comma the "," is the dividing piece of each line
# I then stored this in a variable called row
# Next we will store out two comma seperated values into seperate variables simultaneously instead of in one variable and then selecting for each specific index pair. go to names_houses1.py


