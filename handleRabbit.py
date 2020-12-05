
from globalConstants import *
from globalVariables import *

from display import displayWinner, pos
from utils import handleInputRabbitNumero

def mooveRabbitOnBoard(keyOfRabbit, valeur, player):
    """
    update dictionnaries & board array according to the displacement of a rabbit
    """
    dictionnary = chooseGoodDictionnary(player)
    name = findNameRabbit(player)

    positionRabbit = dictionnary[keyOfRabbit]

    if(positionRabbit+valeur == WIN_CELL):
        displayWinner(player)
        board[positionRabbit] = Board.FREE_PLACE.value
        board[WIN_CELL] = name
        dictionnary[keyOfRabbit] = WIN_CELL
        resetDicionnary()

        return IS_STOP_PLAYING
    
    elif (positionRabbit+valeur > WIN_CELL):
        board[positionRabbit] = Board.FREE_PLACE.value
        newPositionOfRabbit = WIN_CELL - (valeur + dictionnary[keyOfRabbit] - WIN_CELL)

        if board[newPositionOfRabbit] != Board.FREE_PLACE.value: 
            for pos in range(newPositionOfRabbit, 0, -1):               
                if board[pos] == Board.FREE_PLACE.value or board[pos] == Board.HOLE.value:
                    newPositionOfRabbit = pos
                    break;
        board[newPositionOfRabbit] = name
        dictionnary[keyOfRabbit] = newPositionOfRabbit

    elif board[positionRabbit+valeur] == Board.FREE_PLACE.value:
        board[positionRabbit+valeur] = name
        board[positionRabbit] = Board.FREE_PLACE.value
        dictionnary[keyOfRabbit] += valeur

    elif board[positionRabbit+valeur] == Board.HOLE.value:
        board[positionRabbit] = Board.FREE_PLACE.value
        dictionnary[keyOfRabbit] = Board.FALLEN.value

        return isRabbitLeft()

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
        if(dictionnaryRabbit[key] != Board.FALLEN.value):
            listKeys.append(key)
    pos(10, 26)
    print("Pressez [ENTER] pour choisir :", listKeys[0])
    for key, value in dictionnaryRabbit.items():
        if(value != Board.FALLEN.value):
            pos(10, 26+index)
            print(index, ": pour ", key)
            index += 1

    index = handleInputRabbitNumero(len(listKeys))
    print("\n")

    return listKeys[index]

def chooseGoodDictionnary(player):
    return containerDictionnaries[player]

def findNameRabbit(player):
    if player == PLAYER_1:
        return Board.RABBIT_PLAYER_1.value
    else:
        return Board.RABBIT_PLAYER_2.value

def findPosRabbit(keyOfRabbit, player):
    dictionary = chooseGoodDictionnary(player)

    return dictionary[keyOfRabbit]

def makeRabbitFallen(listPositionOfFuturFallenRabbit):
    for dictionnary in containerDictionnaries:
        for position in listPositionOfFuturFallenRabbit:
            for key in dictionnary:
                if(dictionnary[key] == position):
                    dictionnary[key] = Board.FALLEN.value

    return isRabbitLeft()

def isRabbitLeft():
    index = 0

    for dictionnary in containerDictionnaries:
        isAllFallen = True
        for position in dictionnary.values():
            isAllFallen &= (position == Board.FALLEN.value)

        if(isAllFallen):
            # is all rabbit of one's player is fallen, the winner is the other player
            displayWinner((index+1)%2)
            resetDicionnary()

            return IS_STOP_PLAYING

        index += 1

    return IS_CONTINUING_PLAYING


def resetDicionnary():
    for dictionnary in containerDictionnaries:
        for key in dictionnary:
            dictionnary[key] = Board.BEGIN.value
            
    DICO_PLAYER_NAME[PLAYER_1] = "JOUEUR 1"
    DICO_PLAYER_NAME[PLAYER_2] = "JOUEUR 2"