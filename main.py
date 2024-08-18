import os
import random

RULES = """
 - Rock crushes Scissors (Rock wins).
 - Scissors cuts Paper (Scissors wins).
 - Paper covers Rock (Paper wins)."""

HOW_TO_PLAY = """
 Welcome to Rock, Paper, Scissors!
 Enter 'rock', 'paper', or 'scissors' to play.
"""

QUIT = "\n Enter 'q' to quit the game."

RPS = ["rock", "paper", "scissors"]


class Game():

    def __init__(self):
        self.is_finished = False
        self.round = 0
        self.draw = 0
        self.player_score = 0
        self.enemy_score = 0


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def check_result(user_choice: str, computer_choice: str, game: Game):
        if user_choice == computer_choice:
            game.draw += 1
            return "\n Draw"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "scissors" and computer_choice == "paper") or \
            (user_choice == "paper" and computer_choice == "rock"):
            game.player_score += 1
            return "\n You Win"
        else:
            game.enemy_score += 1
            return "\n You Lose"
        

def check_finish(game: Game):
    if game.player_score == 2:
        clear()
        display_result(game)
        print("\n You Won The Game !")
        game.is_finished = True
    elif game.enemy_score == 2:
        clear()
        display_result(game)
        print("\n You Lose The Game :(")
        game.is_finished = True
        

def display_result(game:Game):
    print(f"\n Round: '{game.round}', Your Score: '{game.player_score}', Enemy Score: {game.enemy_score}, Draw: {game.draw}")


def restart():
    while True:
        user_choice = input("\n Do you want to play again? (yes/no): ").strip().lower()
        computer_choice = random.choice((True, False))
        if user_choice in ['yes', 'y']:
            if computer_choice:
                return True
            else:
                print("\n Your enemy escaped!")
                return False
        elif user_choice in ['no', 'n']:
            return False
        else:
            print("\n Invalid input. Please enter 'yes' or 'no'.")


def rock_paper_scissors_function():
    while True:
        game = Game()

        while not game.is_finished:
            clear()
            print(HOW_TO_PLAY)
            print(RULES)
            print(QUIT)
            display_result(game)

            user_input = input("\n Enter your choice: ").strip().lower()

            if user_input == "q":
                break

            if user_input not in RPS:
                print("\n Invalid input. Please try again.")
                input("\n press Enter to continue ...")
                continue
            
            computer_choice = random.choice(RPS)
            game.round += 1
            print(f"\n Computer chose: {computer_choice}")
            print(check_result(user_input, computer_choice, game))

            check_finish(game)

            if game.is_finished:
                break

            input("\n press Enter to continue ...")
    
        if not restart():
            print("\n Thanks for playing!")
            break

if __name__ == '__main__':
    rock_paper_scissors_function()