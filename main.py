from board import *
from constants import *
from handleRabbit import *
from cards import *




if __name__ == "__main__":
    board[1] = RABBIT_PLAYER_1
    board[5] = RABBIT_PLAYER_2
    displayBoard()
    insertRandomHole()
    mooveRabbitOnBoard(1, 4)
    displayBoard()
    print("fghyujikhuio",getCard())