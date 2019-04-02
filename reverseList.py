#!/usr/local/bin/python3

import argparse

# Reverse a list of whatever without using some kind of reverse list function
# Just starting working in python, thought this was a good introduction to programming in the language
# Also introduction to parsing command line arguments in python


reversed_list = []



def reverse_list():
	while len(starting_list) != 0 :
		reversed_list.append(starting_list.pop())


def main(): 
	parser = argparse.ArgumentParser()
	parse.add_argument("list", nargs='*', help='Enter all the items you want to reverse.')
	starting_list = parse.parse_args()
	reversed_list()


if __name__ == '__main__':
	main()










#print(reversed_list)