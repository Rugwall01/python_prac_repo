with open("message_file.txt", mode="r") as file:
        for line in file:
            row = line.split()
            num = row[0]
            word = row[1]
            print(num, word)
