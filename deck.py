#!/usr/local/bin/python3

# Coworker gave me an book about coding in python for advanced users.
# I am not an advanced user, but thought it would be cool to go through some of the example in the book and explain why they are so cool.
# It's all about making things "pythonic", which I assume is just python specific language functionality.

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__ (self):
        self._cards = [Card(rank, suit) for suit in self.suit
                                        for rank in self. ranks]
    def __len__ (self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
