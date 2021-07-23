#   Problem Set 5 - Problem 4 - Decrypt a Story
#
#   Released    2021-07-07 14:00 UTC+00
#   Started     2021-07-08 04:29 UTC+00
#   Finished    2021-07-08 04:32 UTC+00
#   https://github.com/lcsm29/edx-mit-6.00.1x
#
#   oooo                w r i t t e n   b y      .oooo.    .ooooo.
#   `888                                       .dP""Y88b  888' `Y88.
#    888   .ooooo.   .oooo.o ooo. .oo.  .oo.         ]8P' 888    888
#    888  d88' `"Y8 d88(  "8 `888P"Y88bP"Y88b      .d8P'   `Vbood888
#    888  888       `"Y88b.   888   888   888    .dP'           888'
#    888  888   .o8 o.  )88b  888   888   888  .oP     .o     .88P'
#   o888o `Y8bod8P' 8""888P' o888o o888o o888o 8888888888   .oP'
def decrypt_story(story=get_story_string()):
    ciphertext = CiphertextMessage(story)
    return ciphertext.decrypt_message()