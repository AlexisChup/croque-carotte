from board import initBoard, playTurn, croqueCarotteMenu
from handlePlayers import initPlayer, returnNextPlayer
from display import clearConsole
from save import setBackUp

if __name__ == "__main__":
    clearConsole()
    currentPlayer = initPlayer()
    isPlaying = True

    initBoard()
    croqueCarotteMenu() # display rules / resume backup game / start new game 

    while(isPlaying):
        isPlaying = playTurn(currentPlayer)
        currentPlayer = returnNextPlayer(currentPlayer)

    # save the game
    setBackUp()

        
