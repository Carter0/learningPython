#!/usr/local/bin/python3

# Another version of the deck class, this time it implements an ABC in order to allow shuffling
# Also implements protected information _stuff

import collections.abc

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck2(collections.abc.MutableSequence):
    rank = [str(n) for n in range(2, 11)] + list('JQKA')
    suit = 'spades diamonds clubs hearts'.split()

    def __init__ (self):
        self._cards = [Card(rank, suit) for suit in self.suit
                                        for rank in self.rank]

    def __len__ (self):
        return len(self._cards)

    # Allows [] notation
    def __getitem__(self, position):
        return self._cards[position]

    # This method is all we need to enable shuffling
    def __setitem__(self, position, value):
        self._cards[position] = value

    # However, subclassing mutablesequence forces us to implement __delitem__
    def __delitem__(self, position):
        del self._cards[position]

    # We are also required to implement insert
    def insert(self, position, value):
        self._cards.insert(position.value)

    # You can loop over each item in a deck.

