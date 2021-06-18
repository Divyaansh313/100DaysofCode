import random

NAME_LIST = ["Ajay","Aman","Aayush","Arjun","Aaditya"]

def main():
    # Storing a random integer number from 0 to (length of the list-1)
    index_number = random.randint(0 , len(NAME_LIST) - 1)

    # Storing the correct answer in a variable
    correct_answer = NAME_LIST[index_number]

    # Printing the list of names stored as global variable
    for name in NAME_LIST:
        print(name)

    # Prompt user for an answer and check whether correct or not
    user_input = input("Please tell the name at index.........." + str(index_number) + "? \n")

    # Checks if the user's answer matches the actual answer
    if user_input == correct_answer:
        print("GOOD JOB")
    else:
        print("Correct answer was",correct_answer)

if __name__ == '__main__':
    main()
