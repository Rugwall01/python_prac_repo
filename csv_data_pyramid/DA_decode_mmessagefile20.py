
def read_numbers_and_words(message_file):
    with open(message_file, "r") as file:
        numbers_and_words = [line.strip().split() for line in file.readlines()]
    numbers = [item[0] for item in numbers_and_words]
    words = {item[0]: item[1] for item in numbers_and_words}
    return numbers, words

def create_pyramid(numbers, words):
    numbers.sort()
    index = 0
    for i in range(1, len(numbers) - 2):
        line = numbers[index:index + i]
        last_number = line[-1]
        corresponding_word = words[last_number]
        print(f"{last_number}:{corresponding_word}")
        index += i

def main():
    message_file = "coding_qual_input.txt"
    numbers, words = read_numbers_and_words(message_file)
    create_pyramid(numbers, words)

main()
