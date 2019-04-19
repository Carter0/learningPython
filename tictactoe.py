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
            print("X and Y must be between 0 and 2.")
            return False
        else:
            return True

    def double_entry(self, x, y):
        if self.board.board[x][y].get_space() is 'O' or self.board.board[x][y].get_space() is 'X':
            print("Space is already filled.")
            return False
        else:
            return True

    def valid_input(self, x, y):
        if not self.out_of_bounds(x, y):
            return False
        elif not self.double_entry(x, y):
            return False
        else: return True


    def input_info(self, player_index):
        valid_input = False
        while not valid_input:
            x = int(input("Input the Row Position: "))
            y = int(input("Input the Column Position: "))
            valid_input = self.valid_input(x, y)

        self.board.fill_board(x, y, self.players[player_index])
        self.board.print_board()


    def check_full(self):
        is_full = True
        for column in self.board.board:
            for space in column:
                if space.space is '#':
                    is_full = False
        return is_full

    # By using sets, it should shrink the list size down to one because sets cant have duplicates
    def check_column(self):
        for column in self.board.board:
            if len(set(column)) is 1:
                return True
        return False

    # I think this is right, sorta hard to visualize it.
    def check_row(self):
        for i in range(3):
            if self.board.board[0][i].get_space() == self.board.board[1][i].get_space() == self.board.board[2][i].get_space():
                if self.board.board[0][i].get_space() != '#':
                    return True
        return False

    def check_diagonal(self):
        return self.board.board[0][0].get_space() == self.board.board[1][1].get_space() == self.board.board[2][2].get_space() and self.board.board[0][0].get_space() != '#'


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

            # Game over conditions
            self.game_over = self.check_full() or self.check_column() or self.check_row() or self.check_diagonal()

            # You should specify which player won!
            if self.game_over:
                print("Game Over!")


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
                print(item, end=' ')
        print('\n')


class Space:
    def __init__(self, space='#'):
        self.space = space

    def set_space(self, space):
        self.space = space

    def __str__(self):
        return self.space

    def get_space(self):
        return self.space



def main():
    game = Tictactoe()
    game.run_game()



if __name__=='__main__':
    main()




