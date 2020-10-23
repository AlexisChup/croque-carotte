from board import *
from constants import *
from handleRabbit import *
from cards import *
from display import *




if __name__ == "__main__":

    displayBoard()
    insertRandomHole()
    rabbit = chooseRabbitToMoove()
    mooveRabbitOnBoard(rabbit, 1, 1)
    displayBoard()
    mooveRabbitOnBoard(rabbit, 1, 1)
    displayBoard()




    
    # displayMenu()
    # displayOptions()


    # answer = input()
    # isPlaying = False if (answer == 'q') else True

    # while(isPlaying):
    #     displayBoard()
    #     displayMenu()
    #     displayOptions()

    #     answer = input()
    #     isPlaying = False if (answer == 'q') else True

    #     displayValueOfCard(getCard())
    
