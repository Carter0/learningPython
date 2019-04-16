#!/usr/local/bin/python3


# Decided to make tictactoe as another fun program to make.
# Could learn something from it.

# Things this game is going to need.
# A three by three board
# Two players, one x and one o
# Three end game conditions, a tie where whole board is full, a win for x, or a win for o
# Will need some way of determining if a player got three in a row


class Tictactoe:

    def __init__(self):
        self.players = ('X', 'O')
        self.game_over = False


    def setup_game():
        setup_board()

    def run_game():
        while not game_over:
            x = input("Input the X Position")
            y = input("Input the Y Position")
            # Fill in the board
            # Check for game over state

class Board:

    def __init__(self):
        self.board = [[Space() for x in range(3)] for Space() in range(3)]

class Space:

    def __init__(self):
        self.filled = False
        self.player = None

    def set_space(self, player):
        self.filled = True
        self.player = player





def main():
    game = Tictactoe()



if __name__=='__main__':
    main()




