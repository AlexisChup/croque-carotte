import os

from colorama import Fore, Back, Style

from globalConstants import *
from globalVariables import *

def displayMenu():
    pos(75, 17)
    displayHoritonzaleLine()
    pos(75, 18)
    print("         CROQUE-CAROTTE MENU         ".center(60, '█'))
    pos(75, 19)
    displayHoritonzaleLine()
    pos(75, 20)
    print("Entrez un caractère : \n")
    pos(75, 21)
    print("R : afficher les règles du jeu")
    pos(75, 22)
    print("Autre : commencer une partie")

def displayCurrentPlayer(player):
    colorDisplayed = Fore.GREEN if player == PLAYER_1 else Fore.BLUE #each player has his own color
    pos(5, 5)
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
    print("\tEntrez un caractère : ")
    print("\tq : Quitter")
    print("\tAutre : Tirer une carte")
    # print("\tR : afficher les règles du jeu")

def displayValueOfCard(card):
    pos(10, 25)
    print("CARTE TIRÉE : ", Style.BRIGHT, Fore.RED, DICO_DISPLAY_CARD[card], Style.RESET_ALL)

def displayBoard():
    """
    Call all functions for display
    the board properly
    """
    pos(50, 15)
    displayHorizontalLineBoard()
    pos(50, 16)
    displayBoardCell()
    pos(50, 17)
    displayHorizontalLineBoard()
    pos(50, 18)
    displayCaseNumer()

def displayHorizontalLineBoard():
    print(Fore.RED, Style.BRIGHT, "▬"*NUMBER_OF_CELL*5, Style.RESET_ALL, end='', sep="")
    print("")

def displayBoardCell():
    for cell in range(NUMBER_OF_CELL-1):
        if board[cell] == Board.HOLE.value:
            printOneCell(Fore.WHITE, "████")
            
        elif board[cell] == Board.RABBIT_PLAYER_1.value:
            for key in dictionnaryRabbitPLayer1:
                if cell == dictionnaryRabbitPLayer1[key]:
                    printOneCell(Fore.GREEN, "█"+key+"█")

        elif board[cell] == Board.RABBIT_PLAYER_2.value:
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
    for num in range(1, NUMBER_OF_CELL+1):
        print("", str(num).zfill(2), "", end="│")
    
    print("")

def displayWinner(player):
    print(DICO_PLAYER_NAME[player], "WON !!!!")

def displayRules():
    pos(10, 10)
    print("Règles du jeu de croque-carotte :")
    pos(10, 12)
    print("Pour débuter une partie de croque carotte, il faut d’abord que tout le monde puisse voir l'écran.") 
    pos(10, 13)
    print("Le jeu se joue à deux joueurs. Le tas de carte est déjà préparer par la machine.")
    pos(10, 15) 
    print("Le plus jeune joueur débute la partie en tirant une carte :") 
    pos(10, 16)
    print("- Si la carte retournée correspond à avancé un lapin, le joueur avance le lapin de son choix du nombre de cases indiquées.") 
    pos(10, 17)
    print("- Si elle correspond à une carotte, alors les trous vont changer de positions, attention à vous lapin.")
    pos(10, 19)
    print("Puis, les autres joueurs jouent ensuite à tour de rôle dans le sens des aiguilles d’une montre.")
    pos(10, 21)
    print("Au croque carotte, il existe plusieurs règles de déplacement :")
    pos(10, 23)
    print("- Chaque joueur choisit le lapin qu’il souhaite déplacer.")
    pos(10, 24)
    print("- Il peut déplacer un lapin déjà en jeu ou choisir d’en ajouter un nouveau.")
    pos(10, 25)
    print("- Un seul lapin par case doit être présent.")
    pos(10, 26)
    print("- Chaque joueur saute la ou les cases occupées. Elle ne sont pas comptabilisées dans le déplacement.")
    pos(10, 27)
    print("- Un trou équivaut à une case. Le lapin ne tombe dedans que s’il s’agit de sa destination finale. Un trou peut aussi s’ouvrir sous les pieds d’un lapin lorsque la carotte est tournée.")
    pos(10, 28)
    print("- Si l’un des joueurs voit tous ses lapins tomber dans un trou, il sort du jeu et devra attendre la prochaine partie pour retenter sa chance.")
    pos(10, 30)
    print("Comment gagner une partie de croque carotte ?")
    pos(10, 32)
    print("Le joueur qui remporte la partie de croque carotte est celui qui a amené l’un de ses lapins au niveau de la carotte.")
    pos(10, 33)
    print("cela correpond à la dernière case du plteau mais attention il ne suffit pas de dépasser cette case... Il faut arriver pile dessus ou vous reculerez.")
    pos(10, 35)
    input("appuyer sur une touche pour passer")

def pos(x,y):
   print( "\x1b["+str(y)+";"+str(x)+"H",end="",sep="")