
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

    return isRabbitLeft()
    
def chooseRabbitToMoove(player):
    """
    Show to user only not fallen rabbit
    """

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
    return containerDictionnaries[player]

def findNameRabbit(player):
    dic = chooseGoodDictionnary(player)
    
    if player == PLAYER_1:
        return RABBIT_PLAYER_1
    else:
        return RABBIT_PLAYER_2

def findPosRabbit(keyOfRabbit, player):
    dictionary = chooseGoodDictionnary(player)

    return dictionary[keyOfRabbit]

def makeRabbitFallen(listPositionOfFuturFallenRabbit):
    for dictionnary in containerDictionnaries:
        for position in listPositionOfFuturFallenRabbit:
            for key in dictionnary:
                if(dictionnary[key] == position):
                    dictionnary[key] = FALLEN

    return isRabbitLeft()

def isRabbitLeft():
    index = 0

    for dictionnary in containerDictionnaries:
        isAllFallen = True
        for position in dictionnary.values():
            isAllFallen &= (position == FALLEN)

        if(isAllFallen):
            # is all rabbit of one's player is fallen, the winner is the other player
            displayWinner((index+1)%2)
            return IS_STOP_PLAYING

        index += 1

    return IS_CONTINUING_PLAYING
