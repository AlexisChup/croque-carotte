from board import *
from constants import *
from handleRabbit import *
from cards import *
from display import *




if __name__ == "__main__":
    displayMenu()
    displayOptions()

    answer = input()
    isPlaying = False if (answer == 'q') else True

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
        