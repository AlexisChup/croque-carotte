import random

from globalConstants import *
from globalVariables import *

def returnRandomPositionOfHole():
    isPositionFound = False

    while(not isPositionFound):
        positionOfHole = random.randint(0, WIN_CELL-1)

        if(board[positionOfHole] != HOLE):
            isPositionFound = True
        
    return positionOfHole

def removeOlderHoles():
    for index in range(len(board)):
        if(board[index] == HOLE):
            board[index] = FREE_PLACE


def insertRandomHole():
    removeOlderHoles()
    numberOfHoles = random.randint(1, 3)
    listPositionOfFuturFallenRabbit = []

    for hole in range(numberOfHoles):
        positionOfHole = returnRandomPositionOfHole()

        if(board[positionOfHole] != FREE_PLACE):
            listPositionOfFuturFallenRabbit.append(positionOfHole)

        board[positionOfHole] = HOLE

    return listPositionOfFuturFallenRabbit