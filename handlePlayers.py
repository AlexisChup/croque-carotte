from globalConstants import PLAYER_1, PLAYER_2
from display import pos
from globalVariables import DICO_PLAYER_NAME

def initPlayer():
    return PLAYER_1

def returnNextPlayer(currentPlayer):
    return (currentPlayer + 1) % 2


def chooseNameOfPlayer():
    pos(15, 15)
    namePlayer1 = str(input('Entrez le nom du joueur 1 : '))
    if(namePlayer1 == ""):
        namePlayer1 = "JOUEUR 1"
    DICO_PLAYER_NAME[PLAYER_1] = namePlayer1

    pos(15, 17)
    namePlayer2 = str(input('Entrez le nom du joueur 2 : '))
    if(namePlayer2 == ""):
        namePlayer2 = "JOUEUR 2"
    DICO_PLAYER_NAME[PLAYER_2] = namePlayer2