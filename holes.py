import random

from globalConstants import *
from globalVariables import *

def insertRandomHole():
    """
    Remove & insert 
    between 1 & 3 holes on the board.

    Also detect & return if they are rabbits
    on the futur hole's position
    """
    removeOlderHoles()
    numberOfHoles = 0
    # numberOfHoles = random.randint(1, 3)
    listPositionOfFuturFallenRabbit = []

    for hole in range(numberOfHoles):
        positionOfHole = returnRandomPositionOfHole()

        if(board[positionOfHole] != FREE_PLACE):
            listPositionOfFuturFallenRabbit.append(positionOfHole)

        board[positionOfHole] = HOLE

    return listPositionOfFuturFallenRabbit

def removeOlderHoles():
    """
    Remove all older holes on the board
    """
    for index in range(len(board)):
        if(board[index] == HOLE):
            board[index] = FREE_PLACE

def returnRandomPositionOfHole():
    """
    Return 1 random position in the board
    to insert hole
    """
    isPositionFound = False

    while(not isPositionFound):
        positionOfHole = random.randint(0, WIN_CELL-1)

        if(board[positionOfHole] != HOLE):
            isPositionFound = True
        
    return positionOfHole