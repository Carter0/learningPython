#!/usr/local/bin/python3
from math import hypot

# Also another example from the book. This time about vectors.

class Vector:

    # What is interesting to note here is that...
    # We have created 6 special methods and most are not called by the user. Most are called by the python interpreter.

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # Gets the string reprentation of the object for inspection. Like toString in java?
    # Also that is basically string.format()
    # Instead of <Vector object at <memory address>> we get something human readable
    # %r means the fields are integers, not strings
    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    # bool(x) calls x.__bool__() and returns true or false
    # Returns false if magnitude 0, true otherwisev
    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.x + other.x
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
