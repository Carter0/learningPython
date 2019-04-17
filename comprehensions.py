#!/usr/local/bin/python3

# Felt like I didn't have a good grasp of list comprehensions.
# So I thought it prudent to go over some examples

example1 = [x for x in range(5)]
print(example1)

names = ['Carter', 'Sarah', 'Chris', 'Ryan', 'Sean', 'Phil']
names2 = [name for name in names]
print(names2)


doubleList = [[x for x in range(5)] for y in range(10)]
print(doubleList)

odds = [x for x in range(20) if x % 2]
print(odds)

double = [x * x for x in range(10)]
print(double)

example2 = [(letter, number) for letter in 'happy' for number in range(3)]
print(example2)

my_dict = {employee: n for employee, n in zip(names2, range(6))}
print(my_dict)


board = [[x for x in range(3)] for y in range(3)]
print(board)

for x, y, z in zip(*board):
    print(x, y, z)





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

