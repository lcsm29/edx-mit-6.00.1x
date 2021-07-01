#   Problem Set 3 - Problem 4 - The Game
#   
#   Released    2021-06-16 14:00 UTC+00
#   Started     2021-06-16 14:27 UTC+00
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
