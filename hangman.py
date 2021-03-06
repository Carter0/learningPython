#!/usr/local/bin/python3
import argparse
import os

# Decided to try making hangman, thought it could be fun before I get to some web stuff.
# No front end or GUI for this. Just input word and then guess word.

# I did this without classes, but perhaps I should go back and make it with one to consider whether the code is easier to understand.


def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')

def is_game_over(lives, word):
	if lives <= 0:
		print("You ran out of lives!")
		return True
	elif not word:
		print("You guessed all the letters in the word!")
		return True
	else:
		return False


def lose_life(lives):
	lives = lives - 1
	print(lives)
	return lives;


def remove_char(char, word):
	while char in word:
		word.remove(char)
		print("You removed an " + char + "!")
	return word

def ask_input():
	while True:
		print("Enter a char to print: ")
		char = input()
		if char == len(char) * char[0]:
			print("The char you wrote is: " + char)
			return char
		else:
			print("You can only enter a char")

def game_setup(word, lives):
	while True:
		if is_game_over(lives, word):
			break
		char = ask_input()
		# Guess char code
		if char in word:
			word = remove_char(char, word)
		else:
			lives = lose_life(lives)


def main():
	parser = argparse.ArgumentParser(description= 'Program runs a game of hangman.')
	parser.add_argument('word', help='Enter the word you want to play with.')
	parser.add_argument('lives', type=int, help='Enter the number of lives you want to play with.')
	args = parser.parse_args()
	clear_screen()
	game_setup(list(args.word), args.lives)



if __name__ == '__main__':
	main()






