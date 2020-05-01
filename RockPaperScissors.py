from os import system

RPS = "ROCK, PAPER & SCISSORS"

live_rule = """

Live Rules
You start with {} lives
If you win you get a extra live.
If you loose you loose a live.
If you draw the lives stay the same.
----------------------------------------
The computer has lives as well.
Can you beat the computer ?
Good Luck !!!
----------------------------------------
"""
resultString = """

Player Lives = {}
Computer Lives = {}
Drew = {}
Round = {}

"""

rock = "rock"
paper = "paper"
scissors = "scissors"

looseString = "    Lose !!!"
winString = "    Win !!!"
drewString = "    Drew"

class Player():

    def __init__(self):
        self.player_lives = 5
        self.score = 0
        self.drew = 0

    def choice(self,player_choice:str):
        temp = player_choice.lower().replace(" ", "")
        return temp

class Computer():

    def __init__(self):
        self.computer_lives = 7

    def choice(self):
        from random import choice
        computer = ("rock", "paper", "scissors")
        return choice(computer)

class Check():

    def __init__(self, player_lives, computer_lives, drew):
        self.player_lives = player_lives
        self.computer_lives = computer_lives
        self.drew = drew

    # GETTERS
    def return_player_lives(self):
        return self.player_lives

    def return_computer_lives(self):
        return self.computer_lives

    def return_drew(self):
        return self.drew

    def check(self, player_choice, computer_choice):

        # Rock if statements
        if player_choice == rock:
            if computer_choice == scissors:
                print("")
                print(winString)
                print("")
                self.player_lives+=1
                self.computer_lives-=1

            if computer_choice == paper:
                print("")
                print(looseString)
                print("")
                self.player_lives-=1

            if computer_choice == rock:
                print("")
                print(drewString)
                print("")
                self.drew+=1

        # Paper if statements
        if player_choice == paper:
            if computer_choice == rock:
                print("")
                print(winString)
                print("")
                self.player_lives+=1
                self.computer_lives-=1

            if computer_choice == scissors:
                print("")
                print(looseString)
                print("")
                self.player_lives -= 1

            if computer_choice == paper:
                print("")
                print(drewString)
                print("")
                self.drew+=1

        # Scissors if statements
        if player_choice == scissors:
            if computer_choice == paper:
                print("")
                print(winString)
                print("")
                self.player_lives+=1
                self.computer_lives-=1

            if computer_choice == rock:
                print("")
                print(looseString)
                print("")
                self.player_lives -= 1

            if computer_choice == scissors:
                print("")
                print(drewString)
                print("")
                self.drew+=1

def main():
    system("cls")
    round = 0
    player = Player()
    computer = Computer()
    check = Check(player.player_lives, computer.computer_lives, player.drew)

    print(RPS)
    print(live_rule.format(player.player_lives))
    start = input("Enter \"1\" Start: ")

    if start == "1":
        while True:
            rps = input("Rock, Paper, Scissors ?: ")
            comChoice = computer.choice()
            check.check(rps, comChoice)
            print("Computer choice :",comChoice)
            print("\nPlayer Lives = {}\nComputer Lives = {}\nDrew = {}\n".format(check.player_lives, check.computer_lives, check.drew))
            round+=1

            if check.player_lives == 0 or check.computer_lives ==0:
                break

        system("cls")

        if check.player_lives == 0:
            print("You lost !!!")
            print(resultString.format(check.player_lives, check.computer_lives, check.drew, round))
        elif check.computer_lives == 0:
            print("You WON")
            print(resultString.format(check.player_lives, check.computer_lives, check.drew, round))

if __name__ == '__main__':
    main()