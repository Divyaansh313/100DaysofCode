"""
TODO: Ancient Game of Nimm
Nimm is an ancient game of strategy that is named after the old German word for "take." It is also called Tiouk Tiouk in West Africa and Tsynshidzi in China. Players alternate taking stones until there are zero left.

The game of Nimm goes as follows:

1. The game starts with a pile of 20 stones between the players.
2. The two players alternate turns.
3. On a given turn, a player may take either 1 or 2 stone from the center pile.
4. The two players continue until the center pile has run out of stones.

The last player to take a stone loses. 
"""

import random

def main():
    total_stones = 20
    flag = 1
    while total_stones > 0:
        print(f"There are {total_stones} stones left")
        if flag == 1:
            user_num = int(input("Player 1 would you like to remove 1 or 2 stones? "))
            while user_num != 1 and user_num !=2:
                amount = int(input("Please enter 1 or 2: "))
                user_num = amount
            flag += 1
        else:
            user_num = int(input("Player 2 would you like to remove 1 or 2 stones? "))
            while user_num != 1 and user_num != 2:
                user_num = int(input("Please enter 1 or 2: "))
            flag -= 1
        total_stones -= user_num
        print()
    print(f"Player {flag} wins!")

if __name__ == '__main__':
    main()