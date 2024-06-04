
with open("message_file.txt", mode="r") as file:
        for line in file:
            row = line.split()
            num, word = row[0], row[1]
            print(num, word)
