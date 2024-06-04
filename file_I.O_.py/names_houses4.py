# Each of the students is a dictionary

names_houses = []

with open("names_houses.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        namehouse = {"name": name, "house": house}
        names_houses.append(namehouse)

def get_name(namehouse):
    return namehouse["name"]

for namehouse in sorted(names_houses, key=get_name):
    print(f"{namehouse['name']} is in {namehouse['house']}") 


# In names_houses5.py I will replace the get_name function with an inline function created by the key=lambda parameter inside the sorted function see the file 
