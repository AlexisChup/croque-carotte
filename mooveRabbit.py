
from board import*

def mooveRabbitOnBoard(Posrabbit, valeur):
    if board[Posrabbit+valeur] == 0:
        board[Posrabbit+valeur] = board[Posrabbit]
        board[Posrabbit] = 0

    elif board[Posrabbit+valeur] == 3:
        board[Posrabbit] = 0

    else:
        mooveRabbitOnBoard(Posrabbit, valeur+1)

    return board
    
