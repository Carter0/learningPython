#!/usr/local/bin/python3

import argparse

# Reverse a list of whatever without using some kind of reverse list function
# Just starting working in python, thought this was a good introduction to programming in the language
# Also introduction to parsing command line arguments in python, which proved to be the far more time consuming task.

def reverse_list(starting_list):
	reversed_list = []
	while len(starting_list) != 0 :
		reversed_list.append(starting_list.pop())
	return reversed_list


def main(): 
	parse = argparse.ArgumentParser()
	parse.add_argument("starting_list", nargs='*', help='Enter all the items you want to reverse.')
	args = parse.parse_args()
	print(reverse_list(args.starting_list))


if __name__ == '__main__':
	main()
