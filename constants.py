# General constants
NUMBER_OF_CELL =    24
WIN_CELL = NUMBER_OF_CELL - 1
NUMBER_OF_CARDS =   24
NUMBER_OF_PLAYERS = 2

# Easily understand when stop the game
IS_CONTINUING_PLAYING = True
IS_STOP_PLAYING =       False

# Board's cells
FALLEN =            -2
BEGIN =             -1
FREE_PLACE =        0
RABBIT_PLAYER_1 =   1
RABBIT_PLAYER_2 =   2
HOLE =              3

SYMBOL_CELL = {
    FREE_PLACE:         " ",
    RABBIT_PLAYER_2:    "R2",
    RABBIT_PLAYER_1:    "R1",
    HOLE:               "O"
}

# Information about players
PLAYER_1 =      0
PLAYER_2 =      1

DICO_PLAYER_NAME = {
    PLAYER_1: "TRISTAN",
    PLAYER_2: "ZAZA"
}

# Signification of all cards
MOVING_1 =      1
MOVING_2 =      2
MOVING_3 =      3
MOVING_CARROT = 4

DICO_DISPLAY_CARD = {
    MOVING_1: "Avancez de 1 case",
    MOVING_2: "Avancez de 2 cases",
    MOVING_3: "Avancez de 3 cases",
    MOVING_CARROT: "Tournez la carotte"
}

ORIGINAL_LIST_CARDS = []
