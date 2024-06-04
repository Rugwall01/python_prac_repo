
rows = []

def main():
    decode = decode_messagefile()
    print({decode["num"]})

def decode_messagefile(): 
    with open("message_file.txt", mode="r") as file:
            for line in file:
                row = line.split()
                num, word = row[0], row[1]
                return {"num": num, "word": word}




main()            
