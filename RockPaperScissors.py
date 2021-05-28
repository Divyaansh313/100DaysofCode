"""
Implements the game of Rock-Paper-Scissors!

History:
This classic game dates back to the Han Dinesty, over 2200 years ago.
The First International Rock-Paper-Scissors Programming Competition 
was held in 1999 and was won by a team called "Iocaine Powder"

The Game:
Each player choses a move (simultaneously) from the choices:
rock, paper or scissors. 
If they chose the same move the game is a tie. Otherwise:
rock beats scissors
scissors beats paper
paper beats rock.

In this program a human plays against an AI. The AI choses randomly
(we promise). The game is repeated N_GAMES times and the human gets
a total score. Each win is worth +1 points, each loss is worth -1
"""
import random

N_GAMES = 3

def main():
    print_welcome()
    score = 0 

    for i in range(N_GAMES):
        ai_move = get_ai_move()
        human_move = get_human_move()
        winner = choose_winner(ai_move, human_move)
        announce_winner(ai_move, winner)
        score = calculate_score(score, winner)
    print("Your score", score)

def calculate_score(score, winner):
    if winner == 'human':
        score += 1
    if winner == 'ai':
        score -= 1
    if winner == 'tie':
        score +=0
    return score
    print("You shouldn't reach here")

def announce_winner(ai_move, winner):
    print("AI plays", ai_move)
    print("The winner is", winner)
    print('')

def get_ai_move():
    """
    for now the AI plays randomly. But the optimal strategy is:
    If you lose, switch to the thing that beats the thing your opponent just played. 
    If you win, switch to the thing that would beat the thing that you just played.
    """
    int = random.randint(1,3)
    if int == 1:
        return 'rock'
    if int == 2:
        return 'paper'
    return 'scissors'

def get_human_move():
    while True:
        move = input("What do you play? ")
        if move_is_valid(move):
            return move
        print("Invalid move, try again: ")

def choose_winner(ai_move, human_move):
    if ai_move == human_move:
        return 'tie'
    if ai_move == 'rock':
        if human_move == 'paper':
            return 'human'
        return 'ai'
    if ai_move == 'paper':
        if human_move == 'scissors':
            return 'human'
        return 'ai'
    if ai_move == 'scissors':
        if human_move == 'rock':
            return 'human'
        return 'ai'
    print("You shouldn't reach here")

def move_is_valid(move):
    if move == 'rock':
        return True
    if move == 'scissors':
        return True
    if move == 'paper':
        return True
    return False

def print_welcome():
    print('Welcome to Rock Paper Scissors')
    print('You will play '+str(N_GAMES)+' games against the AI')
    print('rock beats scissors')
    print('scissors beats paper')
    print('paper beats rock')
    print('----------------------------------------------')
    print('')

if __name__ == '__main__':
    main()