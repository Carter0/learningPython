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


    def input_info(self, player_index):
        x = int(input("Input the X Position"))
        y = int(input("Input the Y Position"))
        self.board.fill_board(x, y, self.players[player_index])
        print(self.board)

        #for x in range(0, len(self.board.board)):
        #    for y in range(0, len(self.board.board[x])):
        #        print(self.board.get_space(x, y))

    def run_game(self):
        turn_counter = 0;
        while not self.game_over:
            if(turn_counter % 2 == 0):
                self.input_info(0)
                turn_counter += 1
            else:
                self.input_info(1)
                turn_counter += 1


            # Check for game over state




class Board:

    def __init__(self):
        self.board = [[Space(x, y) for x in range(3)] for y in range(3)]

    def get_space(self, x, y):
        return self.board[x][y]

    def fill_board(self, x ,y, player):
        return self.board[x][y].set_space(player)

    def __str__(self):
        for x in range(0, len(self.board)):
            for y in range(0, len(self.board[x])):
                print(self.get_space(x, y))

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
        if self.filled:
            return " "
        elif self.player is 'X':
            return 'X'
        else:
            return 'O'



#testing = Board()
#for x in range(0, len(testing.board)):
#    for y in range(0, len(testing.board[x])):
#        print(testing.get_space(x, y))





def main():
    game = Tictactoe()
    game.run_game()



if __name__=='__main__':
    main()




