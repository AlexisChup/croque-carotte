import os

from constants import *
from board import *

def displayMenu():
    # os.system("clear")

    displayHoritonzaleLine()
    print("    CROQUE-CAROTTE MENU    ".center(60, '~'))
    displayHoritonzaleLine()

def displayHoritonzaleLine():
    print("".center(60, "-"))

def displayOptions():
    print("Entrez un caractère : ")
    print("\tEntrer : Tirer une carte")
    print("\tq : Quitter")

def displayValueOfCard(card):
    print("\nCARTE TIRÉE : ", DICO_DISPLAY_CARD[card], "\n")

def displayBoard():
    displayVerticalLineBoard()
    displayBoardCell()
    displayVerticalLineBoard()
    displayCaseNumer()

def displayVerticalLineBoard():
    print("▬"*NUMBER_OF_CELL*4, end='',)
    print("")

def displayBoardCell():
    for cell in board:
        # if board == RABBIT_PLAYER_1
        #     print(SYMBOL_CELL[cell], end='│ ',)

        print(SYMBOL_CELL[cell], end=' │ ',)

    print("")

def displayCaseNumer():
    for num in range(1, NUMBER_OF_CELL+1):
        print(str(num).zfill(2), end="│ ")
    
    print("")

def displayCurrentPlayer(player):
    print(DICO_PLAYER_NAME[player], " À toi de jouer !")

def displayWinner(player):
    print(DICO_PLAYER_NAME[player], "WON !!!!")