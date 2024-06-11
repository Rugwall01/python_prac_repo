rows = []

class message:
    def __init__(self, num, word):
        self.num = num
        self.word = word
        

    def __str__(self):
        return f"{self.num} from {self.word}"

def main():
    listed = decode_message()
    print(listed)


def decode_message():
    with open("message_file.txt") as file:
        reader = file.read().split(" ")
        for line in reader:
            num = line.lstrip().split(" ")
            word = line.rstrip()
            row = {"num": num, "word": word}
        return rows.append(row)

main()
