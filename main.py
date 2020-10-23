from board import *
from constants import *
from handleRabbit import *
from cards import *
from display import *




if __name__ == "__main__":

    # displayBoard()
    # insertRandomHole()
    # rabbit = chooseRabbitToMoove()
    # mooveRabbitOnBoard(rabbit, 1, 1)
    # displayBoard()
    # mooveRabbitOnBoard(rabbit, 1, 1)
    # displayBoard()

    currentPlayer = 0
    currentCard = MOVING_CARROT

    while(isPlaying):
        displayBoard()
        displayMenu()
        displayCurrentPlayer(currentPlayer)

        displayOptions()
        answer = input()
        isPlaying = False if (answer == 'q') else True

        currentCard = getCard()
        displayValueOfCard(currentCard)

        currentPlayer = (currentPlayer + 1) % 2
        
