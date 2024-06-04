import json


rows = []

with open("message_file.txt") as file:
    reader = file.:read()
    for line in reader:
        num = line.lstrip().split(" ")
        word = line.rstrip()
        row = {"num": num, "word": word}
        rows.append(row)
       
json.dumps(rows["num"])
#for row in rows:
 #   print(f"{row['num']}")
