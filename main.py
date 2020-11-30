from board import initBoard, playTurn, beforePlayTurn
from handlePlayers import initPlayer, returnNextPlayer
import os

if __name__ == "__main__":
    os.system('clear')
    currentPlayer = initPlayer()
    isPlaying = True

    initBoard()
    beforePlayTurn()
    while(isPlaying):
        isPlaying = playTurn(currentPlayer)
        currentPlayer = returnNextPlayer(currentPlayer)
        
