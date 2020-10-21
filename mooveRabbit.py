



def mooveRabbitOnBoard(Posrabbit, board, valeur):
    if board[Posrabbit+valeur] == 0:
        board[Posrabbit+valeur] = board[Posrabbit]
        board[Posrabbit] = 0

    elif board[Posrabbit+valeur] == 3:
        board[Posrabbit] = 0

    else:
        mooveRabbitOnBoard(Posrabbit, board, valeur+1)

    return board
    

tab = [0 for i in range(24)]
tab[1] = "RV"
tab[4] = "RB"
print (tab)
tab[7] = 3

mooveRabbitOnBoard(4, tab, 3)
print(tab)