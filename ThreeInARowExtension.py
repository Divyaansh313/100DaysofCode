"""
TODO: Three in a row extension
You should randomly generate addition, subtraction, multiplication and division problems until the user has gotten 3 problems correct in a row. 
(Note: the number of problems the user needs to get correctly in a row to complete the program is just one example of a good place to specify a constant in your program).
"""

import random 

def main():
    do_operation = True
    while do_operation != False:
        math_operation = int(input('''
Choose from the following mathematical operation by entering the assigned number:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
Enter num:  '''))
        counter = 0
        while counter != 3:
            num1 = random.randint(10,99)
            num2 = random.randint(10,99)
            res = 0
            if math_operation == 1:
                print(f"What is {num1} + {num2}?")
                res = num1+num2
                operation = "Addition"
            elif math_operation == 2:
                print(f"What is {num1} - {num2}?")
                res = num1-num2
                operation = "Subtraction"
            elif math_operation == 3:
                print(f"What is {num1} * {num2}?")
                res = num1*num2
                operation = "Multiplication"
            elif math_operation == 2:
                print(f"What is {num1} / {num2}?")
                res = num1/num2
                operation = "Division"
            else:
                print("Thank you for coming! Visit again.")
                do_operation = False
                break
            ans = int(input("Your answer: "))
            if ans == res:
                counter += 1
                print(f"Correct! You've gotten {counter} correct in a row.")
            else:
                print("Incorrect. The expected answer is", res)
                counter = 0
        print(f"Congratulations! You mastered {operation}")

if __name__ == "__main__":
    main()