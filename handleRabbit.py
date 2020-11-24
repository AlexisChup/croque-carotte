
from globalConstants import *
from globalVariables import *

from display import displayWinner
from utils import handleInputRabbitNumero

def mooveRabbitOnBoard(keyOfRabbit, valeur, player):
    dictionnary = chooseGoodDictionnary(player)
    name = findNameRabbit(player)

    positionRabbit = dictionnary[keyOfRabbit]

    # À changer par la suite
    if(positionRabbit+valeur == WIN_CELL):
        displayWinner(player)
        board[positionRabbit] = FREE_PLACE
        board[WIN_CELL] = name
        dictionnary[keyOfRabbit] = WIN_CELL

        return IS_STOP_PLAYING
    
    elif (positionRabbit+valeur > WIN_CELL):
        board[positionRabbit] = FREE_PLACE
        newPositionOfRabbit = WIN_CELL - (valeur + dictionnary[keyOfRabbit] - WIN_CELL)
        moveBack = 0
        if board[newPositionOfRabbit] != FREE_PLACE:
            while board[newPositionOfRabbit] != FREE_PLACE:
                newPositionOfRabbit = WIN_CELL - (valeur + dictionnary[keyOfRabbit] - WIN_CELL) - moveBack
                moveback =+1
        
        board[newPositionOfRabbit] = name
        dictionnary[keyOfRabbit] = newPositionOfRabbit

    elif board[positionRabbit+valeur] == FREE_PLACE:
        board[positionRabbit+valeur] = name
        board[positionRabbit] = FREE_PLACE
        dictionnary[keyOfRabbit] += valeur

    elif board[positionRabbit+valeur] == HOLE:
        board[positionRabbit] = FREE_PLACE
        dictionnary[keyOfRabbit] = FALLEN

    else:
        mooveRabbitOnBoard(keyOfRabbit, valeur+1, player)

    return isRabbitLeft()
    
def chooseRabbitToMoove(player):
    """
    Display only not fallen rabbit
    & all user to choose which rabbit will move forward
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
