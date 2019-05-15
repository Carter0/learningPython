#!/usr/local/bin/python3


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

test = Board()
test.print_board()


