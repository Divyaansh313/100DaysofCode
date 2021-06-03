"""
Prompts the user to enter numbers and prints
the running total until the user enters 0.
"""

END_VALUE = 0 

def main():
    # Fill this function out!
    user_input = int(input("Enter a value: "))
    total_so_far = user_input
    max_so_far = user_input
    min_so_far = user_input

    while user_input != END_VALUE:
        print("Running total is", total_so_far)
        print("Maximum so far is", max_so_far)
        print("Minimum so far is", min_so_far)
        print()
        user_input = int(input("Enter a value: "))
        total_so_far = total_so_far + user_input
        if user_input > max_so_far:
            max_so_far = user_input
        if user_input < min_so_far:
            min_so_far = user_input


if __name__ == '__main__':
    main()