def read_numbers_and_words(message_file):
    with open(message_file, "r") as file:
        numbers_and_words = [line.strip().split() for line in file.readlines()]
    numbers = [item[0] for item in numbers_and_words]
    words = {item[0]: item[1] for item in numbers_and_words}
    return numbers, words

def create_pyramid(numbers, words):
    numbers.sort(key=int)
    index = 0
    line_length = 1
    while index + line_length <= len(numbers):
        line = numbers[index:index + line_length]
        last_number = line[-1]
        corresponding_word = words[last_number]
        print(f"{last_number}:{corresponding_word}")
        index += line_length
        line_length += 1
    if index < len(numbers):
        line = numbers[index:]
        last_number = line[-1]
        corresponding_word = words[last_number]
        print(f"{last_number}:{corresponding_word}")

def decode(message_file):
    numbers, words = read_numbers_and_words(message_file)
    create_pyramid(numbers, words)

message_file = "coding_qual_input.txt"
decode(message_file)
