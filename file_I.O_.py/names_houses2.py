# Here we will make the list sorted by puting the outputs into another list
# Re-designed to sort by actual name instead of whole sentence in names_houses3.py




names_houses = []

with open("names_houses.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        names_houses.append(f"{name} is in {house}")

for namehouse in sorted(names_houses):
    print(namehouse)
