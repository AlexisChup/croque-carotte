import random

from globalConstants import *
from globalVariables import *

def insertRandomHole(randomPosition):
    """
    Remove & insert 
    between 1 & 3 holes on the board.

    Also detect & return if they are rabbits
    on the futur hole's position

    If listPositionOfHoles is set, set holes in those positions
    """
    # random position
    if(randomPosition == True):
        removeOlderHoles()
        numberOfHoles = random.randint(1, 3)
        listPositionOfFuturFallenRabbit = []

        for hole in range(numberOfHoles):
            positionOfHole = returnRandomPositionOfHole()
            listPositionOfHoles.append(positionOfHole)

            if(board[positionOfHole] != Board.FREE_PLACE.value):
                listPositionOfFuturFallenRabbit.append(positionOfHole)

            board[positionOfHole] = Board.HOLE.value
    # backup
    else:
        for holePosition in listPositionOfHoles:
            print(holePosition)
            board[holePosition] = Board.HOLE.value

        listPositionOfFuturFallenRabbit = []



    return listPositionOfFuturFallenRabbit

def removeOlderHoles():
    """
    Remove all older holes on the board & in the global variable
    """
    for index in range(len(board)):
        if(board[index] == Board.HOLE.value):
            board[index] = Board.FREE_PLACE.value

    listPositionOfHoles.clear()

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