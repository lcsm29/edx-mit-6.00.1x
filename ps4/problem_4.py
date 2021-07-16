#   Problem Set 4 - Problem 4 - Hand Length
#
#   Released    2021-06-30 14:00 UTC+00
#   Started     2021-06-30 14:26 UTC+00
#   Finished    2021-06-30 14:27 UTC+00
#   https://github.com/lcsm29/edx-mit-6.00.1x
#
#   oooo                w r i t t e n   b y      .oooo.    .ooooo.
#   `888                                       .dP""Y88b  888' `Y88.
#    888   .ooooo.   .oooo.o ooo. .oo.  .oo.         ]8P' 888    888
#    888  d88' `"Y8 d88(  "8 `888P"Y88bP"Y88b      .d8P'   `Vbood888
#    888  888       `"Y88b.   888   888   888    .dP'           888'
#    888  888   .o8 o.  )88b  888   888   888  .oP     .o     .88P'
#   o888o `Y8bod8P' 8""888P' o888o o888o o888o 8888888888   .oP'
def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    return sum(hand.values())
