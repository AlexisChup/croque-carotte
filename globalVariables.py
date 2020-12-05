from globalConstants import *

"""
Those dictrionnaries will saved the place
& the state of all rabbits
"""
dictionnaryRabbitPLayer1 = {
    "A1": Board.BEGIN.value,
    "B1" : Board.BEGIN.value, 
    "C1": Board.BEGIN.value,
    "D1": Board.BEGIN.value
}
dictionnaryRabbitPLayer2 = {
    "A2": Board.BEGIN.value,
    "B2" : Board.BEGIN.value, 
    "C2": Board.BEGIN.value, 
    "D2": Board.BEGIN.value 
}

# Displayed names
DICO_PLAYER_NAME = {
    PLAYER_1: "JOUEUR 1",
    PLAYER_2: "JOUEUR 2"
}

# use to loop over the 2 dictionnary
containerDictionnaries = [dictionnaryRabbitPLayer1, dictionnaryRabbitPLayer2]

# board to contain rabbits / holes / free places
board = [0 for i in range (NUMBER_OF_CELL)]

# list of all hole's position
listPositionOfHoles = []