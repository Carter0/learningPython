#!/usr/local/bin/python3
import argparse

# Decided to try making hangman, thought it could be fun before I get to some web stuff.
# No front end or GUI for this. Just input word and then guess word.




def guess_char(char, word, lives):
	if char in word:
		remove_char(char)
	else:
		lose_life()

def lose_life(lives):
	lives = lives - 1;
	# Every time you lose a life do a check to see if you are out of lives.
	if lives == 0:
		game_over = True

def remove_char(char):
	while char in word:
		word.remove(char)

def ask_input():
	char = ""
	while True:
		print("Enter a char to print: ")
		char = input()
		if char == len(char) * char[0] and char.isdigit() != True:
			print("The char you wrote is: " + char)
			return char
		else:
			print("You can only enter a char")

def game_setup(word, lives):

	game_over = False

	# Checking if the word is empty
	if not word:
		game_over = True
	while game_over == False:
		print(word)
		char = ask_input()
		guess_char(char)


def main():
	parser = argparse.ArgumentParser(description= 'Program runs a game of hangman.')
	parser.add_argument('word', help='Enter the word you want to play with.')
	parser.add_argument('lives', type=int, help='Enter the number of lives you want to play with.')
	args = parser.parse_args()

	game_setup(args.word, args.lives)



if __name__ == '__main__':
	main()

# Add in the variables above as arguments to the program. I think that is way forward.







