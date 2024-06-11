import re


def decode_message():
    rows = []
    with open("message_file.txt", mode="r") as file:
        for line in file:
            row = line.split()
        return rows.append(row)
    print(rows)



