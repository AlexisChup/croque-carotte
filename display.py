import os

from constants import *
from board import *

def displayMenu():
    # os.system("clear")

    displayHoritonzaleLine()
    print("         CROQUE-CAROTTE MENU         ".center(60, '█'))
    displayHoritonzaleLine()

def displayHoritonzaleLine():
    print("".center(60, "▬"))

def displayPlayerAction():
    print("Entrez un caractère : ")
    print("\tq : Quitter")
    print("\tAutre : Tirer une carte")

def displayValueOfCard(card):
    print("\nCARTE TIRÉE : ", DICO_DISPLAY_CARD[card], "\n")

def displayBoard():
    displayHorizontalLineBoard()
    displayBoardCell()
    displayHorizontalLineBoard()
    displayCaseNumer()

def displayHorizontalLineBoard():
    print("▬"*NUMBER_OF_CELL*4, end='',)
    print("")

def displayBoardCell():
    for cell in range(NUMBER_OF_CELL):
        if board[cell] == RABBIT_PLAYER_1:
            for key in dictionnaryRabbitPLayer1:
                if cell == dictionnaryRabbitPLayer1[key]:
                    print(key, end='│  ')

        elif board[cell] == RABBIT_PLAYER_2:
            for key in dictionnaryRabbitPLayer2:
                if cell == dictionnaryRabbitPLayer2[key]:
                    print(key, end='│  ')

        elif board[cell] == HOLE:
            print(".0", end='│  ')

        else :
            print(" ", end='│  ')

    print("")

def displayCaseNumer():
    for num in range(1, NUMBER_OF_CELL+1):
        print(str(num).zfill(2), end="│ ")
    
    print("")

def displayCurrentPlayer(player):
    print(DICO_PLAYER_NAME[player], " À toi de jouer !")

def displayWinner(player):
    print(DICO_PLAYER_NAME[player], "WON !!!!")