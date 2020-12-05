from Errors import ValueNotInInterval
from display import pos

def handleInputRabbitNumero(numberOfRabbitAlive):
    """
    display only rabbit that they aren't fallen.
    if the player's input isn't correct, the program will display an error
    """
    isInputCorrect = False
    inputNumeroOfRabbit = None

    while(not isInputCorrect):
        try:
            pos(10, 32)
            inputNumeroOfRabbit = input("Saisir le numéro du lapin à avancer : ")

            # this if is used to be faster in the game
            # by default, if the user press [ENTER], the rabbit number will be 1
            if(inputNumeroOfRabbit == ""):
                isInputCorrect = True
                inputNumeroOfRabbit = 1
            
            inputNumeroOfRabbit = int(inputNumeroOfRabbit)

            if(inputNumeroOfRabbit >= 1 and inputNumeroOfRabbit <= numberOfRabbitAlive):
                isInputCorrect = True

            elif(inputNumeroOfRabbit < 1 or inputNumeroOfRabbit > numberOfRabbitAlive):
                raise ValueNotInInterval

        except ValueError:
            print("Oops! Ce n'était pas un nombre.  Réessayez...")
            
        except ValueNotInInterval:
            print("Oops! Ce n'était pas un nombre compris entre 1 et", numberOfRabbitAlive, "inclus.  Réessayez...")

    return (inputNumeroOfRabbit - 1) # -1 because array start at 0

def handleInputIsPlaying():
    pos(9, 11)
    playerAction = input()

    return False if (playerAction == 'q' or playerAction == 'Q') else True

def handleInputPlayerActionMenu():
    pos(75, 26)
    actionMenu = input()

    if(actionMenu == 'R' or actionMenu == 'r'):
        return "displayRules"
    elif(actionMenu == 'S' or actionMenu == 's'):
        return "getBackup"
    else:
        return "startNewGame"


