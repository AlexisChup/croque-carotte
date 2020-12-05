import os
import platform

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
    pos(75, 21)
    print("Entrez un caractère : ")
    pos(75, 23)
    print("[r] : afficher les règles du jeu")
    pos(75, 24)
    print("[s] : reprendre la partie sauvegardé")
    pos(75, 25)
    print("Autre : commencer une nouvelle partie")

def displayCurrentPlayer(player):
    colorDisplayed = Fore.GREEN if player == PLAYER_1 else Fore.BLUE #each player has his own color
    pos(5, 5)
    print(Style.BRIGHT, colorDisplayed, "\t"+DICO_PLAYER_NAME[player], Style.RESET_ALL, " À toi de jouer !")

def clearConsole():
    if(platform.system() == "Windows"):
        os.system("cls")
    else:
        os.system("clear")

def displayHoritonzaleLine():
    print("".center(60, "▬"))

def displayPlayerAction():
    """
    Either player continuing or quit
    """    
    print("\tEntrez un caractère : \n")
    print("\t[q] : Quitter et sauvegarder")
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
    """
    display the board in the console
    """
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
    """
    display one cell of the board in the console
    """
    print(color, content, Fore.RED, Style.BRIGHT, "│", Style.RESET_ALL, end='', sep="")

def displayCaseNumer():
    for num in range(1, NUMBER_OF_CELL+1):
        print("", str(num).zfill(2), "", end="│")
    
    print("")

def displayWinner(player):
    clearConsole()
    rabbitEndGame(player)

def displayRules():
    pos(10, 8)
    print("Règles du jeu de croque-carotte :")
    pos(10, 10)
    print("Pour débuter une partie de croque carotte, il faut d’abord que tout le monde puisse voir l'écran.") 
    pos(10, 11)
    print("Le jeu se joue à deux joueurs. Le tas de carte est déjà préparé par la machine.")
    pos(10, 13) 
    print("Le plus jeune joueur débute la partie en tirant une carte :") 
    pos(10, 14)
    print("- Si la carte retournée correspond à avancer un lapin, le joueur avance le lapin de son choix du nombre de cases indiquées.") 
    pos(10, 15)
    print("- Si elle correspond à une carotte, alors les trous vont changer de positions, attention à vous lapin.")
    pos(10, 17)
    print("Puis, les autres joueurs jouent ensuite à tour de rôle.")
    pos(10, 19)
    print("Au croque carotte, il existe plusieurs règles de déplacement :")
    pos(10, 21)
    print("- Chaque joueur choisit le lapin qu’il souhaite déplacer.")
    pos(10, 22)
    print("- Il peut déplacer un lapin déjà en jeu ou choisir d’en ajouter un nouveau.")
    pos(10, 23)
    print("- Un seul lapin par case doit être présent.")
    pos(10, 24)
    print("- Chaque joueur saute la ou les cases occupées. Elles ne sont pas comptabilisées dans le déplacement.")
    pos(10, 25)
    print("- Un trou équivaut à une case. Le lapin ne tombe dedans que s’il s’agit de sa destination finale. Un trou peut aussi s’ouvrir sous les pieds d’un lapin lorsque la carotte est tournée.")
    pos(10, 27)
    print("Comment gagner une partie de croque carotte ?")
    pos(10, 29)
    print("Le joueur qui remporte la partie de croque-carotte est celui qui a amené l’un de ses lapins au niveau de la carotte ou que tous les lapins d'un joueur soient tombés dans un trou.")
    pos(10, 30)
    print("Cela correspond à la dernière case du plateau mais attention il ne suffit pas de dépasser cette case... Il faut arriver pile dessus ou vous reculerez.")
    pos(10, 33)
    print("Voici le code couleur du jeu :")
    pos(10, 35)
    print(Fore.RED, Style.BRIGHT, "│",Style.RESET_ALL,Fore.WHITE,"    ",Fore.RED, Style.BRIGHT, "│",Style.RESET_ALL, sep="", end =" ") 
    print(Fore.WHITE,": une case libre")
    pos(10, 37)
    print(Fore.WHITE,"████", end =" ") 
    print(Fore.WHITE," : un trou")
    pos(10, 39)
    print(Fore.YELLOW,"████", end =" ") 
    print(Fore.WHITE," : la carotte")
    pos(10, 41)
    print(Fore.GREEN,"█"+"X1"+"█", end =" ") 
    print(Fore.WHITE," : lapin du joueur 1")
    pos(10, 43)
    print(Fore.BLUE,"█"+"X2"+"█", end =" ") 
    print(Fore.WHITE," : lapin du joueur 2")
    pos(10, 45)
    input("appuyer sur une touche pour passer")

def pos(x,y):
    """
    place the cursor in the console according to (x, y) coordinates
    """
    print( "\x1b["+str(y)+";"+str(x)+"H",end="",sep="")

def rabbitEndGame(player):
    pos(70, 12)
    print(Fore.RED, Style.BRIGHT, "▬"*17*5, Style.RESET_ALL, end='', sep="")
    pos(70, 13)
    print("                  ____     ____ ")
    pos(70, 14)
    print("                /'    |   |    \  ")
    pos(70, 15)
    print("              /    /  |   | \   \  ")
    pos(70, 16)
    print("            /    / |  |   |  \   \  ")
    pos(70, 17)
    print("           (   /   |  ----   |\   \  ")
    pos(70, 18)
    print("           | /   / /^\    /^\  \  _|              ",Fore.WHITE, DICO_PLAYER_NAME[player]," Gagne la partie !!!", sep = '')
    pos(70, 19) 
    print("            ~   | |   |  |   | | ~     ")
    pos(70, 20)
    print("                | |__O|__|O__| | ")
    pos(70, 21)
    print("              /~~      \/     ~~\  ")
    pos(70, 22)
    print("             /   (      |      )  \  ")
    pos(70, 23)
    print("       _--_  /,   \____/^\___/'   \  _--_  ")
    pos(70, 24)
    print("    /~    ~\ / -____-|_|_|-____-\ /~    ~\  ")
    pos(70, 25)
    print("   /________|___/~~~~\___/~~~~\ __|________\  ")
    pos(70, 26)
    print(Fore.YELLOW,"--~~~          ^ |     |   |     |  -     :  ~~~~~:~",Fore.GREEN,"-_  ___-----~~~~~~~~| ")
    pos(70, 27)
    print(Fore.YELLOW,"|             `^-^-^'   `^-^-^'                  :  ~\ ",Fore.GREEN,"/'   ____/--------| ",sep='')
    pos(70, 28)
    print(Fore.YELLOW,"|   --                                            ;   ",Fore.GREEN,"|/~~~------~~~~~~~~~| ",sep='')
    pos(70, 29)
    print(Fore.YELLOW,"(                                    :              :    ",Fore.GREEN,"|----------/--------| ",sep='')
    pos(70, 30)
    print(Fore.YELLOW,"(                     ,                           ;    .  ",Fore.GREEN,"|---\\--------------| ",sep='')
    pos(70, 31)
    print(Fore.YELLOW,"(     -                          .                  : : ",Fore.GREEN,"|______________-__| ",sep='')
    pos(70, 32)
    print(Fore.YELLOW,"|              ,                 ,                :   ",Fore.GREEN,"/'~----___________| ",sep='')
    pos(70, 33)
    print(Fore.YELLOW,"|_  \\\        ^                          ,, ;; ;; ;._-~ ")
    pos(70, 34)
    print(Fore.YELLOW,"|~~-----____________________________________----~~~ ")
    pos(70, 35)
    print(Fore.RED, Style.BRIGHT, "▬"*17*5, Style.RESET_ALL, sep="")

