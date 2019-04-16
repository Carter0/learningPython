#!/usr/local/bin/python3

# Coworker gave me an book about coding in python for advanced users.
# I am not an advanced user, but thought it would be cool to go through some of the example in the book and explain why they are so cool.
# It's all about making things "pythonic", which I assume is just python specific language functionality.


# The Collections datatypes
# Apparently collections provides "specialized container datatypes besides pythons built in containers."
# Basically that just means it is data structures other than lists and sets.

import collections

# I have a "tuple" of named items called cards. Each card has a rank and a suit.
# A tuple is just an immutable list. You use parens instead of brackets.
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    # This python code is kinda crazy. It is doing what I would do, but it does it more efficiently.
    rank = [str(n) for n in range(2, 11)] + list('JQKA')
    suit = 'spades diamonds clubs hearts'.split()

    # These three methods are also interesting. I should consider using them more often.
    # These are called "special methods" and are called by the python interpreter and not by you.
    # You write len(my_object) and the interpreter calls my_object.__len__
    # Init is the only method often called explicitely by the user.
    # Special methods often have shortcuts and tricks implemented by the compiler and functionality written in the underlying C code.
    def __init__ (self):
        self._cards = [Card(rank, suit) for suit in self.suit
                                        for rank in self.rank]
    def __len__ (self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


# This code supposedly has a lot of functionality to it. Should be easy to do a lot with very few lines of code.
