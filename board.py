# This files is used to created
# and display the board
# of the game

import random
from constants import *
        
dictionnaryRabbitPLayer1 = {
    "A1": BEGIN,
    "B1" : BEGIN , 
    "C1": BEGIN , 
    "D1": BEGIN 
}
dictionnaryRabbitPLayer2 = {
    "A2": BEGIN,
    "B2" : BEGIN, 
    "C2": BEGIN, 
    "D2": BEGIN 
}

def initBoard():
    return [0 for i in range (NUMBER_OF_CELL)]

board = initBoard()

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

    for hole in range(numberOfHoles):
        positionOfHole = returnRandomPositionOfHole()
        board[positionOfHole] = HOLE