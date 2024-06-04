
names_houses = []

with open("names_houses.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        namehouse = {"name": name, "house": house}
        names_houses.append(namehouse)

for namehouse in sorted(names_houses, key=lambda namehouse: namehouse["name"]):
    print(f"{namehouse['name']} is in {namehouse['house']}") 
