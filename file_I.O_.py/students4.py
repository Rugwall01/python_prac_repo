# This time I am going to have this program take an input and write it to a file

import csv
name = input("What's your name? ")
home = input("Where do you live? ")


with open("students4.csv","a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])



# Now in students5.py we are going to write these as dictionaries instead of rows
