#!/usr/local/bin/python3

# Decided to try making hangman, thought it could be fun before I get to some web stuff. 
# No front end or GUI for this. Just input word and then guess word. 


# The word the user has to guess. 
word = ['t', 'e', 's', 't', 'i', 'n', 'g']
lives = 5
game_over = False

def guess_word(char):
	if char in word:
		# Do guess correct stuff. 
	else: 
		# Do guess incorrect stuff 

def lose_life():
	lives = lives - 1;

# Remove the char in the word as long as that character exists in it
def remove_char(char):
	while char in word:
		word.remove(char)

def main():
	# Checking if the word is empty
	if not word:
		game_over = True
	while game_over == False: 
		guess_word()



