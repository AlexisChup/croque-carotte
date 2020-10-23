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

# TODO: Select in dictionary only left rabbit
# def displayOptionsRabbit():

def displayValueOfCard(card):
    print("Carte tirée : ", DICO_DISPLAY_CARD[card])

def displayBoard():
    for cell in board:
        print(SYMBOL_CELL[cell], end=' | ',)

    print("")