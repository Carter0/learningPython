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
        self.board = [[Space(x, y) for x in range(3)] for y in range(3)]

    def get_space(self, x, y):
        return self.board[x][y]

class Space:

    def __init__(self, x ,y):
        self.filled = False
        self.player = None
        self.x = x
        self.y = y

    def set_space(self, player):
        self.filled = True
        self.player = player

    def __str__(self):
        return f"This is a space at ({self.x}, {self.y}) owned by {self.player} {'and is filled' if self.filled else 'and is empty'}."


testing = Board()
for x in range(0, len(testing.board)):
    for y in range(0, len(testing.board[x])):
        print(testing.get_space(x, y))





def main():
    game = Tictactoe()



if __name__=='__main__':
    main()




