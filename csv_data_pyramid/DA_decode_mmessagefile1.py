
rows = []

with open("message_file.txt") as file:
    reader = file. read()
    for line in reader:
        num = line.lstrip().split(" ")
        word = line.rstrip()
        row = {"num": num, "word": word}
        rows.append(row)
       

for row in rows:
    print(f"{row['num']}")
