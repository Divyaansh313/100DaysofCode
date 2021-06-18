import random

# Name of the file to read in!
FILE_NAME = 'cswords.txt'

def list_of_words():
    word_list = []
    with open(FILE_NAME) as file:
        for line in file:
            word_list.append(line.strip())
    return word_list

def play_game(words):
    while True:
        input(random.choice(words))

def main():
    words = list_of_words()
    play_game(words)

if __name__ == '__main__':
    main()

