# This files is used to created
# and display the board
# of the game
from globalConstants import *
from globalVariables import *

from display import *
from handleRabbit import *
from utils import *

from cards import getCard
from holes import insertRandomHole

from save import setBackUp, getBackUp

def initBoard():
    insertRandomHole(True)

def playTurn(player):
        
        print('player : ', player)
        # MENU & CURRENT PLAYER
        displayMenu()
        displayCurrentPlayer(player)

        # IS PLAYING AGAIN
        displayPlayerAction()
        isPlaying = handleInputPlayerAction()
        # clearConsole()

        if(isPlaying):
            # CARD
            getBackUp()
            insertRandomHole(False)
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

        return isPlaying