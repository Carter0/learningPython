#!/usr/local/bin/python3

# Decided to try mkaing my own interpretation of a deck just to see how it would compare to the books.

import collections

class MyDeck:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K', 'A']
    suits = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
    Card = collections.namedtuple('Card', ['numbers', 'suits'])




