import os

from colorama import Fore, Back, Style

from globalConstants import *
from globalVariables import *

def displayMenu():
    displayHoritonzaleLine()
    print("         CROQUE-CAROTTE MENU         ".center(60, '█'))
    displayHoritonzaleLine()

def displayCurrentPlayer(player):
    colorDisplayed = Fore.GREEN if player == PLAYER_1 else Fore.BLUE #each player has his own color

    print(Style.BRIGHT, colorDisplayed, DICO_PLAYER_NAME[player], Style.RESET_ALL, " À toi de jouer !")

def clearConsole():
    """
    Efface tout le contenu de la console
    pour un affichage plus clair
    """
    os.system("clear")

def displayHoritonzaleLine():
    print("".center(60, "▬"))

def displayPlayerAction():
    """
    Either player continuing or quit
    """
    print("Entrez un caractère : ")
    print("\tq : Quitter")
    print("\tAutre : Tirer une carte")

def displayValueOfCard(card):
    print("\nCARTE TIRÉE : ", Style.BRIGHT, Fore.RED, DICO_DISPLAY_CARD[card], Style.RESET_ALL,"\n")

def displayBoard():
    """
    Call all functions for display
    the board properly
    """
    displayHorizontalLineBoard()
    displayBoardCell()
    displayHorizontalLineBoard()
    displayCaseNumer()

def displayHorizontalLineBoard():
    print(Fore.RED, Style.BRIGHT, "▬"*NUMBER_OF_CELL*5, Style.RESET_ALL, end='', sep="")
    print("")

def displayBoardCell():
    for cell in range(NUMBER_OF_CELL-1):
        if board[cell] == HOLE:
            printOneCell(Fore.WHITE, "████")
            
        elif board[cell] == RABBIT_PLAYER_1:
            for key in dictionnaryRabbitPLayer1:
                if cell == dictionnaryRabbitPLayer1[key]:
                    printOneCell(Fore.GREEN, "█"+key+"█")

        elif board[cell] == RABBIT_PLAYER_2:
            for key in dictionnaryRabbitPLayer2:
                if cell == dictionnaryRabbitPLayer2[key]:
                    printOneCell(Fore.BLUE, "█"+key+"█")

        else :
            printOneCell(Fore.CYAN, "    ")

    # print the WIN CELL
    printOneCell(Fore.YELLOW, "████")
    print("")

def printOneCell(color, content):
    print(color, content, Fore.RED, Style.BRIGHT, "│", Style.RESET_ALL, end='', sep="")

def displayCaseNumer():
    for num in range(0, NUMBER_OF_CELL):
        print("", str(num).zfill(2), "", end="│")
    
    print("")

def displayWinner(player):
    print(DICO_PLAYER_NAME[player], "WON !!!!")