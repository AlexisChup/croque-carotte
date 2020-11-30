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
    numberOfHoles = random.randint(1, 3)
    listPositionOfFuturFallenRabbit = []

    for hole in range(numberOfHoles):
        positionOfHole = returnRandomPositionOfHole()

        if(board[positionOfHole] != Board.FREE_PLACE.value):
            listPositionOfFuturFallenRabbit.append(positionOfHole)

        board[positionOfHole] = Board.HOLE.value

    return listPositionOfFuturFallenRabbit

def removeOlderHoles():
    """
    Remove all older holes on the board
    """
    for index in range(len(board)):
        if(board[index] == Board.HOLE.value):
            board[index] = Board.FREE_PLACE.value

def returnRandomPositionOfHole():
    """
    Return 1 random position in the board
    to insert hole
    """
    isPositionFound = False

    while(not isPositionFound):
        positionOfHole = random.randint(0, WIN_CELL-1)

        if(board[positionOfHole] != Board.HOLE.value):
            isPositionFound = True
        
    return positionOfHole