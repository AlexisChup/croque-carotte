import os

from constants import *
from board import *
from handleRabbit import*

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
    for case in range(len(board)):
        listeRabbit =  []
        if board[case] == 1:
            for key in dictionnaryRabbitPLayer1:
                if case == dictionnaryRabbitPLayer1[key]:
                    print(key, end='│ ')
        if board[case] == 2:
            for key in dictionnaryRabbitPLayer2:
                if case == dictionnaryRabbitPLayer2[key]:
                    print(key, end='│ ')
        elif board[case] == 3:
            print("0", end='│ ')
        else :
            print(" ", end='│ ')
    print("")

def displayCaseNumer():
    for num in range(1, NUMBER_OF_CELL+1):
        print(str(num).zfill(2), end="│ ")
    
    print("")

def displayCurrentPlayer(player):
    print(DICO_PLAYER_NAME[player], " À toi de jouer !")
