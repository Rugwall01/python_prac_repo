# Creating  dictionries that store the associations of name and house key value pairs, then calling sorting by the key or name and getting both the sorted key and value as a result
# Each line of names_houses.csv below gets split and stored spit in its own dictionary, the dictionaries are stored in a list


names_houses = []

with open("names_houses.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        namehouse = {}
        namehouse["name"] = name
        namehouse["house"] = house
        names_houses.append(namehouse)

for namehouse in names_houses:
    print(f"{namehouse['name']} is in {namehouse['house']}")   

# To simplify the namehouse dictionary assignments you can do it ot all(in this case 2 lines) in one line, look below



names_houses = []

with open("names_houses.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        namehouse = {"name": name, "house": house}
        names_houses.append(namehouse)

for namehouse in names_houses:
    print(f"{namehouse['name']} is in {namehouse['house']}") 

# Now we will make it sorted go to names_houses4.py
