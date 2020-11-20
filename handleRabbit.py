
from board import*

dictionnaryRabbitPLayer1 = {
    "TriTri": BEGIN,
    "Tropical" : BEGIN , 
    "Topinembourg": BEGIN , 
    "Tyty": BEGIN 
}
dictionnaryRabbitPLayer2 = {
    "Zebre": BEGIN,
    "Zebron" : BEGIN, 
    "Zebru": BEGIN, 
    "Zimbabwa": BEGIN 
}

def mooveRabbitOnBoard(keyOfRabbit, valeur, player):
    dictionnary = chooseGoodDictionnary(player)
    posRabbit = findPosRabbit(keyOfRabbit, player)
    name = findNameRabbit(player)

    if board[posRabbit+valeur] == FREE_PLACE:
        board[posRabbit+valeur] = name
        dictionnary[keyOfRabbit] += valeur
        board[posRabbit] = FREE_PLACE

    elif board[posRabbit+valeur] == HOLE:
        board[posRabbit] = FREE_PLACE
        dictionnary[keyOfRabbit] = FALLEN

    else:
        mooveRabbitOnBoard(keyOfRabbit, valeur+1, player)

    return board
    


def chooseRabbitToMoove(player):
    dictionnaryRabbit = chooseGoodDictionnary(player)
    index = 1
    listKeys = []

    for key in dictionnaryRabbit:
        if(dictionnaryRabbit[key] != FALLEN):
            listKeys.append(key)

    for key, value in dictionnaryRabbit.items():
        if(value != FALLEN):
            print(index, ": pour ", key)
            index += 1

    index = int(input("Saisir le numéro du lapin à avancer : ")) - 1

    return listKeys[index]

def chooseGoodDictionnary(player):
    return dictionnaryRabbitPLayer1 if(player == PLAYER_1) else dictionnaryRabbitPLayer2

def findNameRabbit(player):
    dic = chooseGoodDictionnary(player)
    if player == PLAYER_1:
        return RABBIT_PLAYER_1
    else:
        return RABBIT_PLAYER_2

def findPosRabbit(keyOfRabbit, player):
    dictionary = chooseGoodDictionnary(player)

    return dictionary[keyOfRabbit]