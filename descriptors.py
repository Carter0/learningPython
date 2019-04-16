#!/usr/local/bin/python3

class MyDescriptor:
    def __get__(self, obj, type):
        print(self, obj, type)
    def __set__(self, obj, value):
        print("Got %s" % value)

class MyClass(object):
    x = MyDescriptor()

