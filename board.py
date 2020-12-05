# This files is used to created
# and display the board
# of the game
from globalConstants import *
from globalVariables import *

from display import *
from handleRabbit import *
from utils import *

from handlePlayers import chooseNameOfPlayer

from cards import getCard
from holes import insertRandomHole

from save import setBackUp, getBackUp


def initBoard():
    insertRandomHole(True)

def croqueCarotteMenu():
        clearConsole()
        displayMenu()
        actionPlayerInMenu = handleInputPlayerActionMenu()
        clearConsole()

        if(actionPlayerInMenu == "displayRules"):
            displayRules()
            croqueCarotteMenu()
        elif(actionPlayerInMenu == "getBackup"):
            isBackupSucced = getBackUp()

            if(isBackupSucced):
                print("Chargement de la sauvegarde réussite !")
                insertRandomHole(False)
                insertRabbitsInBoard()
            else:
                print("Chargement de la sauvegarde non réussite !")
        else:
            chooseNameOfPlayer()
            clearConsole()

def insertRabbitsInBoard():
    """
    this function is called after getting backup
    this will look into the dicitonnaries & place the rabbits
    on the board
    """
    indexDictionnary = 0
    containerRabbitBoardValues = [Board.RABBIT_PLAYER_1.value, Board.RABBIT_PLAYER_2.value]

    for dictionnary in containerDictionnaries:
        for position in dictionnary.values():
            if(position != Board.FALLEN.value and position != Board.BEGIN.value): # we place on the board only if the position is valid
                board[position] = containerRabbitBoardValues[indexDictionnary]
            
        indexDictionnary += 1



def playTurn(player):
        
    # MENU & CURRENT PLAYER
    displayCurrentPlayer(player)

    # IS PLAYING AGAIN
    displayPlayerAction()
    isPlaying = handleInputPlayerAction()
    # clearConsole()

    if(isPlaying):
        # CARD
        displayBoard()
        currentCard = getCard()
        displayValueOfCard(currentCard)

        # MOOVE RABBIT
        if(currentCard != MOVING_CARROT):
            keyOfRabbit = chooseRabbitToMoove(player)
            isPlaying = mooveRabbitOnBoard(keyOfRabbit, currentCard, player)
        # MOOVE CARROT
        else:
            listPositionOfFuturFallenRabbit = insertRandomHole(True)
            if(len(listPositionOfFuturFallenRabbit) > 0):
                isPlaying = makeRabbitFallen(listPositionOfFuturFallenRabbit)

        # BOARD
        displayBoard()
        pos(120, 40)
        input("appuyer sur une touche quand vous avez fini votre tour")
        clearConsole()

    return isPlaying


