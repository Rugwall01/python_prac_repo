rows = []
with open("message_file.txt", mode="r") as file:
    lines = file.readlines()

for line in lines:
    row = line.split()
    num, word = row[0], row[1]
    rows.append({num: word})
print(rows[1])
