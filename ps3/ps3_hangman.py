#   Problem Set 3 - Hangman game
#   
#   Released    2021-06-16 14:00 UTC+00
#   Started     2021-06-16 14:05 UTC+00
#   Finished    2021-06-16 14:51 UTC+00
#   https://github.com/lcsm29/edx-mit-6.00.1x
#
#   oooo                w r i t t e n   b y      .oooo.    .ooooo.
#   `888                                       .dP""Y88b  888' `Y88.
#    888   .ooooo.   .oooo.o ooo. .oo.  .oo.         ]8P' 888    888
#    888  d88' `"Y8 d88(  "8 `888P"Y88bP"Y88b      .d8P'   `Vbood888
#    888  888       `"Y88b.   888   888   888    .dP'           888'
#    888  888   .o8 o.  )88b  888   888   888  .oP     .o     .88P'
#   o888o `Y8bod8P' 8""888P' o888o o888o o888o 8888888888   .oP'
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "ps3_words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    return all(0 for c in secretWord if c not in lettersGuessed)


def getGuessedWord(secretWord, lettersGuessed):
    ''' Returns True if all the letters of secretWord are in lettersGuessed;
        False otherwise
        Args:
            secretWord (str): the word the user is guessing
            lettersGuessed (list): lowercase letters which have been guessed
        Returns (bool): True if all letters of secretWord are in 
                        lettersGuessed, False otherwose
    '''
    return ''.join(['_ ' if c not in lettersGuessed else c + ' ' for c in secretWord])


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    return string.ascii_lowercase if not lettersGuessed else ''.join([c for c in string.ascii_lowercase if c not in lettersGuessed])


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
    letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
    about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
    partially guessed word so far, as well as letters that the 
    user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    def is_guess_invalid(guess):
        if len(guess) != 1 or not guess.encode().isalpha():
            print("Oops! That is not a valid letter. ", end='')
            if len(guess) != 1:
                print("You need to supply a letter, not {} letter{}.".format(
                    len(guess), 's' if len(guess) > 1 else ''))
            if not guess.encode().isalpha():
                print("English Alphabet only.")
            return True
        return False
    
    sw, lg, mistakesMade = secretWord, '', 0  # lg: lettersGuessed
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is {} letter{} long.".format(
                                        len(sw), 's' if len(sw) > 1 else ''))
    while mistakesMade < 8 and not isWordGuessed(sw, lg):
        print("------------")
        print("You have {} guesses left.".format(8 - mistakesMade))
        print("Available letters: {}".format(getAvailableLetters(lg)))
        guess = input("Please guess a letter: ").lower()
        if is_guess_invalid(guess):
            continue
        if guess in lg:
            print("Oops! You've already guessed that letter:", getGuessedWord(sw, lg))
        else:
            if getGuessedWord(sw, lg + guess) != getGuessedWord(sw, lg):
                print("Good guess:", getGuessedWord(sw, lg + guess))
            else:
                print("Oops! That letter is not in my word:", getGuessedWord(sw, lg + guess))
                mistakesMade += 1
            lg += guess if guess.encode().isalpha() else ''
    print("------------")
    if isWordGuessed(sw, lg):
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was {}.".format(sw))


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
