
from board import *

def mooveRabbitOnBoard(posRabbit, valeur):
    if board[posRabbit+valeur] == FREE_PLACE:
        board[posRabbit+valeur] = board[posRabbit]
        board[posRabbit] = FREE_PLACE

    elif board[posRabbit+valeur] == HOLE:
        board[posRabbit] = FREE_PLACE

    else:
        mooveRabbitOnBoard(posRabbit, valeur+1)

    return board
    
