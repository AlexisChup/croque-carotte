from board import *
from constants import *
from handleRabbit import *
from cards import *
from display import *




if __name__ == "__main__":
    isPlaying = True
    currentPlayer = PLAYER_1
    currentCard = MOVING_CARROT

    insertRandomHole()

    while(isPlaying):
        # MENU & CURRENT PLAYER
        displayMenu()
        displayCurrentPlayer(currentPlayer)

        # IS PLAYING AGAIN
        displayOptions()
        answer = input()
        isPlaying = False if (answer == 'q') else True

        # CARD
        displayBoard()
        currentCard = getCard()
        displayValueOfCard(currentCard)

        # MOOVE RABBIT
        if(currentCard != MOVING_CARROT):
            keyOfRabbit = chooseRabbitToMoove(currentPlayer)
            mooveRabbitOnBoard(keyOfRabbit, currentCard, currentPlayer)
        else:
            insertRandomHole()

        # BOARD
        displayBoard()

        currentPlayer = (currentPlayer + 1) % 2
        
