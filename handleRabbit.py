
from board import*

dictionnaryRabbitPLayer1 = {
    "rabbit_1": BEGIN,
    "rabbit_2" : BEGIN , 
    "rabbit_3": BEGIN , 
    "rabbit_4": BEGIN 
}
dictionnaryRabbitPLayer2 = {
    "rabbit_1": BEGIN,
    "rabbit_2" : BEGIN, 
    "rabbit_3": BEGIN, 
    "rabbit_4": BEGIN 
}

def mooveRabbitOnBoard(nameOfRabbit, valeur, player):
    dictionnary = chooseGoodDictionnary(player)
    posRabbit = findPosRabbit(nameOfRabbit, player)
    name = findNameRabbit(player)

    if board[posRabbit+valeur] == FREE_PLACE:
        board[posRabbit+valeur] = name
        dictionnary[nameOfRabbit] = dictionnary[nameOfRabbit] + valeur
        board[posRabbit] = FREE_PLACE

    elif board[posRabbit+valeur] == HOLE:
        board[posRabbit] = FREE_PLACE

    else:
        mooveRabbitOnBoard(posRabbit, valeur+1)

    return board
    


def chooseRabbitToMoove():
    nombreToFindRabbit = int(input("entrez le nom du lapin que vous voulez avancer"))
    if nombreToFindRabbit == 1:
        return "rabbit_1"
    elif nombreToFindRabbit == 2:
        return "rabbit_2"
    elif nombreToFindRabbit == 3:
        return "rabbit_3"
    elif nombreToFindRabbit == 4:
        return "rabbit_4"

def chooseGoodDictionnary(player):
    if player == PLAYER_1:
        return dictionnaryRabbitPLayer1
    else:
        return dictionnaryRabbitPLayer2

def findNameRabbit(player):
    dic = chooseGoodDictionnary(player)
    if player == PLAYER_1:
        return RABBIT_PLAYER_1
    else:
        return RABBIT_PLAYER_2

def findPosRabbit(nameOfRabbit, player):
    dic = chooseGoodDictionnary(player)
    if player == PLAYER_1:
        return dictionnaryRabbitPLayer1[nameOfRabbit]
    else:
        return dictionnaryRabbitPLayer2[nameOfRabbit]