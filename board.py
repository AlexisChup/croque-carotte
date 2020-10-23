# This files is used to created
# and display the board
# of the game

import random
from constants import *


board = [0 for i in range (NUMBER_OF_CELL)]


def displayBoard():
    print("")
    print("    CROQUE CAROTTE   ".center(50, "-"))
    print("")

    for cell in board:
        print(SYMBOL_CELL[cell], end=' | ',)

    print("")

def returnRandomPositionOfHole():
    isPositionFound = False

    while(not isPositionFound):
        positionOfHole = random.randint(0, 23)

        if(board[positionOfHole] != HOLE):
            isPositionFound = True
        
    return positionOfHole


def insertRandomHole():
    numberOfHoles = random.randint(1, 3)
    for hole in range(numberOfHoles):
        positionOfHole = returnRandomPositionOfHole()
        board[positionOfHole] = HOLE

