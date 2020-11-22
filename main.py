from board import initBoard, playTurn
from handlePlayers import initPlayer, returnNextPlayer

if __name__ == "__main__":
    currentPlayer = initPlayer()
    isPlaying = True

    initBoard()

    while(isPlaying):
        isPlaying = playTurn(currentPlayer)
        currentPlayer = returnNextPlayer(currentPlayer)
        
