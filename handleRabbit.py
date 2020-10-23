
from board import*

dictionnaryRabbitPLayer1 = {
    "rabbit_1": BEGIN,
    "rabbit_2" : BEGIN , 
    "rabbit_3": BEGIN , 
    "rabbit_4": BEGIN 
}
dictionnaryRabbitPLayer2 = {
    "rabbit_2": BEGIN,
    "rabbit_2" : BEGIN, 
    "rabbit_3": BEGIN, 
    "rabbit_4": BEGIN 
}

def mooveRabbitOnBoard(nameOfRabbit, valeur, player):
    if player == PLAYER_1:
        posRabbit = dictionnaryRabbitPLayer1[nameOfRabbit]
        dictionnary = dictionnaryRabbitPLayer1
        name = RABBIT_PLAYER_1

    else:
        posRabbit = dictionnaryRabbitPLayer2[nameOfRabbit]
        dictionnary = dictionnaryRabbitPLayer2
        name = RABBIT_PLAYER_2

    if board[posRabbit+valeur] == FREE_PLACE:
        board[posRabbit+valeur] = name
        dictionnary[nameOfRabbit] = dictionnary[nameOfRabbit] + valeur
        board[posRabbit] = FREE_PLACE

    elif board[posRabbit+valeur] == HOLE:
        board[posRabbit] = FREE_PLACE

    else:
        mooveRabbitOnBoard(posRabbit, valeur+1)

    return board
    


def ChooseRabbitToMoove():
    nameOfRabbit = input("entrez le nom du lapin que vous voulez avancer")
    return nameOfRabbit

def chooseGoodDictionnary(player):
    if player == PLAYER_1:
        return dictionnaryRabbitPLayer1
    else:
        return dictionnaryRabbitPLayer2
