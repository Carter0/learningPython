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
        self.board = Board()

    def out_of_bounds(self, x, y):
        if x > 2 or y > 2 or x < 0 or y < 0:
            print("X and Y must be between 0 and 2")
            return False
        else:
            return True


    def input_info(self, player_index):
        valid_input = False
        while not valid_input:
            x = int(input("Input the X Position"))
            y = int(input("Input the Y Position"))
            valid_input = self.out_of_bounds(x, y)

        self.board.fill_board(x, y, self.players[player_index])
        self.board.print_board()

    def run_game(self):
        turn_counter = 0;
        while not self.game_over:
            if(turn_counter % 2 == 0):
                print("X player turn")
                self.input_info(0)
                turn_counter += 1
            else:
                print("O player turn")
                self.input_info(1)
                turn_counter += 1


            # Check for game over state





class Board:
    def __init__(self):
        self.board = [[Space() for x in range(3)] for y in range(3)]

    def get_space(self, x, y):
        return self.board[x][y]

    def fill_board(self, x ,y, player):
        return self.board[x][y].set_space(player)

    def print_board(self):
        for column in self.board:
            print('\n')
            for item in column:
                print(item, end='')
        print('\n')


class Space:
    def __init__(self, space='#'):
        self.space = space

    def set_space(self, space):
        self.space = space

    def __str__(self):
        return self.space



def main():
    game = Tictactoe()
    game.run_game()



if __name__=='__main__':
    main()




