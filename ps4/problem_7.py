#   Problem Set 4 - Problem 7 - You and your Computer
#
#   Released    2021-06-30 14:00 UTC+00
#   Started     2021-06-30 15:42 UTC+00
#   Finished    2021-06-30 15:55 UTC+00
#   https://github.com/lcsm29/edx-mit-6.00.1x
#
#   oooo                w r i t t e n   b y      .oooo.    .ooooo.
#   `888                                       .dP""Y88b  888' `Y88.
#    888   .ooooo.   .oooo.o ooo. .oo.  .oo.         ]8P' 888    888
#    888  d88' `"Y8 d88(  "8 `888P"Y88bP"Y88b      .d8P'   `Vbood888
#    888  888       `"Y88b.   888   888   888    .dP'           888'
#    888  888   .o8 o.  )88b  888   888   888  .oP     .o     .88P'
#   o888o `Y8bod8P' 8""888P' o888o o888o o888o 8888888888   .oP'
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
          But if no hand was played, output "You have not played a hand yet. 
          Please play a new hand first!"
        
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    option, hand = '', {}
    while option != 'e':
        option = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        print('Invalid command.\n' if option not in ('n', 'r', 'e') else '', end='')
        if hand == {} and option == 'r':
            print('You have not played a hand yet. Please play a new hand first!')
            continue
        if option in ('n', 'r'):
            u_or_c = ''
            while u_or_c not in ('u', 'c'):
                u_or_c = input('Enter u to have yourself play, c to have the computer play: ')
                print('Invalid command.\n' if u_or_c not in ('u', 'c') else '', end='')
            if option == 'n':
                hand = dealHand(HAND_SIZE)
            playHand(hand, wordList, HAND_SIZE) if u_or_c == 'u' else compPlayHand(hand, wordList, HAND_SIZE)
