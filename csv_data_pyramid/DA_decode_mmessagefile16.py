


rows = []

def read_numbers(message_file_numbers):
    with open("message_file.txt", "r") as file:
     numbers = [str(line.strip()) for line in file.readlines()]
     return numbers

def create_pyramid(numbers):
    numbers.sort()
    index = 0
    for i in range(1, len(numbers) - 2):
        line = numbers[index:index + i]
        print(" ".join(map(str, line)))
        index += i


def create_pyramid1(numbers):
    numbers.sort()
    index = 0
    for i in range(1, len(numbers) - 2):
        lines = numbers[index: index + i]
        rows.append(lines[0:4]) 
        index += i

def get_words(Create_pyramid):
    for line in rows:
        #print(f"{line[0]}")
        print(f"{line}")
        

    
def main():
    message_file_numbers = "message_file.txt"
    numbers = read_numbers(message_file_numbers)
    Create_pyramid = create_pyramid1(numbers)
    create_pyramid(numbers)
    get_words(Create_pyramid)
 #   print(rows)
    #element = ['2 dogs', '3 love']
    #where = rows.index(element)
    #print(where)
main()

