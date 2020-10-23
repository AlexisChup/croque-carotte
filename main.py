from board import*
from constants import *
from handleRabbit import*




if __name__ == "__main__":

    displayBoard()
    insertRandomHole()
    mooveRabbitOnBoard("rabbit_1", 10, 1)
    mooveRabbitOnBoard("rabbit_1", 1, 1)
    displayBoard()