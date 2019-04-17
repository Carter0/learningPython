#!/usr/local/bin/python3


class Board:

    def __init__(self):
        self.board = [[Space(x, y) for x in range(3)] for y in range(3)]

    def get_space(self, x, y):
        return self.board[x][y]

    def fill_board(self, x ,y, player):
        return self.board[x][y].set_space(player)

    def __str__(self):
        return [y for x in self.board for y in x]
                #strings.append((x,y))
        #return ''.join(strings)

    ## Function above needs to return something, try adding it to a temp and then returning that??


class Space:

    def __init__(self, x ,y):
        self.filled = False
        self.player = None
        self.x = x
        self.y = y

    def set_space(self, player):
        self.filled = True
        self.player = player

    #def __str__(self):
    #    return f"This is a space at ({self.x}, {self.y}) owned by {self.player} {'and is filled' if self.filled else 'and is empty'}."

    def __str__(self):
        if not self.filled:
            return " "
        elif self.player is 'X':
            return 'X'
        else:
            return 'O'

print(Board())
