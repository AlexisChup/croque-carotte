import os

from colorama import Fore, Back, Style

from globalConstants import *
from globalVariables import *

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
    print("\nCARTE TIRÉE : ", Style.BRIGHT, Fore.RED, DICO_DISPLAY_CARD[card], Style.RESET_ALL,"\n")

def displayBoard():
    displayHorizontalLineBoard()
    displayBoardCell()
    displayHorizontalLineBoard()
    displayCaseNumer()

def displayHorizontalLineBoard():
    print(Fore.RED, Style.BRIGHT, "▬"*NUMBER_OF_CELL*5, Style.RESET_ALL, end='', sep="")
    print("")

def displayBoardCell():
    for cell in range(NUMBER_OF_CELL):
        if board[cell] == HOLE:
            print(Fore.WHITE, "████", Fore.RED, Style.BRIGHT, "│", Style.RESET_ALL, end='', sep="")
            
        elif board[cell] == RABBIT_PLAYER_1:
            for key in dictionnaryRabbitPLayer1:
                if cell == dictionnaryRabbitPLayer1[key]:
                    print(Fore.GREEN,"█", key, "█", Fore.RED, Style.BRIGHT, "│", Style.RESET_ALL, end='', sep="")

        elif board[cell] == RABBIT_PLAYER_2:
            for key in dictionnaryRabbitPLayer2:
                if cell == dictionnaryRabbitPLayer2[key]:
                    print(Fore.BLUE, "█", key, "█", Fore.RED, Style.BRIGHT, "│", Style.RESET_ALL, end='', sep="")

        else :
            print("    ", Fore.RED, Style.BRIGHT, "│", Style.RESET_ALL, end='', sep="")

    print("")

def displayCaseNumer():
    for num in range(0, NUMBER_OF_CELL):
        print("", str(num).zfill(2), "", end="│")
    
    print("")

def displayCurrentPlayer(player):
    print(Style.BRIGHT, Fore.RED, DICO_PLAYER_NAME[player], Style.RESET_ALL, " À toi de jouer !")

def displayWinner(player):
    print(DICO_PLAYER_NAME[player], "WON !!!!")