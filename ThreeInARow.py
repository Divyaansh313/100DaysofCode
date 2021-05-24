"""
TODO: Three in a row
You should randomly generate addition problems until the user has gotten 3 problems correct in a row. 
(Note: the number of problems the user needs to get correctly in a row to complete the program is just one example of a good place to specify a constant in your program).
"""

import random

CORRECT_IN_ROW = 3

def main():
    counter = 0
    while counter != 3:
        num1 = random.randint(10,99)
        num2 = random.randint(10,99)
        print(f"What is {num1} + {num2}?")
        ans = int(input("Your answer: "))
        sum = num1+num2
        if ans == sum:
            counter += 1
            print(f"Correct! You've gotten {counter} correct in a row.")
        else:
            print("Incorrect. The expected answer is", sum)
            counter = 0
    print("Congratulations! You mastered addition.")
        
if __name__ == '__main__':
    main()