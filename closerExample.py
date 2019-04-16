#!/usr/local/bin/python3

def deco(func):
    def inner():
        print('Running inner()')
        func()
    return inner

@deco
def target():
    print ('Running Target()')

