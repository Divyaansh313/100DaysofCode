NUMBER_OF_ROWS = 20
NUMBER_OF_COLUMNS = 20
OPTION = "What would you like to do? You can move and turn left. Press enter to finish. "

def main():
    curr_row = 1
    curr_column = 1
    curr_dir = "East"
    print("Welcome to first person Karel. You're at row", curr_row,"column", curr_row, "facing", curr_dir, "(facing column 2)")
    choice = input(OPTION)
    while choice != "":
        if curr_dir == "East":
            if choice == "move":
                if curr_column <20:
                    curr_column += 1
                    print("You moved one step forward and now you're at row", curr_row, "column", curr_column, ".")
                else:
                    print("You can't move forward!")
            elif choice == "turn left":
                curr_dir = "North"
                print(f"You turned left and are now facing {curr_dir}.")
            else:
                print("Invalid operation.")
        elif curr_dir == "North":
            if choice == "move":
                if curr_row < 20:
                    curr_row += 1
                    print("You moved one step forward and now you're at row", curr_row, "column", curr_column, ".")
                else:
                    print("You can't move forward!")
            elif choice == "turn left":
                curr_dir = "West"
                print(f"You turned left and are now facing {curr_dir}.")
            else:
                print("Invalid operation.")
        elif curr_dir == "West":
            if choice == "move":
                if curr_column > 1:
                    curr_column -= 1
                    print("You moved one step forward and now you're at row", curr_row, "column", curr_column, ".")
                else:
                    print("You can't move forward!")
            elif choice == "turn left":
                curr_dir = "South"
                print(f"You turned left and are now facing {curr_dir}.")
            else:
                print("Invalid operation.")
        else:
            if choice == "move":
                if curr_row > 1:
                    curr_row -= 1
                    print("You moved one step forward and now you're at row", curr_row, "column", curr_column, ".")
                else:
                    print("You can't move forward!")
            elif choice == "turn left":
                curr_dir = "East"
                print(f"You turned left and are now facing {curr_dir}.")
            else:
                print("Invalid operation.")
        choice = input(OPTION)
    print(f"You've ended up at row {curr_row} and column {curr_column} facing {curr_dir}.")

if __name__ == "__main__":
    main()