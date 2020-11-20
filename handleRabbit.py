
from board import*
from constants import *
from display import displayWinner
from utils import handleInputRabbitNumero

def mooveRabbitOnBoard(keyOfRabbit, valeur, player):
    dictionnary = chooseGoodDictionnary(player)
    posRabbit = findPosRabbit(keyOfRabbit, player)
    name = findNameRabbit(player)

    # À changer par la suite
    if(posRabbit+valeur >= WIN_CELL):
        displayWinner(player)
        board[posRabbit] = FREE_PLACE
        dictionnary[keyOfRabbit] = WIN_CELL
        board[WIN_CELL] = name

        return IS_STOP_PLAYING

    elif board[posRabbit+valeur] == FREE_PLACE:
        board[posRabbit+valeur] = name
        dictionnary[keyOfRabbit] += valeur
        board[posRabbit] = FREE_PLACE

    elif board[posRabbit+valeur] == HOLE:
        board[posRabbit] = FREE_PLACE
        dictionnary[keyOfRabbit] = FALLEN

    else:
        mooveRabbitOnBoard(keyOfRabbit, valeur+1, player)

    return IS_CONTINUING_PLAYING
    
def chooseRabbitToMoove(player):
    dictionnaryRabbit = chooseGoodDictionnary(player)
    index = 1
    listKeys = []

    for key in dictionnaryRabbit:
        if(dictionnaryRabbit[key] != FALLEN):
            listKeys.append(key)

    print("Pressez [ENTER] pour choisir :", listKeys[0])
    for key, value in dictionnaryRabbit.items():
        if(value != FALLEN):
            print(index, ": pour ", key)
            index += 1

    index = handleInputRabbitNumero(len(listKeys))
    print("\n")

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