from board import *
from constants import *
from handleRabbit import *
from cards import *
from display import *




if __name__ == "__main__":
    isPlaying = True
    currentPlayer = PLAYER_1
    currentCard = MOVING_CARROT

    while(isPlaying):
        # MENU & CURRENT PLAYER
        displayMenu()
        displayCurrentPlayer(currentPlayer)

        # IS PLAYING AGAIN
        displayOptions()
        answer = input()
        isPlaying = False if (answer == 'q') else True

        # BOARD
        displayBoard()
        currentCard = getCard()
        displayValueOfCard(currentCard)

        # MOOVE RABBIT
        keyOfRabbit = chooseRabbitToMoove(currentPlayer)
        mooveRabbitOnBoard(keyOfRabbit, 1, currentPlayer)
        displayBoard()

        currentPlayer = (currentPlayer + 1) % 2
        
