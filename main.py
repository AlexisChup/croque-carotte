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
        displayMenu()
        displayCurrentPlayer(currentPlayer)

        displayOptions()
        answer = input()
        isPlaying = False if (answer == 'q') else True

        displayBoard()
        currentCard = getCard()
        displayValueOfCard(currentCard)

        currentPlayer = (currentPlayer + 1) % 2
        
