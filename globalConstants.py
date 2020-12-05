from enum import Enum, auto
from Errors import PositionIncorrect

# General constants
NUMBER_OF_CELL =    24
WIN_CELL = NUMBER_OF_CELL - 1
NUMBER_OF_CARDS =   24

# Easily understand when stop the game
IS_CONTINUING_PLAYING = True
IS_STOP_PLAYING =       False

# Board's cells signification
class Board(Enum):
    FALLEN =            -2
    BEGIN =             auto() # -1
    FREE_PLACE =        auto() # 0
    RABBIT_PLAYER_1 =   auto() # 1
    RABBIT_PLAYER_2 =   auto() # 2
    HOLE =              auto() # 3

    def getFirstElement():
        """
        return the first element in the enum
        """
        return list(Board)[0].value

# Naming players for functions
PLAYER_1 =      0
PLAYER_2 =      1

# Displayed names
DICO_PLAYER_NAME = {
    PLAYER_1: "TRISTAN",
    PLAYER_2: "ZAZA"
}

# Meaning of all cards
MOVING_1 =      1
MOVING_2 =      2
MOVING_3 =      3
MOVING_CARROT = 4

DICO_DISPLAY_CARD = {
    MOVING_1: "Avancez d'1 case",
    MOVING_2: "Avancez de 2 cases",
    MOVING_3: "Avancez de 3 cases",
    MOVING_CARROT: "Tournez la carotte"
}


