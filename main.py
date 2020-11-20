from board import *
from constants import *
from handleRabbit import *
from cards import *
from display import *
from utils import handleInputPlayerAction
from handlePlayers import returnNextPlayer

if __name__ == "__main__":
    isPlaying = True
    currentPlayer = PLAYER_1
    currentCard = MOVING_CARROT
    listPositionOfFuturFallenRabbit = []

    insertRandomHole()

    while(isPlaying):
        # MENU & CURRENT PLAYER
        displayMenu()
        displayCurrentPlayer(currentPlayer)

        # IS PLAYING AGAIN
        displayPlayerAction()
        isPlaying = handleInputPlayerAction()

        # CARD
        displayBoard()
        currentCard = getCard()
        displayValueOfCard(currentCard)

        # MOOVE RABBIT
        if(currentCard != MOVING_CARROT):
            keyOfRabbit = chooseRabbitToMoove(currentPlayer)
            isPlaying = mooveRabbitOnBoard(keyOfRabbit, currentCard, currentPlayer)
        else:
            listPositionOfFuturFallenRabbit = insertRandomHole()
            if(len(listPositionOfFuturFallenRabbit) > 0):
                makeRabbitFallen(listPositionOfFuturFallenRabbit)

        # BOARD
        displayBoard()

        currentPlayer = returnNextPlayer(currentPlayer, NUMBER_OF_PLAYERS)
        
