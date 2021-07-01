#   Problem Set 3 - Problem 1 - Is the Word Guessed
#
#   Released    2021-06-16 14:00 UTC+00
#   Started     2021-06-16 14:05 UTC+00
#   Finished    2021-06-16 14:06 UTC+00
#   https://github.com/lcsm29/edx-mit-6.00.1x
#
#   oooo                w r i t t e n   b y      .oooo.    .ooooo.
#   `888                                       .dP""Y88b  888' `Y88.
#    888   .ooooo.   .oooo.o ooo. .oo.  .oo.         ]8P' 888    888
#    888  d88' `"Y8 d88(  "8 `888P"Y88bP"Y88b      .d8P'   `Vbood888
#    888  888       `"Y88b.   888   888   888    .dP'           888'
#    888  888   .o8 o.  )88b  888   888   888  .oP     .o     .88P'
#   o888o `Y8bod8P' 8""888P' o888o o888o o888o 8888888888   .oP'
def isWordGuessed(secretWord, lettersGuessed):
    ''' Returns True if all the letters of secretWord are in lettersGuessed;
        False otherwise
        Args:
            secretWord (str): the word the user is guessing
            lettersGuessed (list): lowercase letters which have been guessed
        Returns (bool): True if all letters of secretWord are in 
                        lettersGuessed, False otherwose
    '''
    return all(0 for c in secretWord if c not in lettersGuessed)


if __name__ == '__main__':
    import io
    import random
    import string

    def verifier(sw, lg):
        for c in sw:
            if c not in lg:
                return False
        return True

    manual_tests = [
        ['test', []],
        ['test', ['t','t','s','t','e']],
    ]
    failed = False
    for test in manual_tests:
        sw, lg = test
        if verifier(sw, lg) != isWordGuessed(sw, lg):
            failed = True
    print('success: manual tests' if not failed else 'failed: manual tests')

    words = [l.split() for l in io.open('ps3_words.txt', 'r').readlines()][0]
    verbose = False
    for i in range(1, 101):
        secret_word = random.choice(words)
        random_guessed = [random.choice(string.ascii_lowercase) for _ in range(random.randint(0, len(secret_word) * (i + 1)))]
        sorted_sw = sorted([c for c in secret_word])
        if verbose:
            print(f'secretWord: {secret_word}, lettersGuessed: {random_guessed}, expected: {verifier(secret_word, random_guessed)} result: {isWordGuessed(secret_word, random_guessed)}')
            print(f'secretWord: {secret_word}, lettersGuessed: {sorted_sw}, expected: {True}, actual: {isWordGuessed(secret_word, sorted_sw)}')
        else:
            if verifier(secret_word, random_guessed) != isWordGuessed(secret_word, random_guessed) or not isWordGuessed(secret_word, sorted_sw):
                print(f'failed on either of the follwoings:'
                      f'secretWord: {secret_word}, lettersGuessed: {random_guessed}, expected: {verifier(secret_word, random_guessed)} result: {isWordGuessed(secret_word, random_guessed)}'
                      f'secretWord: {secret_word}, lettersGuessed: {sorted_sw}, expected: {True}, actual: {isWordGuessed(secret_word, sorted_sw)}')
            else:
                if i % 10 == 0: print(f'success: {i}th random test')
