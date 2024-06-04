

rows = []

#def main():
#    decode(message_file)

#def decode(message_file):
with open("message_file.txt") as file:
    reader = file.read()
    for line in reader:
        num = line.lstrip().split(" ")
        word = line.rstrip().split(" ")
        row = {"num": num, "word": word}
        rows.append(row)
       

for row in rows:
    print(f"{row['num']}")

#main()
