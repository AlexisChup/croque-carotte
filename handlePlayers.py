from globalConstants import PLAYER_1

def initPlayer():
    return PLAYER_1

def returnNextPlayer(currentPlayer):
    return (currentPlayer + 1) % 2