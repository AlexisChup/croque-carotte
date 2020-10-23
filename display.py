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
    print("\t1 : Tirer une carte")
    print("\tq : Quitter")

def displayValueOfCard(card):
    print("Carte tirée : ", DICO_DISPLAY_CARD[card])

def displayBoard():
    displayVerticalLineBoard()
    displayBoardCell()
    displayVerticalLineBoard()

def displayVerticalLineBoard():
    print("▬"*len(board)*3, end='',)
    print("")

def displayBoardCell():
    for cell in board:
        print(SYMBOL_CELL[cell], end='│ ',)
    print("")

def displayCurrentPlayer(player):
    print(DICO_PLAYER_NAME[player], " À toi de jouer !")
